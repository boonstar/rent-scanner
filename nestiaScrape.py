import requests
import json
import csv
import logging
import os
import time
import sys
import traceback
from gdriveUpload import uploadSpreadsheet
LOG_FILENAME = 'log.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
start = time.time()
# Reloading decoding to accept utf-8 characters
reload(sys)
sys.setdefaultencoding('utf-8')
# Output file name
fileName = 'properties.csv'
# List for ID's to check if they already exist output
list = []
# Checking if output already exist, if NO - Create, if YES - skip and append new values
if os.path.isfile(fileName):
    print 'Result file already exist'
    with open(fileName) as f:
        # Adding all ids from existing output to place holder
        list = [row.split(',')[1].replace('"', '') for row in f]
else:
    print 'Creating result file'
    with open(fileName, 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # Writing headers to newly created output file
        wr.writerow((
            'url',
            'id',
            'propertyLeaseId',
            'name',
            'street',
            'block',
            'propertyTypeName',
            'propertyTypeCode',
            'rentalTypeName',
            'rentalTypeCode',
            'bedroomNumberName',
            'bedroomNumberCode',
            'bathroomNumberName',
            'bathroomNumberCode',
            'roomTypeName',
            'roomTypeCode',
            'bathroomTypeName',
            'bathroomTypeCode',
            'price',
            'ImageURL1',
            'ImageURL2',
            'ImageURL3',
            'ImageURL4',
            'ImageURL5',
            'isLike',
            'tags',
            'subDistrictId',
            'latitude',
            'longitude',
            'projectId',
            'isRecommendAgent',
            'date'
        ))

# Appending result row
def save_csv(mainData,url):
    with open(fileName, 'a') as myfile:
        try:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=",", lineterminator="\n")
            wr.writerow(mainData)
        except:
            print traceback.print_exc()
            logging.debug('Error while adding new line: '+str(url))
            print

# Link to API. Can bechanged by prefrence and search criterias
api = 'https://property.nestia.com/webapi/property/rentals?sort=1&propertyType=2%2C3&rentalType=2&limit=100000&offset=0&layer=0'
data = requests.get(api)
dataJson = json.loads(data.content)
n = 0
uniq = 0
for property in dataJson['properties']:
    try:
        id = dataJson['properties'][n]['id']
        url = 'https://property.nestia.com/rental/detail/' + str(id)
    except:
        id = ''
        url =''
    #     Checking if id is already in output. If not, adding it and other values.
    if str(id) not in list:
        uniq +=1
        try:
            propertyLeaseId = dataJson['properties'][n]['propertyLeaseId']
        except:
            propertyLeaseId = ''
        try:
            name = dataJson['properties'][n]['name'].replace(',',';')
        except:
            name = ''
        try:
            street = dataJson['properties'][n]['street'].replace(',',';')
        except:
            street = ''
        try:
            block = dataJson['properties'][n]['block'].replace(',',';')
        except:
            block = ''
        try:
            propertyTypeName = dataJson['properties'][n]['propertyType']['name']
        except:
            propertyTypeName = ''
        try:
            propertyTypeCode = dataJson['properties'][n]['propertyType']['code']
        except:
            propertyTypeCode = ''
        try:
            rentalTypeName = dataJson['properties'][n]['rentalType']['name']
        except:
            rentalTypeName = ''
        try:
            rentalTypeCode = dataJson['properties'][n]['rentalType']['code']
        except:
            rentalTypeCode = ''
        try:
            bedroomNumberName = dataJson['properties'][n]['bedroomNumber']['name']
        except:
            bedroomNumberName = ''
        try:
            bedroomNumberCode = dataJson['properties'][n]['bedroomNumber']['code']
        except:
            bedroomNumberCode = ''
        try:
            bathroomNumberName = dataJson['properties'][n]['bathroomNumber']['name']
        except:
            bathroomNumberName = ''
        try:
            bathroomNumberCode = dataJson['properties'][n]['bathroomNumber']['code']
        except:
            bathroomNumberCode = ''
        try:
            roomTypeName = dataJson['properties'][n]['roomType']['name']
        except:
            roomTypeName = ''
        try:
            roomTypeCode = dataJson['properties'][n]['roomType']['code']
        except:
            roomTypeCode = ''
        try:
            bathroomTypeName = dataJson['properties'][n]['bathroomType']['name']
        except:
            bathroomTypeName = ''
        try:
            bathroomTypeCode = dataJson['properties'][n]['bathroomType']['code']
        except:
            bathroomTypeCode = ''
        try:
            price = dataJson['properties'][n]['price']
        except:
            price = ''
        try:
            ImageURL1 = dataJson['properties'][n]['images'][0]['path']
        except:
            ImageURL1 = ''
        try:
            ImageURL2 = dataJson['properties'][n]['images'][1]['path']
        except:
            ImageURL2 = ''
        try:
            ImageURL3 = dataJson['properties'][n]['images'][2]['path']
        except:
            ImageURL3 = ''
        try:
            ImageURL4 = dataJson['properties'][n]['images'][3]['path']
        except:
            ImageURL4 = ''
        try:
            ImageURL5 = dataJson['properties'][n]['images'][4]['path']
        except:
            ImageURL5 = ''
        try:
            isLike = dataJson['properties'][n]['isLike']
        except:
            isLike = ''
        try:
            tags = '; '.join(dataJson['properties'][n]['tags'])
        except:
            tags = ''
        try:
            subDistrictId = dataJson['properties'][n]['subDistrictId']
        except:
            subDistrictId = ''
        try:
            latitude = dataJson['properties'][n]['latitude']
        except:
            latitude = ''
        try:
            longitude = dataJson['properties'][n]['longitude']
        except:
            longitude = ''
        try:
            projectId = dataJson['properties'][n]['projectId']
        except:
            projectId = ''
        try:
            isRecommendAgent = dataJson['properties'][n]['isRecommendAgent']
        except:
            isRecommendAgent = ''
        date = (time.strftime("%d/%m/%Y")) +' '+ (time.strftime("%H:%M:%S"))
        # Forming variable for output line
        mainData = (
        url,id, propertyLeaseId, name, street, block, propertyTypeName, propertyTypeCode, rentalTypeName, rentalTypeCode,
        bedroomNumberName, bedroomNumberCode, bathroomNumberName, bathroomNumberCode, roomTypeName, roomTypeCode,
        bathroomTypeName, bathroomTypeCode, price, ImageURL1,ImageURL2,ImageURL3,ImageURL4,ImageURL5, isLike, tags, subDistrictId, latitude, longitude, projectId,
        isRecommendAgent,date)
        # Calling function save_csv to append new line to output file.
        save_csv(mainData,url)
    n += 1
# Logging successful run
logging.debug('Scrapped without Errors. Api: '+api+' DATE: '+ (time.strftime("%d/%m/%Y")) +' '+ (time.strftime("%H:%M:%S")) + ' Results: '+ str(n) + ' Unique: '+str(uniq))
# Calling uploadSpreadsheet function from gdriveUpload.py to update spreadsheet in google drive
uploadSpreadsheet(fileName)


end = time.time()
print(end - start)
