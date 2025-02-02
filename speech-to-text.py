import azure.cognitiveservices.speech as speechsdk
import streamlit as st

if "transcriptions" not in st.session_state:
    st.session_state.transcriptions = []

speech_config = speechsdk.SpeechConfig(
    subscription="4Qg9h0dEahkmGRZ7kJfdGaMVCR5k0igzRNqGBbNElM9ZmVYdTc4AJQQJ99BBACBsN54XJ3w3AAAYACOG7oir",
    region="canadacentral")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)


def start_recognition():
    st.session_state.transcription = ""
    with st.spinner("Taking notes..."):
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            st.session_state.transcription = speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            st.session_state.transcription = "No speech could be recognized"
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            st.session_state.transcription = f"Speech Recognition canceled: {speech_recognition_result.cancellation_details.reason}"

# Streamlit UI
st.title("Baymax Med-AI Visit Notes")

# Button to start recognition
if st.button("🎙"):
    start_recognition()

# Show transcription result
if "transcription" in st.session_state:
    st.header("Transcription:")
    st.write(st.session_state.transcription)
