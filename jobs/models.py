from django.db import models

class Job (models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField(max_length=500)
    salary = models.DecimalField(max_digits=60, decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    #Metadata
    class Meta :
        ordering = ['id']

    #Methods
    def __str__(self):
        return f"{self.company_name}"
