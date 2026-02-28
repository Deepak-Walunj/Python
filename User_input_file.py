file_name=input('Enter file name in .txt extension\n')

while True:
    act=input("What action would you like to perform?\nw)Write a new file\na)Append to existing file\nd)Show the file\ns)Stop\n").lower()
    if act=='s':
        break
    if act=='d':
        with open(file_name,'r') as file:
            print("\n"+file.read())
            continue
    if act not in ['a','w','d','s']:
        print("Enter a valid option (a,w,d,s)")
        continue
    else:
        mode='w' if act=='w' else 'a'
        content=input("Write the content of file\n")
        with open(file_name,mode) as file:
            file.write(content+'\n')
            
    t=input("Do you want to see your file (y/n)\n").lower()
    if t=='y':
        with open(file_name,'r') as file:
            print(file.read())
    elif t=='n':
            print("Ok not displaying your file...")
    else:
        print('Invalid option. Enter (y/n)')