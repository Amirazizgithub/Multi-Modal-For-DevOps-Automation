# app/models/storage_model.py
import re


class StorageModel:
    """
    Simulates storage management tasks.
    Handles requests like "Add 50GB to my current volume".
    """

    def handle(self, user_id: str, message: str) -> dict:
        """
        Processes storage modification requests.
        Extracts amount and unit (GB, TB) if provided.
        """

        if (
            ("add" in message)
            and ("mb" in message or "gb" in message or "tb" in message)
            and ("volume" in message or "storage" in message)
        ):
            amount = "0"
            unit = "GB"

            # Extract numerical amount
            amount_match = re.search(r"(\d+)\s*(mb|gb|tb)", message)
            if amount_match:
                amount = amount_match.group(1)
                unit = amount_match.group(2).upper()

            return {
                "reply": f"Successfully added {amount}{unit} to current volume.",
                "module": "storage",
                "status": "success",
            }
        elif "increase storage" in message or "expand volume" in message:
            amount = "0"
            unit = "GB"

            # Extract numerical amount
            amount_match = re.search(r"(\d+)\s*(mb|gb|tb)", message)
            if amount_match:
                amount = amount_match.group(1)
                unit = amount_match.group(2).upper()
            return {
                "reply": f"Storage expansion initiated. Successfully added {amount}{unit} to current volume.",
                "module": "storage",
                "status": "success",
            }

        return {
            "reply": "I can help manage storage. Try: 'Add 50GB to my current volume'.",
            "module": "storage",
            "status": "failure",
        }


# Instantiate the model for use by the router
storage_model_instance = StorageModel()
