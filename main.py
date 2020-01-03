from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager,Screen
#import pyrebase
#from getpass import getpass
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class LoadingPopup(Popup):
	def __init__(self, **kwargs):
		super(LoadingPopup, self).__init__(**kwargs)
		Clock.schedule_once(self.dismiss_popup, 2)

	def dismiss_popup(self, dt):
		self.dismiss()

class StartWindow(Screen):
	pass

class SignUpWindow(Screen):
	pass
	"""
	firebaseConfig = {
	"apiKey":"xxxxxxxxx",
    "authDomain": "testapp-4d890.firebaseapp.com",
    "databaseURL": "https://testapp-4d890.firebaseio.com",
    "projectId": "testapp-4d890",
    "storageBucket": "testapp-4d890.appspot.com",
    "messagingSenderId": "36918692990",
    "appId": "1:36918692990:web:062e49602291d980425c2f",
    "measurementId": "G-6QV2PTYTFR"
	}

	firebase = pyrebase.initialize_app(firebaseConfig)

	auth = firebase.auth()


	def auth_user(self,email,password):
		user = self.auth.create_user_with_email_and_password(email,password)
		print("Success")"""

class LoginWindow(Screen):
    pass

class WindowManager(ScreenManager):
	pass

GUI = Builder.load_file("main.kv")

class BushFinder(App):  
    def build(self):
        return GUI

BushFinder().run()  
