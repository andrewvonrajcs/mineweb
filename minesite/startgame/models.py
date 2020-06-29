from django.db import models
from mcstatus import MinecraftServer

class minecraftServer(models.Model):
    # TODO: add query to get online player usernames

    def __init__(self):
        self.server = MinecraftServer("minecraft-1.labfall.com", 25565) 

    def reload(self):
        # could add empty str defaults for description and the like
        self.ping()
        self.status()

    def status(self):
        # handle errors
        raw = self.server.status().raw
        self.description = raw['description']['text']
        self.players = raw['players']['online']
        self.version = raw['version']['name']

    def ping(self):
        # handle errors
        self.latency = self.server.ping() 
    
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
