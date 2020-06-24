from django.db import models
from mcstatus import MinecraftServer

class MyModelName(models.Model):

    def getstatus(self):
        self.server = MinecraftServer.lookup("minecraft-1.labfall.com:25565") 
        self.status = self.server.status() 
        self.latency = self.server.ping() 
        self.query = self.server.query()

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        self.getstatus()
        a = "The server has {0} players and replied in {1} ms".format(self.status.players.online, self.status.latency)
        b = "The server replied in {0} ms".format(self.latency)
        c = "The server has the following players online: {0}".format(", ".join(self.query.players.names))
        status = a + '\n' + b + '\n' + c
        return status
