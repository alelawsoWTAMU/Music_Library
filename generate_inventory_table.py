import pandas as pd
import os

# Set base path to scan your entire music library
base_path = os.path.expanduser("~/Music")
output_csv = os.path.join(base_path, "Music_Inventory.csv")
music_data = []

# Walk through all directories
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".mp3"):
            # Get path relative to the Music folder
            rel_path = os.path.relpath(os.path.join(root, file), base_path)
            parts = rel_path.split(os.sep)
            
            # Logic: Artist / Year - Album / Track - Title.mp3
            if len(parts) >= 3:
                artist = parts[0]
                album_folder = parts[1]
                filename = parts[2]
                
                # Split Year and Album
                if " - " in album_folder:
                    year, album = album_folder.split(" - ", 1)
                else:
                    year, album = "Unknown", album_folder
                
                # Split Track and Title, convert " - " to "."
                clean_filename = filename.replace(".mp3", "")
                track_song = clean_filename.replace(" - ", ".")
                
                music_data.append({
                    "Artist": artist,
                    "Album": album,
                    "Track.Song": track_song,
                    "Year": year
                })

# Create DataFrame and save as CSV (which opens perfectly in Excel)
df = pd.DataFrame(music_data)
df.to_csv(output_csv, index=False)
print(f"Inventory saved to {output_csv}")
