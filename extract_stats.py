import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Load the flat CSV
df = pd.read_csv('EN_Card_Data.csv')

# 2. Clean Damage column (handles 30+, 30x, etc.)
def clean_damage(val):
    if pd.isna(val) or val == 'n/a' or val == '': 
        return 0
    match = re.search(r'\d+', str(val))
    return int(match.group()) if match else 0

# 3. Clean Cost column (counts energy symbols like {R}, {W}, or ●)
def clean_cost(val):
    if pd.isna(val) or val in ['No cost', 'n/a', '']: 
        return 0
    return len(re.findall(r'\{.*?\}|●', str(val)))

df['Clean_Damage'] = df['Damage'].apply(clean_damage)
df['Clean_Cost'] = df['Cost'].apply(clean_cost)

# 4. Calculate Efficiency strictly as Damage / (Cost + 1)
df['Efficiency'] = df['Clean_Damage'] / (df['Clean_Cost'] + 1)

# 5. Get top 3 unique attackers
top_3 = df.sort_values(by='Efficiency', ascending=False).drop_duplicates(subset=['Card Name', 'Move Name']).head(3)

print("=== TOP 3 ENERGY-EFFICIENT ATTACKERS ===")
for _, row in top_3.iterrows():
    print(f"Card: {row['Card Name']} | Move: {row['Move Name']} | Cost: {row['Cost']} | Damage: {row['Damage']} | Efficiency: {row['Efficiency']:.2f}")

# 6. Calculate weakness distribution
weakness_dist = df['Weakness'].dropna().value_counts()
print("\n=== WEAKNESS DISTRIBUTION ===")
for w, count in weakness_dist.items():
    print(f"{w}: {count}")

# 7. Save the chart
plt.figure(figsize=(8, 5))
weakness_dist.plot(kind='bar', color='#8B4513')
plt.title('Type Weakness Distribution')
plt.xlabel('Weakness Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('weakness_meta.png')
print("\n[SUCCESS] 'weakness_meta.png' generated and saved to your directory.")