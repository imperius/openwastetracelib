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
       return "<Stati_scheda_sistri('%s','%s')>" % (self.id_stato_scheda_sistri,self.stato_scheda_sistri)

class Stati_fisici_rifiuto(object):
    __tablename__ = 'stati_fisici_rifiuto'

    sfrid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_stato_fisico_rifiuto = Column(String(255),nullable=False,index=True)
    descr_stato_fisico_rifiuto = Column(String(255),nullable=False )
    codice_stato_fisico = Column(String(255),nullable=False )

    def __init__ (self, id_stato_fisico_rifiuto, descr_stato_fisico_rifiuto, codice_stato_fisico):
        # sfrid
        self.id_stato_fisico_rifiuto = id_stato_fisico_rifiuto
        self.descr_stato_fisico_rifiuto = descr_stato_fisico_rifiuto
        self.codice_stato_fisico = codice_stato_fisico

    def __repr__(self)
       return "<Stati_fisici_rifiuto('%s','%s','%s')>" % (self.id_stato_fisico_rifiuto,self.descr_stato_fisico_rifiuto,self.codice_stato_fisico)

class Forme_giuridiche(object):
    __tablename__ = 'forme_giuridiche'

    fgid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_forma_giuridica = Column(String(255),nullable=False,index=True)
    descrizione_forma_giuridica = Column(String(255),nullable=False )

    def __init__ (self, id_tipo_forma_giuridica, descrizione_forma_giuridica):
        # fgid
        self.id_tipo_forma_giuridica = id_tipo_forma_giuridica
        self.descrizione_forma_giuridica = descrizione_forma_giuridica

    def __repr__(self)
       return "<Forme_giuridiche('%s','%s')>" % (self.id_tipo_forma_giuridica,self.descrizione_forma_giuridica)

class Tipi_reg_cronologico(object):
    __tablename__ = 'tipi_reg_cronologico'

    trcid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_reg_cronologico = Column(String(255),nullable=False,index=True)
    descrizione_tipo_reg_crono = Column(String(255),nullable=False )
    macro_categoria = Column(String(255),nullable=False )

    def __init__ (self,id_tipo_reg_cronologico,descrizione_tipo_reg_crono,macro_categoria):
        # trcid
        self.id_tipo_reg_cronologico = id_tipo_reg_cronologico
        self.descrizione_tipo_reg_crono = descrizione_tipo_reg_crono
        self.macro_categoria = macro_categoria

    def __repr__(self)
       return "<Tipi_reg_cronologico('%s','%s','%s')>" % (self.id_tipo_reg_cronologico,self.descrizione_tipo_reg_crono,self.macro_categoria)

class Operazioni_impianti(object):
    __tablename__ = 'operazioni_impianti'

    oiid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_operazione_impianto = Column(String(255),nullable=False,index=True)
    id_tipo_operazione_impianto = Column(String(255),nullable=False )
    operazione_impianto = Column(String(255),nullable=False )
    ordinamento = Column(Integer,nullable=False )

    def __init__ (self,id_operazione_impianto,id_tipo_operazione_impianto,operazione_impianto,ordinamento):
        # oiid
        self.id_operazione_impianto = id_operazione_impianto
        self.id_tipo_operazione_impianto = id_tipo_operazione_impianto
        self.operazione_impianto = operazione_impianto
        self.ordinamento = ordinamento

    def __repr__(self)
       return "<Operazioni_impianti('%s','%s','%s','%s')>" % (self.id_operazione_impianto,self.id_tipo_operazione_impianto,self.operazione_impianto,self.ordinamento)

class Categorie_raee(object):
    __tablename__ = 'categorie_raee'

    crid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_categoria_raee = Column(String(255),nullable=False,index=True)
    descrizione_categoria_raee = Column(String(255),nullable=False )

    def __init__ (self,id_categoria_raee,descrizione_categoria_raee):
        # crid
        self.id_categoria_raee = id_categoria_raee
        self.descrizione_categoria_raee = descrizione_categoria_raee

    def __repr__(self)
       return "<Categorie_raee('%s','%s')>" % (self.id_categoria_raee,self.descrizione_categoria_raee)

