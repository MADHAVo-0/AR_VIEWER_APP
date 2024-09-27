# ar_app/models.py
from django.db import models

class ARModel(models.Model):
    name = models.CharField(max_length=100)
    glb_file = models.FileField(upload_to='glb_models/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
