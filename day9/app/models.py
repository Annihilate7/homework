from django.db import models

from day9 import settings


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    show_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to='img', default='img/1.jpg')
    authors = models.ManyToManyField(to='Author', db_constraint=False, related_name='books')
    Presses = models.ForeignKey(to='Press', on_delete=models.CASCADE, db_constraint=False, related_name='books')

    class Meta:
        db_table = 't_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

    @property
    def pho(self):
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(self.pic))

    @property
    def presses(self):
        return self.Presses.press_name

    @property
    def author(self):
        return self.authors.values('author_name', 'age')

class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = 't_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    class Meta:
        db_table = 't_press'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name