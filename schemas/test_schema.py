"""Pydantic schemas for test entity."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
import uuid


class TestEntityBase(BaseModel):
    """Base schema for test entity."""
    name: str = Field(..., min_length=1, max_length=100, description="Name of the test entity")
    description: Optional[str] = Field(None, description="Description of the test entity")
    is_active: bool = Field(default=True, description="Whether the entity is active")


class TestEntityCreate(TestEntityBase):
    """Schema for creating a test entity with pre-populated defaults for Swagger."""
    name: str = Field(
        default="Test Entity " + str(uuid.uuid4())[:8],
        min_length=1,
        max_length=100,
        description="Name of the test entity"
    )
    description: Optional[str] = Field(
        default="This is a test entity created via API",
        description="Description of the test entity"
    )
    is_active: bool = Field(
        default=True,
        description="Whether the entity is active"
    )


class TestEntityUpdate(BaseModel):
    """Schema for updating a test entity."""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Name of the test entity")
    description: Optional[str] = Field(None, description="Description of the test entity")
    is_active: Optional[bool] = Field(None, description="Whether the entity is active")


class TestEntityResponse(TestEntityBase):
    """Schema for test entity response."""
    id: int = Field(..., description="Unique identifier")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    model_config = ConfigDict(from_attributes=True)
