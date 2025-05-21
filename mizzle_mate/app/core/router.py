import importlib
import json


class ModuleRouter:
    def __init__(self, config_path="config/modules.json"):
        self.module_map = {}
        with open(config_path, "r") as f:
            self.module_config = json.load(f)
        self.loaded_modules = {}  # For lazy loading

    def route_request(self, module_name: str, user_id: str, message: str) -> dict:
        if module_name == "unknown":
            return {
                "reply": "I'm sorry, I don't understand that request. Please try rephrasing.",
                "module": "unknown",
                "status": "failure",
            }

        # Lazy loading of modules
        if module_name not in self.loaded_modules:
            try:
                # Assuming module_name maps directly to file name without '_model'
                # and contains an instance named '<module_name>_instance'
                module_file_name = self.module_config.get(module_name)
                if not module_file_name:
                    raise ImportError(f"Module configuration missing for {module_name}")

                # Dynamically import the module
                module = importlib.import_module(f"app.models.{module_file_name}")

                # Assuming the instance is named after the module (e.g., ci_cd_model_instance)
                self.loaded_modules[module_name] = getattr(
                    module, f"{module_file_name}_instance"
                )

            except (ImportError, AttributeError) as e:
                return {
                    "reply": f"Internal error: Could not load handler for {module_name}. Error: {str(e)}",
                    "module": module_name,
                    "status": "error",
                }

        handler = self.loaded_modules[module_name]
        return handler.handle(user_id, message)


router = ModuleRouter()
