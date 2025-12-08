# Lab 2.4: Custom Skills

**Duration:** 60 minutes
**Level:** 2

## Objectives

Create a custom skill using SkillBase to package reusable functionality.

## Prerequisites

- Completed previous labs
- Python 3.10+ with signalwire-agents installed
- Virtual environment activated

## Instructions

### 1. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Implement Your Solution

This lab requires **two files**:

1. `solution/weather_skill.py` - Your custom skill class
2. `solution/agent.py` - An agent that uses the skill

### 3. Test Locally

```bash
# List available functions (should show skill functions)
swaig-test solution/agent.py --list-tools

# Check SWML output
swaig-test solution/agent.py --dump-swml

# Test the get_weather function
swaig-test solution/agent.py --exec get_weather --city "New York"
```

### 4. Submit

```bash
git add solution/
git commit -m "Complete Lab 2.4: Custom Skills"
git push
```

## Grading

| Check | Points |
|-------|--------|
| Agent Instantiation | 20 |
| SWML Generation | 20 |
| WeatherSkill Class Exists | 20 |
| get_weather Function Works | 20 |
| list_weather_cities Function Works | 20 |
| **Total** | **100** |

**Passing Score:** 70%

## Reference

See `reference/starter_skill.py` and `reference/starter_agent.py` for boilerplate templates.

---

*SignalWire AI Agents Certification*
