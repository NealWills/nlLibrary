from django.db import models
from django.utils import timezone
import uuid


class Books(models.Model):
    book_name = models.CharField(verbose_name='Book Name', max_length=128, unique=False, null=True, blank=True)
    book_user = models.CharField(verbose_name='User Name', max_length=64, unique=False, null=False, blank=False)
    book_type = models.CharField(verbose_name='Book Type', max_length=64, unique=False, null=True, blank=True)
    book_content = models.CharField(verbose_name="Book Content", max_length=100000, unique=False, null=True, blank=True)
    book_ssin = models.IntegerField(verbose_name='Book SSIN', unique=False, blank=False, null=False, default="-1")

    default_time_now = timezone.now


    book_id = models.CharField(verbose_name='Book Id', unique=True, max_length=50, null=False, blank=False)    
    create_date = models.DateTimeField(verbose_name='create_date', null=False, blank=False, default=default_time_now)
    update_date = models.DateTimeField(verbose_name='update_date', null=False, blank=False, default=default_time_now)
    delete_date = models.DateTimeField(verbose_name='delete_date', null=False, blank=False, default=default_time_now)
    is_delete = models.IntegerField(verbose_name='is_delete', null=False, blank=False, default=0)

    def transToDic(self):
        return {
            'book_id': self.book_id,
            'book_name': self.book_name,
            'book_user': self.book_user,
            'book_type': self.book_type,
            'book_content': self.book_content,
            'book_ssin': self.book_ssin,
            'create_date': str(self.create_date),
            'update_date': str(self.update_date),
            'delete_date' : str(self.delete_date),
            'is_delete': self.is_delete
        }
