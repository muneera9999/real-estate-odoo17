{
    'name':"App one", #name of App eg. CRM 
    'author': "Muneera Abdulaziz",
    'category':'', # Categories :Sales, Services, Accounting, Inventory, Manufacturing, Website, Marketing, Human Resources, Productivity ,Administration
    'version':'17.0.0.1.0', #the first three "17.0.0" is the odoo version, the last two numbers "1.0" is the version of our app, if it gets updated it might be 1.2
    'depends': ['base',  #other apps needed to support our main app "base" is the The kernel of Odoo, needed for all installation. used in most app models with database
                'sale_management',
                'account',
                'contacts'
               ],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views\owner_view.xml',
        'views/tag_view.xml',
        'views/new_view.xml',
        'views\sale_order_view.xml',
        'views/res_partner_view.xml'
    ],
    'assets': { ## for css and javscript files
        'web.assets_backend': ['app_one\static\src\css\property.css']

    },
    'applications': True, #ask about this i didn't understand fully////////////////////////////////////////////////////////////////
}