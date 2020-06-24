from django.db import models
from mcstatus import MinecraftServer

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

	self.server = MinecraftServer.lookup("example.org:1234") 
	self.status = server.status() 
	self.latency = server.ping() 
	self.query = server.query()


    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
	print("The server has {0} players and replied in {1} ms".format(self.status.players.online, self.status.latency))
	print("The server replied in {0} ms".format(self.latency))
	print("The server has the following players online: {0}".format(", ".join(self.query.players.names)))
        return self.my_field_name
