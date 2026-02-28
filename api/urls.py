from django.urls import path
from .views import ProjectList, ContactCreate, ContactList, ContactDelete, ExpertiseList, SiteSettingsDetail, api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('contact/', ContactCreate.as_view(), name='contact-create'),
    path('messages/', ContactList.as_view(), name='contact-list'),
    path('messages/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
    path('expertise/', ExpertiseList.as_view(), name='expertise-list'),
    path('settings/', SiteSettingsDetail.as_view(), name='site-settings'),
]
