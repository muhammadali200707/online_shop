from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=90)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices, default=RatingChoices.zero.value,
                                              null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return f" {self.product} commented from {self.name}"


class Order(models.Model):
    name = models.CharField(max_length=80)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='order')
    phone_number = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} ordered , this person's phone number {self.phone_number}"

