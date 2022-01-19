# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Rainhistory',
    'category': 'Sales/CRM',
    'sequence': 150,
    'summary': 'Shows historical rain data',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
