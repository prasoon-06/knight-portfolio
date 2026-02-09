from django.db import models


class SiteProfile(models.Model):
    display_name = models.CharField(max_length=120, blank=True)
    tagline = models.CharField(max_length=200, blank=True)

    tenth = models.CharField(max_length=200, blank=True)
    twelfth = models.CharField(max_length=200, blank=True)
    college = models.CharField(max_length=200, blank=True)

    tech_stack = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
    currently_working_on = models.TextField(blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
    upload_to="profile/",
    blank=True,
    null=True
)
    about_me = models.TextField(blank=True)

    def __str__(self):
        return self.display_name


class Project(models.Model):
    """
    Projects you can add/remove from admin.
    """
    title = models.CharField(max_length=160)
    one_liner = models.CharField(max_length=260, blank=True)
    tech_stack = models.CharField(max_length=220, blank=True)

    # keep empty until you decide
    repo_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class HobbyImage(models.Model):
    title = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to="hobbies/")
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title or "Hobby Image"

class ChapterImage(models.Model):
    CHAPTER_CHOICES = [
        ("philosophy", "Chapter II — Philosophy"),
        ("teen", "Chapter III — Teen"),
        ("adult", "Chapter IV — Adult"),
        ("battles", "Chapter V — Battles"),
        ("old", "Chapter VI — Old (3 images)"),
    ]

    chapter = models.CharField(max_length=20, choices=CHAPTER_CHOICES)
    image = models.ImageField(upload_to="chapters/")
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.chapter} #{self.sort_order}"
