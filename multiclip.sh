#!/bin/bash

video_name="$1"
timestamp_file="$2"

# Read timestamps and cut clips
while read -r line; do
    [[ "$line" =~ ^#.*$ || -z "$line" ]] && continue
    start=$(echo "$line" | awk '{print $1}')
    end=$(echo "$line" | awk '{print $2}')
    name=$(echo "$line" | awk '{print $3}')
    echo "Extracting $name from $start to $end"
    ffmpeg -ss "$start" -to "$end" -i "$video_name" -c copy "$name"
done < "$timestamp_file"
