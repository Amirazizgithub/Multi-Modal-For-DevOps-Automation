# Mizzle Mate – Multi-Modal DevOps Automation

**Mizzle Mate** is an AI-powered multi-modal chatbot designed to streamline DevOps automation. It leverages LLMs, computer vision, and structured data processing to optimize CI/CD pipelines, infrastructure monitoring, and security compliance. Built with FastAPI, Docker, and AWS ECS, it enables real-time anomaly detection, log analysis, and troubleshooting.

---

## Features

- **AI-Powered CI/CD Monitoring** – Automates deployment tracking and optimizes workflows.
- **Intent Detection & Routing** – Uses NLP to classify user queries and direct requests to the right module.
- **Infrastructure & Log Analysis** – Parses system logs for anomaly detection and troubleshooting.
- **Multi-Modal Support** – Handles structured data, logs, and AI-driven insights.
- **Cloud Integration** – Deployable on AWS ECS, Lambda, or Kubernetes.

## Folder Structure

```plaintext
mizzle_mate/
├── app/
│   ├── main.py                # FastAPI application
│   ├── __init__.py
│   ├── models/                # Simulated models/modules
│   │   ├── __init__.py
│   │   ├── ci_cd_model.py
│   │   ├── instance_creation_model.py
│   │   ├── logs_model.py
│   │   ├── monitoring_model.py
│   │   └── storage_model.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── intent_classifier.py  # Intent detection logic
│   │   └── router.py             # Request routing logic
│   └── utils/
│       ├── __init__.py
│       ├── message_preprocessor.py # NLP preprocessing
│       └── logger.py               # Logging utility
├── config/
│   └── modules.json           # Module configuration/registry
├── Dockerfile                 # For Docker deployment
├── requirements.txt           # Python dependencies
├── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Amirazizgithub/Multi-Modal-For-DevOps-Automation.git
cd mizzle_mate
```

### 2. Create and Activate a Virtual Environment & Install Dependencies

On **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

On **Linux/macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the API

```sh
uvicorn app.main:app --reload
```

## Usage

- **Start API Server** – Access the chatbot via REST endpoints.
- **Monitor Logs & Deployments** – Use integrated models to analyze system health.
- **Deploy with Docker** – Build and run the containerized application:

```sh
docker build -t mizzle-mate .
docker run -p 8000:8000 mizzle-mate
```

## API Endpoints

- `GET /health` – Health check for the service.
- `GET /logs` – Retrieve all logged interactions.
- `POST /chat` – Send a message to the chatbot.
    - **Request Body:**
      ```json
      {
        "user_id": "dev100",
        "message": "Create a new CI/CD pipeline for frontend"
      }
      ```
    - **Response:** List of module responses.

## Example Request

```sh
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "dev100", "message": "Create a new CI/CD pipeline for frontend"}'
```

## Future Enhancements

- Extend multi-agent AI for workflow orchestration.
- Enhance security automation for compliance checks.
- Optimize retrieval-based reasoning with advanced chunking techniques.

---

MIT License © 2025 Amir Aziz