#!/bin/bash

output="combined.mkv"
rm -f file_list.txt

# Sort filenames using natural order (clip1, clip2, ..., clip10)
for f in $(ls *.mkv | sort -V); do
    echo "file '$PWD/$f'" >> file_list.txt
done

ffmpeg -f concat -safe 0 -i file_list.txt -c copy "$output"

echo "✅ Combined video saved as: $output"
