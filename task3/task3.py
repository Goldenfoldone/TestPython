import sys
import json

if len(sys.argv) != 4:
    print("Использование: python task3.py values.json tests.json report.json")
    sys.exit(1)

file1, file2, file3 = sys.argv[1], sys.argv[2], sys.argv[3]

values = json.load(open(file1))['values']
tests = json.load(open(file2))['tests']

valuesdist = {}
for i in values:
    valuesdist[i['id']] = i['value']
    
def update_values(data, valuesdist):
    if isinstance(data, list):
        for item in data:
            update_values(item, valuesdist)  
    elif isinstance(data, dict):
        if 'value' in data and data['value'] is not None:
            data['value'] = valuesdist.get(data['id']) 
        if 'values' in data and data['values'] is not None:
            update_values(data['values'], valuesdist) 

update_values(tests, valuesdist)

x = {'tests': tests}
with open(file3, 'w', encoding='utf-8') as file:  
    json.dump(x, file, ensure_ascii=False, indent=4) 