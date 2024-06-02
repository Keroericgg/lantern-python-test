from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from asgi_correlation_id import CorrelationIdMiddleware

from .logger import logger, configure_logging
from .routers import company

app = FastAPI(on_startup=[configure_logging])


@app.exception_handler(FileNotFoundError)
async def validation_exception_handler(request: Request, exc: FileNotFoundError):
    logger.error(f"A File Not Found Error is thrown", extra={"data": None})
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({"message": str(exc), "filename": exc.filename}),
    )


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    logger.error(f"A Validation Error for '{exc.title}' is thrown", extra={"data": exc.errors()})
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"message": f"Validation Error for {exc.title}"}),
    )


@app.exception_handler(ValueError)
async def validation_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"message": str(exc)}),
    )


app.add_middleware(CorrelationIdMiddleware)
app.include_router(company.router)
