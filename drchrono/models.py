from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class PatientModel(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    doctor_id = models.IntegerField(null=False)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=10, null=True)
    patient_id = models.IntegerField(null=False, primary_key=True)
    patient_email = models.EmailField(default="")

    def __str__(self):
        hyphen = "|"
        patient = (str(self.patient_id),self.first_name,self.last_name,str(self.birthday),str(self.patient_email))
        return hyphen.join(patient)