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
    'name': 'Mattioli - Package manager',
    'version': '0.1',
    'category': '',
    'description': """
                    Questo modulo permette di tenere traccia, in fase di vendita,
                    del pacco di provenienza del prodotto, permettendo di selezionare
                    per ogni prodotto, il pacco di origine.
                   """,
    'author': 'ISA srl',
    'depends': ['procurement',
                'sale',
                'stock',
                'sale_stock',
                'stock_makeover',
                'delivery_makeover',
                'sale_product_variant_grid',
                ],
    'data': ['sale_order.xml',
             'stock_view.xml',
             'sale_stock_view.xml',
             'stock_transfer_details.xml',
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
    'certificate': '',
}
