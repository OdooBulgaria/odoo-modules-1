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

from openerp.osv import fields, orm
from openerp.tools.translate import _


class wizard_values_customer_confirm(orm.TransientModel):
    _name = 'wizard.values.customer.confirm'
    _description = 'Wizard Confirm Values'
    
    def onchange_operation_date(self, cr, uid, ids, operation_date, context=None):
        
        period_obj = self.pool.get('account.period')
        t_period_id = period_obj.find(cr, uid, operation_date, context)[0]

        return {
                'value': {
                          'operation_date': operation_date,
                          'period_id': t_period_id
                          }
                }

    def onchange_bank_id(self, cr, uid, ids, bank_id, context=None):
        
        bank_obj = self.pool.get('res.partner.bank')
        t_bank_data = bank_obj.browse(cr, uid, bank_id, context)
        t_account_id = t_bank_data.journal_id.default_credit_account_id.id

        return {
                'value': {
                          'journal_id': t_bank_data.journal_id.id,
                          'account_id': t_account_id,
                          }
                }

    _columns = {
        'partner_id': fields.many2one('res.partner',
                                   'Customer',
                                   readonly=True),
        'maturity': fields.date('Maturity Maximum',
                                readonly=True),
        'all_customer': fields.boolean('All customers',
                                       readonly=True),
        'journal_id':fields.many2one('account.journal',
                                     'Sezionale',
                                     readonly=True),
        'account_id':fields.many2one('account.account',
                                     'Account',
                                     readonly=True),
        'bank_id': fields.many2one('res.partner.bank',
                                   'Bank',
                                   required=True),
        'period_id': fields.many2one('account.period',
                                     'Period',
                                     required=True),
        'riba': fields.boolean('Exclude Riba',
                                readonly=True),
        
        'operation_date': fields.date('Operation Date',
                                      required=True),
        'currency_date': fields.date('Currency Date'),
      
    }
    _defaults = {
                 'currency_date': fields.date.context_today,
                 }
    
    def set_confirm_payment_lines(self, cr, uid, context=None):

        t_lines = []
        list_partner = []
        vals = {}
            
        context_partner_id =    context.get('default_partner_id', None)
        t_journal_id =          context.get('default_journal_id', None)
        t_all_customers =       context.get('default_all_customer', None)
        t_maturity =            context.get('default_maturity', None)
        t_operation_date =      context.get('default_operation_date', None)
        t_currency_date =       context.get('default_currency_date', None)
        t_wizard =              context.get('wizard_id', None)
        t_riba =                context.get('default_riba', None)
        
        vals['partner_id'] = context_partner_id
        vals['maturity'] = t_maturity
        vals['journal_id'] = t_journal_id
        vals['all_customer'] = t_all_customers
        vals['operation_date'] = t_operation_date
        vals['currency_date'] = t_currency_date
        vals['riba'] = t_riba
        
        list_partner.append(context_partner_id)
        if(t_all_customers):
            list_partner = []
            vals['partner_id'] = None
            list_partner = self.pool.get('res.partner').search(cr,
                                                                uid,
                                                                [('customer', '=', True)])
              
        res_id = self.pool.get('wizard.confirm.customer.payment').create(cr, uid, vals, context=context)
        wizard_line_obj = self.pool.get('wizard.confirm.customer.payment.line')
        
        for t_partner_id in list_partner:
            vals = {}
            t_filter2 = ['&', ('partner_id', '=', t_partner_id), ('is_selected', '=', 'accepted'), ('confirm_payment_id', '=', t_wizard)]
           
            wizard_line_ids = wizard_line_obj.search(cr,
                                                    uid,
                                                    t_filter2,
                                                    context=context)
           
            if wizard_line_ids:
                for line_id in wizard_line_obj.browse(cr, uid, wizard_line_ids):
                    t_move_line = line_id.move_line_id
                    t_state = t_move_line.state
                    t_lines.append((0, 0, {
                                          'partner_id': t_move_line.partner_id.id,
                                          'account_id': t_move_line.account_id.id,
                                          'state': t_state,
                                          'is_selected': 'accepted',
                                          'move_line_id': t_move_line.id,
                                          'confirm_payment_id': res_id,
                                          'amount': line_id.amount,
                                          'amount_partial': line_id.amount_partial,
                                          'payment_type': line_id.payment_type,
                                          'allowance': line_id.allowance,
                                          'amount_allowance': line_id.amount_allowance,
                                          'partner_bank_id': line_id.partner_bank_id.id
                                          }))

        self.pool.get('wizard.confirm.customer.payment').write(cr, uid, [res_id], {'line_ids': t_lines})

        return res_id
    
    
    def confirm(self, cr, uid, ids, context=None):
        t_partner_id = None
        t_journal_id = None
        t_period_id = None
        t_bank_id = None
        
        form = self.read(cr, uid, ids)[0]
        if(form["partner_id"]):
            t_partner_id = form["partner_id"][0]
        t_maturity = form["maturity"]
        t_operation_date = form["operation_date"]
        t_currency_date = form["currency_date"]
        t_all_customer = form["all_customer"]
        t_riba = form["riba"]
        if (form["period_id"]):
            t_period_id = form["period_id"][0]
        if (form["journal_id"]):
            t_journal_id = form["journal_id"][0]
        if(form["bank_id"]):
            t_bank_id = form["bank_id"][0]
        
        context.update({
            'default_partner_id': t_partner_id,
            'default_maturity': t_maturity,
            'default_all_customer': t_all_customer,
            'default_riba': t_riba,
            'default_period_id': t_period_id,
            'default_journal_id': t_journal_id,
            'default_bank_id': t_bank_id,
            'default_operation_date': t_operation_date,
            'default_currency_date': t_currency_date
        })

        res_id = self.set_confirm_payment_lines(cr, uid, context)
        
        mod_obj = self.pool.get('ir.model.data')
        result = mod_obj.get_object_reference(cr, uid,
                                              'account_voucher_makeover',
                                              'wizard_confirm_customer_payment_view')
        view_id = result and result[1] or False

        return {
              'name': _("Confirm Payment Action"),
              'view_type': 'form',
              'view_mode': 'form',
              'res_model': 'wizard.confirm.customer.payment',
              'type': 'ir.actions.act_window',
              'res_id': res_id,
              'view_id': view_id,
              'context': context,
              'target': 'inlineview',
              }
