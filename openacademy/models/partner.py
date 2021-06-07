# -*- coding: utf-8 -*-
from odoo import fields, models, api
    
class Partner(models.Model):

    _inherit = 'res.partner'


    # add a new colum to res.partner, by default partner are not
    instructor = fields.Boolean('Instructor', default=False)

    session_ids = fields.Many2many('openacademy.session', 
        string='Attended Sessions', readonly=True)
