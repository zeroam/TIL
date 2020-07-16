"""json_dumps.py
파이썬 데이터를 JSON 문자열 데이터로 변환하기
"""
import json

python_value = {"isCat": True, "miceCaught": 0, "name": "Zophie", "felineIQ": None}
string_json_data = json.dumps(python_value)
print(string_json_data)
