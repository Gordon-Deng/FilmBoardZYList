
import json

with open('sdfg.txt', 'r', encoding='utf-8') as f:
	result = f.read()
	f.close()

#result = '{"sr":3, "sd":"df"}'
result = json.loads(result)
print(result[3])