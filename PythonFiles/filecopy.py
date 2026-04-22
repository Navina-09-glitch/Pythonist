#Program for Copying the content of One File into Another File
#To copy,we need two files--source file and destination file
#source file must be opened in readmode
#filecopy.py
try:
    srcfile=input("Enter the source file name")
    with open(srcfile,"r") as rp: #here we are choosing the file ,rp means read pointer
        dstfile=input("Enter the destination file name")
        with open(dstfile,"a") as wp: #here we are choosing the destination file to write, wp means write pointer
            #Read the data from source file:
            srcdata=rp.read()
            #write the source file data to Destination file we can enter destination file as new file sample.data or already existing file. it will append the data withold file
            wp.write(srcdata)
            print("one file copied-verify")
except FileNotFoundError:
    print("source file doesn't exist")