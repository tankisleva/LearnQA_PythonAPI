import requests

class TestCookie:

    def test_home_cookie(self):
        response = requests.head("https://playground.learnqa.ru/api/homework_cookie")
        cookies = response.cookies
        print(cookies)
        assert "HomeWork" in cookies, "There is no cooke name = HomeWork in response"
        assert "hw_value" in cookies.values(), "There is no cooke value = hw_value in response"



