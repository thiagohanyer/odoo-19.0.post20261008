from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Préstamo de un libro'
    _order = 'fecha_prestamo desc, id desc'

    name = fields.Char(string='Referencia', required=True, copy=False,
                       readonly=True, default='Nuevo')
    libro_id = fields.Many2one('biblioteca.libro', string='Libro',
                               required=True, ondelete='restrict')
    socio_id = fields.Many2one('res.partner', string='Socio', required=True,
                               ondelete='restrict',
                               domain=[('es_socio', '=', True)])
    fecha_prestamo = fields.Date(string='Fecha de préstamo', required=True,
                                 default=fields.Date.context_today)
    dias = fields.Integer(string='Días de préstamo', default=15)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
    ], string='Estado', default='borrador', required=True)

    # Campos calculados
    fecha_prevista = fields.Date(string='Devolución prevista',
                                 compute='_compute_fecha_prevista', store=True)
    retrasado = fields.Boolean(string='Retrasado', compute='_compute_retrasado')
    fecha_devolucion = fields.Date(string='Fecha de devolución', readonly=True)

    @api.depends('fecha_prestamo', 'dias')
    def _compute_fecha_prevista(self):
        for prestamo in self:
            if prestamo.fecha_prestamo:
                dias = timedelta(days=prestamo.dias)
                prestamo.fecha_prevista = prestamo.fecha_prestamo + dias
            else:
                prestamo.fecha_prevista = False

    @api.depends('estado', 'fecha_prevista')
    def _compute_retrasado(self):
        hoy = fields.Date.context_today(self)
        for prestamo in self:
            prestamo.retrasado = (prestamo.estado == 'prestado'
                                  and bool(prestamo.fecha_prevista)
                                  and prestamo.fecha_prevista < hoy)

    # Restricción
    @api.constrains('dias')
    def _check_dias(self):
        for prestamo in self:
            if prestamo.dias < 1 or prestamo.dias > 60:
                raise ValidationError(
                    'Los días de préstamo deben estar entre 1 y 60.')

    # Numeración automática al crear
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                secuencia = self.env['ir.sequence']
                vals['name'] = secuencia.next_by_code('biblioteca.prestamo') or 'Nuevo'
        return super().create(vals_list)

    # Botones
    def action_prestar(self):
        for prestamo in self:
            if not prestamo.libro_id.disponible:
                raise UserError(
                    'El libro «%s» no está disponible.' % prestamo.libro_id.name)
            prestamo.libro_id.disponible = False
            prestamo.estado = 'prestado'

    def action_devolver(self):
        for prestamo in self:
            prestamo.libro_id.disponible = True
            prestamo.estado = 'devuelto'
            prestamo.fecha_devolucion = fields.Date.context_today(self)