#Program for copying an image
#Imagecopy.py #image files are binary files
try:
    with open("E:\comsys experiments\pyt.jpg","rb") as rp: #even you can copy videos by mentioning rb only which means readbinary it wont work if you put only read , rp is read pointer
        with open ("btechexp.jpg","wb") as wp:#even you can putcopied videos by mentioning wb only which means writebinary it wont work if you put only write , wp is write pointer i
            imgdata=rp.read()
            wp.write(imgdata)
            print("Image copied-verify")
except FileNotFoundError:
    print("Source image does not exist")