from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

database_url="mysql+pymsql://root:Bankai@123@localhost/fastapi"
engine =create_engine(database_url)


session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
