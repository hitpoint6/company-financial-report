from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    business_model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    founder_quality = models.TextField()
    feature_set = models.TextField()

    def __str__(self):
        return self.name
    
class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    revenue = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True)
    cash_burn = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True)
    gross_profit = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True)
    ebitda = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True) 
    cash_on_hand = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True) 
    cac = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True)
    ltv = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True)
    lacvtv = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True) 
    customer_count = models.IntegerField(blank=True, null=True)
    next_fundraising = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)