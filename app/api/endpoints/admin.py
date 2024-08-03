# app/api/endpoints/admin.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.security import get_current_user

router = APIRouter()

@router.post("/admin/user/professional-status", response_model=schemas.User)
def upgrade_professional_status(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not current_user.has_role(models.UserRole.ADMIN):
        raise HTTPException(status_code=403, detail="Not authorized")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.update_professional_status(True)
    db.commit()
    db.refresh(user)
    return user
