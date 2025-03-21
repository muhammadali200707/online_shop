from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'category'


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
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices, default=RatingChoices.zero.value,
                                              null=True, blank=True)
    discount = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class Order(models.Model):
    name = models.CharField(max_length=80)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='order')
    phone = models.BigIntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ordered , this person's phone number {self.phone}"

    class Meta:
        db_table = 'order'


class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    is_provide = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.product} commented by {self.name}"

    class Meta:
        db_table = 'comment'
