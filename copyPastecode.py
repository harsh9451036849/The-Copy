'''THIS CODE IS FOR COPING THE FILE FROM GIVEN DIRECTORY TO GIVEN LOCATION '''

f = open(input("provide the name and path of file from where you want to copy file : "))
g = open(input("provide the name and path of file  where you want to paste file : "), "w") 
s = f.readlines()
for x in s:
	print(x)
	g.write(x)
	
g.close()
f.close()
print ("\nFILE HAS BEEN COPIED\n")
print ("--------------------------")
