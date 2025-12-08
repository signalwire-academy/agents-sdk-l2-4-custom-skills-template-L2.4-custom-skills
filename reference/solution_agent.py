#!/usr/bin/env python3
"""Lab 2.4: Custom Skills - Reference Solution (Agent)

Complete implementation of the WeatherAgent.
"""

from signalwire_agents import AgentBase, register_skill
from solution_skill import WeatherSkill

# Register the custom skill with the skill registry
register_skill(WeatherSkill)


class WeatherAgent(AgentBase):
    """Weather information agent using custom skill."""

    def __init__(self):
        super().__init__(name="weather-agent", route="/agent")

        self.prompt_add_section(
            "Role",
            "You are a weather information assistant. "
            "Help users check weather conditions in various cities."
        )

        self.prompt_add_section(
            "Instructions",
            bullets=[
                "Use the weather skill to look up conditions",
                "If city not found, suggest available cities",
                "Provide helpful weather-related advice"
            ]
        )

        self.add_language("English", "en-US", "rime.spore")

        # Add custom weather skill by name (must match SKILL_NAME)
        self.add_skill("weather_lookup")


agent = WeatherAgent()

if __name__ == "__main__":
    agent.run()
