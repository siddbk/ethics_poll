"""
AI Ethics Poll Game - Data Models

This module defines the data structures used throughout the application:
- Scenario: An ethical dilemma with options and framework positions
- Response: A participant's vote on a specific scenario
- GameState: The current state of the game including all scenarios and responses
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import time


@dataclass
class Scenario:
    """Represents an ethical dilemma scenario."""
    id: str
    title: str
    description: str
    options: List[Dict[str, str]]  # List of {"id": "A", "text": "Option text"}
    frameworks: Dict[str, Dict[str, str]]  # Framework name -> {"choice": "A", "explanation": "..."}
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "options": self.options,
            "frameworks": self.frameworks
        }


@dataclass
class Response:
    """Represents a participant's response to a scenario."""
    voter_id: str
    scenario_id: str
    choice: str
    timestamp: float = field(default_factory=time.time)
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            "voter_id": self.voter_id,
            "scenario_id": self.scenario_id,
            "choice": self.choice,
            "timestamp": self.timestamp
        }


class GameState:
    """Manages the current state of the game."""
    
    def __init__(self):
        self.scenarios: List[Scenario] = []
        self.responses: List[Response] = []
        self.current_scenario: Optional[str] = None
        self.show_results: bool = False
        self.show_frameworks: bool = False
    
    def reset(self):
        """Reset the game state."""
        self.scenarios = []
        self.responses = []
        self.current_scenario = None
        self.show_results = False
        self.show_frameworks = False
    
    def add_scenario(self, scenario: Scenario):
        """Add a scenario to the game."""
        self.scenarios.append(scenario)
        # Set as current if it's the first one
        if not self.current_scenario:
            self.current_scenario = scenario.id
    
    def get_scenario(self, scenario_id: str) -> Optional[Scenario]:
        """Get a scenario by ID."""
        for scenario in self.scenarios:
            if scenario.id == scenario_id:
                return scenario
        return None
    
    def set_current_scenario(self, scenario_id: str):
        """Set the current active scenario."""
        if self.get_scenario(scenario_id):
            self.current_scenario = scenario_id
            self.show_results = False
            self.show_frameworks = False
    
    def add_response(self, response: Response):
        """Add a participant response."""
        # Check if this voter has already responded to this scenario
        for i, existing_response in enumerate(self.responses):
            if (existing_response.voter_id == response.voter_id and 
                existing_response.scenario_id == response.scenario_id):
                # Replace the existing response
                self.responses[i] = response
                return
        
        # Add new response
        self.responses.append(response)
    
    def get_responses_for_scenario(self, scenario_id: str) -> List[Response]:
        """Get all responses for a specific scenario."""
        return [r for r in self.responses if r.scenario_id == scenario_id]
    
    def toggle_results_display(self):
        """Toggle whether to show results."""
        self.show_results = not self.show_results
    
    def toggle_frameworks_display(self):
        """Toggle whether to show framework positions."""
        self.show_frameworks = not self.show_frameworks