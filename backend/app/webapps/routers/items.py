from fastapi import APIRouter, Request, Depends, HTTPException
import schemas.schemas as schemas
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import get_db
import db.crud as crud


router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")

@router.get("/")
def item_home(request: Request):
    return templates.TemplateResponse("item_homepage.html", {"request": request})


@router.get("/registration", response_model=schemas.User, tags=["Users"])
def registration(request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    check_user = crud.check_user(user)
    if check_user is False:
        raise HTTPException(status_code=400, detail="Passwords don't match")
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)