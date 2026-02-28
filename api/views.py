from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project, Contact, ExpertiseCategory, SiteSettings
from .serializers import ProjectSerializer, ContactSerializer, ExpertiseCategorySerializer, SiteSettingsSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        "projects": "/api/projects/",
        "expertise": "/api/expertise/",
        "contact": "/api/contact/ [POST]",
        "messages": "/api/messages/ [GET]",
        "settings": "/api/settings/ [GET, PUT]",
    })

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer

class ContactDelete(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ExpertiseList(generics.ListAPIView):
    queryset = ExpertiseCategory.objects.all()
    serializer_class = ExpertiseCategorySerializer

class SiteSettingsDetail(generics.RetrieveUpdateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

    def get_object(self):
        obj, created = SiteSettings.objects.get_or_create(id=1)
        return obj
