from odoo import fields, models


class Tema(models.Model):
    _name = 'biblioteca.tema'
    _description = 'Tema de un libro'
    _order = 'name'

    name = fields.Char(string='Tema', required=True)