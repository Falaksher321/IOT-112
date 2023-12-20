import base64
from PIL import Image
import streamlit as st
import speech_recognition as sr
from gtts import gTTS

# Load the background image
image = Image.open('C:/Users/pc/Pictures/back.PNG')

# Encode the image to base64
encoded_image = base64.b64encode(image.tobytes()).decode()

# Define a function to set the background of the Streamlit app
def set_background(encoded_image):
    """
    A function to set the background of a Streamlit app.

    Args:
        encoded_image (str): The base64-encoded string of the image you want to use as the background.
    """
    page_bg_img = f'''
    <style>
    body {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the set_background function
set_background(encoded_image)

# Function for Audio to Text conversion
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError as e:
            return f"Error: {str(e)}"

# Function for Text to Audio conversion
def text_to_audio(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("output_audio.mp3")
        return True, None
    except Exception as e:
        return False, e

# Main function for Streamlit app
def main():
    st.title("Audio-Text Converter")
    st.markdown(
        '<h1 style="text-align: center; color: white;">Welcome to Audio-Text Converter</h1>',
        unsafe_allow_html=True
    )
    st.markdown('<h3 style="text-align: center; color: lightgreen;">Created by Falak Sher</h3>', unsafe_allow_html=True)
    st.markdown("---")

    user_choice = st.selectbox("Why do you want to use this web app?", ("Audio to Text", "Text to Audio"))

    if user_choice == "Audio to Text":
        uploaded_file = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])

        if uploaded_file is not None:
            st.audio(uploaded_file, format='audio/ogg', start_time=0)
            st.markdown("---")

            if st.button('Convert'):
                text_result = audio_to_text(uploaded_file)
                st.success("Converted Text:")
                st.write(text_result)

    elif user_choice == "Text to Audio":
        st.write("Enter up to 100 characters of text below:")
        user_text = st.text_area("Input text", max_chars=100)

        if st.button('Convert to Audio'):
            if len(user_text.strip()) > 0:
                success, error = text_to_audio(user_text)
                if success:
                    st.success("Audio Generated!")
                    st.audio("output_audio.mp3", format='audio/ogg', start_time=0)
                    st.markdown(get_binary_file_downloader_html("output_audio.mp3", 'Audio Download'), unsafe_allow_html=True)
                else:
                    st.error("Error generating audio. Please try again.")
                    st.write(f"Error Details: {error}")

if __name__ == "__main__":
    main()
