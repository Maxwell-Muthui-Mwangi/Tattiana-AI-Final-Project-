import streamlit as st
import os
from time import sleep
import requests
from pytube import YouTube
from zipfile import ZipFile

bar = st.progress(0)

# 1. API
api_key = st.secrets['api_key']

# 2. Retrieving audio file from YouTube video
def get_yt(inputURL):
    video = YouTube(inputURL)
    yt = video.streams.get_audio_only()
    yt.download()

    st.info('2. Audio file has been retrieved from YouTube video')
    bar.progress(10)

# 3. Upload YouTube audio file to AssemblyAI
def transcribe_yt():

    current_dir = os.getcwd()

    for file in os.listdir(current_dir):
        if file.endswith(".mp4"):
            mp4_file = os.path.join(current_dir, file)
            #print(mp4_file)
    filename = mp4_file
    bar.progress(20)

    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    headers = {'authorization': api_key}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(filename))
    audio_url = response.json()['upload_url']
    st.info('3. YouTube audio file has been uploaded to AssemblyAI')
    bar.progress(30)

    # 4. Transcribe uploaded audio file
    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
        "audio_url": audio_url,
        "content_safety": True
    }

    headers = {
        "authorization": api_key,
        "content-type": "application/json"
    }

    transcript_input_response = requests.post(endpoint, json=json, headers=headers)

    st.info('4. Transcribing uploaded file')
    bar.progress(40)

    # 5. Extract transcript ID
    transcript_id = transcript_input_response.json()["id"]
    st.info('5. Extract transcript ID')
    bar.progress(50)

    # 6. Retrieve transcription results
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = {
        "authorization": api_key,
    }
    transcript_output_response = requests.get(endpoint, headers=headers)
    st.info('6. Retrieve transcription results')
    bar.progress(60)

    # Check if transcription is complete

    st.warning('Transcription is processing ...')
    while transcript_output_response.json()['status'] != 'completed':
        sleep(1)
        transcript_output_response = requests.get(endpoint, headers=headers)
    
    bar.progress(100)

    # 7. Print transcribed text
    st.header('Output')
    
    with st.expander('Show Text'):
        st.success(transcript_output_response.json()["text"])

    # 8. Save transcribed text to file

    # Save as TXT file
    yt_txt = open('yt.txt', 'w')
    yt_txt.write(transcript_output_response.json()["text"])
    yt_txt.close()

    # 9. Write JSON to app
    with st.expander('Show Full Results'):
        st.write(transcript_output_response.json())
    
    # 10. Write content_safety_labels
    with st.expander('Show content_safety_labels'):
        st.write(transcript_output_response.json()["content_safety_labels"])
    
    with st.expander('Summary of content_safety_labels'):
        st.write(transcript_output_response.json()["content_safety_labels"]["summary"])
        
    # Save as SRT file
    srt_endpoint = endpoint + "/srt"
    srt_response = requests.get(srt_endpoint, headers=headers)
    with open("yt.srt", "w") as _file:
        _file.write(srt_response.text)
    
    zip_file = ZipFile('transcription.zip', 'w')
    zip_file.write('yt.txt')
    zip_file.write('yt.srt')
    zip_file.close()
    
    # Delete processed files
    for file in os.listdir(current_dir):
        if file.endswith(".mp4"):
            os.remove(file)
        if file.endswith(".txt"):
            os.remove(file)
        if file.endswith(".srt"):
            os.remove(file)
