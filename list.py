import os
from fnmatch import fnmatch

root = "/media/sarthak/Windows/Movies"#Path of your movies folder
listofpattern = ["*.mp4",".avi",".mkv"]
listofmovies = []

for path, subdirs, files in os.walk(root):
    for name in files:
    	for pattern in listofpattern:
        	if fnmatch(name, pattern):
        		listofmovies.append(os.path.join(name))
