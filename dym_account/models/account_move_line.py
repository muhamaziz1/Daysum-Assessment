# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = 'Account Move Line'
    
    manual_total_price = fields.Float(string='Manual Total Price', help='Manually entered total amount including tax')
    
    @api.onchange('manual_total_price', 'tax_ids', 'quantity')
    def _onchange_manual_total_price(self):
        for line in self:
            qty = line.quantity or 1.0
            if not line.manual_total_price or not line.tax_ids:
                line.price_unit = line.manual_total_price / qty
                continue

            all_inclusive = all(tax.price_include for tax in line.tax_ids)

            if all_inclusive:
                line.price_unit = line.manual_total_price / qty
            else:
                sorted_taxes = line.tax_ids.sorted(key=lambda t: t.sequence)
                total_incl = line.manual_total_price
                subtotal_excl_tax = total_incl
                for tax in reversed(sorted_taxes):
                    if tax.amount_type == 'percent':
                        rate = tax.amount / 100.0
                        if 1 + rate != 0:
                            subtotal_excl_tax /= (1 + rate)
                        else:
                            subtotal_excl_tax = 0.0
                            break
                    else:
                        subtotal_excl_tax = 0.0
                        break
                line.price_unit = subtotal_excl_tax / qty