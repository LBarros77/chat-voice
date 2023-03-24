import openai
import pyttsx3
import speech_recognition as sr
import time

# Set your Open PAI key
openai.api_key = ""

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.record(source)
    except:
        print("Skipping unknowh error")

def generate_response(prompt):
    response = openai.Completation.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        # Wait for user to say "genius"
        print("Say 'Genius' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognizer_google(audio)
                if transcriptio.lower() == "genius":
                    # Record audio
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                        # Transcribe audio to text
                        text = transcribe_audio_to_text(filename)
                        if text:
                            print(f"You said: {text}")

                            # Generate response wsing GPT-3
                            response = generate_response(text)
                            print(f"GPT-3 says: {response}")

                            # Read response using text-to-speach
                            speach_text(response)
            except Exception as e:
                print(f"An error ocurred: {e}")

if __name__ == '__main__':
    main()
                


