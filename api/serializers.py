from rest_framework import serializers
from .models import Project, Contact, ExpertiseCategory, ExpertiseSkill, SiteSettings

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ExpertiseSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertiseSkill
        fields = ['id', 'name']

class ExpertiseCategorySerializer(serializers.ModelSerializer):
    skills = ExpertiseSkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = ExpertiseCategory
        fields = ['id', 'name', 'icon_name', 'skills']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'
