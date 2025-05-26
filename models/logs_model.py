# app/models/logs_model.py
from datetime import datetime, timedelta


class LogsModel:
    """
    Simulates fetching and displaying server logs.
    Handles requests like "Show me server logs from yesterday".
    """

    def handle(self, user_id: str, message: str) -> dict:
        """
        Processes log retrieval requests.
        Provides dummy log data based on keywords like 'yesterday', 'today', 'last week'.
        """
        log_period = "today"

        if "yesterday" in message:
            log_period = "yesterday"
        elif "last week" in message or "past week" in message:
            log_period = "last week"
        elif "all" in message or "full" in message:
            log_period = "all time"

        # Simulate fetching logs
        dummy_logs = []
        if log_period == "today":
            dummy_logs = [
                f"[INFO] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Application started.",
                f"[DEBUG] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User '{user_id}' accessed dashboard.",
            ]
        elif log_period == "yesterday":
            yesterday = datetime.now() - timedelta(days=1)
            dummy_logs = [
                f"[INFO] {yesterday.strftime('%Y-%m-%d %H:%M:%S')}: Server rebooted.",
                f"[ERROR] {yesterday.strftime('%Y-%m-%d %H:%M:%S')}: Database connection failed.",
            ]
        elif log_period == "last week":
            dummy_logs = [
                f"[WARNING] {(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')}: High CPU usage detected.",
                f"[INFO] {(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}: Security patch applied.",
            ]
        else:  # all time
            dummy_logs = [
                f"[INFO] 2024-01-01: System initialized.",
                f"[CRITICAL] 2024-03-15: Major outage detected.",
                f"[INFO] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Latest activity.",
            ]

        if (
            "show log" in message
            or "show server log" in message
            or "get log" in message
            or "get server log" in message
            or "fetch log" in message
            or "fetch server log" in message
            or "display log" in message
            or "display server log" in message
        ):
            if dummy_logs:
                return {
                    "reply": f"Here are the server logs for {log_period}: "
                    + " ".join(dummy_logs),
                    "module": "logs",
                    "status": "success",
                }
            else:
                return {
                    "reply": f"No logs found for {log_period}.",
                    "module": "logs",
                    "status": "success",
                }

        return {
            "reply": "I can show you server logs. Try: 'Show me server logs'.",
            "module": "logs",
            "status": "failure",
        }


# Instantiate the model for use by the router
logs_model_instance = LogsModel()
