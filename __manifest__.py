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
    'assets': {
        'web.assets_backend': [
            'pdf_reader/static/src/css/pdf_reader_styles.css',
        ],
    },
    'installable': True,
    'application': True,
}
