#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre <paolo.melchiorre@madec.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
The L{storage} module contains the L{OWTStorage} class.
It stores information about storage.
"""

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, \
    ForeignKey, Integer, MetaData, String, Table


class OWTStorage(object):
    """
    Base configuration class that is used for the storage.
    These are generally passed to the OWT request classes as arguments.
    """
    def __init__(self, engine):
        """
        @type meta: L{MetaData}
        @param meta: The metadata object of OWTStorage.
        """
        self.engine = engine
        """@ivar: Engine connected to database."""
        self.metadata = MetaData()
        """@ivar: metadata."""
        #XXX: Cataloghi (ordine alafabetico)
        self.metadata_associazioni_categoria = \
            Table('associazioni_categoria',
                self.metadata,
                Column('id_associazione_categoria', Integer, nullable=False,
                        primary_key=True),
                Column('ass_categoria_nome', String(255), nullable=True),
                Column('id_accordo', String(255), nullable=True),
                Column('sigla_provincia', String(255), nullable=True),
                Column('sigla_cciaa', String(255), nullable=True),
            )
        self.metadata_camere_commercio = \
            Table('camere_commercio',
                self.metadata,
                Column('id_camera_commercio', Integer, nullable=False,
                        primary_key=True),
                Column('indirizzo', String(255), nullable=True),
                Column('numero_civico', String(255), nullable=True),
                Column('cap', String(255), nullable=True),
                Column('nome_persona_riferimento', String(255), nullable=True),
                Column('cognome_persona_riferimento', String(255),
                        nullable=True),
                Column('email_persona_riferimento', String(255),
                        nullable=True),
                Column('telefono_persona_riferimento', String(255),
                        nullable=True),
                Column('sigla_cciaa', String(255), nullable=True),
            )
        self.metadata_caratteristiche_pericolo = \
            Table('caratteristiche_pericolo',
                self.metadata,
                Column('id_caratteristica_pericolo', String(255),
                        nullable=False, primary_key=True),
                Column('descr_car_pericolo', String(255), nullable=True),
            )
        self.metadata_categorie_raee = \
            Table('categorie_raee',
                self.metadata,
                Column('id_categoria_raee', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_categoria_raee', String(255),
                        nullable=True),
            )
        self.metadata_causali_mov = \
            Table('causali_mov',
                self.metadata,
                Column('id_causale_mov', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione', String(255), nullable=True)
            )
        self.metadata_causali_reg = \
            Table('causali_reg',
                self.metadata,
                Column('id_causale_reg', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione', String(255), nullable=True),
                Column('tipo', String(255), nullable=True)
            )
        self.metadata_causali_scheda = \
            Table('causali_scheda',
                self.metadata,
                Column('id_causale_sch', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione', String(255), nullable=True),
                Column('tipo', String(255), nullable=True)
            )
        self.metadata_classi_adr = \
            Table('classi_adr',
                self.metadata,
                Column('id_classe_adr', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_classe_adr', String(255), nullable=True),
            )
        self.metadata_codici_cer_iii_livello = \
            Table('codici_cer_iii_livello',
                self.metadata,
                Column('id_codice_cer_iii_livello', String(255),
                        nullable=False, primary_key=True),
                Column('descrizione_iii_livello', String(255), nullable=True),
                Column('flag_pericoloso', Integer, nullable=True),
                Column('flag_attivo', Integer, nullable=True),
            )
        self.metadata_cod_rec_1013 = \
            Table('cod_rec_1013',
                self.metadata,
                Column('id_cod_rec_1013', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_cod_rec', String(255), nullable=True),
            )
        self.metadata_forme_giuridiche = \
            Table('forme_giuridiche',
                self.metadata,
                Column('id_tipo_forma_giuridica', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_forma_giuridica', String(255),
                        nullable=True),
            )
        self.metadata_localita_estere = \
            Table('localita_estere',
                self.metadata,
                Column('id_localita', Integer, nullable=False,
                        primary_key=True),
                Column('nazione', String(255), nullable=True),
                Column('sigla_nazione', String(255), nullable=True),
            )
        self.metadata_numeri_onu = \
            Table('numeri_onu',
                self.metadata,
                Column('id_numero_onu', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_numero_onu', String(255), nullable=True),
            )
        self.metadata_operazioni_impianti = \
            Table('operazioni_impianti',
                self.metadata,
                Column('id_operazione_impianto', String(255), nullable=False,
                        primary_key=True),
                Column('id_tipo_operazione_impianto', String(255),
                        nullable=True),
                Column('operazione_impianto', String(255), nullable=True),
                Column('ordinamento', Integer, nullable=True),
            )
        self.metadata_ruoli_aziendali = \
            Table('ruoli_aziendali',
                self.metadata,
                Column('id_ruolo_aziendale', String(255), nullable=False,
                        primary_key=True),
                Column('ruolo_aziendale', String(255), nullable=True),
            )
        self.metadata_sottocategorie_star = \
            Table('sottocategorie_star',
                self.metadata,
                Column('id_sottocategoria_star', String(255), nullable=False,
                        primary_key=True),
                Column('id_categoria_star', String(255), nullable=True),
                Column('descrizione_sottocategoria', String(255),
                        nullable=True),
            )
        self.metadata_sottotipi_veicolo = \
            Table('sottotipi_veicolo',
                self.metadata,
                Column('id_sottotipo_veicolo', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione', String(255), nullable=True),
                Column('codice_sottotipo_veicolo', Integer, nullable=True),
            )
        self.metadata_stati_fisici_rifiuto = \
            Table('stati_fisici_rifiuto',
                self.metadata,
                Column('id_stato_fisico_rifiuto', String(255), nullable=False,
                        primary_key=True),
                Column('descr_stato_fisico_rifiuto', String(255),
                        nullable=True),
                Column('codice_stato_fisico', String(255), nullable=True),
            )
        self.metadata_stati_registrazioni_crono = \
            Table('stati_registrazioni_crono',
                self.metadata,
                Column('id_stato_registrazione_crono', String(255),
                        nullable=False, primary_key=True),
                Column('descrizione_stato_reg_crono', String(255),
                        nullable=True),
            )
        self.metadata_stati_registro_cronologico = \
            Table('stati_registro_cronologico',
                self.metadata,
                Column('id_stato_registro_cronologico', String(255),
                        nullable=False, primary_key=True),
                Column('descrizione_stato_reg_crono', String(255),
                        nullable=True),
            )
        self.metadata_stati_scheda_sistri = \
            Table('stati_scheda_sistri',
                self.metadata,
                Column('id_stato_scheda_sistri', String(255), nullable=False,
                        primary_key=True),
                Column('stato_scheda_sistri', String(255), nullable=True),
            )
        self.metadata_stati_utente_idm = \
            Table('stati_utente_idm',
                self.metadata,
                Column('id_stato_utente_idm', String(255), nullable=False,
                        primary_key=True),
            )
        self.metadata_stati_veicolo = \
            Table('stati_veicolo',
                self.metadata,
                Column('id_stato_veicolo', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_stato_veicolo', String(255),
                        nullable=True)
            )
        self.metadata_tipi_documento = \
            Table('tipi_documento',
                self.metadata,
                Column('id_tipo_documento', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione', String(255), nullable=True),
            )
        self.metadata_tipi_esito_trasporto = \
            Table('tipi_esito_trasporto',
                self.metadata,
                Column('id_esito_trasporto', String(255), nullable=False,
                        primary_key=True),
                Column('descr_esito_trasporto', String(255), nullable=True),
            )
        self.metadata_tipi_imballaggi = \
            Table('tipi_imballaggi',
                self.metadata,
                Column('id_tipo_imballaggio', Integer, nullable=False,
                        primary_key=True),
                Column('tipo_imballaggio', String(255), nullable=True),
                Column('codice_imballaggio', String(255), nullable=True),
            )
        self.metadata_tipi_registrazioni_crono = \
            Table('tipi_registrazioni_crono',
                self.metadata,
                Column('id_tipo_registrazione_crono', String(255),
                        nullable=False, primary_key=True),
                Column('descr_tipo_reg_crono', String(255), nullable=True),
            )
        self.metadata_tipi_reg_cronologico = \
            Table('tipi_reg_cronologico',
                self.metadata,
                Column('id_tipo_reg_cronologico', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_tipo_reg_crono', String(255),
                        nullable=True),
                Column('macro_categoria', String(255), nullable=True),
            )
        self.metadata_tipi_sede = \
            Table('tipi_sede',
                self.metadata,
                Column('id_tipo_sede', String(255), nullable=False,
                        primary_key=True),
            )
        self.metadata_tipi_stato_impresa = \
            Table('tipi_stato_impresa',
                self.metadata,
                Column('id_tipo_stato_impresa', String(255), nullable=False,
                        primary_key=True),
            )
        self.metadata_tipi_trasporto = \
            Table('tipi_trasporto',
                self.metadata,
                Column('id_tipo_trasporto', Integer, nullable=False,
                        primary_key=True),
                Column('descrizione_tipo_trasporto', String(255),
                        nullable=True),
            )
        self.metadata_tipi_veicolo = \
            Table('tipi_veicolo',
                self.metadata,
                Column('id_tipo_veicolo', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione', String(255), nullable=True),
                Column('codice_tipo_veicolo', Integer, nullable=True),
                Column('flag_rimorchio', Integer, nullable=True),
            )
        self.metadata_tipologie_raee = \
            Table('tipologie_raee',
                self.metadata,
                Column('id_tipologia_raee', String(255), nullable=False,
                        primary_key=True),
                Column('descrizione_tipologia_raee', String(255),
                        nullable=True),
            )
        #XXX: Oggetti (ordine alafabetico)
        self.metadata_azienda = \
            Table('azienda',
                self.metadata,
                Column('idSIS', String(255), nullable=False, primary_key=True),
                Column('ragioneSociale', String(255), nullable=True),
                Column('cognome', String(255)),
                Column('nome', String(255)),
                Column('formaGiuridicaFK', String(255),
                        ForeignKey('forme_giuridiche.id_tipo_forma_giuridica')
                ),
                Column('tipoStatoImpresaFK', String(255),
                        ForeignKey('tipi_stato_impresa.id_tipo_stato_impresa')
                ),
                Column('codiceFiscale', String(25), nullable=True),
                Column('pIva', String(11)),
                Column('numeroIscrizioneAlbo', String(255)),
                Column('cciaaRea', String(255)),
                Column('numeroIscrizioneRea', String(255)),
                Column('codiceIstatAttPrincipale', String(255)),
                Column('dataIscrizioneStar', DateTime),
                Column('codiceAtecoAttPrincipale', String(255)),
                Column('descrizioneAttPrincipale', String(255)),
                Column('versione', BigInteger, nullable=True),
                Column('sedeLegaleFK', String(255),
                        ForeignKey('sede.idSIS')
                ),
            )
        self.metadata_descrittorecatalogo = \
            Table('descrittorecatalogo',
                self.metadata,
                Column('catalogo', String(255), nullable=False,
                        primary_key=True),
                Column('versione', Integer, nullable=True),
                Column('descrizione', String(255), nullable=True),
            )
        #FIXME: idSISSchedeAssociate come ForeignKey su SchedaSISTRI ?
        self.metadata_movimentazione = \
            Table('movimentazione',
                self.metadata,
                Column('idSIS', String(255), nullable=False, primary_key=True),
                Column('idSISTRI', String(255)),
                Column('versione', BigInteger),
                Column('movimentazioneNumeroSerie', String(255)),
                Column('dataMovimentazione', DateTime),
                Column('dataOraFineMovimentazione', DateTime, nullable=True),
                Column('causaleFineMovimentazioneFK', String(255),
                    ForeignKey('causali_mov.id_causale_mov')
                ),
#                name="idSISSchedeAssociate" nillable="true" type="xsd:string"
#                    maxOccurs="unbounded" minOccurs="0"
#                name="identificativoMovimentazioneAssociata" nillable="true"
#                    type="tns:IdMovimentazioneAssociata" minOccurs="0"
            )
        self.metadata_registrocronologico = \
            Table('registrocronologico',
                self.metadata,
                Column('idSIS', String(255), nullable=False, primary_key=True),
                Column('idSISSedeFK', String(255), ForeignKey('sede.idSIS')),
                Column('codiceRegistroCronologico', String(255),
                        nullable=True),
                Column('versione', BigInteger, nullable=True),
                Column('ultimoNumero', BigInteger, nullable=True),
                Column('dataUltimoNumero', DateTime, nullable=True),
                Column('nomeUnitaOperativa', String(255), nullable=True),
                Column('statoRegistroCronologicoFK', String(255), ForeignKey(\
                    'stati_registro_cronologico.id_stato_registro_cronologico')
                ),
                Column('tipoRegCronologicoFK', String(255),
                    ForeignKey('tipi_reg_cronologico.id_tipo_reg_cronologico')
                ),
                Column('sottocategoriaFK', String(255),
                    ForeignKey('sottocategorie_star.id_sottocategoria_star')
                ),
            )
        self.metadata_sede = \
            Table('sede',
                self.metadata,
                Column('idSIS', String(255), nullable=False, primary_key=True),
                Column('tipoSedeFK', String(255),
                        ForeignKey('tipi_sede.id_tipo_sede')
                ),
                Column('nomeSede', String(255), nullable=True),
                Column('codiceIstatLocalita', String(255), nullable=True),
                Column('codiceCatastale', String(255), nullable=True),
                Column('nazione', String(255), nullable=True),
                Column('siglaNazione', String(255), nullable=True),
                Column('indirizzo', String(255), nullable=True),
                Column('versione', BigInteger, nullable=True),
                Column('nrCivico', String(255)),
                Column('cap', String(255)),
                Column('telefono', String(255)),
                Column('fax', String(255)),
                Column('numeroAddetti', BigInteger),
                Column('cameraCommercioFK', Integer,
                        ForeignKey('camere_commercio.id_camera_commercio')
                ),
                Column('associazioneCategoriaFK', Integer,
                    ForeignKey(\
                        'associazioni_categoria.id_associazione_categoria')
                ),
                Column('codiceIstatAttPrincipale', String(255)),
                Column('codiceAtecoAttPrincipale', String(255)),
                Column('descrizioneAttPrincipale', String(255)),
                Column('numeroIscrizioneRea', String(255)),
                Column('numeroUla', Float),
                Column('latitudine', Float),
                Column('longitudine', Float),
                Column('nomeRappresentanteLegale', String(255)),
                Column('cognomeRappresentanteLegale', String(255)),
                Column('codFiscaleRappresentanteLegale', String(255)),
                Column('codicePraticaIscrizione', String(255)),
                Column('ragioneSocialeDichiarata', String(255))
            )
        self.metadata_tratta_base = \
            Table('tratta_base',
                self.metadata,
                Column('idTratta', String(255), nullable=False,
                    primary_key=True),
                Column('progressivo', BigInteger, nullable=False),
                Column('idSISSede_trasportatoreFK', String(255),
                    ForeignKey('sede.idSIS'), nullable=False),
                Column('flagOperatoreLogistico', Boolean, nullable=False),
                Column('versioneSede_trasportatore', BigInteger,
                    nullable=True),
                Column('movimentazioneFK', String(255),
                    ForeignKey('movimentazione.idSIS'), nullable=True
                )
            )
        self.metadata_veicolo = \
            Table('veicolo',
                self.metadata,
                Column('targa', String(255), nullable=False, primary_key=True),
                Column('tipoVeicoloFK', String(255),
                    ForeignKey('tipi_veicolo.id_tipo_veicolo')
                ),
                Column('sottotipoVeicoloFK', String(255),
                    ForeignKey('sottotipi_veicolo.id_sottotipo_veicolo')
                ),
                Column('statoVeicoloFK', String(255),
                    ForeignKey('stati_veicolo.id_stato_veicolo')
                ),
                Column('annoImmatricolazione', BigInteger, nullable=True),
                Column('marca', String(255), nullable=True),
                Column('modello', String(255), nullable=True),
                Column('sedeFK', String(255), ForeignKey('sede.idSIS'))
            )
        #XXX: Tabelle molti-a-molti (ordine alafabetico)
        #Azienda referenzia Sede in sedeLegale e sediSummary (molti-a-molti)
        self.metadata_azienda_sedisummary = \
            Table('azienda_sedisummary',
                self.metadata,
                Column('aziendaFK', String(255), ForeignKey('azienda.idSIS'),
                    nullable=False),
                Column('sedeFK', String(255), ForeignKey('sede.idSIS'),
                    nullable=False)
            )
        self.metadata_sede_sottocategorie = \
            Table('sede_sottocategorie',
                self.metadata,
                Column('sedeFK', String(255), ForeignKey('sede.idSIS'),
                    nullable=False),
                Column('sottocategorie_starFK', String(255),
                    ForeignKey('sottocategorie_star.id_sottocategoria_star'),
                    nullable=False)
            )
        self.metadata_veicolo_codiciceriii = \
            Table('veicolo_codiciceriii',
                self.metadata,
                Column('veicoloFK', String(255), ForeignKey('veicolo.targa'),
                    nullable=False),
                Column('codici_cer_iii_livelloFK', String(255),
                    ForeignKey(\
                        'codici_cer_iii_livello.id_codice_cer_iii_livello'),
                    nullable=False)
            )
        self.metadata.create_all(self.engine)
