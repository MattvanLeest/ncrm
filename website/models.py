from django.db import models

class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    actueel = models.BooleanField(default = True)
    project = models.CharField(max_length = 100)
    opdrachtgever = models.CharField(max_length = 100)
    tonnage = models.IntegerField()
    bodemas_perc = models.IntegerField()
    status = models.CharField(max_length = 1000)
    slagingskans = models.IntegerField()
    planning = models.CharField(max_length = 20)
    actiehouder = models.CharField(max_length = 2)
    actie = models.CharField(max_length = 1000)

    def __str__(self):
        return(f"{self.project}")

    @property
    def ton_bodemas(self):
        return (int(float(self.tonnage * self.bodemas_perc/100)))

    @property
    def ton_grond(self):
        return self.tonnage - self.ton_bodemas

    @property
    def grond_perc(self):
        return 100 - self.bodemas_perc

    @property
    def nu_actueel(self):
        if self.actueel == True:
            thing = "Ja"
        else:
            thing = "Nee"
        return thing
    


    
    

     

