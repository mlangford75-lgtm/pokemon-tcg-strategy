import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_sovereign_dag():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Node styling
    box_style = dict(boxstyle="round,pad=0.5", fc="#E0F7FA", ec="#00838F", lw=2)
    
    # Draw Nodes
    ax.text(1.5, 2.5, "Finizen\n(Basic, ID 105)", ha="center", va="center", bbox=box_style, fontsize=9, fontweight="bold")
    ax.text(5.0, 2.5, "Palafin\n(Stage 1, ID 106)", ha="center", va="center", bbox=box_style, fontsize=9, fontweight="bold")
    ax.text(8.5, 2.5, "Palafin ex\n(Stage 1 ex, ID 107)", ha="center", va="center", bbox=box_style, fontsize=9, fontweight="bold")

    # Draw standard transition arrows
    arrow_style = dict(arrowstyle="->", lw=2, color="#00838F")
    ax.annotate("Evolve\n(Turn 2)", xy=(3.8, 2.5), xytext=(2.7, 2.5), arrowprops=arrow_style, ha="center", va="center", fontsize=8, fontweight="bold")
    ax.annotate("Retreat/Swap\n(Zero to Hero)", xy=(7.3, 2.5), xytext=(6.2, 2.5), arrowprops=arrow_style, ha="center", va="center", fontsize=8, fontweight="bold")

    # Draw prohibited transition arrow
    arrow_prohibited = dict(arrowstyle="->", lw=2, color="#B22222", linestyle=":")
    ax.annotate("", xy=(8.5, 3.2), xytext=(1.5, 3.2), arrowprops=arrow_prohibited)
    
    # Draw red "X" over the prohibited path
    ax.plot([4.8, 5.2], [3.1, 3.3], color="#B22222", lw=3)
    ax.plot([4.8, 5.2], [3.3, 3.1], color="#B22222", lw=3)
    
    # Annotate prohibited path
    ax.text(5.0, 3.7, "Rare Candy (ID 1079)\nPROHIBITED INVARIANT\n(Hero's Spirit Constraint)", 
            ha="center", va="center", color="#B22222", fontsize=9, fontweight="bold")

    plt.tight_layout()
    plt.savefig("sovereign_dag.png", dpi=300)
    plt.close()
    print("[SUCCESS] 'sovereign_dag.png' generated and saved.")

def generate_item_lock_flow():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Styling
    decision_style = dict(boxstyle="square,pad=0.4", fc="#FFF9C4", ec="#F57F17", lw=2)
    box_style = dict(boxstyle="round,pad=0.4", fc="#E8F5E9", ec="#2E7D32", lw=2)
    warn_style = dict(boxstyle="round,pad=0.4", fc="#FFEBEE", ec="#C62828", lw=2)

    # Draw Nodes
    ax.text(5.0, 9.0, "Item-Lock State Detected?", ha="center", va="center", bbox=decision_style, fontsize=9, fontweight="bold")
    
    ax.text(1.5, 7.0, "Standard Setup\n(w_setup = 500)", ha="center", va="center", bbox=box_style, fontsize=8)
    ax.text(5.0, 7.0, "Apply Decay\n(w_setup * 0.1 = 50)", ha="center", va="center", bbox=warn_style, fontsize=8)
    
    ax.text(5.0, 4.5, "Boss's Orders (ID 1182)\nin Hand?", ha="center", va="center", bbox=decision_style, fontsize=8, fontweight="bold")
    
    ax.text(8.5, 2.5, "Slow-Play Policy\n(Manual Attach & Pass)", ha="center", va="center", bbox=box_style, fontsize=8)
    ax.text(5.0, 2.5, "Apply Disruption Mult.\n(w_supporter * 10 = 500)", ha="center", va="center", bbox=box_style, fontsize=8)
    
    ax.text(5.0, 0.8, "Execute Gust/Bench Play\n(Break Lock)", ha="center", va="center", bbox=box_style, fontsize=9, fontweight="bold")

    # Connect with arrows
    arrow = dict(arrowstyle="->", lw=1.5, color="#555555")
    
    ax.annotate("No", xy=(1.5, 7.5), xytext=(3.5, 9.0), arrowprops=arrow, ha="center", va="center", fontsize=8, fontweight="bold")
    ax.annotate("Yes", xy=(5.0, 7.5), xytext=(5.0, 8.4), arrowprops=arrow, ha="center", va="center", fontsize=8, fontweight="bold")
    
    ax.annotate("", xy=(5.0, 5.0), xytext=(5.0, 6.4), arrowprops=arrow)
    
    ax.annotate("No", xy=(8.5, 3.1), xytext=(6.5, 4.5), arrowprops=arrow, ha="center", va="center", fontsize=8, fontweight="bold")
    ax.annotate("Yes", xy=(5.0, 3.1), xytext=(5.0, 3.9), arrowprops=arrow, ha="center", va="center", fontsize=8, fontweight="bold")
    
    ax.annotate("", xy=(5.0, 1.3), xytext=(5.0, 2.0), arrowprops=arrow)

    plt.tight_layout()
    plt.savefig("item_lock_flow.png", dpi=300)
    plt.close()
    print("[SUCCESS] 'item_lock_flow.png' generated and saved.")

if __name__ == "__main__":
    generate_sovereign_dag()
    generate_item_lock_flow()