from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username="admin",
    host="dnd_postgres_db",
    password="root",
    database="dndDB",
    port="5432"
)
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()