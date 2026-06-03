# Music Library Manager

A simple automation tool to extract and synchronize MP3 metadata into an Excel spreadsheet.

## Overview
This script scans your music folders for `.mp3` files, extracts the **Artist**, **Album**, and **Title** tags using `exiftool`, and updates an existing `.xlsx` file while preserving your formatting and AutoFilters in LibreOffice.

## Prerequisites
* **Python 3**
* **ExifTool**: Install via `sudo apt install libimage-exiftool-perl`
* **Python Libraries**: 
  ```bash
  pip install pandas openpyxl
