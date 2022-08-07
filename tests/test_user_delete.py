import allure

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

@allure.epic("Delete Cases")
class TestUserDelete(BaseCase):

    @allure.description("This test can't delete user with id 2")
    def test_delete_user_with_id_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        assert response2.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        Assertions.assert_code_status(response2, 400)

    @allure.description("This test can delete user successfully")
    def test_delete_user_successfully(self):
        # REGISTER
        registration_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=registration_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = registration_data['email']
        first_name = registration_data['firstName']
        password = registration_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_fata = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_fata)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response3, 200)

        # GET USER
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        assert response4.content.decode("utf-8") == f"User not found"

    @allure.description("This test can't delete authorize as other user")
    def test_delete_to_user_authorize_as_other_user(self):
        # REGISTER ONE USER
        registration_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=registration_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = registration_data['email']
        password = registration_data['password']

        # REGISTER SECOND USER
        registration_data1 = self.prepare_registration_data()
        response2 = MyRequests.post("/user", data=registration_data1)
        user_id1 = self.get_json_value(response2, "id")

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        # LOGIN
        login_fata = {
            'email': email,
            'password': password
        }

        response3 = MyRequests.post("/user/login", data=login_fata)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # DELETE
        response4 = MyRequests.delete(f"/user/{user_id1}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        # GET USER
        response5 = MyRequests.get(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        Assertions.assert_json_value_by_name(response5, "username", "learnqa", "User was deleted but shouldn't")