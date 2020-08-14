from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from . import models
from datetime import datetime

@never_cache
def status(request):
    model = models.minecraftStatus()
    if model.reload():
        html = """
<h1>{}</h1>
<h2>{}</h2>
<h2>{}</h2>
<h2>{}</h2>
<h2>{}</h2>
<h2>{}</h2>
""".format(model.description,model.version, model.players,datetime.now(),model.latency,model.playerNames)

    else:
        html = """
<h1>ERROR</h1>
<h2>{}</h2>
""".format(model.error)

    return HttpResponse(html)

