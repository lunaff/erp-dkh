from odoo import models, fields

class TypeCustomer(models.Model):
    _inherit = 'type.customer'

    customer_type = fields.Selection([
        ('toko', 'Toko'),
        ('bengkel', 'Bengkel'),
        ('modern_market', 'Modern Market'),
        ('ex_dealer_danapaint', 'Ex Dealer Danapaint')
    ], string='Customer Type')