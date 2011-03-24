Prove di connessione
====================

Resoconto delle prove di connessione alle rirose di interoperabilità SISTRI.

Premessa
--------

Il documento `Specifica delle interfacce <http://www.sistri.it/Documenti/Allegati/INTEROPERABILITA_SPECIFICA_INTERFACCE.pdf>`_ alla pagina 9 indica due url di accesso: ai Servizi SIS:

- Sperimentazione: http://sis.sistri.it/SIS/services/SIS
- Esercizio: https://sisssl.sistri.it/SIS/services/SIS

Il primo URL, relativa all’ambiente di Sperimentazione, dovrebbe permettere lo sviluppo di opportuni client
di Interoperabilità da utilizzare con gestionali esterni. L’url per ottenere il wsdl da tale ambiente è: http://sis.sistri.it/SIS/services/SIS?wsdl

Il secondo URL, relativo all’ambiente di Esercizio, è l’ambiente di lavoro reale con criteri di
accesso basati su protocollo SSL mutuamente autenticato. L’url per ottenere il wsdl da tale
ambiente è: https://sisssl.sistri.it/SIS/services/SIS?wsdl

Accesso tramite browser Firefox 3.6
-----------------------------------

Sperimentazione
...............

L'accesso alle URL di `sperimentazione <http://sis.sistri.it/SIS/services/SIS>`_ e al `wsdl <http://sis.sistri.it/SIS/services/SIS?wsdl>`_ corrispondente generano lo stesso risultato ovvero il redirect alle seguenti pagine in sequenza:

1. http://portal.sistri.it/portal/
2. http://portal.sistri.it/portal/dt
3. http://portal.sistri.it/tokenUpdate/upd/update.html

Lo stesso avviene per tutti gli indirizzi con dominio di terzo livello sis.sistri.it corrispondente all'indirizzo IP 93.63.171.203 accedendo tramite entramebe le porte 80/tcp http e 443/tcp https.

Esercizio
.........

Accedendo alla URL di `esercizio wsdl <https://sisssl.sistri.it/SIS/services/SIS?wsdl>`_ si riceve il file xml memorizzato con il nome SIS.wsdl

L'accesso alla URL di `esercizio <https://sisssl.sistri.it/SIS/services/SIS>`_ ed a indirizzi simili alla porta 80/tcp http producono pagine di errore.

Accesso tramite Python SUDS
---------------------------

L'accesso con libreria Python SUDS e livello di trasprto con relativi certificati restituisce i seguenti risultati:

- http://sis.sistri.it/SIS/services/SIS?wsdl
  http redirect con conseguente errore

- https://sis.sistri.it/SIS/services/SIS?wsdl
  http redirect con conseguente errore

- http://sisssl.sistri.it/SIS/services/SIS?wsdl
  Erorre 404 not found

- https://sisssl.sistri.it/SIS/services/SIS?wsdl
  Restituisce il file xml corretto

Chiamata dei metodi tramite Python SUDS
---------------------------------------

La chiamata dei metodi tramite Python SUDS restituisce messaggi di timeoute dopo la corretta connessione e recupero del file wsdl::

    version = client.service.GetVersioneSIS("paola.mandragola2039")
    catalog = client.service.GetElencoCataloghi("paola.mandragola2039")

restiruiscono in tutti i casi e con tutti i metodi testati sempre un messaggio di ``urlopen error timed out``.

File WSDL con https
-------------------

Il file wsdl correttamente restituito dalla connessione alla URL di Esercizio contiene riferimenti al protocollo http sulla porta 80/tcp.

Abbiamo inserito un file ``SIS-wsdl.xml`` copiando il file SIS.wsdl e sostiuendo all'interno i riferimenti al tropocollo http con quello al protocollo https ma il risultato finale è lo stesso messaggio di ``urlopen error timed out``.

Accesso diretto
---------------

L'accesso diretto ad un metodo dichiarato nel file WSDL ma alla URL di esercizio restituisce correttamente una richiesta di parametro mancante::

    https://sisssl.sistri.it/SIS/services/SIS/GetVersioneCatalogo
    Required element identity defined in the schema can not be found in the request

Ugualmente l'accesso diretto ad un metodo dichiarato nel file WSDL ma alla URL di esercizio restituisce correttamente un messaggio di errore per metodo mancante::

    https://sisssl.sistri.it/SIS/services/SIS/GetMedotoMancante
    The endpoint reference (EPR) for the Operation not found is /WS_SIS/services/SIS/GetMedotoMancante and the WSA Action = null

File WSDL con URL corretta
--------------------------

Il file wsdl correttamente restituito dalla connessione alla URL di Esercizio contiene riferimenti ad una URL che no è quella di esercizio.

Abbiamo inserito un file ``wsdl`` copiando il file SIS.wsdl e sostiuendo all'interno i riferimenti alla URL con la URL di esercizio in tutti i campi che contenevano indirizzi differenti ed abbiamo ricevuto una risposta di errore invece dell'errore di timeout::

    <HTML><HEAD><TITLE>Forbidden</TITLE></HEAD>
    <BODY><H1>Forbidden</H1>
    Your client is not allowed to access the requested object.
    </BODY></HTML>

Versione finale
---------------

Il file wsdl correttamente restituito dalla connessione alla URL di Esercizio contiene riferimenti ad una URL che no è quella di esercizio.

Abbiamo inserito un file ``wsdl`` copiando il file SIS.wsdl e sostituendo all'interno i riferimenti alla URL con la URL di esercizio **solo** nella sezione del file WSDL relativa al servizio, lasciando invariati il resto del file, compresi gli indirizzi dei metodi, come di seguito riportato::

  <wsdl:service name="SIS">
    <wsdl:port name="SIS_WSDL" binding="tns:SIS_WSDL">
      <soap:address location="https://sisssl.sistri.it/SIS/services/SIS"/>
    </wsdl:port>
  </wsdl:service>

La risposta alla chiamata del metodo ``GetVersioneSIS`` è stata corretta, come di seguito riportato::

  Protocollo: v1.2.1; SIS Software: v1.1.7
