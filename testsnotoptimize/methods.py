import requests


response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
# 1) Wrong method provided

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print(response.text)
# 2) Ничего не выводит

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response.text)
# 3) {"success":"!"}


# 4) Методы put и delete, что с data, что с params выводят {"success":"!"}
methods = ["POST", "GET", "PUT", "DELETE", "HEAD"]

for method in methods:
    if method == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
        print(response.text)
    if method == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": method})
        print(response.text)
    if method == "HEAD":
        response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
        print(response.text)
    if method == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
        print(response.text)
    if method == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
        print(response.text)
