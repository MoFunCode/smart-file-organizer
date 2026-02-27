# smart-file-organizer

Ever look at a Downloads folder with 200 random files and just... close it? This script fixes that.

It scans a folder and sorts everything into tidy subfolders by file type — no manual dragging required.

---

## What it does

Drops your files into these categories automatically:

| Category | Examples |
|---|---|
| Images | .jpg, .png, .gif, .svg... |
| Documents | .pdf, .docx, .txt, .csv... |
| Videos | .mp4, .mov, .mkv... |
| Audio | .mp3, .wav, .flac... |
| Archives | .zip, .rar, .7z... |
| Code | .py, .js, .html, .sql... |
| Executables | .exe, .dmg, .pkg... |
| Others | anything else |

Handles duplicates too — if a file with the same name already exists, it renames it `file_1.ext`, `file_2.ext`, etc. rather than overwriting anything.

---

## How to use it

1. Open `organizer.py` and set `target_folder` to the path you want to clean up:

```python
target_folder = "/Users/yourname/Desktop/messy_folder"
```

2. Run it:

```bash
python organizer.py
```

That's it.

---

## Example

Before — a folder with random files dumped in it. After running the script:
<img width="1800" height="1169" alt="Screenshot 2026-02-26 at 11 22 20 PM" src="https://github.com/user-attachments/assets/b3e09d23-2764-4136-9800-d6dc661b028b" />
Everything sorted into its own folder in one shot.

---

## Requirements

- Python 3
- No external libraries needed (just `os` and `shutil` from the standard library)
