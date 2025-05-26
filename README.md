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

├── models/                     # Simulated models/modules
│   ├── __init__.py
│   ├── ci_cd_model.py
│   ├── instance_creation_model.py
│   ├── logs_model.py
│   ├── monitoring_model.py
│   └── storage_model.py
├── core/
│   ├── __init__.py
│   ├── intent_classifier.py    # Intent detection logic
│   └── router.py               # Request routing logic
│── utils/
│   ├── __init__.py
│   ├── message_preprocessor.py # NLP preprocessing
│   └── logger.py               # Logging utility
├── config/
│   └── modules.json            # Module configuration/registry
├── tests/
│   ├── __init__.py             # Makes 'tests' a Python package
│   └── test_api.py             # Testing FastAPIs in ci/cd pipeline
├── .github/                    # GitHub Actions workflow directory
│   └── workflows/
│       └── ci-cd-pipeline.yaml # CI/CD pipeline definition
├── app.py                      # Main FastAPI application entry point
├── __init__.py
├── .env                        # Environment variables
├── .gitignore                  # Files and directories to ignore in Git
├── .dockerignore               # Files and directories to ignore in Docker builds
├── Dockerfile                  # For Docker deployment
├── requirements.txt            # Python dependencies
└── README.md                   # Project README file
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Amirazizgithub/Multi-Modal-For-DevOps-Automation.git
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
uvicorn app:app --reload
```

## Usage

- **Start API Server** – Access the chatbot via REST endpoints.
- **Monitor Logs & Deployments** – Use integrated models to analyze system health.
- **Deploy with Docker** – Build and run the containerized application:

```sh
docker build -t mizzle-mate .
docker run -p 8000:8000 mizzle-mate
```

## Deploying to AWS ECS

You can deploy Mizzle Mate as a Docker container on AWS ECS (Elastic Container Service) for scalable, production-grade hosting.

### 1. Build and Push Docker Image to Amazon ECR

- Authenticate Docker to your ECR registry:
  ```sh
  aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
  ```

- Build your Docker image:
  ```sh
  docker build -t mizzle-mate .
  ```

- Tag the image for ECR:
  ```sh
  docker tag mizzle-mate:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/mizzle-mate:latest
  ```

- Push the image to ECR:
  ```sh
  docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/mizzle-mate:latest
  ```

### 2. Create an ECS Cluster and Task Definition

- In the AWS ECS console, create a new cluster (e.g., "MizzleMateCluster").
- Define a new Task Definition using the pushed ECR image.
- Set environment variables (like `OPENAI_API_KEY`) in the task definition. (I have uploaded a .env file to an AWS S3 bucket and fetched environment variables from this bucket.)

### 3. Run the Service

- Launch a service in your ECS cluster using the task definition.
- Expose port 8000 (or your chosen port) via a load balancer or security group.

### 4. Access the API

- Once the service is running, access your API using the load balancer DNS or public IP:
  ```
  http://<your-load-balancer-or-ec2-public-ip>:8000
  ```

**Tip:**  
You can automate this workflow using the provided GitHub Actions CI/CD pipeline, which can build and push your Docker image to ECR and trigger ECS deployments on code changes.

---

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.