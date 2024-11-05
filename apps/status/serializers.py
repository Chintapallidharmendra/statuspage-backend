from rest_framework import serializers
from .models import Page, Component, Account, Incident, SystemMetric, Subscriber
from apps.userauth.serializers import UserSerializer

class AccountSerializer(serializers.ModelSerializer):

    owner_data = UserSerializer(source='owner', read_only=True)

    class Meta:
        model = Account
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):

    account_name = serializers.CharField(write_only=True)
    account_details = AccountSerializer(source='account', read_only=True)

    def create(self, validated_data):
        account_name = validated_data.pop('account_name')
        account = Account.objects.filter(name=account_name).first()
        if not account:
            account = Account.objects.create(name=account_name, owner=self.context['request'].user)
        validated_data['account'] = account
        return super().create(validated_data)

    class Meta:
        model = Page
        fields = '__all__'
        read_only_fields = ('account','account_details')

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class SystemMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMetric
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'