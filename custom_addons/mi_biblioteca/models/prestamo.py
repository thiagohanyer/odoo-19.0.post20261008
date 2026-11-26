from odoo import fields, models


class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Préstamo de un libro'
    _order = 'fecha_prestamo desc, id desc'

    name = fields.Char(string='Referencia', required=True, copy=False,
                       default='Nuevo')
    libro_id = fields.Many2one('biblioteca.libro', string='Libro',
                               required=True, ondelete='restrict')
    socio_id = fields.Many2one('res.partner', string='Socio', required=True,
                               ondelete='restrict')
    fecha_prestamo = fields.Date(string='Fecha de préstamo', required=True,
                                 default=fields.Date.context_today)
    dias = fields.Integer(string='Días de préstamo', default=15)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
    ], string='Estado', default='borrador', required=True)