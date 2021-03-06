# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 ISA s.r.l. (<http://www.isa.it>).
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
    'name': "ISA s.r.l. - Hr Holidays",
    'summary': "Manage Employee's Holidays",
    'version': "1.0",
    'author': "ISA srl",
    'category': 'Generic Modules/Human Resources',
    'website': 'http://www.isa.it',
    'depends': ['hr_holidays',
                'hr_contract',
                'base_res_company_isa',
                'report_webkit',
                'account_financial_report_webkit',
                ],
    'data': ['security/ir.model.access.csv',
             'views/hr_holidays_view.xml',
             'views/hr_holidays_status_view.xml',
             'views/resource_calendar_view.xml',
             'wizard/hr_holidays_bymonth_view.xml',
             'report/report.xml',
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
}
