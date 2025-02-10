# 

import sounddevice as sd
from datetime import datetime
import wave
import numpy as np
import speech_recognition as sr
import os

# List available audio devices
print("Available audio devices:")
print(sd.query_devices())

# Choose the input device (Stereo Mix)
input_device_index = 19  # Index for Stereo Mix

def record_audio():
    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    output_file = f"meeting_audio_{timestamp}.wav"  
    DURATION = 40  # Record for 40 seconds (adjust as needed)
    SAMPLE_RATE = 48000  # Standard for video and professional audio
    CHANNELS = 2  # Stereo recording
    print(f"Recording started... ({output_file})")
   
    # Record audio with the specified input device
    audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=np.int16, device=input_device_index)
    sd.wait()  # Wait until recording is finished
   
    # Save audio to file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())
 
    print(f"Recording saved as {output_file}")
    
    # Transcribe the audio
    transcribe_audio(output_file)

def transcribe_audio(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Read the entire audio file
    
    # Perform transcription
    try:
        # Use Google Web Speech API for transcription
        transcription = recognizer.recognize_google(audio)
        print("Transcription:")
        print(transcription)
        
        # Save transcription to a text file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        transcription_file = f"transcription_{timestamp}.txt"
        with open(transcription_file, 'w') as f:
            f.write(transcription)
        
        print(f"Transcription saved as {transcription_file}")
    
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

