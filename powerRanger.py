from bs4 import BeautifulSoup
import requests
import csv

# from website
url = 'https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

data = y.find_all('tbody')[1]
nama = data.find_all('i')

tgl1 = data.find_all('span', class_='bday dtstart published updated')
tgl11 = data.find_all('tr')[31]
tgl12 = tgl11.find_all('td')[4]

tgl2 = data.find_all('span', class_='dtend')
tgl21 = data.find_all('tr')[30]
tgl22 = tgl21.find_all('td')[4]
tgl23 = data.find_all('tr')[31]
tgl24 = tgl23.find_all('td')[5]

lnama = []
for i in nama:
    lnama.append(i.text)

# tgl riris
lrilis =[]
for i in tgl1:
    lrilis.append(i.text)
lrilis.pop(1)
lrilis.pop(1)
lrilis.append(tgl12.text.replace('\n',''))

# akhir rilis
lakhir = []
for i in tgl2:
    lakhir.append(i.text)
lakhir.pop(1)
lakhir.pop(1)
lakhir.append(tgl22.text.replace('[3]','').replace('\n',''))
lakhir.append(tgl24.text.replace('\n',''))


print(len(lnama))
print(len(lrilis))
print(len(lakhir))


csvData =[['Judul','Tayang','Berakhir']]
for i in range(len(lnama)):
    l1 = lnama[i]
    l2 = lrilis[i]
    l3 = lakhir[i]
    hasil = list((l1,l2,l3))
    csvData.append(hasil)

# print(csvData)
with open('powerRanger.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=';')
    writer.writerows(csvData)

csvFile.close()