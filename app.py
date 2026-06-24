import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter Text")

target_lang = st.selectbox(
    "Translate To",
    ["hi", "fr", "es", "de", "ja"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source="auto",
        target=target_lang
    ).translate(text)

    st.success(translated)