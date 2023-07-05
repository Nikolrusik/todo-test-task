from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.TextField(verbose_name='description')
    completed = models.BooleanField(default=False, verbose_name='completed')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created_at')

    def __str__(self):
        return self.title