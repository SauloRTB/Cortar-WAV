# coding=UTF-8
# contato: saulortb@gmail.com
import re
from pydub import AudioSegment
import os
import glob




busca1 = os.getcwd() + r"//*.wav"
arquivoswav = glob.glob(busca1)
busca2 = os.getcwd() + r"//*.txt"
arquivostxt = glob.glob(busca2)
busca3 = os.getcwd() + r"//*.mp3"
arquivosmp3 = glob.glob(busca2)

for txt in arquivostxt:
    nomewav = txt.replace

arquivo = open(arquivostxt[0], 'r', encoding="utf-8")
audio = AudioSegment.from_wav(arquivoswav[0])




frases = []
opcoesvalidas = ["1","2"]

print("Você deseja exportar os recortes em qual formato? Para WAV digite 1 para MP3 digite 2")

opcaoformato = input("Opção >>  ")



while opcaoformato not in opcoesvalidas:
    print("Digite 1 para WAV ou 2 para MP3")
    opcaoformato = input("Opção >>  ")



for l in arquivo:

    tempos = re.findall(r'..:..:..\....', l)
    texto = re.sub(r'..:..:..\....+\...*\t', '', l)
    texto = texto.strip()
    tempoinicial = tempos[0]
    tempofinal = tempos[1]

    print('cortanto trecho: ' + texto + '. Tempo inicial: ' + tempoinicial + '. Tempo final: ' + tempofinal)

    horainicial = re.sub(r':..:..\....', '', tempoinicial)
    minutoinicial = re.sub(r':..\....', '', tempoinicial)
    minutoinicial = re.sub(r'..:', '', minutoinicial)
    segundoinicial = re.sub(r'..:..:', '', tempoinicial)
    segundoinicial = re.sub(r'\....', '', segundoinicial)
    milisegundoinicial = re.sub(r'..:..:..\.', '', tempoinicial) 

    horafinal = re.sub(r':..:..\....', '', tempofinal)
    minutofinal = re.sub(r':..\....', '', tempofinal)
    minutofinal = re.sub(r'..:', '', minutofinal)
    segundofinal = re.sub(r'..:..:', '', tempofinal)
    segundofinal = re.sub(r'\....', '', segundofinal)
    milisegundofinal = re.sub(r'..:..:..\.', '', tempofinal) 

    tempoinicialmili = float(horainicial)*60*60*1000 + float(minutoinicial)*60000 + float(segundoinicial)*1000 + float(milisegundoinicial)
    tempofinalmili = float(horafinal)*60*60*1000 + float(minutofinal)*60000 + float(segundofinal)*1000 + float(milisegundofinal)
    cont = 0
    print(tempoinicialmili)
    print(tempofinalmili)

    if not texto in frases:
        frases.append(texto)
    else:
        while texto in frases:
            cont += 1
            texto =   texto + cont * '_'  
        frases.append(texto)
            

    texto = texto.replace('_','')        

    
    if opcaoformato == "2":
        if cont == 0:
            recorte = audio[tempoinicialmili:tempofinalmili]
            recorte.export('recortes/' + texto + '.mp3', format="mp3")
            arquivo = open('recortes/' + texto + '.txt', 'a', encoding="UTF-8")
            print(texto,file=arquivo) 
            arquivo.close()
        else:
            recorte = audio[tempoinicialmili:tempofinalmili]
            recorte.export('recortes/' + texto + str(cont) + '.mp3', format="mp3")
            arquivo = open('recortes/' + texto + str(cont) + '.txt', 'a', encoding="utf-8")
            print(texto,file=arquivo) 
            arquivo.close()    
    elif opcaoformato == "1":
        if cont == 0:
            recorte = audio[tempoinicialmili:tempofinalmili]
            recorte.export('recortes/' + texto + '.wav', format="wav")
            arquivo = open('recortes/' + texto + '.txt', 'a', encoding="UTF-8")
            print(texto,file=arquivo) 
            arquivo.close()
        else:
            recorte = audio[tempoinicialmili:tempofinalmili]
            recorte.export('recortes/' + texto + str(cont) + '.wav', format="wav")
            arquivo = open('recortes/' + texto + str(cont) + '.txt', 'a', encoding="utf-8")
            print(texto,file=arquivo) 
            arquivo.close() 

fechar = 'n'

while fechar != 's':
    print('Deseja fechar? s/n')
    fechar = input('s/n:')