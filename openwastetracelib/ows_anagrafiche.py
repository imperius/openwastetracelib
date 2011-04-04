from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session


from db_metadata import *
from db_mapper import *

import wsdl_anagrafiche  as wa

dbengine = create_engine(config.DB_STRING, echo=False)
meta = MetaData()
meta.bind = dbengine
Session = sessionmaker(bind=dbengine)
session = Session()



#Funsioni da implementare

# owsGetAzienda
# owsUpAzienda
# owsUpAllAzienda
#

def owsGetAzienda (codiceFiscale):
    az, sl, sedesummary=wa.GetAzienda(codiceFiscale)
    test=session.query(Azienda).filter (Azienda.codiceFiscale == codiceFiscale)
    if test.count()==0:
        #non c'e' aggiungo
        session.add(az)
    else:
        az=test.one()


    az.RelSedeLegale.append(sl)
    session.add(sl)

    for sede1 in sedesummary:
        az.RelSedi.append(sede1)
        session.add(sede1)

    session.commit()