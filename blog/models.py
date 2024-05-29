from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Post model

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

SUGGESTED_RIDING_ABILITY = (
    (0, 'All Abilities'),
    (1, "Beginner"),
    (2, "Novice"),
    (3, "Intermediate"),
    (4, "Advanced")
)  # riding ability dropdown choices


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    suggested_riding_ability = models.IntegerField(
        choices=SUGGESTED_RIDING_ABILITY, default=0
    )  # Riding ability dropdown
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    county = models.CharField(max_length=100, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField(
        User, related_name='upvoted_posts', through='Upvote'
    )
    downvotes = models.ManyToManyField(
        User, related_name='downvoted_posts', through='Downvote'
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_suggested_riding_ability_display(self):
        return dict(SUGGESTED_RIDING_ABILITY).get(
            self.suggested_riding_ability, "Unknown")

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Downvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"