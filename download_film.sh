#!/bin/bash

video_url="$1"
output_name="$2"

# Download the full video only once
yt-dlp "$video_url" -o "$output_name" --cookies cookies.txt || { echo "Download failed"; exit 1; }
