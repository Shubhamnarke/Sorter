import os
import shutil

path = os.path.expanduser("C:/Users/PISTON/lock/")


worked = os.listdir(path)
folder_name = ['image','files',"pdf","audio","video","others","app","zip"]

for x in range(0,8):
    if not os.path.exists(path + folder_name[x]):
        os.mkdir(path + folder_name[x])


for file in worked:


    #for img separating.

    if ".jpg" in file and not os.path.exists(path + 'image/' + file):
        shutil.move(path + file, path + 'image/'+file)
    elif ".png" in file and not os.path.exists(path + 'image/' + file):
        shutil.move(path + file, path + 'image/'+file)
    elif ".bmp" in file and not os.path.exists(path + 'image/' + file):
        shutil.move(path + file, path + 'image/'+file)
    elif ".jpeg" in file and not os.path.exists(path + 'image/' + file):
        shutil.move(path + file, path + 'image/'+file)
    elif ".psd" in file and not os.path.exists(path + 'image/' + file):
        shutil.move(path + file, path + 'image/'+file)

    #for files separating

    elif ".txt" in file and not os.path.exists(path + 'files/' + file):
        shutil.move(path + file, path + 'files/'+ file )
    elif ".doc" in file and not os.path.exists(path + 'files/' + file):
        shutil.move(path + file, path + 'files/'+ file )
    elif ".docx" in file and not os.path.exists(path + 'files/' + file):
        shutil.move(path + file, path + 'files/'+ file )
    elif ".odt" in file and not os.path.exists(path + 'files/' + file):
        shutil.move(path + file, path + 'files/'+ file )
    elif ".wps" in file and not os.path.exists(path + 'files/' + file):
        shutil.move(path + file, path + 'files/'+ file )
    elif ".wpd" in file and not os.path.exists(path + 'files/' + file):
        shutil.move(path + file, path + 'files/'+ file )

    # for pdf separating
    elif ".pdf" in file and not os.path.exists(path + 'pdf/' + file):
        shutil.move(path + file, path + 'pdf/'+ file )

    #for audio file separating
    elif ".mp3" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, new + 'audio/'+file)
    elif ".wav" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".ogg" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".gsm" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".dct" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".flac" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".au" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".aeliff" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".vox" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)
    elif ".row" in file and not os.path.exists(path + 'audio/' + file):
        shutil.move(path + file, path + 'audio/'+file)

    #for video separating.
    elif ".mp4" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".mkv" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".3gp" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".avi" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".flv" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".mov" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".mpg" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".mpeg" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".wmv" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)
    elif ".AVI" in file and not os.path.exists(path + 'video/' + file):
        shutil.move(path + file, path + 'video/'+file)

    #for executable files.
    elif ".exe" in file and not os.path.exists(path + 'app/' + file):
        shutil.move(path + file, path + 'app/'+file)


    # for zip file separating.
    elif ".zip" in file and not os.path.exists(path + 'zip/' + file):
        shutil.move(path + file, path + 'zip/'+file)

    else:
        shutil.move(path + file, path + 'others/' + file)


















