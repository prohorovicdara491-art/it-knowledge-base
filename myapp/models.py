from django.db import models

CATEGORY_CHOICES = [
    ('work', 'Работа'),
    ('personal', 'Личное'),
    ('study', 'Учёба'),
    ('other', 'Другое'),
]

TECH_CATEGORY_CHOICES = [
    ('linux', '🐧 Linux'),
    ('python', '🐍 Python'),
    ('django', '🌐 Django'),
    ('docker', '🐳 Docker'),
    ('database', '🗄️ Базы данных'),
    ('network', '🌍 Сети / SSH'),
    ('git', '📦 Git'),
]

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    tech_category = models.CharField(max_length=20, choices=TECH_CATEGORY_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
