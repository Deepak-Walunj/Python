# with open('readme.txt','r') as file:
#     print(file.read())
    
with open("new_file.txt",'w') as file:
    file.write("Hey there my anme is Deepak")

with open('new_file.txt','a') as file1:
    file1.write("\nNow we are appending a new line in the file")