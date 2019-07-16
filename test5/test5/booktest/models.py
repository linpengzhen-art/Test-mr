from django.db import models


# Create your models here.

class AreaInfo(models.Model):
    """地区模型类"""
    atitle = models.CharField(verbose_name='标题', max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle

    class Meta:
        db_table = "areas"
