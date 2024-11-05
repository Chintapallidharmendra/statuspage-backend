from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Page(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    account = models.ForeignKey(Account, related_name="pages", on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)

class Component(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('Operational', 'Operational'),
        ('Partial Outage', 'Partial Outage'),
        ('Degraded Performance', 'Degraded Performance'),
        ('Major Outage', 'Major Outage'),
        ('Under Maintenance', 'Under Maintenance'),
    ])
    page = models.ForeignKey(Page, related_name="components", on_delete=models.CASCADE)

class Incident(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Investigating', 'Investigating'),
        ('Identified', 'Identified'),
        ('Monitoring', 'Monitoring'),
        ('Resolved', 'Resolved'),
    ])
    page = models.ForeignKey(Page, related_name="incidents", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscriber(models.Model):
    email = models.EmailField()
    page = models.ForeignKey(Page, related_name="subscribers", on_delete=models.CASCADE)

class SystemMetric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, related_name="metrics", on_delete=models.CASCADE)
