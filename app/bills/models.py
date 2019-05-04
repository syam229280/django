from django.db import models

class BillCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class BillTag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name

class Bill(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.FloatField()
    bill_file = models.FileField(upload_to='uploads/%Y/%m/',blank=True,max_length=500)
    category = models.ForeignKey(
        BillCategory,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(BillTag,related_name='photos')
    remainder_date = models.DateField(null=True, blank=True)
