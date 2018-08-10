'''THIS CODE IS FOR COPYING THE FILE FROM GIVEN DIRECTORY TO GIVEN LOCATION '''
#THIS CODE WILL WORK FOR TEXT FILE ONLY...
#NO SUPPORT FOR .JPG OR .MP4 EXTENSIONS

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