class Tipi_veicolo(object):
    __tablename__ = 'tipi_veicolo'

    tvid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_veicolo = Column(String(255),nullable=False,index=True)
    descrizione = Column(String(255),nullable=False )
    codice_tipo_veicolo = Column(Integer,nullable=False )
    flag_rimorchio = Column(Integer,nullable=False )

    def __init__ (self,id_tipo_veicolo,descrizione,codice_tipo_veicolo,flag_rimorchio):
        # tvid
        self.id_tipo_veicolo = id_tipo_veicolo
        self.descrizione = descrizione
        self.codice_tipo_veicolo = codice_tipo_veicolo
        self.flag_rimorchio = flag_rimorchio

    def __repr__(self)
       return "<Tipi_veicolo('%s','%s','%s','%s')>" % (self.id_tipo_veicolo,self.descrizione,self.codice_tipo_veicolo,self.flag_rimorchio)

class Tipi_sede(object):
    __tablename__ = 'tipi_sede'

    tsid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_sede = Column(String(255),nullable=False,index=True)
    descrizione = Column(String(255),nullable=False )

    def __init__ (self,id_tipo_sede,descrizione):
        # tsid
        self.id_tipo_sede = id_tipo_sede
        self.descrizione = descrizione

    def __repr__(self)
       return "<Tipi_sede('%s','%s')>" % (self.id_tipo_sede,self.descrizione)

class Tipi_registrazioni_crono(object):
    __tablename__ = 'tipi_registrazioni_crono'

    trcid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_registrazione_crono = Column(String(255),nullable=False,index=True)
    descr_tipo_reg_crono = Column(String(255),nullable=False )

    def __init__ (self,id_tipo_registrazione_crono,descr_tipo_reg_crono):
        # trcid
        self.id_tipo_registrazione_crono = id_tipo_registrazione_crono
        self.descr_tipo_reg_crono = descr_tipo_reg_crono

    def __repr__(self)
       return "<Tipi_registrazioni_crono('%s','%s')>" % (self.id_tipo_registrazione_crono,self.descr_tipo_reg_crono)

class Numeri_onu(object):
    __tablename__ = 'numeri_onu'

    noid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_numero_onu = Column(String(255),nullable=False,index=True)
    descrizione_numero_onu = Column(String(255),nullable=False )

    def __init__ (self,id_numero_onu,descrizione_numero_onu):
        # noid
        self.id_numero_onu = id_numero_onu
        self.descrizione_numero_onu = descrizione_numero_onu

    def __repr__(self)
       return "<Numeri_onu('%s','%s')>" % (self.id_numero_onu,self.descrizione_numero_onu)

class Localita_estere(object):
    __tablename__ = 'localita_estere'

    leid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_localita = Column(Integer,nullable=False,index=True)
    nazione = Column(String(255),nullable=False )
    sigla_nazione = Column(String(255),nullable=False )

    def __init__ (self,id_localita,nazione,sigla_nazione):
        # leid
        self.id_localita = id_localita
        self.nazione = nazione
        self.sigla_nazione = sigla_nazione

    def __repr__(self)
       return "<Localita_estere('%s','%s','%s')>" % (self.id_localita,self.nazione,self.sigla_nazione)

class Associazioni_categoria(object):
    __tablename__ = 'associazioni_categoria'

    acid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_associazione_categoria = Column(Integer,nullable=False,index=True)
    ass_categoria_nome = Column(String(255),nullable=False )
    id_accordo = Column(String(255),nullable=False )
    sigla_provincia = Column(String(255),nullable=False )
    sigla_cciaa = Column(String(255),nullable=False )

    def __init__ (self,id_associazione_categoria,ass_categoria_nome,id_accordo,sigla_provincia,sigla_cciaa):
        # acid
        self.id_associazione_categoria = id_associazione_categoria
        self.ass_categoria_nome = ass_categoria_nome
        self.id_accordo = id_accordo
        self.sigla_provincia = sigla_provincia
        self.sigla_cciaa = sigla_cciaa

    def __repr__(self)
       return "<Associazioni_categoria('%s','%s','%s','%s','%s')>" % (self.id_associazione_categoria,self.ass_categoria_nome,self.id_accordo,self.sigla_provincia,self.sigla_cciaa)

