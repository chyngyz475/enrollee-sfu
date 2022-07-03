from django.db import models


class FeedBack(models.Model):
  'Форма обратной связи'
  name = models.CharField(
    'Ф И О',
    max_length=150
    )
  phone = models.CharField(
    'ТЕЛЕФОН',
    max_length=15,
  )
  description = models.TextField(
    'Коментария',
    blank=True
  )
  
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Форма обратной связи'
    verbose_name_plural = 'Форма обратной связи'
  
  