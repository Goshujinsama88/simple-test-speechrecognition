#-------------------------------------------------------------------------------------------------------------
#
#                                   Script de prueba de speech_recognition
#
# Este script es una prueba que realice de la librería speech_recognition. Básicamente, primero grabamos algo
# que el usuario diga y luego lo traducimos para mostrar la traducción al inglés en la consola o terminal.
#
# Script creado por: Guadalupe Fernando Escutia Rodríguez.
# Página web: https://ferplace.site
# GitHub: https://github.com/Goshujinsama88
#
# ------------------------------------------------------------------------------------------------------------

#Importamos las librerias necesarias
import speech_recognition as sr
from googletrans import Translator, constants

#Iniciamos el reconocedor de voz y el traductor
r = sr.Recognizer()
translator = Translator()

#Grabamos audio
with sr.Microphone() as source:
    print('Dí algo: ')
    audio = r.listen(source)

#Tratamos de reconocer lo dicho en el audio y lo pasamos a una nueva variable    
try:
    text = r.recognize_google(audio, language='es-MX')
    print('Has dicho: {}'.format(text))
    textf = format(text)

#Si no se logra escuchar lo que se ha dicho mandamos mensaje de error
except:
    print('Lo siento, no te he podido escuchar.')

#Tratamos de traducir lo dicho en la grabación
try:    
    translation = translator.translate(textf, dest="en", src="es")
    print('La traducción al ingles es: ' + translation.text)

#Si no se logra traducir mandamos mensaje de error
except:
    print('No se ha podido traducir.')