class Stati_registro_cronologico(object):
    __tablename__ = 'stati_registro_cronologico'

    srcid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_stato_registro_cronologico = Column(String(255),nullable=False,index=True)
    descrizione_stato_reg_crono = Column(String(255),nullable=False )

    def __init__ (self,id_stato_registro_cronologico,descrizione_stato_reg_crono):
        # srcid
        self.id_stato_registro_cronologico = id_stato_registro_cronologico
        self.descrizione_stato_reg_crono = descrizione_stato_reg_crono

    def __repr__(self)
       return "<Stati_registro_cronologico('%s','%s')>" % (self.id_stato_registro_cronologico,self.descrizione_stato_reg_crono)

class Tipi_imballaggi(object):
    __tablename__ = 'tipi_imballaggi'

    tiid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_imballaggio = Column(Integer,nullable=False,index=True)
    tipo_imballaggio = Column(String(255),nullable=False )
    codice_imballaggio = Column(String(255),nullable=False )

    def __init__ (self,id_tipo_imballaggio,tipo_imballaggio,codice_imballaggio):
        # tiid
        self.id_tipo_imballaggio = id_tipo_imballaggio
        self.tipo_imballaggio = tipo_imballaggio
        self.codice_imballaggio = codice_imballaggio

    def __repr__(self)
       return "<Tipi_imballaggi('%s','%s','%s')>" % (self.id_tipo_imballaggio,self.tipo_imballaggio,self.codice_imballaggio)

class Sottocategorie_star(object):
    __tablename__ = 'sottocategorie_star'

    ssid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_sottocategoria_star = Column(String(255),nullable=False,index=True)
    id_categoria_star = Column(String(255),nullable=False )
    descrizione_sottocategoria = Column(String(255),nullable=False )

    def __init__ (self,id_sottocategoria_star,id_categoria_star,descrizione_sottocategoria):
        # ssid
        self.id_sottocategoria_star = id_sottocategoria_star
        self.id_categoria_star = id_categoria_star
        self.descrizione_sottocategoria = descrizione_sottocategoria

    def __repr__(self)
       return "<Sottocategorie_star('%s','%s','%s')>" % (self.id_sottocategoria_star,self.id_categoria_star,self.descrizione_sottocategoria)

class Tipi_documento(object):
    __tablename__ = 'tipi_documento'

    ssid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_documento = Column(String(255),nullable=False,index=True)
    descrizione = Column(String(255),nullable=False )

    def __init__ (self,id_tipo_documento,descrizione):
        # ssid
        self.id_tipo_documento = id_tipo_documento
        self.descrizione = descrizione

    def __repr__(self)
       return "<Tipi_documento('%s','%s')>" % (self.id_tipo_documento,self.descrizione)

class Classi_adr(object):
    __tablename__ = 'classi_adr'

    caid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_classe_adr = Column(String(255),nullable=False,index=True)
    descrizione_classe_adr = Column(String(255),nullable=False )

    def __init__ (self,id_classe_adr,descrizione_classe_adr):
        # caid
        self.id_classe_adr = id_classe_adr
        self.descrizione_classe_adr = descrizione_classe_adr

    def __repr__(self)
       return "<Classi_adr('%s','%s')>" % (self.id_classe_adr,self.descrizione_classe_adr)

class Ruoli_aziendali(object):
    __tablename__ = 'ruoli_aziendali'

    raid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_ruolo_aziendale = Column(String(255),nullable=False,index=True)
    ruolo_aziendale = Column(String(255),nullable=False )

    def __init__ (self,id_ruolo_aziendale,ruolo_aziendale):
        # raid
        self.id_ruolo_aziendale = id_ruolo_aziendale
        self.ruolo_aziendale = ruolo_aziendale

    def __repr__(self)
       return "<Ruoli_aziendali('%s','%s')>" % (self.id_ruolo_aziendale,self.ruolo_aziendale)

