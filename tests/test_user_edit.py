import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("Edit user cases")
class TestUserEdit(BaseCase):

    @allure.description("This test successfully edit user")
    def test_edit_just_created_user(self):

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

        # EDIT
        new_name = "Changed_name"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of user after edit")

    @allure.description("This test as auth don't edit user")
    def test_edit_nod_authorize_user(self):

        # EDIT
        new_name = "Changed_name"

        response3 = MyRequests.put(f"/user/2",  data={"firstName": new_name}
                                 )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == f"Auth token not supplied"

    @allure.description("This test as auth one don't edit second user")
    def test_edit_other_user(self):

        # REGISTER
        registration_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=registration_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = registration_data['email']
        first_name = registration_data['firstName']
        password = registration_data['password']
        user_id = self.get_json_value(response1, "id")

        # REGISTER SECOND USER
        registration_data1 = self.prepare_registration_data()
        response2 = MyRequests.post("/user", data=registration_data1)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email1 = registration_data1['email']
        first_name1 = registration_data1['firstName']
        password1 = registration_data1['password']
        user_id1 = self.get_json_value(response2, "id")

        # LOGIN FIRST USER
        login_fata = {
            'email': email,
            'password': password
        }

        response3 = MyRequests.post("/user/login", data=login_fata)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # EDIT SECOND USER
        new_name = "Changed_name"

        response4 = MyRequests.put(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"username": new_name}
                                   )
        # Assertions.assert_code_status(response3, 200)
        print(user_id)
        print(user_id1)
        print(response4.status_code)
        print(response4.text)

        # GET
        response5 = MyRequests.get(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        print(response5.json())

        Assertions.assert_json_value_by_name(response5, "username", "learnqa", "Wrong name of user after edit")

    @allure.description("This test don't edit to an incorrect email")
    def test_edit_not_correct_mail_just_created_user(self):

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

        # EDIT
        new_email = "Changed_name"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email}
                                 )
        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == f"Invalid email format"

    @allure.description("This test don't edit to an short name")
    def test_edit_not_short_name_just_created_user(self):

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

        # EDIT
        new_first_name = "Y"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_first_name}
                                 )


        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName", "The First name has changed, but it shouldn't")





