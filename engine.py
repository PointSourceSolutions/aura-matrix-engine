import networkx as nx  
import numpy as np     

def run_party_simulation(config):
    env = config["environment"]
    num_guests = env["num_guests"]                      
    k_neighbors = env["topology"]["k_neighbors"]        
    fluidity = env["topology"]["space_fluidity"]        
    
    baseline = env["baseline_stats"]
    mu_energy = baseline["mu_energy"]                   
    sigma_energy = baseline["sigma_energy"]             
    base_rho = baseline["base_rate_rho"]                
    E_eq = baseline["E_eq"]
    lambda_decay = baseline["lambda_decay"]
    
    G = nx.watts_strogatz_graph(n=num_guests, k=k_neighbors, p=fluidity)
    
    for i in G.nodes():
        G.nodes[i]['type'] = 'guest' 
        G.nodes[i]['energy'] = np.clip(np.random.normal(mu_energy, sigma_energy), 0, 1)
        G.nodes[i]['rho'] = base_rho 
        G.nodes[i]['momentum'] = 0.0 

    agent_presets = config.get("agent_presets", {})
    available_nodes = list(G.nodes()) 
    np.random.shuffle(available_nodes) 
    
    node_idx = 0 
    for agent_name, props in agent_presets.items():
        for _ in range(props["count"]):
            target_node = available_nodes[node_idx] 
            G.nodes[target_node]['type'] = agent_name
            G.nodes[target_node]['energy'] = props["initial_energy_E"]
            G.nodes[target_node]['rho'] = props["base_interaction_rate_rho"]
            G.nodes[target_node]['impact_factor'] = props["impact_factor_delta_E"]
            node_idx += 1 

    duration = config["simulation_meta"]["duration_steps"]
    energy_audit_trail = []
    
    for t in range(duration):
        # --- ACTION PHASE ---
        for i in G.nodes():
            current_energy = G.nodes[i]['energy']
            current_momentum = G.nodes[i]['momentum']
            base_p = G.nodes[i]['rho']
            
            P_t = np.clip(base_p + current_energy + current_momentum, 0.0, 1.0)
            
            if np.random.rand() < P_t:
                neighbors = list(G.neighbors(i))
                if len(neighbors) > 0:
                    target = np.random.choice(neighbors)
                    
                    if 'impact_factor' in G.nodes[i]:
                        impact = G.nodes[i]['impact_factor'] 
                    else:
                        excess_hype = max(0.0, G.nodes[i]['energy'] - E_eq)
                        impact = excess_hype * 0.30 
                        
                    G.nodes[target]['energy'] = np.clip(G.nodes[target]['energy'] + impact, 0.0, 1.0)
                    G.nodes[i]['momentum'] += 0.05 
                        
        # --- CLEANUP PHASE ---
        for i in G.nodes():
            current_energy = G.nodes[i]['energy']
            current_momentum = G.nodes[i]['momentum']
            G.nodes[i]['energy'] = E_eq + (current_energy - E_eq) * np.exp(-lambda_decay)
            G.nodes[i]['momentum'] = current_momentum * 0.9
            
        # RECORD KPI
        current_avg = np.mean([G.nodes[n]['energy'] for n in G.nodes()])
        energy_audit_trail.append(current_avg)

    return G, energy_audit_trail
