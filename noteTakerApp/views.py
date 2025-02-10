from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage
from .models import History, User
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
import os
import os
import shutil
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .record import record_audio  # Assuming record_audio() is in record.py
import threading
import torch
# print(torch.__version__)  # For PyTorch

import tensorflow as tf
# print(tf.__version__)  # For TensorFlow
# from flask import request
import shutil
def delete_temp_files(temp_dir):
    """Deletes all files in the specified temporary directory."""
    if os.path.exists(temp_dir):
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                print(f"Deleting {file_path}...")   
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
import sounddevice as sd
from datetime import datetime
import wave
import numpy as np
import speech_recognition as sr
import os
import threading
import time
from transformers import pipeline
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List available audio devices
# print("Available audio devices:")
# print(sd.query_devices())

# Choose the input device (Stereo Mix)
input_device_index = 19  # Index for Stereo Mix
AUDIO_DIR = "audio"
TRANSCRIBE_DIR = "transcribe"
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSCRIBE_DIR, exist_ok=True)
def record_audio(user_id,stop_event):
    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    # output_file = f"meeting_audio_{timestamp}.wav"  
    output_file = os.path.join(AUDIO_DIR, f"meeting_audio_{timestamp}.wav")  # Save to audio folder
    DURATION = 40  # Record for 40 seconds (adjust as needed)
    SAMPLE_RATE = 48000  # Standard for video and professional audio
    CHANNELS = 2  # Stereo recording
    print(f"Recording started... ({output_file})")
   
    # Record audio with the specified input device
    audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=np.int16, device=input_device_index)
    
    while not stop_event.is_set():
        sd.sleep(100)  # Sleep for 100ms and check again
    
    sd.stop()  # Stop the recording
    
    # Save audio to file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())
 
    print(f"Recording saved as {output_file}")
    
    # Transcribe the audio
    transcribe_audio(user_id,output_file)

