from django.db import models
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    COURSE = (
        ('1 курс бакалавру', '1 курс бакалавру'),
        ('2 курс бакалавру', '2 курс бакалавру'),
        ('3 курс бакалавру', '3 курс бакалавру'),
        ('4 курс бакалавру', '4 курс бакалавру'),
        ('Інше', 'Інше'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, default="1")
    course = models.CharField(max_length=200, null=True, choices=COURSE)
    pdf = models.FileField(upload_to='files/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name