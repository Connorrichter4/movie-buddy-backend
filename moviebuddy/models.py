from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()
    year_released = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=100)
    review_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.title
