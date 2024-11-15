import os, sys
from gtts import gTTS
def iniciar():

 os.system('cls' if os.name == 'nt' else 'clear')
 texto=input("Que quieres decir ---> ")
 tts=gTTS(text=texto, lang="es", tld="com")
 tts.save("audio.mp3")
 if os.path.exists('audio.mp3'):
  print('Audio Almacenado Exitosamente\n')
 sn=input('\nPresiona ENTER Para Continuar...\n[X] Para cerrar el script = ')
 if sn == 'X' or sn == 'x':
  sys.exit()
 else:
  pass
 iniciar()
iniciar()

