import pyttsx3
import wikipedia
import webbrowser
#let name of our assitance be 'Siri'
while True:      
    siri = pyttsx3.init()
    voices = siri.getProperty('voices')
    siri.setProperty('voice', voices[2].id)
    siri.say('Hello I am Siri, how may I help you')
    siri.runAndWait()  #for female voice
    siri.setProperty('rate', 175)
    x=int(input("1. Search on wikipedia\n2. Search on google\n3. Open Youtube\n4. Open facebook\n5. Open whatsapp web\n6. Open instagram\n7. Open telegram web\n8. Opem oracle live SQL\n9. Open google colab\n10. Find location\n11. Exit\nEnter your choice: "))
    if x==1:
        In = input("Search for Wikipedia: ")
        result = wikipedia.summary(In, sentences = 2)
        siri.say("According to wikipedia")
        print(result)
        siri.say(result)

    elif x==2:
        search = input('What do you want to search for?\n')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        siri.say('Here is what I found for ' + search)

    elif x==3:
        siri.say("Opening youtube")
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)

    elif x==4:
        siri.say("Opening facebook")
        url = 'https://www.facebook.com/'
        webbrowser.get().open(url)

    elif x==5:
        siri.say("Opening whatsapp web")
        url = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)

    elif x==6:
        siri.say("Opening instagram")
        url = 'https://www.instagram.com/'
        webbrowser.get().open(url)

    elif x==7:
        siri.say("Opening telegram web")
        url = 'https://web.telegram.org/'
        webbrowser.get().open(url)
    
    elif x==8:
        siri.say("Opening Oracle live sql")
        url = 'https://livesql.oracle.com/'
        webbrowser.get().open(url)

    elif x==9:
        siri.say("Opening google colab")
        url = 'https://research.google.com/colaboratory/'
        webbrowser.get().open(url)

    elif x==10:
        location = input('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        siri.say('Here is the location of ' + location)
    else:
        exit()
