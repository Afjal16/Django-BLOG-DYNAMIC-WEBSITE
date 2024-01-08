

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    


class Post(models.Model):
    STATUS=(
        ('0','Draft'),
        ('1','Publish'),
    )

    SECTION=(
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editors_Pick','Editors_Pick'),
        ('Trending','Trending'),
        ('Inspiration','Inspiration'),
        ('Latest_Posts','Latest_Posts'),
    )
    feature_image=models.ImageField(upload_to="Images")
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    author_image=models.ImageField(upload_to="Author")
    date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content=RichTextField()
    slug=models.SlugField(max_length=500,null=True,blank=True,unique=True)
    status=models.CharField(choices=STATUS,max_length=100)
    section=models.CharField(choices=SECTION,max_length=200,)
    main_post=models.BooleanField(default=False)
    
     
    def __str__(self):
        return self.title
    
def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
class Tag(models.Model):
    name=models.CharField(max_length=100)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Author_name(models.Model):
    name=models.CharField(max_length=200)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField()
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username + ": " + self.text[0:15]
    
    

class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.username