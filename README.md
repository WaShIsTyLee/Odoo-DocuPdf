# Módulo Odoo - `pdf_reader`

Este módulo de Odoo está diseñado para la gestión y visualización de documentos PDF. A continuación, se describe la estructura y contenido básico del módulo.

## Estructura del módulo


pdf_reader/ ├── init.py ├── manifest.py ├── controllers/ │ └── pdf_controller.py ├── models/ │ ├── init.py │ ├── pdf_document.py │ └── pdf_reader_folder.py ├── static/ │ └── src/ │ └── js/ │ └── pdf_viewer.js ├── views/ │ ├── pdf_folder.xml │ └── pdf_reader_views.xml



## Explicación de la estructura

### `__init__.py`
Este archivo se utiliza para marcar el directorio como un paquete Python y para inicializar la estructura del módulo.
> [!TIP]  
> En este `__init__` deberemos importar los Controladores y el Modelo.

### `__manifest__.py`
Es el archivo de configuración del módulo, donde se definen los metadatos del módulo, como el nombre, la versión, las dependencias y los archivos que se cargan al instalar el módulo.

### Carpeta `controllers/`
- **`pdf_controller.py`**: Este archivo contiene el controlador que gestiona las rutas de acceso web y la visualización de documentos PDF.

### Carpeta `models/`
- **`__init__.py`**: Inicializa los modelos en esta carpeta.
> [!TIP]  
> En este `__init__` deberemos importar nuestro modelo.
- **`pdf_document.py`**: Define el modelo para los documentos PDF, incluyendo campos como el nombre del documento y el archivo binario.
> [!WARNING]  
> Asegúrate de que el campo binario esté correctamente definido, ya que los documentos PDF se almacenan en este formato. Si no lo haces bien, podrías perder la información o generar errores al intentar cargar el documento.
- **`pdf_reader_folder.py`**: Define el modelo para las carpetas que almacenan los documentos PDF.

### Carpeta `static/src/js/`
- **`pdf_viewer.js`**: Este archivo contiene el código JavaScript necesario para visualizar los documentos PDF en la interfaz de usuario.
> [!DANGER]  
> Si hay algún error en este archivo JavaScript, puede afectar la visualización de los documentos PDF. Asegúrate de probar completamente este archivo en la interfaz para evitar problemas de usabilidad.

### Carpeta `views/`
- **`pdf_folder.xml`**: Define las vistas de Odoo para gestionar las carpetas de documentos PDF.
- **`pdf_reader_views.xml`**: Define las vistas de Odoo para la visualización de documentos PDF.

## Contenido de los Archivos Importantes

### `__manifest__.py`
```python
{
    'name': 'PDF Reader',
    'version': '1.0',
    'category': 'Document Management',
    'author': 'Tu Nombre',
    'website': 'http://www.tusitio.com',
    'depends': ['base'],
    'data': [
        'views/pdf_folder.xml',
        'views/pdf_reader_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
