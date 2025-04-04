{
    'name': 'PDF Reader',
    'version': '1.0',
    'category': 'Document Management',
    'author': 'Juan Jesus',
    'summary': 'Módulo para leer y gestionar documentos PDF',
    'depends': ['base', 'web'],
    'data': [
        'views/pdf_reader_views.xml',
        'views/pdf_folder.xml',
    ],
    'installable': True,
    'application': True,
}
