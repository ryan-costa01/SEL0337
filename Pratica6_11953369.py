#Ryan Fellipe Silva Costa - nUSP: 11953369
#Pratica 6 - SEL0337 Aplicacao de Microprocessadores 2 

#Bibliotecas importadas
import json
import pprint
from requests import get
from picamera import PiCamera
from time import sleep

#Variavel 'camera' definida pra funcao 'Picamera()'
camera = PiCamera()

#configuracao da imagem da camera
camera.resolution = (2592, 1944)
camera.framerate = 15

#armazena a imagem com o meu numero usp impresso
#e salva na pasta destinada
camera.start_preview('/home/sel/69/foto.jpg')
camera.annotate_text_size = 50
camera.annotate_text = "11953369"
sleep(5)
camera.stop_preview()

#inicia e armazena video de 5 segundos
camera.start_recording('/home/sel/69/pratica6_video.h264') 
sleep(5) 
camera.stop_recording() 

#URL API com as estacoes do planeta
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations' 
#URL API com ultimos dados do clima da UFSC
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583' 

#faz a obtencao dos dados climaticos e imprime no painel
my_weather = get(weather).json()['items'] 
pprint(my_weather) 