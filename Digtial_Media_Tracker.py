from pathlib import Path
import pandas as pd

def videogames():
    data = []

    for pattern in ['*.7z', '*.zip']:
        for file_path in Path('/media/alelawso/97C0-65F5/Emulation/Games/').rglob(pattern):
            if file_path.is_file():
                file_size = (file_path.stat().st_size)/ (1024**3)
                clean_path = str(file_path.resolve()).replace('/media/alelawso/97C0-65F5/Emulation/Games/', '')
                parts = clean_path.split('/')

                data.append({
                    'Console': parts[0],
                    'Game Name': parts[-1],
                    'Size (GB)': round(file_size, 2)
                })
                
    df = pd.DataFrame(data)
    df.to_excel('/home/alelawso/Documents/DigitalLibrary.xlsx', index=False, sheet_name='Videogames')
    print(f"Videogame library updated with {len(data)} games.")



# Call functions
videogames()
