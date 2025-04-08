import os
import shutil

class FileOrganizer:
    def __init__(self):
        self.zips = ['.zip', '.rar', '.tar', '.gz']
        self.apps = ['.exe', '.msi', '.apk']
        self.pdfs = ['.pdf']
        self.presentations = ['.pptx', '.docx']
        self.codes = ['.py', '.js', '.java', '.cpp']
        self.audio = ['.mp3', '.wav']
        self.video = ['.mp4', '.avi']
        self.img = ['.jpg', '.jpeg', '.png']
        self.iso = ['.iso']
        self.fileFound = []
    
    def is_compressed(self, file):
        return os.path.splitext(file)[1] in self.zips
    
    def is_app(self, file):
        return os.path.splitext(file)[1] in self.apps
    
    def is_pdf(self, file):
        return os.path.splitext(file)[1] in self.pdfs
    
    def is_present(self, file):
        return os.path.splitext(file)[1] in self.presentations
    
    def is_code(self, file):
        return os.path.splitext(file)[1] in self.codes
    
    def is_audio(self, file):
        return os.path.splitext(file)[1] in self.audio
    
    def is_video(self, file):
        return os.path.splitext(file)[1] in self.video
    
    def is_image(self, file):
        return os.path.splitext(file)[1] in self.img
    
    def is_iso(self, file):
        return os.path.splitext(file)[1] in self.iso
    
    def is_screenshot(self, file):
        name, ext = os.path.splitext(file)
        return (ext in self.img) and "screenshot" in name.lower()
    
    def organize_files(self):
        # Move into unorganized directory
        os.chdir("C:/Users/daary/Downloads")
        print("Starting file organization...")

        # While loop for constant automated organization
        while True:
            for file in os.listdir():
                if file in self.fileFound:
                    print(f'System already organized.')
                    return
                self.fileFound.append(file)

                print(f'Organizing {file}...')
                for folder, extensions in self.file_types.items():
                    if os.path.splitext(file)[1] in extensions:
                        shutil.move(file, f"C:/Users/daary/Documents/{folder}")
                        break