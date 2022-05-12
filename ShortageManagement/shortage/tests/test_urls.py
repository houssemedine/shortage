from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shortage.views import core,update_core


class TestUrls(SimpleTestCase):

    def test_core_index_url(self):
        url = reverse('update_core')
        self.assertEquals(resolve(url).func, core)

