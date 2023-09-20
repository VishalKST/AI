import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize and process voice commands
def process_command():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)

            # Process voice command
            if "hello" in command.lower():
                speak("Hello! How can I assist you?")
            elif "what's the weather" in command.lower():
                speak("I'm sorry, I cannot provide weather information at the moment.")
            elif "goodbye" in command.lower():
                speak("Goodbye! Have a great day.")
            else:
                speak("I didn't understand your command. Please try again.")

        except sr.WaitTimeoutError:
            print("Timeout. Please speak again.")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    speak("Welcome! How can I assist you?")
    while True:
        process_command()
