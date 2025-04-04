from odoo import http
from odoo.http import request

class PdfReaderController(http.Controller):
    
    @http.route('/pdf_reader/document/<model("pdf.reader.document"):document>/', type='http', auth="public")
    def get_pdf(self, document, **kwargs):
        if document.pdf_file:
            pdf_content = document.pdf_file
            pdf_filename = document.pdf_filename or "documento.pdf"
            return request.make_response(pdf_content,
                                         headers=[('Content-Type', 'application/pdf'),
                                                  ('Content-Disposition', f'inline; filename={pdf_filename}')])
        return "PDF no disponible"
