import streamlit as st
import os
from download import download
from time import sleep

st.header('App') 

url = 'https://checker.in/go/4626012'
youtube_ffmpeg_command = 'ffmpeg -re  -stream_loop -1 -i video.mp4 -c copy output.mp4 -c:v libx264 -c:a aac -f flv rtmp://a.rtmp.youtube.com/live2/egr2-jwmx-pshz-e1g8-cc6k'

status = download(url,'video.mp4')
st.markdown(status)

sleep(100)

text = os.popen(youtube_ffmpeg_command).read()
st.markdown(text)

st.text("Working")
