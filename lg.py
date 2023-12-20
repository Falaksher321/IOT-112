import streamlit as st
from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def main():
    st.title("Language Translator App")
    st.write("Welcome to QuantumReach Translator!")

    languages = ['Select Language', 'English', 'Urdu', 'Spanish', 'French', 'German', 'Chinese', 'Japanese']  # Add more languages

    st.subheader("Translate From:")
    from_lang = st.selectbox("Choose a language", languages)

    st.subheader("Translate To:")
    # Exclude the 'Select Language' option to prevent duplicate structure
    to_languages = [lang for lang in languages if lang != 'Select Language']
    to_lang = st.selectbox("Choose a language", to_languages)

    input_text = st.text_area("Enter text to translate")

    if st.button("Translate"):
        if from_lang != 'Select Language' and to_lang:
            # Map the selected language to Google Translate language codes
            google_lang_codes = {
                'English': 'en',
                'Urdu': 'ur',
                'Spanish': 'es',
                'French': 'fr',
                'German': 'de',
                'Chinese': 'zh-CN',  # Use 'zh-CN' or 'zh-TW' for Chinese
                'Japanese': 'ja'
            }
            translated_text = translate_text(input_text, google_lang_codes[to_lang])
            st.write(f"Translated text: {translated_text}")
        else:
            st.warning("Please select languages for translation.")

if __name__ == "__main__":
    main()
