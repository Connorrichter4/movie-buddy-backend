from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(default='https://lh6.googleusercontent.com/proxy/hIgFSMyx4VsuoQh8h-ZfI3IiK9uFSLZ7pG67H_1RwEBDEPiWX-odcJ0PkWriAPeqwKyC6n-12UTrNmQF2ul9DAjwKMljG3zSCCTDoTVDPexFHV9l_JD5WMbmpnUJqWLqYA=s0-d', editable=False)
    trailer_url = models.URLField(blank=True, default='')
    description = models.TextField()
    year_released = models.CharField(max_length=100)

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
