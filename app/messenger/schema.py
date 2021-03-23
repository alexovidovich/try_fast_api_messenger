from pydantic import BaseModel
from datetime import datetime
class UserSerializer(BaseModel):
    email :str
    password :str
    _phone_number:int
    country_code :str
    nickname :str
    

class UserSerializerDb(BaseModel):
    email :str
    nickname :str
    image: any
    is_active:bool
    is_admin:bool
    created: datetime
    class Config:
        orm_mode=True