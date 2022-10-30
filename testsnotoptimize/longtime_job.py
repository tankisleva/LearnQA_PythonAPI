import requests
import time
import json


response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json_text = response.json()

key = "token"
if key in json_text:
   mytoken = json_text[key]
else:
    print(f"Ключа {key} в Json нет")

key1 = "seconds"
if key1 in json_text:
   seconds = json_text[key1]
else:
    print(f"Ключа {key1} в Json нет")

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": mytoken})
json_text1 = response1.json()

key2 = "status"
if key2 in json_text1:
   status = json_text1[key2]
else:
    print(f"Ключа {key2} в Json нет")

if status == "Job is NOT ready":
    time.sleep(seconds)
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": mytoken})
    json_text2 = response2.json()

    key3 = "status"
    if key3 in json_text2:
        status = json_text2[key3]
    else:
        print(f"Ключа {key3} в Json нет")

    key4 = "result"
    if key4 in json_text2:
        result = json_text2[key4]
    else:
        print(f"Ключа {key4} в Json нет")

    if status == "Job is ready":
        if result != "":
           print("Task is ready!")
        else:
            print("something wrong")



