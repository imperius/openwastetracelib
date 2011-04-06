from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session


from db_metadata import *
from db_mapper import *

import wsdl_anagrafiche as wa

dbengine = create_engine(config.DB_STRING, echo=False)
meta = MetaData()
meta.bind = dbengine
Session = sessionmaker(bind=dbengine)
session = Session()


#Funzioni da implementare

# owsAzienda
# owsGetUpAzienda
# owsGetUpSedeLegale
# owsGetUpSedeSummary

# owsUpAllAzienda
#
def owsAzienda (codiceFiscale):
    az, sl, sedesummary=wa.GetAzienda(codiceFiscale)
    az=owsGetUpAzienda (az)
    owsGetUpSedeLegale (az, sl)
    owsGetUpSedeSummary (az, sedesummary)


def owsGetUpAzienda (az):
    #data un oggetto azienda restituisce l'oggetto azienda eventualmente aggiornato, si occupa del salvataggio sul db.
    session.merge(az)
    session.commit()
    return az

def owsGetUpSedeLegale (az, sl):
    #dato un oggetto sede legale e un azienda associata aggiorna eventualmente l'oggetto sede legale , si occupa del salvataggio su db e non restituisce niente.
    session.merge(sl)
    az.RelSedeLegale.append(sl)
    session.commit()

def owsGetUpSedeSummary (az, sedesummary):
    #data un azienda e una sedesummary (che e' una lista di sedi), aggiorna le sedi e si occupa del saltaggio sul db.
    for sede1 in sedesummary:
        session.merge(sede1)
        az.RelSediSummary.append(sede1)
        session.commit()

