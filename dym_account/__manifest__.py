# -*- coding: utf-8 -*-
{
    'name': "DYM Account",

    'summary': """
        Add manual total price field on invoice lines for tax-inclusive pricing.
    """,

    'description': """
        This module extends the account.move.line model to support manual entry of total price including tax, and automatically computes the price_unit based on applied inclusive taxes. The field is visible only on customer and vendor invoices/credit notes.
    """,

    'author': "Muhamad Abdul Aziz",
    'website': "daysum.net",

    'category': 'Accounting',
    'version': '16.0.1.0.0',

    'depends': ['base', 'account'],

    'data': [
        'views/account_move_line_view.xml',
    ],

    'application': False,
}