class Stati_utente_idm(object):
    __tablename__ = 'stati_utente_idm'

    suid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_stato_utente_idm = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_stato_utente_idm):
        # suid
        self.id_stato_utente_idm = id_stato_utente_idm

    def __repr__(self)
       return "<Stati_utente_idm('%s')>" % (self.id_stato_utente_idm)

class Camere_commercio(object):
    __tablename__ = 'camere_commercio'

    ccid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_camera_commercio = Column(Integer,nullable=False,index=True)
    indirizzo = Column(String(255),nullable=False,index=True)
    numero_civico = Column(String(255),nullable=False,index=True)
    cap = Column(String(255),nullable=False,index=True)
    nome_persona_riferimento = Column(String(255),nullable=False,index=True)
    cognome_persona_riferimento = Column(String(255),nullable=False,index=True)
    email_persona_riferimento = Column(String(255),nullable=False,index=True)
    telefono_persona_riferimento = Column(String(255),nullable=False,index=True)
    sigla_cciaa = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_camera_commercio,indirizzo,numero_civico,cap,nome_persona_riferimento,cognome_persona_riferimento,email_persona_riferimento,telefono_persona_riferimento,sigla_cciaa):
        # ccid
        self.id_camera_commercio = id_camera_commercio
        self.indirizzo = indirizzo
        self.numero_civico = numero_civico
        self.cap = cap
        self.nome_persona_riferimento = nome_persona_riferimento
        self.cognome_persona_riferimento = cognome_persona_riferimento
        self.email_persona_riferimento = email_persona_riferimento
        self.telefono_persona_riferimento = telefono_persona_riferimento
        self.sigla_cciaa = sigla_cciaa

    def __repr__(self)
       return "<Camere_commercio('%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.id_camera_commercio,self.indirizzo,self.numero_civico,self.cap,self.nome_persona_riferimento,self.cognome_persona_riferimento,self.email_persona_riferimento,self.telefono_persona_riferimento,self.sigla_cciaa)

class Tipi_esito_trasporto(object):
    __tablename__ = 'tipi_esito_trasporto'

    tetid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_esito_trasporto = Column(String(255),nullable=False,index=True)
    descr_esito_trasporto = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_esito_trasporto,descr_esito_trasporto):
        # tetid
        self.id_esito_trasporto = id_esito_trasporto
        self.descr_esito_trasporto = descr_esito_trasporto

    def __repr__(self)
       return "<Tipi_esito_trasporto('%s','%s')>" % (self.id_esito_trasporto,self.descr_esito_trasporto)

class Stati_veicolo(object):
    __tablename__ = 'stati_veicolo'

    svid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_stato_veicolo = Column(String(255),nullable=False,index=True)
    descrizione_stato_veicolo = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_stato_veicolo,descrizione_stato_veicolo):
        # svid
        self.id_stato_veicolo = id_stato_veicolo
        self.descrizione_stato_veicolo = descrizione_stato_veicolo

    def __repr__(self)
       return "<Stati_veicolo('%s','%s')>" % (self.id_stato_veicolo,self.descrizione_stato_veicolo)

class Cod_rec_1013(object):
    __tablename__ = 'cod_rec_1013'

    crid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_cod_rec_1013 = Column(String(255),nullable=False,index=True)
    descrizione_cod_rec = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_cod_rec_1013,descrizione_cod_rec):
        # crid
        self.id_cod_rec_1013 = id_cod_rec_1013
        self.descrizione_cod_rec = descrizione_cod_rec

    def __repr__(self)
       return "<Cod_rec_1013('%s','%s')>" % (self.id_cod_rec_1013,self.descrizione_cod_rec)

class Stati_registrazioni_crono(object):
    __tablename__ = 'stati_registrazioni_crono'

    srcid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_stato_registrazione_crono = Column(String(255),nullable=False,index=True)
    descrizione_stato_reg_crono = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_stato_registrazione_crono,descrizione_stato_reg_crono):
        # srcid
        self.id_stato_registrazione_crono = id_stato_registrazione_crono
        self.descrizione_stato_reg_crono = descrizione_stato_reg_crono

    def __repr__(self)
       return "<Stati_registrazioni_crono('%s','%s')>" % (self.id_stato_registrazione_crono,self.descrizione_stato_reg_crono)

