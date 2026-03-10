data = {"name": "Alice", "age": 25, "scores": [90, 85, 92]}

import json

print(json.dumps(data, ensure_ascii=False, indent=2))

from json import dumps

print(dumps(data, ensure_ascii = False, indent = 2))

import json as j

print(j.dumps(data, ensure_ascii = False, indent = 2))

from json import dumps as to_json

print(to_json(data, ensure_ascii = False, indent = 2))


from my_math import E, factorial, fibonacci

print(E)
print(factorial(5))
print(fibonacci(7))

