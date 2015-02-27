# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

class Generator:

    def gen_from_files(self, out, files):
        (w, h) = A4
        c = canvas.Canvas(out, pagesize = A4)
        for image in files:
            try:
                url = image.get_name()
                c.drawImage(url, 0, 0, w, h)
                c.showPage()
            except:
                continue
        c.save()