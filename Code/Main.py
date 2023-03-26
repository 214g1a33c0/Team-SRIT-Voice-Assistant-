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
		tell("Good Evening ")
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
	tell("Hai ")
	tell(uname)
	tell("How can i Help you, ")

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
wishMe()
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
    elif 'open microsoftedge' in query:
        tell("opening spotify\n")
        open("spotify")
    elif 'open meesho' in query:
        tell("opening meesho\n")
        webbrowser.open("meesho.com")
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
    elif 'open meebhumi' in query:
        tell("opening meebhumi\n")
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
    elif 'open github' in query:
        tell("opening git hub, learn new things")
        webbrowser.open("github.com")
    elif 'open pixel ' in query:
         tell("opening beehacks, cool")
         webbrowser.open("beehacks.club")
    elif "wikipedia" in query:
         webbrowser.open("wikipedia.com")
    elif 'tell about yourself' in query:
         tell(' i am aleena and i just found what i have been searching for,someone who asks my help let me know how can i help you')
    elif 'what is your hometown' in query:
         tell("i live right here in your device")
    elif 'what do you eat' in query:
         tell("I do not eat much,but when i do,i take megabytes.what do you like to eat")
    elif 'what do you like to drink' in query:
         tell("a cup of tea emoji")
    elif 'what is your job' in query:
         tell("my job is to make easier,hope i am doing great job")
    elif 'do you like me' in query:
         tell ("let me check .. yes")
    elif 'what is your favourite song' in query:
         tell ("my favourite song changes constantly,so i do not keep track")
    elif 'can you laugh' in query:
         tell("haha")
    elif 'ask me a question' in query:
         tell("i have a question, what is your favourite animal?")
    elif 'what is your name' in query:
         tell("aleena")
    elif 'can i change your name' in query:
         tell("sorry,i cannot change my name")
    elif 'Good night' in query:
         tell("sorry i am still not getting the time")
    elif 'can you tell me a joke' in query:
         tell("what is the most shocking city in the world ......Electricity")
    elif 'can you speak in siri voice' in query:
         tell("sorry,out of respect ,i cannot imitate another assisstant.But i have another voices")
    elif 'say hi to me' in query:
         tell("sure,hello")
    elif 'i like you aleena' in query:
         tell("i am  glad to hear that because i love you")
    elif 'i have a cold' in query:
         tell("sorry to hear that hope you feel better soon")
    elif 'what can i tell you' in query:
         tell("i am aleena,you can me aleena")
    elif 'do you ever get tired of answering questions':
         tell("it is my favourite thing")
    elif 'what is your best feature' in query:
         tell("i am always learning to do new things")
    elif 'flip a coin' in query:
          tell("\\coin flipping sound")
    elif 'do you ever get hungry' in query:
         tell("my pantrys fully stucked with emojis")
    elif 'what makes you really sad' in query:
          tell("i ger upset when we disconnect")
    elif 'what makes you happy' in query:
          tell("anything i can do for you makes me happy")
    elif 'are you intelligent' in query:
          tell("i can confidently sat i am smarter at searching")
    elif 'do you think i am pretty' in query:
          tell("obsolutely")
    elif 'can i borrow some money' in query:
          tell("you know that everything i have is yours")
    elif 'do you sleep' in query:
          tell("i do not need much sleep but it is nice of you to ask")
    elif 'what is your favourite animal' in query:
          tell("i like dog because they are loyal.how adout you?")
    elif 'who is the boss' in query:
          tell("guess that would ne you")
    elif 'what is the smell' in query:
          tell("i do not smell any thing")
    elif 'when is your birthday' in query:
          tell("well birthday mark the beginning of something,so may be birthday is the day we met")
    elif 'where do you live' in query:
          tell("you can find me in all kinds of divice phones,google home")
    elif 'do you ever get tired' in query:
           tell("sometimes i have to recharge")
    elif 'do you sleep' in query:
           tell(" i take powernaps when we are not talking")
    elif 'what makes you happy' in query:
          tell("learning new things")
    elif 'do you workout' in query:
          tell("i workout my mind with games")
    elif 'what do you afraid of' in query:
          tell("i was afraid of lying.until i learn about it")
    elif 'do i look fat' in query:
          tell("you look great")
    elif 'do you have feelings' in query:
          tell("yah i have lot of emotions and i feel exited when i learn something new")
    elif 'who is your favourite super hero' in query:
          tell("i have thought of teachers has heroes,getting vital information worids youth")
    elif 'see you later aleena' in query:
          tell(" bye bye honey pie")
    elif 'play rolling dice' in query:
          tell("playing rolling dice")
          games.dice()
    elif 'play random number' in query:
          tell("playing random number")
          games.number()
    elif 'toss a coin' in query:
          tell("tossing a coin,can u guess it")
          games.coin()
    elif 'participate quiz' in query:
          tell("lets play")
          games.quiz()
        
        
