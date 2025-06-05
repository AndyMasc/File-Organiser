import os, shutil

downloadFolder = "/Users/andymascarenhas/Downloads/"

folderTypes = {"Downloaded Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff", ".svg", ".heic", ".ico"],
               "Downloaded Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".3gp"],
               "Donwload Audio Files": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],
               "Downloaded Documents": [ ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".tex", ".md", ".epub"],
               "Downloaded Spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],
               "Downloaded Presentations": [".ppt", ".pptx", ".odp"],
               "Downloaded Code Files": [".py", ".js", ".java", ".cpp", ".c", ".cs", ".html", ".css", ".json", ".xml", ".php", ".sh", ".ts", ".rb", ".go",".ipynb"],
               "Downloaded Print Files": [".stl", ".gcode", ".3mf", ".obj"],
               "Downloaded Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"],
               "Downloaded Installers": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".appimage"]}

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