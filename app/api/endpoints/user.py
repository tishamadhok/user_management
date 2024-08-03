from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List, Optional

router = APIRouter()

@router.get("/users", response_model=List[schemas.User])
def list_users(
    db: Session = Depends(get_db),
    username: Optional[str] = None,
    email: Optional[str] = None,
    role: Optional[models.UserRole] = None,
    created_before: Optional[datetime] = None,
    created_after: Optional[datetime] = None,
    is_active: Optional[bool] = None,
):
    query = db.query(models.User)
    if username:
        query = query.filter(models.User.username.contains(username))
    if email:
        query = query.filter(models.User.email.contains(email))
    if role:
        query = query.filter(models.User.role == role)
    if created_before:
        query = query.filter(models.User.created_at <= created_before)
    if created_after:
        query = query.filter(models.User.created_at >= created_after)
    if is_active is not None:
        query = query.filter(models.User.is_active == is_active)
    return query.all()
