from django.db import models


# Create A Blog models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')



# Add the Blog app to the setting

# Create a migration

# Migrate

# Add to the main