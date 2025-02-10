from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage
from .models import User
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import the Service class
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument(r'--user-data-dir=C:\Users\ANKITA\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Profile 1')
#  Set up the ChromeDriver service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
if True:
                options = webdriver.ChromeOptions()
                options.add_argument(r'--user-data-dir=C:\Users\ANKITA\AppData\Local\Google\Chrome\User Data')
                options.add_argument('--profile-directory=Default')
                options.add_argument("--no-sandbox")  # Bypass OS security model
                options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
                options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
                options.add_argument("--window-size=1920x1080")
                options.add_argument("--headless")
                options.add_argument("--disable-extensions")
                options.add_argument("--enable-logging")
                options.add_argument("--v=1")
                service = Service(ChromeDriverManager().install())  # Get the ChromeDriver path and pass it to Servicetry:
                try:
                    driver = webdriver.Chrome(service=service, options=options)
                    driver.get("https://meet.google.com/")
                except Exception as e:
                    print("Error initializing WebDriver:", e)
                    driver.quit()
  
                
    
            