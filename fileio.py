# f=open("document.txt",'a')
# text="Hello, I am an enginering student"
# f.write(text)
# f.close()






# g=open("document.txt",'r')
# while True:
#     sc=g.readline()
#     if not sc:
#         print(type(sc))
#         break
#     print(sc)
# g.close()





f=open("document.txt",'r')
i=0
while True:
    
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(',')[0]
    m2=line.split(',')[1]
    m3=line.split(',')[2]

    print(f"Marks of student {i} in maths is {m1}")
    print(f"Marks of student {i} in sc is {m2}")
    print(f"Marks of student {i} in eng is {m3}")


# f.tell() tells us the current position of cursor in the file
    print(f.tell())



# f.seek(...) sets the position of cursor to that specified position

# f.truncate(...) cuts the length of the string entered to that particular value to enter it into the file



