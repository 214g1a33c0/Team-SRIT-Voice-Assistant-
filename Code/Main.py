import pyttsx3
import speech_recognition as sr
import webbrowser
from AppOpener import open,mklist,give_appnames
import datetime
import games

speech = pyttsx3.init()
voices = speech.getProperty('voices')

speech.setProperty('voice', voices[1].id)
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		tell("Good Morning ")

	elif hour>= 12 and hour<18:
		tell("Good Afternoon ")

	else:
		tell("Good Evening ")
ass="eleeena"
speech.say("Hello,I am your")
speech.say(ass)
speech.runAndWait()
def tell(audio):
	speech.say(audio)
	speech.runAndWait()
def username():
	tell("What is your name")
	uname = takeCommand()
	tell("Hai")
	tell(uname)
	tell("How can i Help you")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("I am Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		

	except Exception as e:
		print(e)
		print(" I am  Unable to Recognize your voice.")
		tell(" I am  Unable to Recognize your voice.")
		return "friend"
	
	return query
w-ishMe()
username()

while True:
    query = takeCommand().lower()
    if 'open youtube' in query:
        tell("Openning youtube,enjoy with awesome coontent\n")
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        tell("Opening google,enjoy with great content\n")
        webbrowser.open("google.com")
    elif 'open stack overflow' in query:
        tell("Opening Stack Over flow, code carefully")
        webbrowser.open("stackoverflow.com")
    elif 'open chrome' in query:
        tell("opening google chromes")
        open("google chrome")
    elif 'open facebook' in query:
        tell("opening facebook\n")
        webbrowser.open("facebook.com")
    elif 'open instagram web' in query:
        tell("opening instagram\n")
        webbrowser.open("instagram.com")
    elif 'open whatsapp web' in query:
        tell("opening whatsapp\n")
        webbrowser.open("web.whatsapp.com")
    elif 'open edge' in query:
        tell("opening edge\n")
        open("microsoft edge")
    elif 'open dailyhunt' in query:
        tell("opening dailyhunt\n")
        webbrowser.open("dailyhunt.com")
    elif 'open file manager' in query:
        tell("opening file manager\n")
        open("file explorer")
    elif 'open amazon' in query:
        tell("opening amazon, happy shopping\n")
        webbrowser.open("amazon.com")
    elif 'open spotify' in query:
        tell("opening spotify,sounds good vibes\n")
        webbrowser.open("spotify.com")
    elif 'open ajio' in query:
        tell("opening ajio\n")
        webbrowser.open("ajio.com")
    elif 'open flipkart' in query:
        tell("opening flipkart\n")
        webbrowser.open("flipkart.com")
    elif 'open myntra' in query:
        tell("opening myntra\n")
        webbrowser.open("myntra.com")
    elif 'open twitter' in query:
        tell("opening twitter\n")
        webbrowser.open("twitter.com")
    elif 'open msn' in query:
        tell("Opening msn\n")
        webbrowser.open("msn.com")
    elif 'open tik tok' in query:
        tell("opening tiktok\n")
        webbrowser.open("tiktok.com")
    elif 'open disha' in query:
        tell("opening disha site\n")
        webbrowser.open("https://rural.nic.in/en/disha")
        webbrowser.open("meebhumi.com")
    elif 'open notepad' in query:
        tell(" opening notepad\n")
        open("notepad")
        mklist(name="app_data.json")
        appnames = give_appnames()
    elif 'open command prompt' in query:
        tell("opening command prompt\n")
        open("command prompt")
    elif 'open visual studio' in query:
        open("visual studio code")
        tell("opening visual studio")
    elif 'open whatsapp' in query:
        open("whatsapp")
        tell("opening whatsapp")
    elif 'open snapchat' in query:
        tell("opening git hub, learn new things")
        webbrowser.open("github.com")
    elif 'open pixel ' in query:
         tell("openning pixel")
         webbrowser.open("pixel.com")
    elif 'bye' in query:
         tell("Bye bye")
         break
    elif 'play rolling dice' in query:
         tell("playing rolling dice")
         games.dice()
    elif 'play random numbers' in query:
         tell("play random number")
         games.number()
    elif 'toss a coin' in query:
         tell("tossing a coin,can you guess it")
         games.coin()
    elif 'quiz game' in query:
         tell("lets play quiz")
         games.quiz()
    elif 'what do you eat' in query:
         tell("i donnot eat much, but when i do i take megabyte")
    elif 'what do you like to drink' in query:
         tell("a cup of tea emoji")
    elif 'do you like me' in query:
         tell("let me check...yes")
    elif 'can you laugh' in query:
         tell("hahahahaha")
    elif 'say hai to me' in query:
         tell("sure hello")
    elif 'ask me a question' in query:
         tell("i have a question whats your favourite animal")
    elif 'see you later' in query:
         tell("bye bye honey pie")
    
