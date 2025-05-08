"""Logger configuration."""

import os
import sys

from loguru import logger

from core.config import get_settings

settings = get_settings()


def configure_logger():
    """Configure the logger with common settings."""
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Remove default logger
    logger.remove()

    # Configure console logger with pretty formatting and colors
    logger.add(
        sys.stdout,
        level=settings.log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True,
    )

    # Configure file logger with rotation
    logger.add(
        "logs/app.log",
        rotation="10 MB",
        retention="1 week",
        level=settings.log_level,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        enqueue=True,  # Makes logging thread-safe
    )

    # Configure JSON logger for structured logging (useful for log analysis tools)
    if settings.api_env.value == "production":
        logger.add(
            "logs/app.json",
            rotation="10 MB",
            retention="1 week",
            level=settings.log_level,
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name}:{function}:{line} - {message}",
            serialize=True,
            enqueue=True,
        )

    logger.info(f"Logger configured with level {settings.log_level}")
    return logger


logger = configure_logger()
