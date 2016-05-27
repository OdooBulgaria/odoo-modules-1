# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Abstract (http://www.abstract.it)
#    @author Davide Corio <davide.corio@abstract.it>
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

from openerp import models, api


class better_zip_geonames_import(models.TransientModel):
    _inherit = 'better.zip.geonames.import'

    @api.model
    def create_better_zip(self, row, country):
        res = super(better_zip_geonames_import, self).create_better_zip(
            row, country)
        if not res.state_id.region_id:
            region_model = self.env['res.country.region']
            region = region_model.search([('code', '=', row[4])])
            if not region:
                region = region_model.create(
                    {'name': row[3], 'code': row[4]})
            res.state_id.region_id = region.id
        return res

    @api.model
    def select_or_create_state(
        self, row, country_id, code_row_index=4, name_row_index=3
    ):
        res = super(better_zip_geonames_import, self).select_or_create_state(
            row, country_id, code_row_index=6, name_row_index=5)

        region_model = self.env['res.country.region']
        region = region_model.search([('code', '=', row[4])])
        if not region:
            region = region_model.create(
                {'code': row[4], 'name': row[3]})
        res.region_id = region.id
        return res
