import json

def divide_into_subdictionaries(input_dict, num_subdictionaries, target_sum):
    subdictionaries = {f'subdict{i}': {'current_sum': 0, 'items': {}} for i in range(num_subdictionaries)}
    remaining_space = {key: target_sum for key in subdictionaries}

    for key, value in sorted(input_dict.items(), key=lambda x: x[1], reverse=True):
        best_subdict = max(subdictionaries, key=lambda subdict_key: remaining_space[subdict_key])
        if remaining_space[best_subdict] >= value:
            subdictionaries[best_subdict]['items'][key] = value
            subdictionaries[best_subdict]['current_sum'] += value
            remaining_space[best_subdict] -= value

    return subdictionaries


with open("Z:\\KLA Hackathon\\Input data\\level1a.json", 'r') as file:
    data = json.load(file)

n_neighbourhoods = data["n_neighbourhoods"]
n_restaurants = data["n_restaurants"]
neighbourhoods = data["neighbourhoods"]
restaurants = data["restaurants"]
vehicles = data["vehicles"]

orders = {}
for neighbourhood_key, neighbourhood_value in neighbourhoods.items():
    orders[neighbourhood_key] = neighbourhood_value.get("order_quantity", 0)

print(orders)

# Number of subdictionaries
num_subdictionaries = 3

# Target sum for each subdictionary
target_sum = 600

# Divide into subdictionaries
result = divide_into_subdictionaries(orders, num_subdictionaries, target_sum)

# Output the result
print(result)

level1a = {}
output = {}

for i, subdict in enumerate(result.values(), start=1):
    path = ["r0"] + list(subdict.get('items', {}).keys()) + ["r0"]
    print(path)
    output[f"path{i}"] = path

level1a["v0"] = output

output_json = json.dumps(level1a, indent=2)

print(output_json)

jsonString = json.dumps(level1a)
jsonFile = open("Z:\\KLA Hackathon\\Validators\\level1a_output.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
