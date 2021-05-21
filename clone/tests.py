from django.test import TestCase
from .models import Image

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
