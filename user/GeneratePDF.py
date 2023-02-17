from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import View
from django.template.loader import get_template
from .reportPDF import render_to_pdf




class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('site/report.html')
        context = {
            "invoice_id": 123,
            "username": "Kwame"
            }
        html = template.render(context)
        pdf = render_to_pdf('site/report.html', context)
        if pdf:
            #return HttpResponse(pdf, content_type='application/pdf')
            ##to force a download of pdf
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Report_%s.pdf" %("1234567")
            content = "inline; filename='%s'" %(filename)
            #response['Content-Disposition'] = content
            download = request.GET.get('download')
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse('Not found')