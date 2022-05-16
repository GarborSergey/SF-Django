from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):

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


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)


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
    category = models.ManyToManyField(Category, through='PostCategory')
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


# Промежуточная модель для связи многие к многим
# Зачем такая заморочка непонятно, можно же было у поста:
# category = models.ManyToManyField(Category)
# мб потом это как-то всплывет
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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




