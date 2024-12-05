from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    user_image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='age')
    phone_number = models.IntegerField()
    data_register = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    check_origin = models.BooleanField(default=True)
    product_video = models.FileField(upload_to='product_video', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.product_name}, {self.price}'

    def get_avg_rating(self):
        rating = self.ratings.all()
        if rating.exists():
            return round(sum(i.stars for i in rating) / rating.count(), 1)
        return 0


    def get_count_people(self):
        rating = self.ratings.all()
        if rating.exists():
            return rating.count()
        return 0

class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product}'


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    stars = models .IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'{self.user}, {self.stars}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.product}'