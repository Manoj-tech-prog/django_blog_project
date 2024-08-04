import json

texts = [{
  "name": "John",
  "age": 30,
  "city": "New York"
},{
  "name": "John",
  "age": 30,
  "city": "New York"
},{
  "name": "John",
  "age": 30,
  "city": "New York"
}
]
with open("news_data.json",'r') as file:
    new_data = json.load(file)

print(new_data)