from typing import List

import pytest
import requests
import json


class TestUserAgents:
    #     user_agents = [
    #         (
    #             "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
    #         (
    #             "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
    #         ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    #         (
    #             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
    #         (
    #             "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    #     ]
    agents = [
        ("agent1", "agent2", "agent3"),
        ("Mobile1", "mobile2", "mobile3"),
    ]

    # browsers = [("No"),
    #             ("Chrome"),
    #             ("Unknown"),
    #             ("Chrome"),
    #             ("No")]

    # devices = [("Android"),
    #            ("iOS"),
    #            ("Unknown"),
    #            ("No"),
    #            ("iPhone")]

    # data_users = [user_agents, platforms, browsers, devices]

    # json_text = [
    #     "agents": {
    #         ["agent1", "agent2", "agent3"],
    # }
    #     "platforms": [
    #         ["platform1", "platform2", "platform3"],
    #     ]
    # ]

    # print(json_text["agents"][0])

    @pytest.mark.parametrize('agent', agents[0])
    @pytest.mark.parametrize('platform', agents[1])
    def test_user_agents(self, agent, platform):
        # data = {"User-Agent": user_agent}
        # url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        # response = requests.get(url, headers=data)
        print(f"{agent} относится к {platform}")

        # actual_platform = json_text["platform"]
        # actual_browser = json_text["browser"]
        # actual_device = json_text["device"]
