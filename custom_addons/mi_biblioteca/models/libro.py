from odoo import fields, models


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