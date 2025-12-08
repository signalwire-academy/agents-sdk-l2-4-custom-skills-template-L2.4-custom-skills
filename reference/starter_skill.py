#!/usr/bin/env python3
"""Lab 2.4: Custom Skills - Skill Starter Template

Complete the TODOs to create a custom weather skill.
"""

from signalwire_agents.skills import SkillBase


class WeatherSkill(SkillBase):
    """Custom skill for weather lookups."""

    # TODO: Define SKILL_NAME
    # TODO: Define SKILL_DESCRIPTION

    # Simulated weather data - use this for lookups
    WEATHER_DATA = {
        "new york": {"temp": 45, "condition": "cloudy", "humidity": 65},
        "los angeles": {"temp": 72, "condition": "sunny", "humidity": 40},
        "chicago": {"temp": 38, "condition": "windy", "humidity": 55},
        "miami": {"temp": 82, "condition": "sunny", "humidity": 75},
        "seattle": {"temp": 52, "condition": "rainy", "humidity": 80},
    }

    def setup(self):
        """Register tools for this skill."""
        # TODO: Create a get_weather tool that looks up weather by city
        # TODO: Create a list_weather_cities tool that returns available cities
        pass
