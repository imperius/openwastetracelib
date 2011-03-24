# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre
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
The I{db mapper} module provides mapping for object and tables.
"""


from sqlalchemy.orm import mapper

from db_objects import *
from db_metadata import *

mapperAssociazioniCategoria=mapper(AssociazioniCategoriaObject, AssociazioniCategoria)
mapperCamereCommercio=mapper(CamereCommercioObject, CamereCommercio)
mapperCaratteristichePericolo=mapper(CaratteristichePericoloObject, CaratteristichePericolo)
mapperCataloghiElenco=mapper(CataloghiElencoObject, CataloghiElenco)
mapperCategorieRaee=mapper(CategorieRaeeObject, CategorieRaee)
mapperClassiADR=mapper(ClassiADRObject, ClassiADR)
mapperCodRec1013=mapper(CodRec1013Object, CodRec1013)
mapperCodiciCerIIILievello=mapper(CodiciCerIIILievelloObject, CodiciCerIIILievello)
mapperFormeGiuridiche=mapper(FormeGiuridicheObject, FormeGiuridiche)
mapperLocalitaEstere=mapper(LocalitaEstereObject, LocalitaEstere)
mapperNumeriOnu=mapper(NumeriOnuObject, NumeriOnu)
mapperOperazioniImpianti=mapper(OperazioniImpiantiObject, OperazioniImpianti)
mapperRuoliAziendali=mapper(RuoliAziendaliObject, RuoliAziendali)
mapperSottoCategorieStar=mapper(SottoCategorieStarObject, SottoCategorieStar)
mapperStatiFisiciRifiuto=mapper(StatiFisiciRifiutoObject, StatiFisiciRifiuto)
mapperStatiRegistrazioniCrono=mapper(StatiRegistrazioniCronoObject, StatiRegistrazioniCrono)
mapperStatiSchedaSistri=mapper(StatiSchedaSistriObject, StatiSchedaSistri)
mapperStatiVeicolo=mapper(StatiVeicoloObject, StatiVeicolo)
mapperTipiImballaggi=mapper(TipiImballaggiObject, TipiImballaggi)
mapperTipiRegCronologico=mapper(TipiRegCronologicoObject, TipiRegCronologico)
mapperTipiRegistrazioniCrono=mapper(TipiRegistrazioniCronoObject, TipiRegistrazioniCrono)
mapperTipiSede=mapper(TipiSedeObject, TipiSede)
mapperTipiStatoImpresa=mapper(TipiStatoImpresaObject, TipiStatoImpresa)
mapperTipiTrasporto=mapper(TipiTrasportoObject, TipiTrasporto)
mapperTipiVeicoli=mapper(TipiVeicoliObject, TipiVeicoli)
mapperTipoDocumento=mapper(TipoDocumentoObject, TipoDocumento)
mapperTipoEsitoTrasporto=mapper(TipoEsitoTrasportoObject, TipoEsitoTrasporto)
mapperTipologieRaee=mapper(TipologieRaeeObject, TipologieRaee)
