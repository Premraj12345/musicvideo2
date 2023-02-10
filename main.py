import streamlit as st
import os
from download import download
from time import sleep

st.header('App') 

url = 'https://checker.in/go/4639475'
youtube_ffmpeg_command = 'script.sh "rtmp://a.rtmp.youtube.com/live2" "egr2-jwmx-pshz-e1g8-cc6k" "video.mp4"'

status = download(url,'video.mp4')
st.markdown(status)

sleep(100)

text = os.popen(youtube_ffmpeg_command).read()
st.markdown(text)

st.text("Working")
