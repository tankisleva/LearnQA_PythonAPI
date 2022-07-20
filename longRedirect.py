import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

#сколько редиректов происходит от изначальной точки назначения до итоговой
print(len(response.history))

#URL итоговый.
print(response.url)



