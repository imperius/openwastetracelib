Open Waste Trace
================

What is it?
-----------

A wrapper around Sistri's Web Services Soap API using Suds.

Requirements
------------

The only dependency is the suds SOAP module, which is available at:

- https://fedorahosted.org/suds/

You may also use easy_install or pip to install from PyPi.

Installation
------------

As root/admin on your machine::

  python setup.py install

Documentation
-------------

For documentation, see the project webpage at:

- http://www.openwastetrace.it

There are also a lot of useful examples under the examples directory within
this directory.

Support
-------

Head over to http://www.openwastetrace.it and submut an issue if you have any
problems or questions.

License
-------
::

    Copyright (C) 2011 Madec S.r.l.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contributors
------------

- Massimiliano De Cesare
- Paolo Melchiorre
- Gianluca Tortorella

Convenzioni
-----------

- Il nome della **classe** python è *esattamente* uguale al nome del tipo
  corrispondente presente nel file WSDL.

  es: Type=DescrittoreCatalogo, Classe=DescrittoreCatalogo

- Il nome degli **attributi** delle classi python sono *esattamente* uguali ai
  nomi delle variabili corrispondenti presenti nel file WSDL.

  es: Attribute=associazioneCategoriaDescr, Variable=associazioneCategoriaDescr

- Il nome della **colonna** della tabella sono *esattamente* uguali ai nomi
  degli **attributi** delle classi python di cui memorizza i dati.

  es: Attribute=associazioneCategoriaDescr, Column=associazioneCategoriaDescr

- Il nome della **tabella** corrisponde al nome in *minuscolo* della classe
  python della quale memorizza i dati.

  es: Class=DescrittoreCatalogo, Table=descrittorecatalogo

- Il nome dell'oggetto **metadata** corrisponde al nome della tabella relativa
  con l'aggiunta del seguente *suffisso*: ``metadata_``.

  es: Table=descrittorecatalogo, Metadata=metadata_descrittorecatalogo

- Il nome dell'oggetto **mapper** corrisponde al nome classe di cui esegue il
  mapping con l'aggiunta del seguente *suffisso*: ``mapper``.

  es: Class=DescrittoreCatalogo, Mapper=mapperDescrittoreCatalogo
