from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum
from django.urls import reverse
from django.core.validators import MinValueValidator

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingA = models.SmallIntegerField(default=0)

    #def __init__(self, *args, **kwargs):
        #super().__init__(args, kwargs)
        #self.post_set = None

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.user.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingA = pRat * 3 + cRat + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')
    def __str__(self):
        return self.name

class Post(models.Model):

    POSITIONS = [
        ('new', 'Новость'),
        ('article','Статья' )
    ]
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=POSITIONS, default='new')
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)


    def preview(self):
        return '{} ... {}'.format(self.text[0:123], str(self.rating))

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return '{}'.format(self.title)

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    def __str__(self):
        return f'{self.user.username} :{self.category.name}'
