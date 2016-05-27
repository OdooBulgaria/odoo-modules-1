# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 ISA srl (<http://www.isa.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Montecristo - Grid customization module',
    'version': '0.1',
    'category': '',
    'description': """
Personalizzazioni per Cliente Montecristo
=========================================
Il modulo rende visibile la funzione di ricerca per colore all'interno della funzionalità delle griglie

       """,
    'author': 'ISA srl',
    'depends': ['product_variant_grid',
                'sale_product_variant_grid',
                'purchase_product_variant_grid',
                'account_product_variant_grid',
                ],
    'data': [
             'account/account_invoice_form.xml',
             'sale/sale_order.xml',
             'purchase/purchase_order.xml',
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
    'certificate': '',
}
