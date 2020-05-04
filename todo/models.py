from django.db import models

# Create your models here.

# This class represents the Todo table in the database
# Todo will inherit modesls.Model, the latter is a Django class
# that already has the functionality we need. By inheriting, Todo will 
# have all those functionalities
class Todo(models.Model):
    name = models.CharField(max_length=255, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name
