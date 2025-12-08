#!/usr/bin/env python3
"""Lab 2.4: Custom Skills - Reference Solution (Skill)

Complete implementation of the WeatherSkill.
"""

from typing import List, Dict, Any
from signalwire_agents.skills import SkillBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class WeatherSkill(SkillBase):
    """Custom skill for weather lookups."""

    SKILL_NAME = "weather_lookup"
    SKILL_DESCRIPTION = "Look up weather information for cities"
    SKILL_VERSION = "1.0.0"
    REQUIRED_PACKAGES = []
    REQUIRED_ENV_VARS = []

    # Simulated weather data
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
        """Register tools for this skill."""

        self.define_tool(
            name="get_weather",
            description="Get current weather for a city",
            parameters={
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            handler=self._get_weather_handler
        )

        self.define_tool(
            name="list_weather_cities",
            description="Get list of cities with weather data",
            parameters={},
            handler=self._list_cities_handler
        )

    def _get_weather_handler(self, args, raw_data):
        """Handler for get_weather tool."""
        city = args.get("city", "")
        city_lower = city.lower()
        weather = self.WEATHER_DATA.get(city_lower)

        if weather:
            return SwaigFunctionResult(
                f"Weather in {city}: {weather['temp']}F, "
                f"{weather['condition']}, {weather['humidity']}% humidity"
            )
        return SwaigFunctionResult(f"Weather data not available for {city}")

    def _list_cities_handler(self, args, raw_data):
        """Handler for list_weather_cities tool."""
        cities = list(self.WEATHER_DATA.keys())
        return SwaigFunctionResult(
            f"Available cities: {', '.join(c.title() for c in cities)}"
        )

    def get_hints(self) -> List[str]:
        """Return speech recognition hints."""
        return ["weather", "temperature", "forecast"]

    def get_prompt_sections(self) -> List[Dict[str, Any]]:
        """Return prompt sections to add to agent."""
        return [
            {
                "title": "Weather Information",
                "body": "You can provide weather information for various cities.",
                "bullets": [
                    "Use get_weather to check conditions in a city",
                    "Use list_weather_cities to see available cities"
                ]
            }
        ]

    @classmethod
    def get_parameter_schema(cls) -> Dict[str, Dict[str, Any]]:
        """Return the parameter schema for this skill."""
        return super().get_parameter_schema()
