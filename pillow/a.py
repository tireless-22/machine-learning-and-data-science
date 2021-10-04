from PIL import Image
import os
# for f in os.listdir("."):
# 	if f.endswith(".jpeg"):
# 		print(f)

size_300={300,300}



# for f in os.listdir("."):
# 	if f.endswith(".jpeg"):
# 		i=Image.open(f)
# 		fn,fext=os.path.splitext(f)
# 		print(fn)
# 		print(fext)
# 		i.save("pngs/{}.png".format(fn))

		
for f in os.listdir("."):
	if f.endswith(".jpeg"):
		i=Image.open(f)
		fn,fext=os.path.splitext(f)
		# print(fn)
		# print(fext)
		# i.thumbnail(size_300)
		i.save("size300/{}_300".format(fn,fext))


image1=Image.open("11.png")
# to open the file
# image1.show()
# to show the file 
# image1.save("11.jpeg")
# to save the file in different formats










