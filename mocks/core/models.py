from django.db import models


class Congressperson(models.Model):
    applicant_id = models.IntegerField('Applicant ID', db_index=True)
    name = models.CharField('Name', max_length=140)
