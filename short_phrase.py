class TestExample:

    def test_short_phrase(self):
        phrase = input("Set a phrase less than 15 symbols:")
        print(len(phrase))
        expected_len = 15
        actual_len = len(phrase)
        assert actual_len < expected_len, f"{actual_len} is now more then {expected_len}"
