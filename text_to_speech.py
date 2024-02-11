import streamlit as st
# import wave
# import pyaudio
# import librosa
# from settings import DURATION, WAVE_OUTPUT_FILE

# def convert_audio_to_text(audio_file_path):
#     # Basic conversion using librosa
#     audio, sr = librosa.load(audio_file_path)
#     text = "This is a placeholder for converted text"
#     return text

# def record_audio(duration, output_file):
#     CHUNK = 1024
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 2
#     RATE = 44100

#     audio = pyaudio.PyAudio()

#     stream = audio.open(format=FORMAT,
#                         channels=CHANNELS,
#                         rate=RATE,
#                         input=True,
#                         frames_per_buffer=CHUNK)

#     frames = []
#     stop_recording = False

#     st.write(f"Recording for {duration} seconds...")

#     # Continuously record audio until stop_recording is True or duration is reached
#     for i in range(0, int(RATE / CHUNK * duration)):
#         if stop_recording:
#             break
#         data = stream.read(CHUNK)
#         frames.append(data)

#     st.write("Recording completed!")

#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

#     wf = wave.open(output_file, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(audio.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()

# def main():
#     if st.button('Record'):
#         record_audio(DURATION, WAVE_OUTPUT_FILE)

#     # Add a 'Stop Recording' button to stop the recording process
#     if st.button('Stop Recording'):
#         stop_recording = True

#     # Check if 'Convert to Text' button is clicked
#     if st.button('Convert to Text'):
#         try:
#             text = convert_audio_to_text(WAVE_OUTPUT_FILE)
#             st.write('Spoken text:', text)
#         except FileNotFoundError:
#             st.write("Please record sound first")
#         except Exception as e:
#             st.write(f"Error occurred: {e}")

#     if st.button('Play'):
#         try:
#             audio_file = open(WAVE_OUTPUT_FILE, 'rb')
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format='audio/wav')
#         except FileNotFoundError:
#             st.write("Please record sound first")
#         except Exception as e:
#             st.write(f"Error occurred: {e}")

# if __name__ == '__main__':
#     main()


import sounddevice as sd
import numpy as np
import wave

from settings import DURATION, WAVE_OUTPUT_FILE

def record_audio(duration, output_file):
    fs = 44100  # Sample rate
    seconds = duration

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished

    # Save the recorded audio to a WAV file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(b''.join(myrecording))

def main():
    st.title("Audio Recorder Example")

    if st.button("Record"):
        record_audio(DURATION, WAVE_OUTPUT_FILE)
        st.success("Recording completed!")

    if st.button("Play"):
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except FileNotFoundError:
            st.write("Please record sound first")
        except Exception as e:
            st.write(f"Error occurred: {e}")

if __name__ == "__main__":
    main()


