# IMDb-Scrapper
The code will search your movies folder for all movies using list.py and then Movie_excel.py will store the Plot and IMDb rating of all the movies.

Required modules - 
import requests
import xlsxwriter
from bs4 import BeautifulSoup
import os
from fnmatch import fnmatch
Other requirements-
You need to specify the path of Movies folder in list.py and the name of excel sheet in Movie_excel.py
Keep both the files in same folder
