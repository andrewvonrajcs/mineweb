from django.shortcuts import render
from django.http import HttpResponse
from . import models

def status(request):
    model = models.minecraftServer()
    model.reload()

    html = """
<h1>{}</h1>
<h2>{}</h2>
<h2>{}</h2>
""".format(model.description,model.version, model.players)

    return HttpResponse(html)
