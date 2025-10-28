from odoo import models, fields


## first type of Inheritance
# stop suggesting code 

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    property_id = fields.Many2one('property')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print( "----------------------------------------------" )
        print("inside action_confirm method of sale.orderrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        print( "----------------------------------------------" )
        return res
    