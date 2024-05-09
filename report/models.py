from django.db import models


# Create your models here.
class Report(models.Model):
    operator_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    production_piece_count = models.IntegerField()
    defective_piece_count = models.IntegerField()
    machine = models.CharField(max_length=500)
    report_text = models.TextField()
