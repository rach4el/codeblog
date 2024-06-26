from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SUGGESTED_RIDING_ABILITY = ((0, 'All Abilities'),
                            (1, "Beginner"),
                            (2, "Novice"),
                            (3, "Intermediate"),
                            (4, "Advanced"))

APPROVED = ((0, "Open Suggestion"), (1, "Published"))

# Model for the suggest page createpost
# (doesn't get posted to main posts_list page)


class CreatePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    suggested_riding_ability = models.IntegerField(choices=SUGGESTED_RIDING_ABILITY, default=0)
    creator = models.ForeignKey(User,
                                on_delete=models.
                                CASCADE, related_name="blog_poster")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    county = models.CharField(max_length=100, null=True)
    excerpt = models.TextField(blank=False)
    approved = models.IntegerField(choices=APPROVED, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Suggestion Posts"

    def __str__(self):
        return f"New post request{self.title} | created by {self.creator}"

    def get_suggested_riding_ability_display(self):
        return dict(SUGGESTED_RIDING_ABILITY).get(self.suggested_riding_ability, "Unknown")