# File Organizer

A Python script that automatically organizes files in a folder into 
categorized subfolders based on file type.

## Features
- Organizes files into: Documents, Images, Music, Videos, Code, Archives, Others
- Dry-run mode — preview what will happen before moving anything
- Duplicate file handling — renames conflicting files automatically
- JSON move log — full record of every file moved with timestamps
- Graceful error handling — skips locked or missing files without crashing

## How to run
```bash
python file_organize.py
```

## Tech used
- Python OOP (class with 8 methods)
- `os` and `shutil` for file operations
- `json` for move logging
- Exception handling (`FileNotFoundError`, `PermissionError`)
- Decorators pattern (dry_run preview)

## Project structure
```
File_Organizer_Project/
├── file_organize.py    # main program
└── README.md
```