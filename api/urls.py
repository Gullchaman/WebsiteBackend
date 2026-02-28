from django.urls import path
from .views import (
    ContactCreate,
    ContactDelete,
    ContactList,
    ContactPageView,
    ExpertiseList,
    HomePageView,
    ProjectList,
    ProjectsPageView,
    SiteSettingsDetail,
    api_root,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectsPageView.as_view(), name='projects-page'),
    path('contact/', ContactPageView.as_view(), name='contact-page'),
    path('api/', api_root, name='api-root'),
    path('api/projects/', ProjectList.as_view(), name='project-list'),
    path('api/contact/', ContactCreate.as_view(), name='contact-create'),
    path('api/messages/', ContactList.as_view(), name='contact-list'),
    path('api/messages/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
    path('api/expertise/', ExpertiseList.as_view(), name='expertise-list'),
    path('api/settings/', SiteSettingsDetail.as_view(), name='site-settings'),
]
