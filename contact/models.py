from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

RESOLVED_CHOICES = ((0, "Open Query"), (1, "Resolved"))

# Contact us model


class ContactUs(models.Model):
    query_title = models.CharField(max_length=200)
    query_image = CloudinaryField('image', blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    resolved = models.IntegerField(choices=RESOLVED_CHOICES, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="contact_queries")
    admin_response = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Contact Us Query"
        verbose_name_plural = "Contact Us Queries"

    def __str__(self):
        return f"New query request {self.query_title} | created by {self.author}"

    def can_edit_or_delete(self, user):
        """
        Check if the user has permission to edit or delete this contact query.
        """
        return user == self.author
