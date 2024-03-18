from django.db import models


class ProductMaterial(models.Model):
    product_name = models.CharField("Mahsulot nomi", max_length=50)
    fabric = models.FloatField("Mato")
    yarn = models.FloatField("Ip")
    button = models.IntegerField("Tugma", blank=True, null=True)
    zip = models.IntegerField("Zamok", blank=True, null=True)

    def __str__(self) -> str:
        return self.product_name


class Warehouse(models.Model):
    material_name = models.CharField("Xomashyo nomi", max_length=50)
    remainder = models.IntegerField("Qoldiq")
    price = models.IntegerField("Narx")

    def __str__(self) -> str:
        return self.material_name
