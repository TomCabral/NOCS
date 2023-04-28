from django.test import LiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.by import By Pra usar em href


class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert "NOCS" in self.browser.title # Vai rodar o teste

# Rodar teste: diretório onde está o manage.py e dá um python manage.py test
