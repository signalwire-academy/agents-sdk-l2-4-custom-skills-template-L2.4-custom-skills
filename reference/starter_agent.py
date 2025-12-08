#!/usr/bin/env python3
"""Lab 2.4: Custom Skills - Agent Starter Template

Complete the TODOs to create an agent that uses the custom skill.
"""

from signalwire_agents import AgentBase

# TODO: Import your WeatherSkill from weather_skill.py


class WeatherAgent(AgentBase):
    def __init__(self):
        super().__init__(name="weather-agent")

        self.prompt_add_section(
            "Role",
            "You are a weather information assistant."
        )

        self.add_language("English", "en-US", "rime.spore")

        # TODO: Add your custom weather skill


if __name__ == "__main__":
    agent = WeatherAgent()
    agent.run()
