# Imports
import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

# Important Note
messagebox.showerror("WARNING!", "THIS IS A WINDOWS PORT OF THE 'unResolvedOrganizer' APP. THIS APP IS WELL-OPTIMIZED FOR MACOS BUT NOT FOR WINDOWS!\n\nUSE IT AT YOUR OWN RISK! PRESS 'OK' TO CONTINUE.")

# Common File Extensions
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Animations',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'MS Excel Files',
    'zip': 'Archives',
    'rar': 'RAR Archives',
    'exe': 'Executables',
    'msi': 'Executables',
    'dmg': 'macOS Installers',
    'pkg': 'macOS Installers',
    'app': 'macOS App Files',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    'swift': 'Swift Files',
    'py': 'Python Files',
    'java': 'Java Files',
    'jar': 'Java Files',
    'crdownload': 'Unfinished Chrome Download',
    'xcodeproj': 'XCode Projects',
    'pptx': 'MS Powerpoint Files',
    'sln': 'Visual Studio Projects',
    'icns': 'App Icons',
    'ico': 'Windows App Icons',
    'psd': 'Photoshop Documents',
    'cmproj': 'Camtasia Projects',
    'mov': 'Videos',
    'heif': 'Images',
    'hevc': 'Images',
    'playground': 'Swift Files'
}

# Organize Files
def organize_files():
    try:
        path = askdirectory()
        files = os.listdir(path)

        for filename in files:
            file_extension = os.path.splitext(filename)[1][1:]

            if file_extension in file_extensions:
                source_file_path = os.path.join(path, filename)
                target_directory = os.path.join(path, file_extensions[file_extension])

                os.makedirs(target_directory, exist_ok=True)
                shutil.move(source_file_path, os.path.join(target_directory, filename))

        messagebox.showinfo("Success!", "Your files have been Organized!")
    except:
        messagebox.showinfo("Error!", "An unknown error has occured!")

# GUI Setup
window = Tk()

window.title("unResolvedOrganizer")
window.config(padx=25, pady=25)
window.resizable(False, False)

# Labels
app_name_label = Label(window, text="unResolvedOrganizer - WINDOWS PORT", font=('Areal', 25))
app_name_label.grid(row=0, column=0, sticky='w')

app_info_label = Label(window, text="unResolvedOrganizer is a free and open-source Mac that allows you to organize files!")
app_info_label.grid(row=1, column=0, sticky='w')

placeholder_label = Label(window, text="")
placeholder_label.grid(row=2, column=0)

github_label = Label(window, text="\nGitHub: https://github.com/KaungZinLin/unResolvedOrganizer")
github_label.grid(row=4, column=0, sticky='w')

copyright_label = Label(window, text="COPYRIGHT 2023 unResolved. DO NOT DISTRIBUTE!")
copyright_label.grid(row=5, column=0, sticky='w')

# Buttons
organize_button = Button(window, text="Click here to Organize Files", command=organize_files)
organize_button.grid(row=3, column=0, sticky='w')

# GUI Loop
window.mainloop()
