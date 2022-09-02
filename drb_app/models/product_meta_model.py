from django.db import models
import datetime

class ProductMetaModel(models.Model):
    brand = models.ForeignKey('BrandModel', on_delete=models.SET_NULL, null=True, related_name='of_brand')
    category = models.ForeignKey('CategoryModel', on_delete=models.SET_NULL, null=True, related_name='of_category')
    discount = models.ManyToManyField('DiscountModel', related_name='has_discounts', blank=True)
    size = models.CharField(max_length=10, null=False, default='')
    nic = models.CharField(max_length=10, null=False, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.0)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.0)
    priority = models.IntegerField(default=0, null=False)
    nic_unit = models.ForeignKey('UnitsModel', on_delete=models.SET_NULL, null=True, related_name='has_nic_unit')
    size_unit = models.ForeignKey('UnitsModel', on_delete=models.SET_NULL, null=True, related_name='has_size_unit')

    on_sale = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    strong = models.BooleanField(default=False)

    date_created = models.DateField(default=datetime.date.today())

    image = models.ImageField(upload_to='images', null=True, blank=True)


    def __str__(self):
        return self.brand.__str__() + ' ' + self.category.__str__() + ' ' + self.nic.__str__() + self.nic_unit.__str__() + ' ' + self.size.__str__() + self.size_unit.__str__()
