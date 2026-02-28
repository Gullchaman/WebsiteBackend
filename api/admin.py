from django.contrib import admin
from .models import Contact, ExpertiseCategory, ExpertiseSkill, Project, SiteSettings


class ExpertiseSkillInline(admin.TabularInline):
    model = ExpertiseSkill
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'tech_stack', 'created_at')
    search_fields = ('title', 'description', 'tech_stack')
    list_filter = ('created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(ExpertiseCategory)
class ExpertiseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)
    inlines = [ExpertiseSkillInline]


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'location', 'updated_at')
