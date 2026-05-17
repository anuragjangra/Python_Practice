import os

def organise_files(files,ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)

    if not(os.path.exists("Organised_files")):
        os.mkdir("Organised_files")
    
    for i, file in enumerate(files_with_ext):
        os.rename(file,f"Organised_files/photo-{i}{ext}")

if __name__ == "__file_organiser__":
    files = os.listdir()
    organise_files(files,".jpg")
        