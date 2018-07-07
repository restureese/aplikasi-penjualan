from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://restureese:@localhost/toko", isolation_level="READ UNCOMMITTED")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init():
	#import models
	from Penjualan import models
	Base.metadata.create_all(bind=engine)