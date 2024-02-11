import streamlit as st
import librosa
from src.sound import sound
from settings import IMAGE_DIR, DURATION, WAVE_OUTPUT_FILE

def convert_audio_to_text(audio_file_path):
    # Basic conversion using librosa
    audio, sr = librosa.load(audio_file_path)
    text = "This is a placeholder for converted text"
    return text

def main():
    # Check if 'Record' button is clicked
    if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            # Assuming sound.record() method records sound
            sound.record()
        st.success("Recording completed")

    # Check if 'Stop Recording' button is clicked
    if st.button('Stop Recording'):
        # Assuming sound.stop() method stops recording
        sound.stop()

    # Check if 'Convert to Text' button is clicked
    if st.button('Convert to Text'):
        try:
            text = convert_audio_to_text(WAVE_OUTPUT_FILE)
            st.write('Spoken text:', text)
        except FileNotFoundError:
            st.write("Please record sound first")
        except Exception as e:
            st.write(f"Error occurred: {e}")

    # Check if 'Play' button is clicked
    if st.button('Play'):
        try:
            # Read audio file
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except FileNotFoundError:
            st.write("Please record sound first")
        except Exception as e:
            st.write(f"Error occurred: {e}")

if __name__ == '__main__':
    main()
