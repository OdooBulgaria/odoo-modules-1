# -*- encoding: utf-8 -*-
##############################################################################
#
#    Authors: Matthieu Dietrich
#    Copyright Camptocamp SA 2014
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
    'name': 'Add multiple export to ledger reports',
    'version': '0.1',
    'license': 'AGPL-3',
    'author': 'Camptocamp',
    'category': 'Generic Modules/Accounting',
    'description': """
        This module add a multiple export option for ledgers
        (partners and general), in order to export one PDF file
        per account. This is useful if the customer has many lines.
    """,
    'depends': ['account_financial_report_webkit'],
    'demo_xml': [],
    'init_xml': [],
    'update_xml': [
        'report.xml',
        'wizard/general_ledger_wizard_view.xml',
        'wizard/partners_ledger_wizard_view.xml',
    ],
    'active': False,
    'installable': True,
}
