from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #must be
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    University = models.CharField(max_length=50)



    #suggest
    picture = models.ImageField(upload_to='profile_images', blank=True)
    motto   = models.CharField(max_length=300)

    #optional
    website = models.URLField(blank=True)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username