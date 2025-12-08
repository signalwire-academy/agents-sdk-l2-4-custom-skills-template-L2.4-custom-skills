#!/usr/bin/env python3
"""Lab 2.4: Custom Skills - Agent Starter Template

Complete the TODOs to create an agent that uses the custom skill.
"""

from signalwire_agents import AgentBase, register_skill

# TODO: Import your WeatherSkill from weather_skill.py
# from weather_skill import WeatherSkill

# TODO: Register the skill before using it
# register_skill(WeatherSkill)


class WeatherAgent(AgentBase):
    def __init__(self):
        super().__init__(name="weather-agent", route="/agent")

        self.prompt_add_section(
            "Role",
            "You are a weather information assistant. "
            "Help users check weather conditions in various cities."
        )

        self.add_language("English", "en-US", "rime.spore")

        # TODO: Add your custom weather skill by name
        # self.add_skill("weather_lookup")


agent = WeatherAgent()

if __name__ == "__main__":
    agent.run()
