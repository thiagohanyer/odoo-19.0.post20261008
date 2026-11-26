from odoo import api, fields, models


class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor')
    isbn = fields.Char(string='ISBN')
    fecha_publicacion = fields.Date(string='Fecha de publicación')
    disponible = fields.Boolean(string='Disponible', default=True)
    paginas = fields.Integer(string='Número de páginas')
    genero = fields.Selection([('novela', 'Novela'),('tecnico', 'Técnico'),('ensayo', 'Ensayo'),], string='Género')
   
    # Relaciones
    tema_ids = fields.Many2many('biblioteca.tema', string='Temas')
    prestamo_ids = fields.One2many('biblioteca.prestamo', 'libro_id',
                                   string='Préstamos')

    # Campo calculado (no se guarda en la tabla)
    num_prestamos = fields.Integer(string='Nº de préstamos',
                                   compute='_compute_num_prestamos')

    @api.depends('prestamo_ids')
    def _compute_num_prestamos(self):
        for libro in self:
            libro.num_prestamos = len(libro.prestamo_ids)
    