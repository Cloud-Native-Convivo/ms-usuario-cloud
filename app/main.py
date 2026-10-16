import logging

from fastapi import FastAPI

from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.security_middleware import SecurityMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="MS Usuario")

app.add_middleware(SecurityMiddleware)
app.add_middleware(LoggingMiddleware)
