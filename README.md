# Knowledge-Based Systems and Fuzzy Logic Repository

This repository contains a collection of projects and experiments focused on knowledge-based systems, fuzzy logic, and agent-based simulations. It demonstrates the use of rule-based expert systems, fuzzy logic controllers, matchmaking systems, and agent-based modeling.

## Repository Structure

### 1. `labs.ipynb`
This Jupyter Notebook contains multiple demonstrations and implementations of knowledge-based systems and fuzzy logic. Key sections include:

- **Rules-Based Expert System**:
  - Implements a medical diagnosis system using the `experta` library.
  - Users can input symptoms, and the system provides possible diagnoses based on predefined rules.

- **Knowledge-Based Matchmaking System**:
  - A matchmaking system that calculates compatibility scores between user profiles based on attributes like age, interests, and location.
  - Uses domain-specific rules and weights to determine the best matches.

- **Fuzzy Logic Fan Speed Controller**:
  - Demonstrates a fuzzy logic system to control fan speed based on temperature.
  - Includes fuzzy variables (`temperature`, `fan_speed`), membership functions, and rules.

- **Fuzzy Sprinkler System**:
  - A fuzzy logic system to decide water sprinkling levels based on soil moisture, temperature, and time of day.
  - Includes expanded rules for more precise control.

- **Agent-Based Simulation**:
  - Simulates agents moving in a 2D grid.
  - Includes visualization of agent positions over time.

### 2. `roughWrk.ipynb`
This notebook contains experimental code and practice implementations. Key sections include:

- **Decorators in Python**:
  - Demonstrates how decorators work by extending the functionality of a base function.

- **Custom Map Function**:
  - Implements a custom `my_map` function to apply a transformation to a list.

- **Knowledge-Based Systems**:
  - Implements a basic knowledge base for medical diagnosis.
  - Includes a rule-based system for identifying diseases based on symptoms.

- **Matchmaking System**:
  - Similar to the matchmaking system in `labs.ipynb`, but includes additional experimental features and debugging.

- **Agent-Based Simulation**:
  - Experimental implementation of agents moving in a 2D grid.

## How to Use
1. Clone the repository to your local machine.
2. Open the `.ipynb` files in Jupyter Notebook or JupyterLab.
3. Run the cells sequentially to explore the different systems and simulations.

## Requirements
- Python 3.7+
- Required libraries:
  - `numpy`
  - `skfuzzy`
  - `experta`
  - `matplotlib`

Install the required libraries using:
```bash
pip install numpy scikit-fuzzy experta matplotlib