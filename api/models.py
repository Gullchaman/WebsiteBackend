from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=100, default='Full Stack') # e.g. Full Stack, Team Lead
    description = models.TextField()
    key_features = models.TextField(blank=True, null=True) # Bullet points separated by newlines
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ExpertiseCategory(models.Model):
    name = models.CharField(max_length=100) # e.g., Frontend, Backend, Database
    icon_name = models.CharField(max_length=50, blank=True) # e.g., Monitor, Server, Database
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Expertise Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class ExpertiseSkill(models.Model):
    category = models.ForeignKey(ExpertiseCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # e.g., React.js, Python, Django

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class SiteSettings(models.Model):
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(default='gullchaman.bd@gmail.com')
    location = models.CharField(max_length=200, default='Global / Remote')
    phone = models.CharField(max_length=50, default='+92 333 7485759')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"
