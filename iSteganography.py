import os

os.system("color 6")
os.system("cls")

print('''
########    ######   #########   ########    ########
   ##       ##          ##       ##    ##    ##
   ##       ######      ##       ########    ##  ####
   ##           ##      ##       ##    ##    ##    ##
########    ######      ##       ##    ##    ########
''')
print("            The Ultimate Stagnography Tool\n")
# Speaking code start here
code= 'dim speechobject\n\
set speechobject=createobject("sapi.spvoice")\n\
Set speechobject.Voice = speechobject.GetVoices.Item(1)\n\
speechobject.Volume = 100\n'

code2= 'dim speechobject\n\
set speechobject=createobject("sapi.spvoice")\n\
Set speechobject.Voice = speechobject.GetVoices.Item(0)\n\
speechobject.Volume = 100\n'

def runner(ans, code):
    edt='speechobject.speak "'+ans+'"'

    cmd=(str(code) + str(edt))

    f = open("demo.vbs", "w")
    f.write(cmd)
    f.close()

    os.system("demo.vbs")
# speaking code end here


print("Stag - The Stegenography Script")
print("\t\tMade in Python")
print("-"*55)

define='Steganography is the practice of concealing a file,\nmessage, image, or video within another file, message,\nimage, or video. The word steganography comes from Greek\nsteganographia.'
print(define)
print("-"*55)

description='Description: Please make sure the following:\n\
    1. Note the file extension of your image\n\
    2. Make a RAR using (WinRAR) of your secret files\n\
    3. Make sure you have WinRAR installed on your System\n\
    4. Put the image and files in a same New Folder\n\
    5. Run the script in cmd\n\
    \nTroubleshoot:\n\
    If the script is not working then try to run the script with Administrator permission.'
print(description)


for i in range(1):
    runner("Enter Input Folder Path",code)
    inFolder=input("\nEnter The Path/of/Folder_Containg_Images_&_RAR/: ",)
    if inFolder=="":
        print("Invalid Path!")
        runner("Invalid Folder Path, Please Try Again", code)
        break

    runner("What's the Image Name",code)
    image=input("\nEnter The Name of Image File (eg. pic.jpeg): ")
    if image=="":
        print("Image File Name Missing!")
        runner("Image File Name is Empty, Please Try Again", code)
        break

    runner("What's the file name",code)
    rar=input("\nEnter The Name of RAR File (eg. secret.rar): ")
    if rar=="":
        print("RAR File Missing!")
        runner("RAR File Name is Empty, Please Try Again", code)
        break

    runner("enter destination folder path",code)
    outFolder=input("\nEnter The Path/of/Output_Folder/ (Press Enter For Same as Input): ")

    if outFolder=="":
        outFolder=inFolder

    for i in inFolder[-1]:
        if i !="\\":
            inFolder=inFolder+"\\"
            print(inFolder)

    for i in outFolder[-1]:
        if i !="\\":
            outFolder=outFolder+"\\"
            print(outFolder)

    cmd="copy /b "+inFolder+image+"+"+inFolder+rar+" "+outFolder+image+" > out.txt"
    
    os.system(cmd)

    def check():  
        predict='file(s) copied.'
        a=[]
        f = open("out.txt", "r+")
        for i in f:
            a=i

        if predict in a:
            os.system("cls")
            print("Yeah! We did it 😉")
            runner("Yeah! mission successful", code)
        else:
            os.system("cls")
            print("Error: Something went wrong 😢\nPlease Try Again")
            runner("Oops, Something Went Wrong.", code)
        f.close()
    check()

runner("Thanks for downloading my script",code2)
runner("MADE BY RK",code2)
