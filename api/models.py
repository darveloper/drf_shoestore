from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class ShoeType(models.Model):

    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'RED'
    ORANGE = 'ORANGE'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'
    BLUE = 'BLUE'
    INDIGO = 'INDIGO'
    VIOLET = 'VIOLET'
    WHITE = 'WHITE'
    BLACK = 'BLACK'
    COLOR_CHOICES = (
        (RED, 'red'),
        (ORANGE, 'orange'),
        (YELLOW, 'yellow'),
        (GREEN, 'green'),
        (BLUE, 'blue'),
        (INDIGO, 'indigo'),
        (VIOLET, 'violet'),
        (WHITE, 'white'),
        (BLACK, 'black'),
    )
    color_name = models.CharField(max_length=10, choices=COLOR_CHOICES)
    
    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name