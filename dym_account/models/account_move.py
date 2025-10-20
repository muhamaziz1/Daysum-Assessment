from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('invoice_line_ids')
    def _onchange_activate_exact_rounding(self):
        for move in self:
            if move.is_invoice() and any(line.manual_total_price for line in move.invoice_line_ids):
                rounding = self.env['account.cash.rounding'].search([('name', '=', 'Exact Total')], limit=1)
                if rounding:
                    move.invoice_cash_rounding_id = rounding