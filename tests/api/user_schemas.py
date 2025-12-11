from pydantic import BaseModel, EmailStr


class UserResponseSchema(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    address: dict
    phone: str
    website: str
    company: dict
