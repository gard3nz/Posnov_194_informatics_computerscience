from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.orm import declarative_base

# Базовый класс для всех моделей
Base = declarative_base()

# Таблица Artist
class Customer(Base):
    __tablename__ = 'Customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)


# Настройка подключения к базе данных
def setup_database(database_path="sqlite:///customer.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


engine = setup_database("sqlite:///customer.sqlite")
session = create_session(engine)

session.commit()
