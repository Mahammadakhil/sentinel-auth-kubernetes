"""Sentinel-Auth — FastAPI application entry point."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import time
import logging

from api.routes import router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sentinel-auth")

# -------------------------------
# CREATE APP
# -------------------------------
app = FastAPI(
    title="Sentinel-Auth",
    description="Secure user registration service",
    version="1.0.0",
)

# -------------------------------
# ADD MIDDLEWARE (CORS)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# -------------------------------
# LOGGING MIDDLEWARE
# -------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    if request.method == "OPTIONS":
        logger.info(
            f"PREFLIGHT: Path={request.url.path} Origin={request.headers.get('origin')}"
        )

    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    logger.info(
        f"Method: {request.method} Path: {request.url.path} "
        f"Status: {response.status_code} Duration: {duration:.2f}s"
    )
    return response

# -------------------------------
# BASIC HEALTH CHECK
# -------------------------------
@app.get("/ping")
def ping():
    return "pong"

# -------------------------------
# INCLUDE ROUTES
# -------------------------------
app.include_router(router, prefix="/api")

# -------------------------------
# PROMETHEUS METRICS (LAST STEP)
# -------------------------------
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False
)
