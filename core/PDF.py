# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas

class Generator:

    def gen_from_files(self, out, files):
        c = canvas.Canvas(out)
        for x in files:
            c.drawImage(x, 0, 0)
        c.showPage()
        c.save()