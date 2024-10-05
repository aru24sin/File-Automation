import os
import shutil

# Define the file type lists and functions as before

pdfs = (".pdf", ".epub")
presentations = (".pptx", ".doc", ".ppt", ".docx")
zips = (".zip", ".dmg", ".gz")
apps = (".exe")
codes = (".py", ".cpp", ".c")
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv", ".alp", ".asd")
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")
img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif", ".JPG", ".heic")


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
    # Move into unorganized directory
    os.chdir("/Users/aru/Downloads")

    # For loop with if statements for each designated file type
    # Move file into proper folder
    while True:
        for file in os.listdir():
            destination_folder = None
            if is_code(file):
                destination_folder = "/Users/aru/Documents/Programming/Unsorted"
            elif is_app(file):
                destination_folder = "/Users/aru/Documents/apps"
            elif is_compressed(file):
                destination_folder = "/Users/aru/Documents/compressed"
            elif is_pdf(file):
                destination_folder = "/Users/aru/Documents/pdfs"
            elif is_present(file):
                destination_folder = "/Users/aru/Documents/pptx-docs"
            elif is_audio(file):
                destination_folder = "/Users/aru/Documents/audio"
            elif is_video(file):
                destination_folder = "/Users/aru/Documents/video"
            elif is_image(file):
                if is_screenshot(file):
                    destination_folder = "/Users/aru/Documents/screenshots"
                else:
                    destination_folder = "/Users/aru/Documents/images"

            # Check if the file already exists in the destination folder
            if destination_folder and os.path.exists(os.path.join(destination_folder, file)):
                # If file exists, rename it
                basename, extension = os.path.splitext(file)
                index = 1
                while True:
                    new_filename = f"{basename}_{index}{extension}"
                    if not os.path.exists(os.path.join(destination_folder, new_filename)):
                        # Rename and move the file
                        shutil.move(file, os.path.join(destination_folder, new_filename))
                        break
                    index += 1
            elif destination_folder:
                # If file doesn't exist, move it directly
                shutil.move(file, destination_folder)


if __name__ == '__main__':
    main()
