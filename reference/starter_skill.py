#!/usr/bin/env python3
"""Lab 2.4: Custom Skills - Skill Starter Template

Complete the TODOs to create a custom weather skill.
"""

from typing import List, Dict, Any
from signalwire_agents.skills import SkillBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class WeatherSkill(SkillBase):
    """Custom skill for weather lookups."""

    # TODO: Define these class attributes
    SKILL_NAME = "weather_lookup"
    SKILL_DESCRIPTION = "Look up weather information for cities"
    SKILL_VERSION = "1.0.0"
    REQUIRED_PACKAGES = []
    REQUIRED_ENV_VARS = []

    # Simulated weather data - use this for lookups
    WEATHER_DATA = {
        "new york": {"temp": 45, "condition": "cloudy", "humidity": 65},
        "los angeles": {"temp": 72, "condition": "sunny", "humidity": 40},
        "chicago": {"temp": 38, "condition": "windy", "humidity": 55},
        "miami": {"temp": 82, "condition": "sunny", "humidity": 75},
        "seattle": {"temp": 52, "condition": "rainy", "humidity": 80},
    }

    def setup(self) -> bool:
        """Setup the skill - called during initialization."""
        return True

    def register_tools(self) -> None:
        """Register tools for this skill.

        TODO: Use self.define_tool() to register:
        - get_weather: Look up weather by city
        - list_weather_cities: List available cities

        Example:
            self.define_tool(
                name="function_name",
                description="What this function does",
                parameters={"param": {"type": "string", "description": "..."}},
                handler=self._my_handler
            )
        """
        pass

    # TODO: Create handler methods like:
    # def _get_weather_handler(self, args, raw_data):
    #     city = args.get("city", "")
    #     # Look up weather and return SwaigFunctionResult
    #     return SwaigFunctionResult("Weather info...")

    def get_hints(self) -> List[str]:
        """Return speech recognition hints."""
        return []

    def get_prompt_sections(self) -> List[Dict[str, Any]]:
        """Return prompt sections to add to agent."""
        return []

    @classmethod
    def get_parameter_schema(cls) -> Dict[str, Dict[str, Any]]:
        """Return the parameter schema for this skill."""
        return super().get_parameter_schema()
