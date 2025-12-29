import sys
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log details of each request."""
    # Log the request details
    logging.info(f"Request: {request.method} {request.url}")
    logging.info(f"Headers: {request.headers}")
    logging.info(f"Query Params: {request.query_params}")
    logging.info(f"Body: {await request.body()}")
    logging.info(f"IP: {request.client.host}")
    # Process the request
    response = await call_next(request)
    # Log the response status code
    logging.info(f"Response status: {response.status_code}")
    return response

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
async def catch_all(path: str, request: Request):
    """Handle any path and method."""
    # Optionally return details about the request
    return {
        "message": "Request received",
        "method": request.method,
        "path": path,
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "body": await request.body(),
        "ip": request.client.host
    }