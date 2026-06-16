# Process urls into .mp3 files and park in Staging folder
while read -r url; do
  [[ -z "$url" ]] && continue
  
  yt-dlp -x --audio-format mp3 --audio-quality 0 \
    --embed-thumbnail \
    -o "$HOME/Music/STAGING/%(artist,uploader|NA)s/%(title)s.%(ext)s" \
    "$url"
done < "$HOME/Desktop/urls.txt"

# Run inventory script
python3 "$HOME/Desktop/generate_inventory.py"
