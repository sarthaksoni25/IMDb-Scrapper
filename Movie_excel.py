from list import *
import requests
import xlsxwriter
from bs4 import BeautifulSoup

def find_title(soup):
    title = soup.find('title')
    return title.get_text()



def plot(soup):
    try:
        plot = soup.find('div', class_='inline canwrap')
        return plot.get_text()
    except:
        return "Plot not available"


def duration(soup):
    try:
        t = soup.find('time')
        return t.get_text().strip()
    except:
        return "Duration not available"


def imdb(soup):
    try:
        imdb = soup.find('div',class_='ratingValue')
        return imdb.get_text()
    except :
        return "IMDb not available"
def votes(soup):
    try:
        votes = soup.find('span',class_='small')
        return 'Number of votes -', votes.get_text()
    except:
        return "Votes not available"


workbook = xlsxwriter.Workbook('listofmovies.xlsx')#Name of excel file is listofmovies change according to your needs
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})
worksheet.write('A1', 'Title', bold)
worksheet.write('B1', 'Duration', bold)
worksheet.write('C1', 'Plot', bold)
worksheet.write('D1', 'IMDb', bold)
worksheet.set_column(0,0,60 )
worksheet.set_column(2,2,150)


row = 1
col = 0

worksheet.set_default_row(80)
format = workbook.add_format()
format.set_align('justify')
for name in listofmovies:
    print name

    research_later = name + "imdb"
    goog_search = "https://www.google.co.in/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
    r = requests.get(goog_search)
    soup = BeautifulSoup(r.text, "html.parser")
    link =  soup.find('cite').text
    try:
        page = requests.get("http://" + str(link))
        soup = BeautifulSoup(page.content, 'html.parser')
        t = find_title(soup)
        d = duration(soup)
        p = plot(soup).strip()
        i = imdb(soup)
        v = votes(soup)
        worksheet.write(row, col,t)
        worksheet.write(row, col + 1,d)
        worksheet.write(row, col + 2, p, format)
        worksheet.write(row, col + 3,i)
        #worksheet.write(row, col + 4,votes)
        #worksheet.write(row, col + 5,title)
        soup = ''
        row = row + 1
    except:
        print "Information Not Available"
