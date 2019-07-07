
#!/usr/bin/env python3                                                                                
import os
import speech_recognition as sr  
import pygame
def speak():
    
    # get audio from the microphone                                                                       
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Fale agora:")                                                                                   
        audio = r.listen(source)   

    try:
        print("Você disse " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Eu não entendi muito bem oque você disse")
        speak()
    except sr.RequestError as e:
        print("Could not request result; {0}".format(e))
    pygame.init()
    pygame.mixer.music.load('comandos/soung/yes.mp3')
    pygame.mixer.music.play()    
    a=(r.recognize_google(audio))
    b=os.system('python3 comandos/'+'{}'.format(a)) #função que abre os comandos e os executa
    
    if speak() == false:
        speak()
    elif a == 'exit':
        quit()
speak()
try:
    if speak() == false:
        speak()
except NameError:
    print('função acabada')

