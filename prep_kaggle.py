import pandas as pd

# 1. Load the Kaggle CSV (Updated to match your actual file name!)
df = pd.read_csv('EN_Card_Data.csv').fillna('N/A')

# 2. Group by Card ID and Card Name to merge multi-row attacks/abilities
grouped = df.groupby(['Card ID', 'Card Name']).agg(lambda x: ' | '.join(x.astype(str).unique()))

# 3. Open Expanded_Knowledge.md to append the cards
with open('Expanded_Knowledge.md', 'a', encoding='utf-8') as f:
    f.write("\n\n# POKEMON TCG CARD DATABASE\n")
    
    for (card_id, name), row in grouped.iterrows():
        # Build the atomic XML card
        xml_card = f"""
<pattern domain="pokemon_card" name="{name} (ID: {card_id})">
  <why>Category: {row['Category']} | Type: {row['Type']} | HP: {row['HP']} | Weakness: {row['Weakness']} | Retreat: {row['Retreat']}</why>
  <how>Rule/Ability: {row['Rule']} | Move: {row['Move Name']} | Cost: {row['Cost']} | Damage: {row['Damage']} | Effect: {row['Effect Explanation']}</how>
  <pitfall>Card ID {card_id} | Expansion: {row['Expansion']}</pitfall>
</pattern>
"""
        f.write(xml_card)

print("Successfully appended all Pokémon to Expanded_Knowledge.md as atomic XML vectors!")