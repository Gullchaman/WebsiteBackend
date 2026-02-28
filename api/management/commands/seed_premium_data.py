from django.core.management.base import BaseCommand
from api.models import Project, ExpertiseCategory, ExpertiseSkill

class Command(BaseCommand):
    help = 'Seeds the database with premium Black & Gold theme data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Project.objects.all().delete()
        ExpertiseCategory.objects.all().delete()
        
        # 1. Seed Projects
        projects = [
            {
                "title": "Visionary AI Matrix",
                "description": "A high-performance neural network interface designed for real-time predictive analytics in luxury retail.",
                "tech_stack": "React, Django, TensorFlow, PostgreSQL",
                "github_link": "https://github.com"
            },
            {
                "title": "Quantum Ledger",
                "description": "Secure, immutable financial records management system built with military-grade encryption and elegant interfaces.",
                "tech_stack": "Python, Django, React, Redis",
                "github_link": "https://github.com"
            },
            {
                "title": "Astra CMS",
                "description": "A high-end content management system tailored for premium digital agencies and creative studios.",
                "tech_stack": "React, Django, AWS, S3",
                "github_link": "https://github.com"
            }
        ]
        
        for p in projects:
            Project.objects.create(**p)
        
        # 2. Seed Expertise
        expertise_data = [
            {
                "name": "Frontend",
                "icon": "Monitor",
                "skills": ["HTML5", "CSS3 / Tailwind", "JavaScript (ES6+)", "React.js"]
            },
            {
                "name": "Backend",
                "icon": "Server",
                "skills": ["Python", "Django", "REST Framework", "Node.js"]
            },
            {
                "name": "Database",
                "icon": "Database",
                "skills": ["Django ORM", "PostgreSQL", "SQLite", "Database Design"]
            }
        ]
        
        for category_data in expertise_data:
            category = ExpertiseCategory.objects.create(
                name=category_data["name"],
                icon_name=category_data["icon"]
            )
            for skill_name in category_data["skills"]:
                ExpertiseSkill.objects.create(category=category, name=skill_name)
                
        self.stdout.write(self.style.SUCCESS('Successfully seeded premium Black & Gold data'))
