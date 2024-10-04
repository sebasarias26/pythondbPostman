from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

dataBaseName="gestionbd"

userName="root"

userPassword=""

conexionPort="3306"

serverConnection="localhost"

connectionToDataBase=f"mysql+mysqlconnector://{userName}:{userPassword}@{serverConnection}:{conexionPort}/{dataBaseName}"

engine=create_engine(connectionToDataBase)
sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)


