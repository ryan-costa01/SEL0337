
# SEL0337 - Prática 6

```python
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
```
 
 ## Explicação do código
 Inicialmente, são importadas as bibliotecas necessárias para o funcionamento da Rasp, damos destaque à `picamera`, responsável por fazer o controle da câmera.

Em seguida, é criada uma variável `camera` responsável por armazenar as configurações e funções da câmera.

Configuramos a resolução para 2592x1944.

Depois, os números USP dos integrantes da dupla na parte de cima da imagem usando a função `anotate`

No final do código, são feitas três operações com a câmera. A primeira delas é apresentar na tela do computador um preview da imagem com o número USP do discente impresso na parte de cima da imagem usando a função `anotate`, e com o passar de 5 segundos(definido pelo `sleep(5)`) é realizada a captura da imagem e salva no local destinado. Logo depois, é iniciada a gravação de um vídeo de 5 segundos e salvo na mesma pasta da foto.

Finalizado o uso da câmera, é acionado o setor do código responsável pela obtenção dos dados meteorológicos do local definido. Para essa parte foram utilizadas as bibliotecas `json` e `request`. Utilizando a URL presente na variável `weather`, é possível obter os dados climáticos de um local específico de acordo com o ID presente no final da URL(no caso o ID=966583, disponibiliza os dados da UFSC). Os dados obtidos são impressos no terminal na forma de lista pelo comando `pprint`.

 ## Upando o diretório no github
Primeiramente devemos iniciar um repositório usando o comando `git init`.
Logo então linkamos o repositório local com o repositório do github usando o comando `git remote add origin <link do repo>`
Finalmente finalizamos fazendo o `commit` e o `push`

```
git init 
git remote add origin https://github.com/ryan-costa01/SEL0337_Pratica6
git add .
git commit -am "commit inicial"
git push origin master
```
