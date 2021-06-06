# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """ 
        Open Academy modules for managing trainings:
            - training courses
            - training sessions
            -attendees registration
    """,

    'author': "My Company",
    'website': "http://www/yourcompany.com",

    'category' : 'Test',
    'version': '0.1',

    'depends': ['base'],

    'data' : [
        'security/ir.model.access.csv',
        'views/openacademy.xml',
    ],
    
    'demo' : [
        'demo/demo.xml'
    ],
}