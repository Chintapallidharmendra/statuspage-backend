from rest_framework import viewsets, permissions

from .models import Page, Component, Incident, SystemMetric, Subscriber
from .serializers import PageSerializer, ComponentSerializer, IncidentSerializer, SystemMetricSerializer, SubscriberSerializer

class PageViewset(viewsets.ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Page.objects.filter(account__owner=user)

class ComponentViewset(viewsets.ModelViewSet):

    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def get_queryset(self):
        page_id = self.request.query_params.get('page_id')
        if page_id:
            return Component.objects.filter(page_id=page_id)
        return Component.objects.all()

class IncidentViewset(viewsets.ModelViewSet):

    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        page_id = self.request.query_params.get('page_id')
        if page_id:
            return Incident.objects.filter(page_id=page_id)
        return Incident.objects.all()

class SystemMetricViewset(viewsets.ModelViewSet):

    queryset = SystemMetric.objects.all()
    serializer_class = SystemMetricSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        page_id = self.request.query_params.get('page_id')
        if page_id:
            return SystemMetric.objects.filter(page_id=page_id)
        return SystemMetric.objects.all()
    
class SubscriberViewset(viewsets.ModelViewSet):
    
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    
    def get_queryset(self):
        page_id = self.request.query_params.get('page_id')
        if page_id:
            return Subscriber.objects.filter(page_id=page_id)
        return Subscriber.objects.all()