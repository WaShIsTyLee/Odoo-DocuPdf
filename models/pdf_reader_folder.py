from odoo import models, fields

class PDFReaderFolder(models.Model):
    _name = 'pdf.reader.folder'
    _description = 'Carpeta de Documentos PDF'

    name = fields.Char(string="Nombre de la Carpeta", required=True)
    document_ids = fields.One2many('pdf.reader.document', 'folder_id', string="Documentos")
