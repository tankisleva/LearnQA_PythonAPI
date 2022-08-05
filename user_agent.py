import json

import pytest
import requests


class TestUserAgents:

    # expectedResults = [
    #     {"platform": "Mobile", "browser": "No", "device": "Android"},
    #     {"platform": "Mobile", "browser": "Chrome", "device": "iOS"},
    #     {"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"},
    #     {"platform": "Web", "browser": "Chrome", "device": "No"},
    #     {"platform": "Mobile", "browser": "No", "device": "iPhone"}
    # ]
    #
    # user_agents = [
    #     (
    #         "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
    #     (
    #         "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
    #     ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    #     (
    #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
    #     (
    #         "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    # ]
    #
    #
    #
    # @pytest.mark.parametrize('user_agent', user_agents)
    # def test_user_agents(self, user_agent):
    #     data = {"User-Agent": user_agent}
    #     url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
    #     response = requests.get(url, headers=data)
    #     json_text = response.json()
    #     print(json_text["user_agent"])
    #     if json_text["user_agent"] == self.user_agents[0]:
    #           assert json_text["platform"] == self.expectedResults[0]["platform"]
    #           assert json_text["browser"] == self.expectedResults[0]["browser"]
    #           assert json_text["device"] == self.expectedResults[0]["device"]
    #     if json_text["user_agent"] == self.user_agents[1]:
    #           assert json_text["platform"] == self.expectedResults[1]["platform"]
    #           assert json_text["browser"] == self.expectedResults[1]["browser"]
    #           assert json_text["device"] == self.expectedResults[1]["device"]
    #     if json_text["user_agent"] == self.user_agents[2]:
    #         assert json_text["platform"] == self.expectedResults[2]["platform"]
    #         assert json_text["browser"] == self.expectedResults[2]["browser"]
    #         assert json_text["device"] == self.expectedResults[2]["device"]
    #     if json_text["user_agent"] == self.user_agents[3]:
    #         assert json_text["platform"] == self.expectedResults[3]["platform"]
    #         assert json_text["browser"] == self.expectedResults[3]["browser"]
    #         assert json_text["device"] == self.expectedResults[3]["device"]
    #     if json_text["user_agent"] == self.user_agents[4]:
    #         assert json_text["platform"] == self.expectedResults[4]["platform"]
    #         assert json_text["browser"] == self.expectedResults[4]["browser"]
    #         assert json_text["device"] == self.expectedResults[4]["device"]

    data = [
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile",
            "No",
            "Android"
        ),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile",
            "Chrome",
            "iOS"
        ),
        (
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot",
            "Unknown",
            "Unknown"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Googlebot",
            "Chrome",
            "No"
        ),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile",
            "No",
            "iPhone"
        )
    ]

    @pytest.mark.parametrize('agent, platform, browser, device', data)
    def test_check_agent(self, agent, platform, browser, device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"user-agent": agent}
        print(agent)

        response = requests.get(url, headers=data)
        obj = json.loads(response.text)

        assert obj.get("browser") == browser
        assert obj.get("device") == device
        assert obj.get("platform") == platform









