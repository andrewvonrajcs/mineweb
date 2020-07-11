from django.db import models
from mcstatus import MinecraftServer

class minecraftStatus(models.Model):
    # TODO: add query to get online player usernames

    def __init__(self):
        self.server = MinecraftServer("minecraft-1", 25565) 

    def reload(self):
        try:
            self.ping()
            self.status()
            self.onlinePlayers()
            return True
        except Exception as e:
            self.error = e
        return False

    def status(self):
        raw = self.server.status().raw
        self.description = raw['description']['text']
        self.players = raw['players']['online']
        self.version = raw['version']['name']
    
    def onlinePlayers (self):
        self.playerNames = self.server.query().players.names

    def ping(self):
        self.latency = self.server.ping() 
    
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
