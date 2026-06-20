# The Sovereign Engine: Pokémon TCG AI Strategy

This repository contains the mathematically verified strategy write-up, data-engineering scripts, and statistical simulation tools developed for the **Pokémon Company - PTCG AI Battle Challenge (Strategy Category)**.

## Project Structure
*   `Kaggle_Strategy_Submission.md`: The complete, mathematically verified ~1,450-word competitive strategy write-up.
*   `extract_stats.py`: Python script to calculate the Damage-Per-Energy (DPE) and meta-game weakness distribution from the dataset.
*   `generate_plot.py`: Generates the exact line plot comparing static hypergeometric draw baselines against dynamic Markov chain thinning.
*   `generate_diagrams.py`: Programmatically generates the MCTS decision flowcharts and state-transition DAGs.
*   `prep_kaggle.py`: Ingestion script used to compile and format the raw card data.
*   `LICENSE`: Standard MIT Open-Source License.

## Third-Party Software Disclaimer
The strategic modeling, algorithmic heuristics, and decision trees presented in this repository were orchestrated and verified using **Project Jack**, a local-first, closed-source multi-agent development chassis managed under the PolyForm Noncommercial License 1.0.0. To replicate the automated execution, please consult the official Jack Project specifications.

## Local Replication Instructions
To reproduce the mathematical analysis and generate the visual assets (`weakness_meta.png`, `thinning_comparison.png`, `sovereign_dag.png`, `item_lock_flow.png`) locally on your machine, follow these steps:

### 1. Prerequisites
Ensure you have Python 3.10+ installed. Install the required data-science dependencies:
```bash
pip install pandas matplotlib scipy
2. Ingest the Dataset
Due to strict competition data licensing rules (Rule 2.4.b), the raw EN_Card_Data.csv is not hosted in this repository.
Download the official EN_Card_Data.csv from the Kaggle competition page.
Place the EN_Card_Data.csv file directly into the root of this cloned directory.
3. Generate the Analytics & Visual Assets
Run the extraction and plotting scripts:
code
Bash
# Calculate top attackers, weakness distribution, and generate weakness_meta.png
python extract_stats.py

# Generate the hypergeometric vs. Markov thinning comparison plot
python generate_plot.py

# Programmatically draw the MCTS decision flowchart and transition DAG
python generate_diagrams.py
Licensing
The custom scripts, simulations, and documentation developed in this repository are licensed under the MIT License.