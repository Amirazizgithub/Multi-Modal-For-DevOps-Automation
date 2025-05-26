# app/core/intent_classifier.py
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class IntentClassifier:
    def __init__(self):
        # Initialize your LLM client
        self.llm_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Define your list of possible modules/intents
        self.possible_modules = [
            "instance_creation",
            "storage",
            "logs",
            "monitoring",
            "ci_cd",
            "unknown",  # Include a fallback
        ]

    # This function uses an LLM to classify the intent of a message
    def classify(self, message: str) -> str:
        """
        Classifies the intent using an LLM via prompt engineering.
        """
        prompt = (
            "You are an intelligent assistant that classifies user requests for DevOps automation.\n"
            "Here are the possible categories (modules) you can assign:\n"
            "- 'instance_creation': for requests about creating or launching virtual machines or servers.\n"
            "- 'storage': for requests about managing or adding storage volumes or disk space.\n"
            "- 'logs': for requests about retrieving or displaying system logs.\n"
            "- 'monitoring': for requests about checking system metrics like CPU, memory, or network usage.\n"
            "- 'ci_cd': for requests about managing Continuous Integration or Continuous Deployment pipelines, builds, or deployments.\n\n"
            "Please classify the following user message into ALL relevant categories from the list above.\n"
            "If the request does not fit any of the categories, return an empty list.\n"
            "Return the category names as a JSON list of strings, nothing else.\n\n"
            "Examples:\n"
            'User message: "Launch a new instance and show me current CPU usage"\n'
            'Categories: ["instance_creation", "monitoring"]\n\n'
            'User message: "Show server logs"\n'
            'Categories: ["logs"]\n\n'
            'User message: "Tell me a joke"\n'
            "Categories: []\n\n"  # Example for unknown/no match
            f'User message: "{message}"\n'
            "Categories:"
        )

        try:

            response = self.llm_client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=20,
                temperature=0,
            )
            predicted_categories = response.choices[0].message.content.strip().lower()
            predicted_categories_list = json.loads(predicted_categories)

            # Validate the returned categories against our known list
            valid_categories = []
            for cat in predicted_categories_list:
                if cat in self.possible_modules:
                    valid_categories.append(cat)

            # If no valid categories are found, return ['unknown'] as a fallback for router
            if not valid_categories:
                return ["unknown"]

            return valid_categories

        except Exception as e:
            return "unknown"  # Fallback in case of API error


intent_classifier = IntentClassifier()
