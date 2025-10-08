from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

database_url = "mysql+pymysql://root:Bankai%40123@localhost/fastapi"




engine =create_engine(database_url)


session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
