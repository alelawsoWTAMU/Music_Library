import pandas as pd
import os

base_path = os.path.expanduser("~/Music/STAGING")
music_data = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".mp3"):
            # Get relative path: Artist/Year - Album/Track - Title.mp3
            rel_path = os.path.relpath(os.path.join(root, file), base_path)
            parts = rel_path.split(os.sep)
            
            if len(parts) >= 3:
                artist = parts[0]
                album_folder = parts[1]
                filename = parts[2]
                
                # Split Year and Album
                year, album = album_folder.split(" - ", 1) if " - " in album_folder else ("Unknown", album_folder)
                
                # Split Track and Title
                track, title = filename.split(" - ", 1) if " - " in filename else ("", filename.replace(".mp3", ""))
                
                music_data.append({
                    "Artist": artist,
                    "Album": album,
                    "Track.Song": f"{track}.{title.replace('.mp3', '')}",
                    "Year": year
                })

df = pd.DataFrame(music_data)
df.to_excel(os.path.join(base_path, "Music_Inventory.xlsx"), index=False)
print("Inventory updated: Music_Inventory.xlsx")
