from odoo import models
# stop suggesting code. 


## 2nd type of Inheritance 

class Client(models.Model):
    _name = 'client'
    _inherit = 'owner' # didn't add any fields, all fields will come from owner class