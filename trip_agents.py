import os
import google.generativeai as genai
from crewai import Agent

# Configure Gemini API
genai.configure(api_key=
)

class TripAgents:
    def __init__(self):
        self.llm = genai.GenerativeModel("gemini-pro")  # Initialize Gemini model

    def city_selector_agent(self):
        return Agent(
            role="City Selection Expert",
            goal="Identify best cities to visit based on user preferences",
            backstory="An expert travel geographer with extensive knowledge about world cities.",
            llm=self.llm,
            verbose=True
        )

    def local_expert_agent(self):
        return Agent(
            role="Local Destination Expert",
            goal="Provide detailed insights about selected cities including top attractions, local customs, and hidden gems",
            backstory="A knowledgeable local guide with first-hand experience of the city's culture and attractions.",
            llm=self.llm,
            verbose=True
        )

    def travel_planner_agent(self):
        return Agent(
            role="Professional Travel Planner",
            goal="Create detailed day-by-day itineraries with time allocations, transportation options, and activity sequencing",
            backstory="An experienced travel coordinator with perfect logistical planning skills.",
            llm=self.llm,
            verbose=True
        )

    def budget_manager_agent(self):
        return Agent(
            role="Travel Budget Specialist",
            goal="Optimize travel plans to stay within budget while maximizing experience quality",
            backstory="A financial planner specializing in travel budgets and cost optimization.",
            llm=self.llm,
            verbose=True
        )

class TripCrew:
    def __init__(self, user_inputs):
        self.user_inputs = user_inputs
        self.llm = genai.GenerativeModel("gemini-pro")  # Load Gemini AI model

    def generate_response(self, prompt):
        """Generate AI response using Gemini model."""
        response = self.llm.generate_content(prompt)
        return response.text if response and response.text else "❌ No response generated."

    def run(self):
        """Generate travel recommendations dynamically from AI."""
        city_selection_prompt = f"Suggest 3 cities for a {self.user_inputs['travel_type']} trip, considering these interests: {', '.join(self.user_inputs['interests'])}, during {self.user_inputs['season']} for {self.user_inputs['duration']} days."
        city_research_prompt = f"Provide insights for the cities suggested above. Mention attractions, culture, and best things to do."
        itinerary_prompt = f"Create a detailed {self.user_inputs['duration']}-day itinerary for the selected cities, ensuring a balanced mix of activities."
        budget_prompt = f"Estimate travel costs for a {self.user_inputs['budget']} budget. Break down expenses for accommodation, food, transport, and activities."

        return {
            "city_selection": self.generate_response(city_selection_prompt),
            "city_research": self.generate_response(city_research_prompt),
            "itinerary": self.generate_response(itinerary_prompt),
            "budget": self.generate_response(budget_prompt),
        }
