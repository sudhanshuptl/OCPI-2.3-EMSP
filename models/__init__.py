"""Database models package."""
from core.database import Base

# Import all models here for Alembic to detect them
from .test_model import TestEntity

__all__ = ["Base", "TestEntity"]
