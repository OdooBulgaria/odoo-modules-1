# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 ISA s.r.l. (<http://www.isa.it>).
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
    'name': 'Product Variants Grid for Purchase Orders',
    'version': '0.1',
    'category': 'Product Management',
    'sequence': 14,
    'description': """
Il modulo consente di inserire, in qualsiasi documento di acquisto, le quantità 
dei prodotti con varianti, indicandole in un'apposita griglia.
    """,
    'author': 'ISA srl',
    'website': 'http://www.openerp.com',
    'depends': [
                'purchase',
                'product',
                'product_variant_grid',
                ],
    'data': [
             'views/purchase_product_variant_grid.xml',   
             'purchase_order.xml',        
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'qweb': ['static/src/xml/purchase_product_variant_grid.xml',],
}
