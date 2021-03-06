from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    fio: str
    iin: str
    tel: str
    email: str
    scan_udv : bool



class UserCreate(UserBase):
    password: str
    repeat_password: str

class UserUpdate(UserCreate):
    old_password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

# class ShowUser(BaseModel):
#     email: str
#     is_active: bool
