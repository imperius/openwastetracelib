Open Waste Trace
================

Libreria python per interfacciarsi ai Web Services di Sistri.

Realizzata da:

- Massimiliano De Cesare
- Paolo Melchiorre
- Gianluca Tortorella

Convenzioni
-----------

- Il nome della **classe** python è *esattamente* uguale al nome del tipo corrispondente presente nel file WSDL.
  es: Type=DescrittoreCatalogo, Classe=DescrittoreCatalogo

- Il nome degli **attributi** delle classi python sono *esattamente* uguali ai nomi delle variabili corrispondenti presenti nel file WSDL.
  es: Attribute=associazioneCategoriaDescr, Variable=associazioneCategoriaDescr

- Il nome della **colonna** della tabella sono *esattamente* uguali ai nomi degli **attributi** delle classi python di cui memorizza i dati.
  es: Attribute=associazioneCategoriaDescr, Column=associazioneCategoriaDescr

- Il nome della **tabella** corrisponde al nome in *minuscolo* della classe python della quale memorizza i dati.
  es: Class=DescrittoreCatalogo, Table=descrittorecatalogo

- Il nome dell'oggetto **metadata** corrisponde al nome della tabella relativa con l'aggiunta del seguente *suffisso*: ``metadata_``.
  es: Table=descrittorecatalogo, Metadata=metadata_descrittorecatalogo

- Il nome dell'oggetto **mapper** corrisponde al nome classe di cui esegue il mapping con l'aggiunta del seguente *suffisso*: ``mapper``.
  es: Class=DescrittoreCatalogo, Mapper=mapperDescrittoreCatalogo
