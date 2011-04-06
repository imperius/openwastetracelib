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

#def owsGetUpAzienda (az):
    #data un oggetto azienda restituisce l'oggetto azienda eventualmente aggiornato, si occupa del salvataggio sul db.
    #test=session.query(Azienda).filter (Azienda.codiceFiscale == az.codiceFiscale)
    #if test.count()==0:
        ##non c'e' --> aggiungo
        #aznew=az
        #session.add(aznew)
        #session.commit()
    #else:
        ##intanto per ora prendo per buono quello del database.
        #aznew=test.one()
        ##c'e' controlla il numero di versione
        #if az.versione!=test.one().versione:
            ##aggiorna il record, si copia il vecchio id sul nuovo, e sostituice l'oggetto
            #az.Aid=test.one().Aid
            #aznew=az
            #session.merge(aznew)
            #session.commit()
    ##in aznew c'e' sicuramente l'oggetto giusto
    #return aznew

def owsGetUpAzienda (az):
    #data un oggetto azienda restituisce l'oggetto azienda eventualmente aggiornato, si occupa del salvataggio sul db.
    session.merge(az)
    session.commit()
    #in aznew c'e' sicuramente l'oggetto giusto
    return az



def owsGetUpSedeLegale (az, sl):
    #dato un oggetto sede legale e un azienda associata aggiorna eventualmente l'oggetto sede legale , si occupa del salvataggio su db e non restituisce niente.
    test=session.query(SedeLegale).filter (SedeLegale.idSIS == sl.idSIS)
    if test.count()==0:
        az.RelSedeLegale.append(sl)
        session.add(sl)
    else:
        sldb=test.one()
        if sldb.versione!=sl.versione:
            sl.Slid=sldb.Slid
            sldb=sl
            #non serve appende perche' e' gia appeso
            #az.RelSedeLegale.append(sldb)
            session.merge(sldb)
    session.commit()

def owsGetUpSedeSummary (az, sedesummary):
    #data un azienda e una sedesummary (che e' una lista di sedi), aggiorna le sedi e si occupa del saltaggio sul db.
    for sede1 in sedesummary:
        az.RelSedi.append(sede1)
        session.add(sede1)

