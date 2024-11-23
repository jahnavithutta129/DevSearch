from django.db import models
import uuid #though the id field is automatically present ,we can create it manually by importing this
#ovveriding the actual id
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    tags=models.ManyToManyField('Tag',blank=True)  #quotes are put to tag beacuse it is below
    vote_total=models.IntegerField(default=0, null=True,blank=True)
    vote_ratio=models.IntegerField(default=0, null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-vote_ratio','-vote_total','title']

    @property 
    def reviewers(self):   #get the voters
        queryset=self.review_set.all().values_list('owner__id',flat=True) #the owner is an object is converted to actual list using flat=true
        return queryset

#the review gets appeared but the vote remains anonymous
    @property #now we can write it as a property not as a method
    def getVoteCount(self):
        reviews=self.review_set.all()
        upVotes=reviews.filter(value='up').count()
        totalVotes=reviews.count()
        ratio=(upVotes/totalVotes) * 100
        self.vote_total=totalVotes
        self.vote_ratio=ratio
        self.save()
class Review(models.Model):
    VOTE_TYPE=(
        ('up','Up Vote',),
        ('down','Down Vote'),
    )
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True) #if the user deletes that account the whole review gets deleted
    #the user can give only one review per project so we are going to bind that project and owner accordingly done at class meta
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together=[['owner','project']]

    def __str__(self):
        return self.value

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
