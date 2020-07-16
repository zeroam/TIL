"""json_loads.py
JSON 문자열 데이터를 파이썬 데이터로 변환하기
"""
import json

string_json_data = '{"name": "Zopie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
json_data = json.loads(string_json_data)
print(json_data)
