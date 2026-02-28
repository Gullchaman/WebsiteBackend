from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project, Contact, ExpertiseCategory, SiteSettings
from .serializers import ProjectSerializer, ContactSerializer, ExpertiseCategorySerializer, SiteSettingsSerializer


class HomePageView(View):
    template_name = 'api/home.html'

    def get(self, request):
        context = {
            'projects': Project.objects.order_by('-created_at')[:6],
            'expertise_categories': ExpertiseCategory.objects.prefetch_related('skills').all(),
            'site_settings': SiteSettings.objects.first(),
        }
        return render(request, self.template_name, context)


class ProjectsPageView(View):
    template_name = 'api/projects.html'

    def get(self, request):
        context = {
            'projects': Project.objects.order_by('-created_at'),
            'site_settings': SiteSettings.objects.first(),
        }
        return render(request, self.template_name, context)


class ContactPageView(View):
    template_name = 'api/contact.html'

    def get(self, request):
        context = {
            'site_settings': SiteSettings.objects.first(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not message_text:
            messages.error(request, 'Please fill all required fields.')
            return redirect('contact-page')

        Contact.objects.create(
            name=name,
            email=email,
            message=message_text,
        )
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact-page')


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