class Tipi_trasporto(object):
    __tablename__ = 'tipi_trasporto'

    ttid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_trasporto = Column(Integer,nullable=False,index=True)
    descrizione_tipo_trasporto = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_tipo_trasporto,descrizione_tipo_trasporto):
        # ttid
        self.id_tipo_trasporto = id_tipo_trasporto
        self.descrizione_tipo_trasporto = descrizione_tipo_trasporto

    def __repr__(self)
       return "<Tipi_trasporto('%s','%s')>" % (self.id_tipo_trasporto,self.descrizione_tipo_trasporto)

class Tipologie_raee(object):
    __tablename__ = 'tipologie_raee'

    trid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipologia_raee = Column(String(255),nullable=False,index=True)
    descrizione_tipologia_raee = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_tipologia_raee,descrizione_tipologia_raee):
        # trid
        self.id_tipologia_raee = id_tipologia_raee
        self.descrizione_tipologia_raee = descrizione_tipologia_raee

    def __repr__(self)
       return "<Tipologie_raee('%s','%s')>" % (self.id_tipologia_raee,self.descrizione_tipologia_raee)

class Codici_cer_iii_livello(object):
    __tablename__ = 'codici_cer_iii_livello'

    cclid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_codice_cer_iii_livello = Column(String(255),nullable=False,index=True)
    escrizione_iii_livello = Column(String(255),nullable=False,index=True)
    flag_pericoloso = Column(Integer,nullable=False,index=True)
    flag_attivo = Column(Integer,nullable=False,index=True)

    def __init__ (self,id_codice_cer_iii_livello,escrizione_iii_livello,flag_pericoloso,flag_attivo):
        # cclid
        self.id_codice_cer_iii_livello = id_codice_cer_iii_livello
        self.escrizione_iii_livello = escrizione_iii_livello
        self.flag_pericoloso = flag_pericoloso
        self.flag_attivo = flag_attivo

    def __repr__(self)
       return "<Codici_cer_iii_livello('%s','%s','%s','%s')>" % (self.id_codice_cer_iii_livello,self.escrizione_iii_livello,self.flag_pericoloso,self.flag_attivo)

class Tipi_stato_impresa(object):
    __tablename__ = 'tipi_stato_impresa'

    tsilid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_tipo_stato_impresa = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_tipo_stato_impresa):
        # tsilid
        self.id_tipo_stato_impresa = id_tipo_stato_impresa

    def __repr__(self)
       return "<Tipi_stato_impresa('%s')>" % (self.id_tipo_stato_impresa)

class Caratteristiche_pericolo(object):
    __tablename__ = 'caratteristiche_pericolo'

    cpid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_caratteristica_pericolo = Column(String(255),nullable=False,index=True)
    descr_car_pericolo = Column(String(255),nullable=False,index=True)

    def __init__ (self,id_caratteristica_pericolo,descr_car_pericolo):
        # cpid
        self.id_caratteristica_pericolo = id_caratteristica_pericolo
        self.descr_car_pericolo = descr_car_pericolo

    def __repr__(self)
       return "<Caratteristiche_pericolo('%s','%s')>" % (self.id_caratteristica_pericolo,self.descr_car_pericolo)

class Sottotipi_veicolo(object):
    __tablename__ = 'sottotipi_veicolo'

    svid = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    id_sottotipo_veicolo = Column(String(255),nullable=False,index=True)
    descrizione = Column(String(255),nullable=False,index=True)
    codice_sottotipo_veicolo = Column(Integer,nullable=False,index=True)

    def __init__ (self,id_sottotipo_veicolo,descrizione,codice_sottotipo_veicolo):
        # svid
        self.id_sottotipo_veicolo = id_sottotipo_veicolo
        self.descrizione = descrizione
        self.codice_sottotipo_veicolo = codice_sottotipo_veicolo

    def __repr__(self)
       return "<Sottotipi_veicolo('%s','%s','%s')>" % (self.id_sottotipo_veicolo,self.descrizione,self.codice_sottotipo_veicolo)

Base.metadata.create_all()
