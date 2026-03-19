from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.orm import relationship  
from sqlalchemy.ext.declarative import declarative_base  

Base = declarative_base()  

class User(Base):  
    __tablename__ = 'users'  
    id = Column(Integer, primary_key=True)  
    username = Column(String, unique=True)  
    conversations = relationship('Conversation', back_populates='user')  

class Conversation(Base):  
    __tablename__ = 'conversations'  
    id = Column(Integer, primary_key=True)  
    user_id = Column(Integer, ForeignKey('users.id'))  
    content = Column(String)  
    user = relationship('User', back_populates='conversations')  
    interactions = relationship('BotInteraction', back_populates='conversation')  

class BotInteraction(Base):  
    __tablename__ = 'bot_interactions'  
    id = Column(Integer, primary_key=True)  
    conversation_id = Column(Integer, ForeignKey('conversations.id'))  
    response = Column(String)  
    conversation = relationship('Conversation', back_populates='interactions')  

# Other necessary SQLAlchemy setup (e.g. engine creation) goes here
