{
 'name': 'Biblioteca', # nombre que se verá en Odoo
 'version': '19.0.1.0.0', # versión de Odoo + versión del módulo
 'summary': 'Catálogo de libros', # descripción corta
 'author': 'Thiago', # pon aquí tu nombre
 'license': 'LGPL-3', # licencia (evita un aviso)
 'depends': ['base'], # necesita el núcleo de Odoo
 'data': [ 'security/ir.model.access.csv','data/tema_data.xml','views/libro_views.xml','views/tema_views.xml',], # archivos a cargar (aún ninguno)
 'application': True, # es una aplicación (tendrá icono)
}