from odoo import models, fields 

class Tag(models.Model): # owner inherits from Model
    _name = 'tag' #name will be used everywhereeeeeeeeeeeeeee

    name = fields.Char(required= True) 
 