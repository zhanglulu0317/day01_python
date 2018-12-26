from unittest import TestCase
import os,django
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day01.settings")
django.setup()
from  django.test  import   Client
from django.contrib.auth.models import User



class IndexPageTest(TestCase):
    '''测试index登录首页'''
    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        c=Client()
        response=c.get('/index/')
        self.assertEqual(response.status_code,200)
        #self.assertTemplateUsed(response,'index.html')
        print(response)

class  LoginActionTest(TestCase):
    '''测试登录函数'''
    def setUp(self):
    #     User.objects.create_user('ddd','','aaaa')
          self.c=Client()
    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data={'username':'','password':''}
        response=self.c.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error",response.content)
    def test_login_action_username_password_error(self):
         test_data={'username':'abc','password':'123'}
         response=self.c.post('/login_action/',data=test_data)
         self.assertEqual(response.status_code, 200)
         self.assertIn(b"username or password error", response.content)

    def test_login_action_success(self):
         test_data={'username':'admin','password':'admin123'}
         response=self.c.post('/login_action/',data=test_data)
         self.assertEqual(response.status_code,302)

