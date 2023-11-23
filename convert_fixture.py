import json

input_file = 'dataset_world_population_by_country_name.json'
output_file = 'converted_fixture.json'
app_name = 'users'
model_name = 'CountryPopulation'

with open(input_file, 'r') as f:
    data = json.load(f)

converted_data = []

for idx, entry in enumerate(data, start=1):
    converted_entry = {
        "model": f"{app_name}.{model_name}",
        "pk": idx,
        "fields": entry
    }
    converted_data.append(converted_entry)

with open(output_file, 'w') as f:
    json.dump(converted_data, f, indent=2)

print(f"Conversion complete. Fixture saved to {output_file}")
