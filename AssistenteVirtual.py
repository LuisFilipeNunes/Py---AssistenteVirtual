## Luis Nunes ##
## Apenas pra testar umas ideias e utilizar o módulo speec_recognition


import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
wikipedia.set_lang("pt")

# Método para receber comandos e reconhece-los
# utilizando o módulo speech_Recognition 
# O método que foi utilizado para reconhecer é o *.Recognizer()*

def takeCommand():

        r = sr.Recognizer()

        # Aqui vamos utilizar o módulo *Microphone* do 
        # módulo SR para capturar o audio do comando 

        with sr.Microphone() as source:
                print('Ouvindo...')
                r.pause_threshold = 0.7
                audio = r.listen(source)
                
        # Vamos usar um método try/catch para que, se 
        # o som é reconhecido, jogo que segue, caso não, vamos 
        # ter que lidar com algumas exceções.

                try:
                        print("Reconhecendo o audio..")
                        
                        Query = r.recognize_google(audio, language='pt-br')
                        print("O comando reconhecido foi {}".format(Query))
                        
                except Exception as e:
                        print(e)
                        print("Poderia, por favor, repetir o comando?")
                        return "None"
                return Query

def speak(audio):
        
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        # Configurando voz. Só tem feminino para o português.
        engine.setProperty('voice', voices[0].id)
        # Método para converter texto em audio.
        engine.say(audio)
        
        # Tranca outros processo no queue enquanto o último não se resolve.
        engine.runAndWait()

def tellDay():
        
        # método para responder dia da semana.
        day = datetime.datetime.today().weekday() + 1
        
        #dicionário com os dias da semana em pt-br
        Day_dict = {1: 'Segunda-Feira', 2: 'Terça-Feira',
                                3: 'Quarta-Feira', 4: 'Quinta-Feira',
                                5: 'Sexta-Feira', 6: 'Sábado',
                                7: 'Domingo'}
        
        if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("O dia da semana é" + day_of_the_week)


def tellTime():
        
    # Método para retornar o horário.
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13] #Fatia que está posicionado o número que nos interessa
    min = time[14:16]
    speak("O horário atual é:" + hour + "horas e " + min + "minutos")
 
def Hello():
        
        #Método para inicializar o assistente; Inicializa e fica aguardando comandos.
        speak("Olá, eu sou sua assistente virtual! Como posso ajudar?")


def Take_query():
        
        Hello()
        
        #Esse laço é infinito, já que vai ficar esperando pelos comandos até 
        # receber seu comando para desligar. (Ou ser encerrado manualmente)
        while(True):
                
                # recebendo o comando e convertendo para caixa baixa
                # para evitar erros.
                query = takeCommand().lower()
                
                if "abra o google" in query or "pesquisa para mim" in query:
                        speak("Abrindo o Google!")
                        query = query.replace("pesquisa para mim", "")
                        query = query.replace("abra o google", "")
                        webbrowser.open("https://www.google.com/search?q={}".format(query))
                        continue

                elif "que dia é hoje" in query:
                        tellDay()
                        continue
                
                elif "que hora é agora" in query or "que hora é" in query or "que horas são" in query:
                        tellTime()
                        continue
                
                elif "pode dormir" in query:
                        speak("Okay, encerrando sistema")
                        exit()
                
                elif "definição de" in query:
                        speak("conferindo na wikipedia ")
                        query = query.replace("definição de", "")
                        result = wikipedia.summary(query, sentences=4)
                        speak("de acordo com a wikipedia")
                        speak(result)
                
                elif "qual o seu nome" in query or "qual é o seu nome" in query:
                        speak("Eu sou sua assistente virtual")

if __name__ == '__main__':
        
        Take_query()
