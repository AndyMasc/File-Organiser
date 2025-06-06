import os, shutil

downloadFolder = "/Users/andymascarenhas/Downloads/"

folderTypes = {"Downloaded Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff", ".svg", ".heic", ".ico"],
               "Downloaded Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".3gp"],
               "Donwload Audio Files": [".mp3", ".wav", ".aac", ".flac", ".wma"],
               "Downloaded Documents": [ ".pdf", ".doc", ".docx", ".txt", ".rtf"],
               "Downloaded Print Files": [".stl", ".gcode", ".3mf", ".obj"]}

os.chdir(downloadFolder)

for file in os.listdir(downloadFolder):
    name, fileExt = os.path.splitext(file)
    for folder, extensions in folderTypes.items():
        targetFolder = os.path.join(downloadFolder, folder)
        if fileExt in extensions and (not file.startswith(".")) and os.path.isfile(file):
            if not os.path.isdir(targetFolder):
                os.mkdir(targetFolder)
            shutil.move(file, targetFolder)

print('Files organized sucessfully!')