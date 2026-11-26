from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_socio = fields.Boolean(string='Socio de la biblioteca')
    prestamo_ids = fields.One2many('biblioteca.prestamo', 'socio_id',
                                   string='Préstamos')