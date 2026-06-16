# Music Library Manager

A simple automation workflow to populate and visualize an MP3 music library.
![Workflow Diagram](/image.png)


## Overview
This script scans your music folders for `.mp3` files, extracts the **Artist**, **Album**, and **Title** tags using `exiftool`, and updates an existing `.xlsx` file while preserving your formatting and AutoFilters in LibreOffice.

## Prerequisites
* **Python 3**
* **ExifTool**: Install via `sudo apt install libimage-exiftool-perl`
* **Python Libraries**: 
  ```bash
  pip install pandas openpyxl
  pip install exiftool
