"""Test API endpoints for database verification."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from models.test_model import TestEntity
from schemas.test_schema import TestEntityCreate, TestEntityUpdate, TestEntityResponse

router = APIRouter(
    prefix="/test",
    tags=["Test Entities"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/entities",
    response_model=TestEntityResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a test entity",
    description="Create a new test entity in the database. Use this to test database connectivity and CRUD operations."
)
async def create_test_entity(
    entity: TestEntityCreate,
    db: AsyncSession = Depends(get_db)
) -> TestEntityResponse:
    """Create a new test entity."""
    db_entity = TestEntity(
        name=entity.name,
        description=entity.description,
        is_active=entity.is_active
    )
    db.add(db_entity)
    await db.flush()
    await db.refresh(db_entity)
    return db_entity


@router.get(
    "/entities",
    response_model=List[TestEntityResponse],
    summary="List all test entities",
    description="Retrieve all test entities from the database."
)
async def list_test_entities(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
) -> List[TestEntityResponse]:
    """Get all test entities."""
    result = await db.execute(
        select(TestEntity)
        .offset(skip)
        .limit(limit)
    )
    entities = result.scalars().all()
    return entities


@router.get(
    "/entities/{entity_id}",
    response_model=TestEntityResponse,
    summary="Get a test entity by ID",
    description="Retrieve a specific test entity by its ID."
)
async def get_test_entity(
    entity_id: int,
    db: AsyncSession = Depends(get_db)
) -> TestEntityResponse:
    """Get a test entity by ID."""
    result = await db.execute(
        select(TestEntity).where(TestEntity.id == entity_id)
    )
    entity = result.scalar_one_or_none()
    
    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test entity with id {entity_id} not found"
        )
    
    return entity


@router.put(
    "/entities/{entity_id}",
    response_model=TestEntityResponse,
    summary="Update a test entity",
    description="Update an existing test entity."
)
async def update_test_entity(
    entity_id: int,
    entity_update: TestEntityUpdate,
    db: AsyncSession = Depends(get_db)
) -> TestEntityResponse:
    """Update a test entity."""
    result = await db.execute(
        select(TestEntity).where(TestEntity.id == entity_id)
    )
    entity = result.scalar_one_or_none()
    
    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test entity with id {entity_id} not found"
        )
    
    # Update only provided fields
    update_data = entity_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(entity, field, value)
    
    await db.flush()
    await db.refresh(entity)
    return entity


@router.delete(
    "/entities/{entity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a test entity",
    description="Delete a test entity from the database."
)
async def delete_test_entity(
    entity_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a test entity."""
    result = await db.execute(
        select(TestEntity).where(TestEntity.id == entity_id)
    )
    entity = result.scalar_one_or_none()
    
    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test entity with id {entity_id} not found"
        )
    
    await db.delete(entity)
    return None
