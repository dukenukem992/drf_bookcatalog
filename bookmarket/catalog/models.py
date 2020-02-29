from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50, blank = False)
    age = models.IntegerField(blank = True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def full_name(self):
        return 'full name is: {}  {}'.format(self.first_name, self.last_name)

class Book(models.Model):
    BOOK_GENRE = [
        ('1','horror'),
        ('2','comedy'),
        ('3','roman'),
        ('4','science'),
    ]
    title = models.CharField(max_length = 100, blank = False)
    genre = models.CharField(max_length = 10, choices=BOOK_GENRE)
    pub_date = models.DateField(blank = True, null=True)
    author = models.ForeignKey('Author', on_delete = models.DO_NOTHING, related_name='books', blank = False)

    def __str__(self):
        return self.title


