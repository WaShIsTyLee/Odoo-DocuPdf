odoo.define('pdf_reader.pdf_viewer', function (require) {
    "use strict";

    var FormView = require('web.FormView');
    var core = require('web.core');
    var QWeb = core.qweb;
    var ajax = require('web.ajax');

    FormView.include({
        events: _.extend({}, FormView.prototype.events, {
            'click .oe_button_view_pdf': 'viewPdf',
        }),

        viewPdf: function (event) {
            var self = this;
            var pdfData = this.model.get(this.handle).data.pdf_file;
            if (pdfData) {
                var pdfUrl = "data:application/pdf;base64," + pdfData;
                var viewerWindow = window.open(pdfUrl, '_blank');
                viewerWindow.document.write('<iframe src="' + pdfUrl + '" width="100%" height="100%"></iframe>');
            }
        },
    });
});
