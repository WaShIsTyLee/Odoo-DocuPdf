from odoo import models, fields
from odoo.exceptions import UserError
import base64

class PdfDocument(models.Model):
    _name = 'pdf.reader.document'
    _description = 'Documentos PDF'

    name = fields.Char(string="Nombre", required=True)
    subject = fields.Char(string="Asunto")
    contact = fields.Char(string="Contacto")
    owner = fields.Many2one('res.users', string="Propietario")
    pdf_file = fields.Binary(string="Archivo PDF")
    pdf_filename = fields.Char(string="Nombre del archivo PDF")
    
    folder_id = fields.Many2one('pdf.reader.folder', string="Carpeta")


    def action_view_pdf(self):
        self.ensure_one()
        if not self.pdf_file:
            raise UserError("No se ha cargado ningún archivo PDF.")

        return {
            'name': 'Vista previa del PDF',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'pdf.reader.document',
            'view_id': self.env.ref('pdf_reader.view_pdf_preview_form').id, 
            'target': 'new', 
            'res_id': self.id,
        }

