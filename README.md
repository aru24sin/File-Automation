# File-Automation
Python file organizer script for Windows and MacOS

Script searches through the downloads folder for a user and properly allocates the file types into according folders. Easy implementation of new file types. Utilized the os library to give script access to read and write changes in the file system. The shutil library is implemented to move specified files to the proper location for efficient sorting.

File types include:

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
