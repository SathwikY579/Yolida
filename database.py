from sqlalchemy import create_engine, Column, Integer, String, Text, BLOB, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # This should be encrypted

class QueryHistory(Base):
    __tablename__ = 'query_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    user = relationship("User", back_populates="history")

User.history = relationship("QueryHistory", order_by=QueryHistory.id, back_populates="user")

def get_engine():
    return create_engine('sqlite:///document_query.db')

def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
