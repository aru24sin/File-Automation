import os
import shutil

pdfs = (".pdf")

presentations = (".pptx", ".doc", ".ppt", ".docx")

zips = (".zip")

apps = (".exe")

codes = (".py", ".cpp", ".c")

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_compressed(file):
    return os.path.splitext(file)[1] in zips

def is_app(file):
    return os.path.splitext(file)[1] in apps

def is_pdf(file):
    return os.path.splitext(file)[1] in pdfs

def is_present(file):
    return os.path.splitext(file)[1] in presentations

def is_code(file):
    return os.path.splitext(file)[1] in codes

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

def main():
    os.chdir("/Users/daary/Downloads")

    for file in os.listdir():
        if is_code(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/Programming/unsorted")
        elif is_app(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/apps")
        elif is_compressed(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/compressed")
        elif is_pdf(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/pdfs")
        elif is_present(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/pptx-docs")
        elif is_audio(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/audio")
        elif is_video(file):
            shutil.move(file, "C:/Users/daary/OneDrive/Documents/video")
        elif is_image(file):
            if is_screenshot(file):
                shutil.move(file, "C:/Users/daary/OneDrive/Documents/screenshots")
            else:
                shutil.move(file, "C:/Users/daary/OneDrive/Documents/images")

if __name__ == '__main__':
    main()
