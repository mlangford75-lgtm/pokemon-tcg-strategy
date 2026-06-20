import matplotlib.pyplot as plt
import numpy as np

def main():
    # Data from our verified calculations
    actions = np.array([0, 1, 2, 3, 4])
    static_baseline = np.full(5, 50.29)
    targeted_thinning = np.array([50.29, 51.41, 52.56, 53.74, 54.96])
    blind_thinning = np.array([50.29, 46.12, 42.15, 38.37, 34.77])

    plt.figure(figsize=(9, 5.5))
    
    # Plot lines with clean, professional data-science styling
    plt.plot(actions, static_baseline, label="Static Hypergeometric Baseline (Unthinned)", linestyle="--", color="gray", linewidth=2)
    plt.plot(actions, targeted_thinning, label="Targeted Markov Chain Thinning (MCTS Policy)", marker="o", color="#2E8B57", linewidth=2.5)
    plt.plot(actions, blind_thinning, label="Blind Thinning Collapse (Radiant Greninja Discard)", marker="x", color="#B22222", linewidth=2.5)

    # Formatting and labels
    plt.title("PTCG Setup Probability Comparison over Turn 1 Actions", fontsize=12, fontweight="bold", pad=15)
    plt.xlabel("Number of Thinning/Search Actions Executed", fontsize=10, labelpad=10)
    plt.ylabel("Turn 2 Combo Realization Probability (%)", fontsize=10, labelpad=10)
    plt.xlim(-0.2, 4.2)
    plt.ylim(30, 60)
    plt.xticks(actions)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="lower left", fontsize=9, frameon=True, shadow=False)
    
    # Annotate the divergent trends to show the mathematical trade-offs
    plt.annotate("Markov Thinning Gain (+4.67%)", xy=(4, 54.96), xytext=(2.2, 57),
                 arrowprops=dict(facecolor='#2E8B57', shrink=0.08, width=1.2, headwidth=5),
                 fontsize=9, color='#1E5F38', fontweight="bold")
                 
    plt.annotate("Markov Collapse Risk (-15.52%)", xy=(4, 34.77), xytext=(2.2, 31.5),
                 arrowprops=dict(facecolor='#B22222', shrink=0.08, width=1.2, headwidth=5),
                 fontsize=9, color='#801A1A', fontweight="bold")

    plt.tight_layout()
    plt.savefig("thinning_comparison.png", dpi=300)
    print("[SUCCESS] 'thinning_comparison.png' generated and saved.")

if __name__ == "__main__":
    main()