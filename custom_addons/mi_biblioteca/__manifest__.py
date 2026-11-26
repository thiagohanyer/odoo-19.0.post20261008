{
 'name': 'Biblioteca', # nombre que se verá en Odoo
 'version': '19.0.1.0.0', # versión de Odoo + versión del módulo
 'summary': 'Catálogo de libros', # descripción corta
 'author': 'Thiago', # pon aquí tu nombre
 'license': 'LGPL-3', # licencia (evita un aviso)
 'depends': ['base', 'contacts'], # necesita el núcleo de Odoo
 'data': [
    'security/biblioteca_security.xml',
    'security/ir.model.access.csv',
    'data/tema_data.xml',
    'data/prestamo_sequence.xml',
    'views/libro_views.xml',
    'views/tema_views.xml',
    'views/prestamo_views.xml',
    'views/res_partner_views.xml',
],
 'application': True, # es una aplicación (tendrá icono)
}