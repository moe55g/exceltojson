import pandas as pd
import json

# Läs CSV-filen
df = pd.read_csv('resultat.csv')

# Skapa en lista för att hålla JSON-objekt
json_resultat = []

# Loopa igenom varje rad i CSV-filen
for index, row in df.iterrows():
    question = row['Fråga']
    answer = row['Svar']
    
    # Skapa ett JSON-objekt för varje rad
    json_objekt = {
        'question': question,
        'answer': answer
    }
    
    # Lägg till JSON-objektet i listan
    json_resultat.append(json_objekt)

# Konvertera listan med JSON-objekt till JSON-format
json_data = json.dumps(json_resultat, indent=4, ensure_ascii=False)

# Spara JSON-filen med utf-8-kodning
with open('resultat.json', 'w', encoding='utf-8') as json_fil:
    json_fil.write(json_data)

print("resultat.json har skapats.")