def transcribe_audio(user_id,audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Read the entire audio file
    
    # Perform transcription
    try:
        # Use Google Web Speech API for transcription
        transcription = recognizer.recognize_google(audio)
        # transcription = "Good morning everyone, I hope you are all doing well. Today we will discuss the upcoming project and assign tasks to each team member. Let's get started."
        print("Transcription:")
        print(transcription)
        
        # Save transcription to a text file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # transcription_file = f"transcription_{timestamp}.txt"
        transcription_file = os.path.join(TRANSCRIBE_DIR, f"transcription_{timestamp}.txt")  # Save to transcribe folder

        with open(transcription_file, 'w') as f:
            f.write(transcription)
        
        print(f"Transcription saved as {transcription_file}")
        user=User.objects.get(user_id=user_id)
        History_instance=History(user=user,platform='google_meet',note=transcription,transcribe_audio=audio_file,transcribe_file=transcription_file,date=datetime.now())
        History_instance.save()
        summarizer = pipeline("summarization")
        summary = summarizer(transcription, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        print("Summary:")
        transcribe_file=transcription_file
        subject = f"Transcription of Your Today's meeting"
        message = (
        f"Hello {user.name},\n\n"
         f"Thank you for using our service!\n\n"
        f"We are pleased to inform you that the audio you submitted has been successfully transcribed.\n\n"
        f"Here is the transcription of the meeting:\n\n"
        f"{summary}\n\n"
    f"If you have any questions or need further assistance, feel free to reach out.\n\n"
    f"Best regards,\n"
    f"AI NOTE TAKER"
)
        from_email = settings.EMAIL_HOST_USER  # Use email from settings
        recipient_list = [user.email]  # Send to buyer's email
        email_message = EmailMessage(subject, message, from_email, recipient_list)
                
        photo_path=f"D:/Internship/Django/NOTETAKER/AI_NOTE_TAKER/static/note.jpg"
        if photo_path:
                    email_message.attach_file(photo_path)

                # Send the email
        email_r=email_message.send(fail_silently=False)



    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")


class NoteTaker(viewsets.ViewSet):

    def signup(request):
        if 'user_id' in request.session:    
            user=User.objects.get(user_id=request.session['user_id'])
            context={
                "name":user.name,
                "email":user.email,
            }
            return render(request, 'Home.html',context=context
            )
        if request.method=='POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if name and email and password:
                if(User.objects.filter(email=email).exists()):
                    return render(request, template_name='signIn.html')
                else:
                    request.session['name'] = name
                    request.session['email'] = email
                    request.session['password'] = password
                    import random

                    otp= random.randint(10000, 99999)
                    otp="A"+str(otp)
                    # request.session['otp'] = otp

                    subject = f"AI_NOTE_TAKER EMAIL VERIFICATION"
                    message = (
                    f"Hello {name},\n\n"
                    f"This is your email verification otp:{otp} , make sure you put this otp correctly on our site.\n"
                    
                    f"Thank you for using our service!"
                    )
                    from_email = settings.EMAIL_HOST_USER  # Use email from settings
                    recipient_list = [email]  # Send to buyer's email
                    email_message = EmailMessage(subject, message, from_email, recipient_list)
                
                    photo_path=f"D:/Internship/Django/NOTETAKER/AI_NOTE_TAKER/static/note.jpg"
                    if photo_path:
                        email_message.attach_file(photo_path)

                # Send the email
                    email_r=email_message.send(fail_silently=False)
                    if(email_r):
                        context={
                            "otp":otp,
                            "name":name,
                            "email":email,  
                        }
                        return render( request, template_name='votp.html',context=context)
                    else:
                        return HttpResponse("Email not sent")

                    # Return the image as an HTTP response
                    
                    

            
        return render( request, template_name='signUp.html')  
    def home(request):
        
        if request.method=='POST':
            otp = request.POST['otp']
            if(otp.startswith('A')):

                name = request.session.get('name')
                email = request.session.get('email')
                password = request.session.get('password')

                user = User(name=name, email=email)
                user.set_password(password)
                user.save()
                    # Assuming you have a User model to save the user data
                # user = User.objects.create(name=name, email=email, password=password)
                request.session['name'] = None
                request.session['user_id'] = User.objects.get(email=email).user_id
                # request.session['email'] = None
                request.session['password'] = None
            
        # return render( request, template_name='home.html')
            elif(otp.startswith('P')):
                email=request.session['email']
                print(email)
                # context={
                #     "email":email,
                # }
                
                
                return render( request, template_name='ChangePass.html')
            else:
                return HttpResponse("Something is wrong") 
        user=User.objects.get(user_id=request.session['user_id'])
        if 'user_id' in request.session:          
            context={
                            "user_id":request.session['user_id'], 
                            "name":user.name,  
                            "email":user.email,   
                        }   
            return render(request, 'Home.html',context=context)
        else:
            return render(request, 'signIn.html')
    
    def signin(request):
        if 'user_id' in request.session:    
            user=User.objects.get(user_id=request.session['user_id'])
            context={
                "name":user.name,
                "email":user.email,
            }
            return render(request, 'Home.html',context=context
            )
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            print(email)
            print(password)
            try:
                
                user = User.objects.get(email=email)  # Use your custom User model
                print("inside try")
                # user=User.objects.get(email=request.session['email'])
                
                if user.check_password(password):  # Check the password using your method
                    request.session['user_id'] = User.objects.get(email=email).user_id

                    context={
                        "name":user.name,
                        "email":email,
                    }   
                    return render(request, 'Home.html',context=context)
                else:
                    return HttpResponse("Invalid password")
            except User.DoesNotExist:
                return HttpResponse("User  does not exist")
        return render(request, template_name='signIn.html')
    def forget_password(request):
        if request.method == 'POST':
            email = request.POST['email']
            try:
                
                user = User.objects.get(email=email) 
                request.session['email'] = email

                if user:
                    # email=request.session['email']
                    import random
                    otp= random.randint(10000, 99999)
                    otp="P"+str(otp)
                    # request.session['otp'] = otp
                    subject = f"AI_NOTE_TAKER EMAIL VERIFICATION"
                    message = (
                    f"Hello {user.name},\n\n"
                    f"This is your otp:{otp} for changing the password , make sure you put this otp correctly on our site.\n"
                    
                    f"Thank you for using our service!"
                    )
                    from_email = settings.EMAIL_HOST_USER  # Use email from settings
                    recipient_list = [email]  # Send to buyer's email
                    email_message = EmailMessage(subject, message, from_email, recipient_list)
                
                    photo_path=f"D:/Internship/Django/NOTETAKER/AI_NOTE_TAKER/static/note.jpg"
                    if photo_path:
                        email_message.attach_file(photo_path)

                # Send the email
                    email_r=email_message.send(fail_silently=False)
                    if(email_r):
                        context={
                            "otp":otp,
                            "email":email,
                            
                        }
                        return render( request, template_name='votp.html',context=context)
                    else:
                        return HttpResponse("Email not sent")
            except User.DoesNotExist:
                return render( request, template_name='signUp.html',context=context)       

        return render(request, 'forget_password.html')
    
    def change_password(request):
        if request.method=='POST':
            
                email = request.session.get('email')
                password = request.POST['new_password']
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                if(user.check_password(password)):
                    user=User.objects.get(email=request.session['email'])
                    request.session['user_id'] = User.objects.get(email=email).user_id

                    context={
                        "email":email,
                        "name":user.name,
                    }   
                    return render(request, 'Home.html',context=context)
                else:
                    return render(request, 'ChangePass.html')
        return render(request, 'ChangePass.html')
    



    def noteTaker(request):
        
        if 'user_id' in request.session:
            user_id=request.session['user_id']
            if request.method == 'POST':    
                platform = request.POST['platform']
                meetingCode = request.POST['meetingCode'].strip()
                email = request.session.get('email')

                if platform == 'google_meet':
                    options = webdriver.ChromeOptions()
                    options.add_argument(r'--user-data-dir=C:\Users\ANKITA\AppData\Local\Google\Chrome\User Data')
                    options.add_argument('--profile-directory=Profile 1')

                    service = Service(ChromeDriverManager().install())  
                    driver = webdriver.Chrome(service=service, options=options)

                    driver.get("https://meet.google.com/" + meetingCode)

                    record_thread = None  # Initialize record_thread
                    stop_event = threading.Event()  # Create a stop event

                    try:
                        ask_to_join_button = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Ask to join")]'))
                        )
                        ask_to_join_button.click()

                        print("Clicked 'Join now' button successfully!")
                    
                        # Start recording in a separate thread
                        record_thread = threading.Thread(target=record_audio, args=(user_id,stop_event,))
                        record_thread.start()

                        # Monitor for "You left the meeting"
                        while True:
                            if "You left the meeting" in driver.page_source:
                                print("You left the meeting, stopping recording...")
                                stop_event.set()  # Signal the recording thread to stop
                                break
                            time.sleep(5)  # Check every 5 seconds
                    except Exception as e:
                        print("Error occurred:", e)

                    finally:
                        driver.quit()  # Close Selenium
                        if record_thread is not None:  # Check if record_thread was created
                            record_thread.join()  # Ensure recording stops before moving on

                return render(request, 'NoteTaker.html')

            return render(request, 'NoteTaker.html')
        else:
            return render(request, 'signIn.html')
    

    def profile(request):
        if 'user_id' in request.session:
            if request.method == 'POST':
                name = request.POST['name']
                email = request.POST['email']
                print(name)
                print(email)
                user = User.objects.get(user_id=request.session['user_id'])
                print(user.name)
                user.name = name
                user.email = email
                
                user.save()
                context={
                    "user_id":user.user_id,
                    "name":user.name,
                    "email":user.email,
                }
                return render(request, 'profile.html',context=context)
            user=User.objects.get(user_id=request.session['user_id'])
            context={
                "user_id":user.user_id,
                "name":user.name,
                "email":user.email,
            }
            return render(request, 'profile.html',context=context)
        
        return render(request, 'signIn.html')
    
    def logout(request):
        request.session.flush()

        return render(request, 'signIn.html')


    def history(request):
        if 'user_id' in request.session:
            history=History.objects.filter(user=request.session['user_id'])
            context={
                "history":history,
            }
            return render(request, 'history.html',context=context)
        
        return render(request, 'signIn.html')
    