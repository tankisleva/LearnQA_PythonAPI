import requests

class TestHeader:

    def test_home_header(self):
        response = requests.head("https://playground.learnqa.ru/api/homework_header")
        headers = response.headers
        print(headers)
        print(headers.get('x-secret-homework-header'))
        assert "x-secret-homework-header" in headers, "There is no header name = x-secret-homework-header"
        assert "Some secret value" in headers.get('x-secret-homework-header'), "There head value = Some secret value"