from odoo import models, fields, api #api needed for validation for interger and float values
from odoo.exceptions import ValidationError 

class Property(models.Model): # property inherits from Model
    _name = 'property' #name will be used everywhereeeeeeeeeeeeeee
    _inherit = ['mail.thread','mail.activity.mixin'] # add chatter
    _description='Property' # like the string for the class name

    name = fields.Char(required= True) 
    # "required" defalut is false # I can write 1 and 0 instead of True and False 
    #default ='new is the default name 
    #size=5 is the number of char allowed

    # when i use recuired attribute in py it is recognised in both py and xml but if i declare it in xml, it is only know in xml not in logic (py) tier.

    description = fields.Text(tracking=1) #tracking for the chatter activity
    postcode= fields.Char(required=1)
    date_availability= fields.Date(tracking=1) # _ becomes a space #tracking for the chatter activity
    expected_price = fields.Float() # parameters: digits=(0,4)
    selling_price = fields.Float()
    diff= fields.Float(compute="_compute_diff", store=1) #parameters: (though it didn't really work the automation) readonly=0
    total=fields.Float(compute="_compute_total", string="total(auto-total for fun)")
    bedrooms = fields.Integer( default="1") # don't want to deal with the 0 bedrooms constraint LOL
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation =fields.Selection([
        ('north','North'), # the first north is the set name (must bbe small) the second value North is the display name 
        ('south','South'),
        ('east','East'),
        ('west','West'),
    
    ] ) 
    #can use "default= " in all attributes

    owner_id=fields.Many2one('owner', string='Owner')
    tag_ids= fields.Many2many('tag')

    owner_address= fields.Char(related='owner_id.address', readonly=0)          # creating related fields. 
    owner_phone= fields.Char(related= 'owner_id.phone')                         # is automatically readonly but can use "readonly=0" to disable.
                                                                                # doesn't auto store, must use "store=1" but i tried it with save manual and it worked fine without it so idk
                                                                                # must be the same field type Char().
                                                                           
    ## or can use compute method to make this:
    # owner_address=fields.Char(compute="_compute_owner_address")
    # @api.depends('owner_id.address')
    # def _compute_owner_address(self):
    #      for rec in self:
    #         rec.owner_address = rec.owner_id.address
    

    _sql_constraints = [
        ('unique_name','unique(name)','This name already exists! NewJeans do you see?')
    ]

    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold')
    ], default='draft') 


    line_ids= fields.One2many('property.line','property_id')


    @api.depends('expected_price', 'selling_price', 'owner_id.phone') #must use @api.depends when using a compute method, can be used on all fields in the class
    def _compute_diff(self):
        for rec in self:   # rec loop for each record
            print(rec) #returns an actual record after saving
            print("inside _compute_diff method-------------------------------------------------------")
            rec.diff = rec.expected_price - rec.selling_price

    @api.onchange('expected_price') #whenever expected_price changes the method is triggered, can't access owner class fields like depends
    def _onchange_expected_price(self):
        for rec in self:
            print(rec) #saves only in memory, not yet a record, onchange triggered rec only returns sudo record
            print("inside _onchange_expected_price method -------------------------------------------")
            return {
                'warning': {'title':'warning','message':'negative value.', 'type':'notification'}
            }
            

    def _compute_total(self):
        for rec in self:
            rec.total = rec.expected_price + rec.selling_price 

    @api.constrains('bedrooms') 
    def _check_bedrooms_greater_zero(self): # [self] here is a one instance of the class called record
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError("Please add a vaild number of bedrooms") #can't continue to save unless I add a number higher than 0
            
    @api.constrains('name')
    def _name_accurate(self):
        for rec in self:
            if rec.name.isdigit():
                raise ValidationError("please add a vaild name not containing numbers")


    def action_draft(self): #the difference betwen method and fucnction?
        for rec in self:
            print("Draft methoddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
            rec.state='draft'
        #  rec.write({
        #      'state' :'draft'
        #  })
    
    def action_pending(self): #the difference betwen method and fucnction?
        for rec in self:
            print("pending ----------------------------------------------------------------------")
            rec.write({
                'state' :'pending'
                  })
    

    def action_sold(self): #the difference betwen method and fucnction?
        for rec in self:
            print("sold -------------------------------------------------------------------------")
            rec.state='sold'



    # ## [self] here is used as a set for multiple instances called recordset. (avoid this) //research more about it

    #     # if self.bedrooms == 0:
    #     #     raise ValidationError("Please add a vaild number of bedrooms")
         
         
    #     # functions I'm gonna use are all from Models class (inherited)
    #     # CURD Operations: Create, Update, Read, Delete

    # # override for create method    #CRUD: CREATE
    # @api.model_create_multi
    # def create(self,vals): #self is always the first value in models method class methods
    #     res= super(Property,self).create(vals)
    #     #res= super().create(self,vals)     #same thing
    #     print("inside create method")
    #     return res
    
    # # override for search method    #CRUD: READ
    # @api.model  
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None): #_search bc its override
    #     res= super(Property,self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("inside search method")
    #     return res
    
    # def write(self,vals):  
    #     res= super(Property,self).write(vals)
    #     print("inside write method")
    #     return res
    
    # def unlink(self):
    #     res= super(Property,self).unlink()
    #     print("inside unlink method")
    #     return res
    

class PropertyLine(models.Model): # property inherits from Model
    _name = 'property.line' #name will be used everywhereeeeeeeeeeeeeee
    _description='Property Line' # like the string for the class name


    property_id= fields.Many2one('property')
    area = fields.Float()
    description= fields.Char()

  




