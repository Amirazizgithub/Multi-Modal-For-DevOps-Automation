from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

from app.core.intent_classifier import intent_classifier
from app.core.router import router
from app.utils.logger import log_interaction, get_logs
from app.utils.message_preprocessor import message_preprocessor

app = FastAPI(title="Mizzle Mate DevOps Chatbot")


# Pydantic models for request and response
class ChatInput(BaseModel):
    user_id: str
    message: str


# Health Check Endpoint
@app.get("/health", response_model=Dict[str, str])
async def health_check():
    """Checks the health of the chatbot service."""
    return {"status": "Healthy", "message": "Mizzle Mate is up and running!"}


# Logs Endpoint
@app.get("/logs", response_model=List[Dict])
async def get_all_logs():
    """Retrieves all logged interactions."""
    return get_logs()


# Chat Endpoint
@app.post("/chat", response_model=List[Dict])
async def chat_endpoint(input_data: ChatInput):
    """
    Main chat endpoint to process user messages, classify intent,
    route to the appropriate module, and return a response.
    """
    user_id = input_data.user_id
    message = input_data.message

    # Parse user messages (done by FastAPI input_data)
    # Detect the intent/module
    detected_modules = intent_classifier.classify(message)

    # Preprocess the message for better classification
    processed_message = message_preprocessor.preprocess(message)

    # Route the request to the corresponding model/logic handler
    if len(detected_modules) == 1:
        results = []
        response = router.route_request(detected_modules[0], user_id, processed_message)
        results.append(response)

        # Log interaction
        log_interaction(
            user_id=user_id,
            message=message,
            module=response.get("module", "unknown"),
            reply=response.get("reply", "Error processing request."),
            status=response.get("status", "error"),
        )

        # Respond appropriately
        return results

    elif len(detected_modules) > 1:
        # If multiple modules are detected
        results = []
        for detected_module in detected_modules:
            response = router.route_request(detected_module, user_id, processed_message)
            results.append(response)

        # Log interaction
        log_interaction(
            user_id=user_id,
            message=message,
            module=response.get("module", "unknown"),
            reply=response.get("reply", "Error processing request."),
            status=response.get("status", "error"),
        )

        return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
