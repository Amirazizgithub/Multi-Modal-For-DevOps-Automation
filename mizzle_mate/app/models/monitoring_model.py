# app/models/monitoring_model.py
import random


class MonitoringModel:
    """
    Simulates monitoring metrics like CPU usage.
    Handles requests like "How's the CPU usage today?".
    """

    def handle(self, user_id: str, message: str) -> dict:
        """
        Processes monitoring requests.
        Provides simulated metrics for CPU, memory, or network.
        """

        if "cpu usage" in message:
            cpu_usage = round(random.uniform(10.0, 90.0), 2)
            status = "normal"
            if cpu_usage > 75.0:
                status = "high"
            return {
                "reply": f"Current CPU usage is {cpu_usage}%. Status: {status}.",
                "module": "monitoring",
                "status": "success",
            }
        elif "memory usage" in message or "ram usage" in message:
            memory_usage = round(random.uniform(20.0, 85.0), 2)
            status = "normal"
            if memory_usage > 80.0:
                status = "critical"
            return {
                "reply": f"Current memory/ram usage is {memory_usage}%. Status: {status}.",
                "module": "monitoring",
                "status": "success",
            }
        elif "network traffic" in message or "network usage" in message:
            network_traffic = round(random.uniform(50, 500), 2)
            return {
                "reply": f"Current network/usage traffic is {network_traffic} Mbps.",
                "module": "monitoring",
                "status": "success",
            }

        return {
            "reply": "I can provide monitoring data. Try: 'How's the CPU usage today?' or 'Show me network traffic'.",
            "module": "monitoring",
            "status": "failure",
        }


# Instantiate the model for use by the router
monitoring_model_instance = MonitoringModel()
