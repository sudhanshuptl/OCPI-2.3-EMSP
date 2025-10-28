"""Test model to verify database setup and migrations."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.sql import func

from core.database import Base


class TestEntity(Base):
    """
    Test entity model for database verification.
    
    This model can be used to test:
    - Database connection
    - Migrations with Alembic
    - CRUD operations
    - SQLAlchemy async operations
    """
    __tablename__ = "test_entities"
    __table_args__ = {'schema': 'OCPI_2_3'}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<TestEntity(id={self.id}, name='{self.name}', is_active={self.is_active})>"
