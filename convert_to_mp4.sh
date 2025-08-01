#!/bin/bash

input_filename="$1"
output_filename="$2"

ffmpeg -i "$input_filename" -c:v libx264 -crf 23 -preset fast -c:a aac "$output_filename"
