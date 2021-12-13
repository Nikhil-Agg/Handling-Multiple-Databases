from django.db import models

class test(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    either = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title