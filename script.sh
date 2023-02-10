#!/bin/bash

VBR="1500k"
FPS="24"
QUAL="superfast"

YOUTUBE_URL="$1"
KEY="$2"
VIDEO_SOURCE="$3"

ffmpeg \
    -stream_loop -1 \
    -re -i "$VIDEO_SOURCE" \
    -c:v libx264 -pix_fmt yuv420p -preset $QUAL -r $FPS -g $(($FPS * 2)) -b:v $VBR \
    -c:a aac \
    -f flv "$YOUTUBE_URL/$KEY"
