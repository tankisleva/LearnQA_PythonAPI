import json

json_text = {
  "messages": [
    {"message": "This is the first message", "timestamp": "2021-06-04 16:40:53"},
    {"message": "And this is a second message", "timestamp": "2021-06-04 16:41:01"}
  ]
}

json_dump = json.dumps(json_text)
json_object = json.loads(json_dump)

print(json_object["messages"][1])

