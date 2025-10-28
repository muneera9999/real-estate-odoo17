from odoo import models, fields 

class Owner(models.Model): # owner inherits from Model
    _name = 'owner' #name will be used everywhereeeeeeeeeeeeeee

    name = fields.Char(required= True) 
    phone = fields.Char()
    address = fields.Char()

    property_ids=fields.One2many('property','owner_id') #one2many parameters alwasy ('model name','name of inverse field (many2one) ')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'this name already exists!'),
        ('unique_phone', 'unique("phone")', 'this phone already in use!')
    ]

   