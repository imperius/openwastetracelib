==================================
IWS-SSL-MA_ALLINEAMENTOANAGRAFICHE
==================================

Metodi dell'interfaccia **IWS-SSL-MA_ALLINEAMENTOANAGRAFICHE**.

GetAzienda
----------

Parametri
.........

- xs:string identity
- ParametriAggiuntivi parametriAggiuntivi
- xs:string codiceFiscaleAzienda

Chiamata
........

Chiamata di esempio del metodo con parametri arbitrari::

    print client.service.GetAzienda(identity="gabriele.dangelo8571",parametriAggiuntivi="",codiceFiscaleAzienda="02037830698")

Risposta
........

Risposta del servizio alla chiamata di esempio::

    (Azienda){
       ragioneSociale = ""D'ANGELO ANTONIO S.R.L.""
       cognome = "D ANGELO "
       nome = "GABRIELE"
       formaGiuridica = 
          (Catalogo){
             idCatalogo = "SR"
             description = None
          }
       tipoStatoImpresa = 
          (Catalogo){
             idCatalogo = "ATTIVA"
             description = None
          }
       codiceFiscale = "02037830698"
       pIva = "02037830698"
       numeroIscrizioneAlbo = "162"
       cciaaRea = "CH"
       numeroIscrizioneRea = "147248"
       codiceIstatAttPrincipale = "38"
       dataIscrizioneStar = None
       codiceAtecoAttPrincipale = None
       descrizioneAttPrincipale = "ATTIVITA' DI RACCOLTA, TRATTAMENTO E SMALTIMENTO DEI RIFIUTI; RECUPERO DEI MATERIALI"
       versione = 
          (LongNumber){
             long = 2
          }
       idSIS = "88272"
       sedeLegale = 
          (SedeLegale){
             tipoSede = 
                (Catalogo){
                   idCatalogo = "LEGALE"
                   description = None
                }
             nomeSede = None
             codiceIstatLocalita = "069018"
             codiceCatastale = "C114"
             nazione = "ITALIA"
             siglaNazione = "IT"
             indirizzo = "VIA LENTESCO"
             nrCivico = "11"
             cap = "66032"
             sottocategorie[] = 
                (Catalogo){
                   idCatalogo = "LRAP"
                   description = "LEGALE RAPPRESENTANZA"
                },
                (Catalogo){
                   idCatalogo = "TTRA"
                   description = "TRASPORTATORI (art 212, comma 5, D.Lgs 152/2006)"
                },
             versione = 
                (LongNumber){
                   long = 2
                }
             idSIS = "179755"
          }
       sediSummary[] = 
          (Sede_summary){
             tipoSede = 
                (Catalogo){
                   idCatalogo = "UNITA LOCALE"
                   description = None
                }
             nomeSede = None
             codiceIstatLocalita = "069018"
             codiceCatastale = "C114"
             nazione = "ITALIA"
             siglaNazione = "IT"
             indirizzo = "VIA LENTESCO"
             nrCivico = "11"
             cap = "66032"
             sottocategorie[] = 
                (Catalogo){
                   idCatalogo = "AIRA"
                   description = "INTERMEDIARI"
                },
                (Catalogo){
                   idCatalogo = "PDRS"
                   description = "PRODUTTORI-DETENTORI DI RIFIUTI SPECIALI"
                },
             versione = 
                (LongNumber){
                   long = 2
                }
             idSIS = "582426"
          },
          (Sede_summary){
             tipoSede = 
                (Catalogo){
                   idCatalogo = "LEGALE"
                   description = None
                }
             nomeSede = None
             codiceIstatLocalita = "069018"
             codiceCatastale = "C114"
             nazione = "ITALIA"
             siglaNazione = "IT"
             indirizzo = "VIA LENTESCO"
             nrCivico = "11"
             cap = "66032"
             sottocategorie[] = 
                (Catalogo){
                   idCatalogo = "LRAP"
                   description = "LEGALE RAPPRESENTANZA"
                },
                (Catalogo){
                   idCatalogo = "TTRA"
                   description = "TRASPORTATORI (art 212, comma 5, D.Lgs 152/2006)"
                },
             versione = 
                (LongNumber){
                   long = 2
                }
             idSIS = "179755"
          },
     }

GetVersioneAnagraficaAzienda
----------------------------

Parametri
.........

- xs:string identity
- ParametriAggiuntivi parametriAggiuntivi
- xs:string codiceFiscaleAzienda

Chiamata
........

Chiamata di esempio del metodo con parametri arbitrari::

    print client.service.GetVersioneAnagraficaAzienda(identity="gabriele.dangelo8571",ParametriAggiuntivi="",codiceFiscaleAzienda="02037830698")

Risposta
........

Risposta del servizio alla chiamata di esempio::

    (LongNumber){
       long = 2
     }

GetVersioneAnagrafica
---------------------

Parametri
.........

- xs:string identity
- ParametriAggiuntivi parametriAggiuntivi
- xs:string idSIS
- xs:string tipoAnagrafica

Chiamata
........

Chiamata di esempio del metodo con parametri arbitrari::

    print client.service.GetVersioneAnagraficaAzienda(identity="gabriele.dangelo8571",parametriAggiuntivi="",idSIS="88272",tipoAnagrafica="AZIENDA")

Risposta
........

Risposta del servizio alla chiamata di esempio::

    WebFault: Server raised fault: 'GetVersioneAnagraficaAzienda_faultMsg'
