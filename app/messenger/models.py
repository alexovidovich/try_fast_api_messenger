from core.db import Base 

from sqlalchemy_utils import PhoneNumber,EmailType
from sqlalchemy import orm,Column,String,Integer,Text,DateTime, Unicode, Boolean, Table, ForeignKey
from sqlalchemy_imageattach.entity import Image, image_attachment

import datetime
class User(Base):
    """User model."""

    id = Column(Integer, primary_key=True, index=True,unique=True)
    email = Column(EmailType,unique=True,)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    _phone_number = Column(Unicode(20),unique=True)
    image = image_attachment('UserPicture')
    country_code = Column(Unicode(8))
    nickname = Column(String(30),)
    is_admin = Column(Boolean,default=False)
    created= Column(DateTime,default=datetime.datetime.utcnow)
    chat_set = orm.relationship("User_Chat",back_populates='user')
    phone_number = orm.composite(
        PhoneNumber,
        _phone_number,
        country_code
    )
    __tablename__ = "user"

class User_Picture(Base, Image):
    """User picture model."""

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = orm.relationship('User')
    __tablename__ = 'user_picture'

  
class Chat(Base):
  __tablename__ = 'chat'
  id = Column(Integer, primary_key=True)
  member_set = orm.relationship('User_Chat',back_populates='chat')
  name = Column(String(50))
  message_set = orm.relationship('Message',back_populates='owner')

class User_Chat(Base):
  __tablename__ = 'user_chat'
  chat_id = Column(Integer, ForeignKey('chat.id'), primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
  date_joined = Column(DateTime,default=datetime.datetime.utcnow)
  role = Column(String(20))

  chat = orm.relationship("Chat",back_populates='member_set')
   
  user = orm.relationship("User", back_populates="chat_set")

class Message_Picture(Base, Image):
    """User picture model."""

    message_id = Column(Integer, ForeignKey('message.id'), primary_key=True)
    message = orm.relationship('Message')
    __tablename__ = 'message_picture'

class Message(Base):
  __tablename__ = 'message'
  id = Column(Integer, primary_key=True)
  chat_id =  orm.relationship('Chat',back_populates='message_set')
  text = Column(Text)
  owner_id = Column(Integer,ForeignKey("user.id"))
  owner =  orm.relationship(User, back_populates='message_set')
  date = Column(DateTime,default=datetime.datetime.utcnow)
  image = image_attachment('UserPicture')



  

   