# Aura Matrix Engine

An agent-based, stochastic simulation engine designed to model, quantify, and visualize macro-level phase transitions and systemic momentum within complex adaptive networks. 

By framing social dynamics and behavioral contagion through the lens of network topology and physics-based decay models, this framework provides computational proof of how localized, high-momentum nodes ("Catalysts") can permanently alter the operating baseline of an entire system.

## Theoretical Framework

The Aura Matrix Engine operates on a network graph where individual nodes represent agents (e.g., individuals in a crowd, employees in an organization) and edges represent communication channels. The system simulates macro shifts by tracking two primary phases per discrete time step:

### 1. The Action Phase (Stochastic Interaction)
At each time step $t$, every node $i$ evaluates its probability of initiating an interaction $$P_i(t) based on its baseline interaction rate ($\rho_i$), current internal energy ($E_i$), and historical momentum ($M_i$):

$$P_i(t) = \text{clip}(\rho_i + E_i + M_i, 0.0, 1.0)$$

If an interaction is triggered, a neighboring target node is randomly selected via a binomial trial, and an energy transfer occurs governed by the source node's `impact_factor` ($\Delta E$). 

### 2. The Cleanup Phase (Temporal Decay)
To prevent infinite energy loops and mirror physical reality, the network is subjected to an exponential cooling decay toward an environmental equilibrium ($E_{\text{eq}}$) at a rate determined by $\lambda$:

$$E_i(t + \Delta t) = E_{\text{eq}} + (E_i(t^+) - E_{\text{eq}}) \cdot e^{-\lambda \Delta t}$$

## Core Architecture

The repository is modularly structured to maintain structural integrity and separation of concerns:

* `engine.py`: Holds the main execution loop, network graph initialization (Watts-Strogatz small-world architecture), and the mathematical state-transition logic.
* `scenarios.py`: Contains specific experimental JSON-structured presets (`The Spark`, `The Flashover`, `The Dud`) and leverages `matplotlib` to render the time-series comparative analysis.
* `requirements.txt`: Manages the explicit tracking of scientific dependencies (`networkx`, `numpy`, `matplotlib`).

## Experimental Scenarios Modeled

The engine maps out the systemic consequences of network manipulation across three distinct baselines:

1.  **The Spark (Managed Lift):** Demonstrates how dropping two targeted Catalysts into a low-energy system can safely pull the network up to a brand-new, stable equilibrium plateau.
2.  **The Flashover (Uncontrolled Contagion):** Models a high-fluidity, hyper-connected panic cascade where peer-to-peer transmission outpaces natural temporal decay, pushing the entire system into saturation.
3.  **The Dud (Depressive Contagion):** Simulates the destructive impact of negative-value agents draining energy from a moderate-baseline environment, dragging the macro-system below its natural equilibrium.

## Execution

To reproduce the simulation data and generate the phase transition visualization chart:

```bash
# Clone the private repository
git clone [https://github.com/YOUR_USERNAME/aura-matrix-engine.git](https://github.com/YOUR_USERNAME/aura-matrix-engine.git)
cd aura-matrix-engine

# Install required mathematical/graphing libraries
pip install -r requirements.txt

# Run the comparative analysis suite
python scenarios.py# aura-matrix-engine
"Computational simulation engine for modeling network phase transitions and systemic momentum."


Citation & Academic Context

This computational model serves as the primary technical methodology and empirical verification for the accompanying preprint paper submitted to the Social Science Research Network (SSRN).

    Status: Preprint Draft / Intellectual Property Locked

    Rights: Copyright © 2026. All rights Reserved. Unauthorized replication, commercial distribution, or deployment of this proprietary framework without explicit academic citation is strictly prohibited.
