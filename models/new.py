from odoo import models, fields

class New(models.Model): 
    _name = 'new' 
    name=fields.Char()

    