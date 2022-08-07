import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("Get user cases")
class TestUserGet(BaseCase):

    expected_fields = ["email", "firstName", "lastName"]
    expected_fields1 = ["username", "email", "firstName", "lastName"]

    @allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
    @allure.title("This test get details as not authorize user")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_no_keys(response, self.expected_fields)

    @allure.testcase("https://www.youtube.com/watch?v=Su5p2TqZxKU", 'Test case title')
    @allure.title("This test get details as the same authorize user")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_has_keys(response2, self.expected_fields1)

    @allure.testcase("https://www.youtube.com/watch?v=Su5p2TqZxKU", 'Second test case title')
    @allure.title("This test get details as authorize user")
    def test_get_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response3 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response3, "user_id")

        response4 = MyRequests.get(f"/user/1",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_has_no_keys(response4, self.expected_fields)
        Assertions.assert_json_has_key(response4, self.expected_fields1[0])



