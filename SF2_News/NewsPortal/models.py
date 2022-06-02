from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):

        # Агрегация - процесс объединения элементов в одну систему.
        # !!!!!!!!!!!!!!читай доку, там все понятно!!!!!!!!!!!!!!!!!!
        posts_ratings = self.post_set.aggregate(rating=Sum('rating'))
        pRat = 0

        try:
            pRat += int(posts_ratings.get('rating'))
        except TypeError:
            pass

        comments_ratings = self.name.comment_set.aggregate(rating=Sum('rating'))
        cRat = 0

        try:
            cRat += int(comments_ratings.get('rating'))
        except TypeError:
            pass

        posts = Post.objects.filter(author=self.name_id)
        posts_comments_rating = 0
        try:
            for post in posts:
                comments = Comment.objects.filter(post=post)

                for comment in comments:
                    posts_comments_rating += int(comment.rating)
        except TypeError:
            pass

        self.rating = pRat * 3 + cRat + posts_comments_rating
        self.save()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    NEWS = 'N'
    ARTICLE = 'A'
    TYPES = [
        (ARTICLE, 'article'),
        (NEWS, 'news'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPES)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.text) > 124:
            return self.text[:124] + '...'

        return self.text

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_portal:post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()




