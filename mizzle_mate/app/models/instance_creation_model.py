# app/models/instance_creation_model.py
import re


class InstanceCreationModel:
    """
    Simulates the creation of a new instance based on user requests.
    Handles messages like "Launch a new server" or "Create EC2-like instance".
    """

    def handle(self, user_id: str, message: str) -> dict:
        """
        Processes instance creation requests.
        Extracts RAM and CPU details if provided, otherwise uses defaults.
        """
        ram = "unknown"
        cpu = "unknown"

        # Simple parsing for RAM and CPU
        if "ram" in message:
            try:
                # Look for numbers followed by 'gb' or 'ram'
                ram_match = re.search(r"(\d+)\s*gb\s*ram", message)
                if not ram_match:
                    ram_match = re.search(r"(\d+)\s*gb", message)
                if ram_match:
                    ram = f"{ram_match.group(1)}GB"
            except Exception as e:
                print(f"Error parsing RAM: {e}")

        if "cpu" in message:
            try:
                # Look for numbers followed by 'cpu'
                cpu_match = re.search(r"(\d+)\s*cpu?", message)
                if cpu_match:
                    cpu = f"{cpu_match.group(1)} CPUs"
            except Exception as e:
                print(f"Error parsing CPU: {e}")

        if (
            "launch instance" in message
            or "launch new instance" in message
            or "create instance" in message
            or "create new instance" in message
            or "new server" in message
            or "create ec2" in message
            or "create aws ec2" in message
        ):
            reply_message = f"Instance launched"
            if ram != "unknown" and cpu != "unknown":
                reply_message += f" with {ram} RAM and {cpu}."
            elif ram != "unknown":
                reply_message += f" with {ram} RAM."
            elif cpu != "unknown":
                reply_message += f" with {cpu}."
            else:
                reply_message += " successfully with default specifications."

            return {
                "reply": reply_message,
                "module": "instance_creation",
                "status": "success",
            }

        return {
            "reply": "I can help launch new instances. Try: 'Launch an instance with 4GB RAM and 2 CPUs'.",
            "module": "instance_creation",
            "status": "failure",
        }


# Instantiate the model for use by the router
instance_creation_model_instance = InstanceCreationModel()
