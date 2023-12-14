from django.db import models

class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    actueel = models.BooleanField(default = True)
    project = models.CharField(max_length = 100)
    opdrachtgever = models.CharField(max_length = 100)
    tonnage = models.IntegerField()
    bodemas_perc = models.CharField(max_length = 3)
    status = models.CharField(max_length = 1000)
    slagingskans = models.CharField(max_length = 3)
    planning = models.CharField(max_length = 20)
    actiehouder = models.CharField(max_length = 2)
    actie = models.CharField(max_length = 1000)

    def __str__(self):
        return(f"{self.project}")


