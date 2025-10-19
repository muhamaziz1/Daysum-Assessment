# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = 'Account Move Line'
    
    manual_total_price = fields.Float(string='Manual Total Price', help='Manually entered total amount including tax')
    
    @api.onchange('manual_total_price', 'tax_ids', 'quantity')
    def _onchange_manual_total_price(self):
        for line in self:
            if not line.manual_total_price or not line.tax_ids:
                line.price_unit = line.manual_total_price
                continue

            sorted_taxes = line.tax_ids.sorted(key=lambda t: t.sequence)
            price_unit = line.manual_total_price
            for tax in reversed(sorted_taxes):
                if tax.amount_type == 'percent':
                    rate = tax.amount / 100.0
                    if 1 + rate != 0:
                        price_unit /= (1 + rate)
                    else:
                        price_unit = 0.0
                        break
                else:
                    price_unit = 0.0
                    break
            line.price_unit = price_unit / line.quantity