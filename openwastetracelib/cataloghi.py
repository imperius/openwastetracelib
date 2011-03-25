# http://www.sqlalchemy.org/docs/orm/tutorial.html

import config

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(config.DB_STRING, echo=True)
Base = declarative_base(bind=engine)
Session = scoped_session(sessionmaker(engine))

class Stati_scheda_sistri(Base):
    __tablename__ = 'stati_scheda_sistri'

    sssid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_stato_scheda_sistri = Column(String(255),nullable=False,index=True)
    stato_scheda_sistri = Column(String(255),nullable=False )

    def __init__ (self,id_stato_scheda_sistri,stato_scheda_sistri):
        # sssid
        self.id_stato_scheda_sistri = id_stato_scheda_sistri
        self.stato_scheda_sistri = stato_scheda_sistri

    def __repr__(self):
       return "<Stati_scheda_sistri('%s','%s')>" % (self.id_stato_scheda_sistri,
                                                    self.stato_scheda_sistri)

#class Stati_fisici_rifiuto(object):

#    def __init__ (self, id_stato_fisico_rifiuto, descr_stato_fisico_rifiuto, codice_stato_fisico):
#        # sfrid
#        self.id_stato_fisico_rifiuto = id_stato_fisico_rifiuto
#        self.descr_stato_fisico_rifiuto = descr_stato_fisico_rifiuto
#        self.codice_stato_fisico = codice_stato_fisico

Base.metadata.create_all()
