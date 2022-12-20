# Prática 6

## Criação do Diretório

Criamos, para armazenar os códigos e mídias geradas, um novo diretório com o nome da prática dentro da RaspberryPi.

`mkdir pratica6_luciano_andrey`

Dentro dele criamos um novo arquivo com o nome `capture.py` e editamos seu conteúdo usando o VIM.

```
cd pratica6_luciano_andrey
touch capture.py
vim capture.py
```
```python
#capture.py
from time import sleep
import time
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

#anotações na imagem
camera.annotate_text = "Luciano Bacelar 11800740 \n Andrey Cortez 11819487"

#preview da camera
camera.start_preview(alpha=250) # aplha: 0 -255
time.sleep(5)
camera.stop_preview()

#inicio captura de imagem
camera.capture("img_luciano_andrey.png")

#inicia da gravação do vídeo
camera.start_recording("vid_luciano_andrey.h264")
time.sleep(5)
camera.stop_recording()
time.sleep(5)
```
 
 ## Explicação do código
 O código inicia importando as bibliotecas necessárias para seu funcionamento, damos destaque à `picamera`, responsável por fazer o controle da câmera.

Logo então inicializamos uma variável responsável por armazenar as configurações e funções da câmera.

Configuramos a resolução para 1024x768

Depois anotamos os números USP dos integrantes da dupla na parte de cima da imagem usando a função `anotate`

Finalmente fazemos três operações finais com a câmera. A primeira delas é apresentar na tela do computador um preview da imagem. Depois fazemos a captura da imagem, e então gravamos um vídeo.

 ## Upando o diretório no github
Primeiramente devemos iniciar um repositório usando o comando `git init`.
Logo então linkamos o repositório local com o repositório do github usando o comando `git remote add origin <link do repo>`
Finalmente finalizamos fazendo o `commit` e o `push`

```
git init 
git remote add origin https://github.com/AndreyCortez/SEL0337
git add .
git commit -am "commit inicial"
git push origin master
```