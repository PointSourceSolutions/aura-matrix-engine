import matplotlib.pyplot as plt
from engine import run_party_simulation  # Linking our files together!

# SCENARIO CONFIGURATIONS
config_the_spark = {
    "simulation_meta": {"name": "The Spark", "duration_steps": 100},
    "environment": {
        "num_guests": 50,
        "topology": {"type": "watts_strogatz", "space_fluidity": 0.2, "k_neighbors": 4},
        "baseline_stats": {"mu_energy": 0.25, "sigma_energy": 0.1, "base_rate_rho": 0.15, "E_eq": 0.25, "lambda_decay": 0.05}
    },
    "agent_presets": {
        "The_Catalyst": {"count": 2, "initial_energy_E": 1.0, "base_interaction_rate_rho": 0.9, "impact_factor_delta_E": 0.35, "shift_probability_P": 0.8}
    }
}

config_the_flashover = {
    "simulation_meta": {"name": "The Flashover", "duration_steps": 100},
    "environment": {
        "num_guests": 100,
        "topology": {"type": "watts_strogatz", "space_fluidity": 0.6, "k_neighbors": 6},
        "baseline_stats": {"mu_energy": 0.35, "sigma_energy": 0.1, "base_rate_rho": 0.1, "E_eq": 0.35, "lambda_decay": 0.02}
    },
    "agent_presets": {
        "Super_Catalysts": {"count": 5, "initial_energy_E": 1.0, "base_interaction_rate_rho": 0.95, "impact_factor_delta_E": 0.5, "shift_probability_P": 0.9}
    }
}

config_the_dud = {
    "simulation_meta": {"name": "The Dud", "duration_steps": 100},
    "environment": {
        "num_guests": 100,
        "topology": {"type": "watts_strogatz", "space_fluidity": 0.2, "k_neighbors": 4},
        "baseline_stats": {"mu_energy": 0.6, "sigma_energy": 0.1, "base_rate_rho": 0.2, "E_eq": 0.6, "lambda_decay": 0.05}
    },
    "agent_presets": {
        "Toxic_Agents": {"count": 3, "initial_energy_E": 0.1, "base_interaction_rate_rho": 0.7, "impact_factor_delta_E": -0.3, "shift_probability_P": 0.1}
    }
}

def run_comparative_analysis():
    print("Executing Aura Matrix simulation suite...")
    _, history_spark = run_party_simulation(config_the_spark)
    _, history_flashover = run_party_simulation(config_the_flashover)
    _, history_dud = run_party_simulation(config_the_dud)
    print("Simulations complete. Generating visualization...")

    plt.figure(figsize=(12, 6))
    plt.plot(history_flashover, color='red', linewidth=3, linestyle='--', label="The Flashover (Peer-to-Peer Contagion)")
    plt.plot(history_spark, color='purple', linewidth=2, label="The Spark (Managed Lift)")
    plt.plot(history_dud, color='blue', linewidth=2, label="The Dud (Depressive Contagion)")

    plt.axhline(y=0.35, color='gray', linestyle=':', alpha=0.5, label="Low Baseline (Spark/Flashover)")
    plt.axhline(y=0.60, color='blue', linestyle=':', alpha=0.3, label="Moderate Baseline (Dud)")

    plt.title("Aura Matrix: Upgraded Systemic Phase Transitions", fontsize=16, fontweight='bold')
    plt.xlabel("Simulation Time Steps", fontsize=13)
    plt.ylabel("Average Systemic Energy (Mood State E)", fontsize=13)
    plt.ylim(0, 1.0)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    run_comparative_analysis()
