from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit='res.partner'
    
    property_id= fields.Many2one('property')
     

    price= fields.Float(related='property_id.selling_price')

    #OR using related 

    # price = fields.Float(compute='_compute_price')
    
    # @api.depends('property_id', 'property_id.selling_price')
    # def _compute_price(self):
    #     for rec in self:
    #         rec.price = rec.property_id.selling_price

    


       
