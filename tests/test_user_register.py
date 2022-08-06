import allure
import pytest

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    fields = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]

    @allure.description("This test successfully create user")
    def test_create_user_successfully(self):
       data = self.prepare_registration_data()
       response = MyRequests.post("/user/", data=data)
       Assertions.assert_code_status(response, 200)
       Assertions.assert_json_has_key(response, "id")

    @allure.description("This test can't create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
          "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description("This test can't create user with incorrect email with out @")
    def test_create_user_with_incorrect_email(self):
        email = 'vinkotov'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        assert response.content.decode("utf-8") == f"Invalid email format"
        Assertions.assert_code_status(response, 400)

    @allure.description("This test can't create user with first name more than 251 chars")
    def test_create_user_with_long_first_name(self):
        data = self.prepare_registration_data()
        long_first_name = self.generate_random_string(251)
        data["firstName"] = long_first_name
        response = MyRequests.post("/user/", data=data)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long"
        Assertions.assert_code_status(response, 400)

    @allure.description("This test can't create user with first name less than 1 char")
    def test_create_user_with_short_first_name(self):
        data = self.prepare_registration_data()
        short_first_name = self.generate_random_string(1)
        data["firstName"] = short_first_name
        response = MyRequests.post("/user/", data=data)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short"
        Assertions.assert_code_status(response, 400)

    @allure.description("This test can't create user with any missed param")
    @pytest.mark.parametrize('field', fields)
    def test_create_user_with_out_field(self, field):
        data = self.prepare_registration_data()
        data[field] = None
        response = MyRequests.post("/user/", data=data)
        print(response.status_code)
        print(response.content)
        assert response.content.decode("utf-8") == f"The following required params are missed: {field}"
        Assertions.assert_code_status(response, 400)
