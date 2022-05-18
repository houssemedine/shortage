from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shortage.views import core,update_core,kpi


class TestUrls(SimpleTestCase):
    
    def test_shortage_kpi_index_url(self):
        url = reverse('shortage_kpi')
        self.assertEquals(resolve(url).func, kpi)

    def test_core_index_url(self):
        url = reverse('core')
        self.assertEquals(resolve(url).func, core)


