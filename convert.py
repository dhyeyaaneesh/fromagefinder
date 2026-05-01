import csv, json, os

os.makedirs('static', exist_ok=True)

cheeses = []
with open('cheeses.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cheeses.append({
            'name': row['cheese'],
            'milk': row['milk'],
            'country': row['country'].split(',')[0].strip() if row['country'] and row['country'] != 'NA' else 'Unknown',
            'type': row['type'],
            'texture': row['texture'],
            'flavor': row['flavor'],
            'aroma': row['aroma'],
            'color': row['color'],
            'vegetarian': row['vegetarian'],
            'fat_content': row['fat_content'],
            'url': row['url'],
        })

with open('static/cheeses.json', 'w', encoding='utf-8') as f:
    json.dump(cheeses, f)

print(f'Done! {len(cheeses)} cheeses saved to static/cheeses.json')