import os 
import shutil
import json 
from datetime import datetime

def reset_test_folder():
    """Wipes and recreates test_folder with dummy files for testing."""
    subfolders = ["Documents", "Images", "Music", "Videos", "Code", "Archives", "Others"]
    for sf in subfolders:
        sf_path = os.path.join("test_folder", sf)
        if os.path.exists(sf_path):
            shutil.rmtree(sf_path, ignore_errors=True)

    os.makedirs("test_folder", exist_ok=True)

    test_files = [
        "report.pdf", "invoice.docx", "notes.txt",
        "photo.jpg", "wallpaper.png",
        "song.mp3", "movie.mp4",
        "script.py", "archive.zip", "random.xyz"
    ]
    for f in test_files:
        filepath = os.path.join("test_folder", f)
        open(filepath, "w").close()
    print("Test folder reset - fresh start")


class FileOrganizer:
    def __init__(self, source_folder):
        self.source_folder = source_folder 
        self.move_log = []
        self.EXTENSION_MAP = {
            ".pdf":  "Documents",
            ".docx": "Documents",
            ".txt":  "Documents",
            ".jpg":  "Images",
            ".jpeg": "Images",
            ".png":  "Images",
            ".mp3":  "Music",
            ".mp4":  "Videos",
            ".py":   "Code",
            ".js":   "Code",
            ".json":  "Code",
            ".zip":  "Archives",
        }

    def get_destination_folder(self, filename):
        """Returns the destination subfolder name for a given filename."""
        name, extension = os.path.splitext(filename)
        folder = self.EXTENSION_MAP.get(extension, "Others")
        return folder

    def create_folder_if_missing(self, folder_path):
        """Creates a folder if it doesn't already exist."""
        os.makedirs(folder_path, exist_ok=True)
        
    def handle_duplicate(self, destination_path):
        """Returns a safe destination path, remaining if a conflict exists."""
        if not os.path.exists(destination_path):
            return destination_path
        
        folder = os.path.dirname(destination_path)
        filename = os.path.basename(destination_path)
        name, ext = os.path.splitext(filename)

        counter = 1 
        new_path = destination_path
        while os.path.exists(new_path):
            new_name = f"{name}_{counter}{ext}"
            new_path = os.path.join(folder, new_name)
            counter += 1

        return new_path

    def move_file(self, filename):
        """Moves a single file to its destination subfolder"""
        try:
            source_path = os.path.join(self.source_folder, filename)
            sub_folder = self.get_destination_folder(filename)
            dest_folder = os.path.join(self.source_folder, sub_folder)
            dest_path = os.path.join(dest_folder, filename)

            self.create_folder_if_missing(dest_folder)
            final_path = self.handle_duplicate(dest_path)
            shutil.move(source_path, final_path)

            self.log_move(filename, final_path, "moved")
            print(f"Moved: {filename} -> {final_path}")

        except FileNotFoundError:
            print(f"Skipped: {filename} - file not found at source")
            self.log_move(filename, "", "failed - not found")
        except PermissionError:
            print(f"Skipped: {filename} - permission denied")
            self.log_move(filename, "", "failed - permission denied")

    def dry_run(self):
        """Previews what organize() would do - without moving anything."""
        print("── DRY RUN PREVIEW ──────────────────────────")
        for item in os.listdir(self.source_folder):
            if item == "move_log.json":
                continue 
            full_path = os.path.join(self.source_folder, item)
            if os.path.isfile(full_path):
                subfolder = self.get_destination_folder(item)
                dest = os.path.join(self.source_folder, subfolder, item)
                print(f"  [DRY RUN] {item} -> {dest}")
        print("── NO FILES WERE MOVED ──────────────────────\n")

    def organize(self):
        """Move all files in source_folder into categorized subfolders."""
        print("── ORGANIZING ───────────────────────────────")
        for item in os.listdir(self.source_folder):
            if item == "move_log.json":
                continue
            full_path = os.path.join(self.source_folder, item)
            if os.path.isfile(full_path):
                self.move_file(item)
        self.save_log()

    def log_move(self, filename, destination, action):
        """Appends a move record to the in-memory log."""
        new_data = {
            "filename":filename,
            "destination": destination,
            "action": action,
            "timestamp": datetime.now().isoformat()
            }
        self.move_log.append(new_data) 
    
    def save_log(self):
        """Writes the move log to move_log.json inside source_folder."""
        log_path = os.path.join(self.source_folder, "move_log.json")
        with open(log_path, "w") as f:
            json.dump(self.move_log, f, indent=2)
        print(f"Log saved - {len(self.move_log)} entries written to move_log.json")

if __name__ == "__main__":
    reset_test_folder()

    org = FileOrganizer("test_folder")

    #Preview first - nothing moves
    org.dry_run()

    # Now actually organize
    org.organize()