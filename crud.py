from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select
import schemas, models

def get_user(db: Session, user_id: int):
    return db.execute(select(models.User).where(models.User.id == user_id)).first()

def get_user_by_email(db: Session, email: str):
    return db.execute(select(models.User).where(models.User.email == email)).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()  
    db.refresh(db_user)
    return db_user
