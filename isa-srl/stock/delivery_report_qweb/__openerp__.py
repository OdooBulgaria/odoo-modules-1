# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 ISA s.r.l. (<http://www.isa.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Delivery report - Stampa DDT e Fattura Accompagnatoria',
    'version': '0.1',
    'sequence': 14,
    'summary': 'Print DDT',
    'description': """
Print DDT report
================
With this module you can personalize the DDT report.


Fattura Accompagnatoria
-----------------------
Mostra il riferimento al DDT, nel caso si crea un ordine di vendita
e la fattura viene generata "su ordine di consegna" (impostando
il campo "crea fattura").

Il nome del file di stampa di una fattura contiene il numero fattura
(con l'underscore al posto dei caratteri non alfanumerici).

Configurazione->Technical->Azioni->Reports->Stampa Fattura Accompagnatoria

    """,
    'author': 'ISA srl',
    'website': 'http://www.isa.it',
    'depends': ['delivery_makeover',
                'stock_makeover',
                'report',
                ],
    'category': '',
    'data': [
             'report/report.xml',
             'views/report_ddt.xml',
             'views/report_invoice.xml',
             ],
    'demo': [],
    'installable': True,
    'auto_install': True,
}