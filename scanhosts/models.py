from django.db import models


# Create your models here.

class UserIPInfo(models.Model):
    ip = models.CharField(verbose_name="ip地址", max_length=40, default="", null=True)
    time = models.DateField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "用户访问地址信息"
        verbose_name_plural = verbose_name
        db_table = "a_useripinfo"


class BrowseInfo(models.Model):
    useragent = models.CharField(max_length=100, default="", verbose_name="用户浏览器agent信息", null=True)
    only_id = models.CharField(max_length=256, verbose_name="唯一设备ID", default="")
    userip = models.ForeignKey("UserIPInfo", on_delete=models.CASCADE)

    class Meta:
        db_table = "a_browseinfo"
        verbose_name = "用户浏览器信息表"
        verbose_name_plural = verbose_name
