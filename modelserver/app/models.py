from django.db import models

class AiModel(models.Model):
    name=models.CharField(max_length=200, blank=True, null=True)
    modelfile=models.FileField(upload_to='model/')

    def __str__(self) -> str:
        return  self.name