from django.test import TestCase
from .models import Image,Profile,Comment

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(id=1,name="Slide Away",caption="nice place to  call home",comments= "pretty" ,likes= 2)
        self.image.save_image()
    
    def test_save_image(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)


    def test_delete_image(self):
        self.image.delete_image()
        image=Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_update_image(self):
        self.image.update_image()
        image=Image.objects.all()
        self.assertTrue(len(image)>1)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(name= "Alicia",gender= "female",phonenumber= "07158585858585")
        self.profile.save_profile()
    
    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


    def test_delete_profile(self):
        self.profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)==0)

    def test_update_profile(self):
        self.profile.update_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)==1)

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment = Comment(id=1,comment="nice",)
        self.comment.save_comment()
    
    def test_save_comment(self):
        self.comment.save_comment()
        comment= Comment.objects.all()
        self.assertTrue(len(comment) > 1)


    def test_delete_comment(self):
        self.comment.save_comment()
        comment= Comment.objects.all()
        self.assertTrue(len(comment) > 0)
    

