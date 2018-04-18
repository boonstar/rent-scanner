import requests
import json
import csv
import os
import time
import sys
from .models import NestiaEstate


# Output file name
fileName = 'properties.csv'
# List for ID's to check if they already exist output
list = []
# Checking if output already exist, if NO - Create, if YES - skip and append new values
if os.path.isfile(fileName):
    print('Result file already exist')
    with open(fileName) as f:
        # Adding all ids from existing output to place holder
        list = [row.split(',')[1].replace('"', '') for row in f]
else:
    print('Creating result file')
    with open(fileName, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        # Writing headers to newly created output file
        wr.writerow((
            'url',
            'nestiaId',
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
            print(traceback.print_exc())
            logging.debug('Error while adding new line: '+str(url))
            print()
            
            
def test(qns):
    print('testing')
    nest = NestiaEstate()
    nest.name = qns
    nest.save()

            
def scrape(qns):
    # Link to API. Can bechanged by prefrence and search criterias
    api = 'https://property.nestia.com/webapi/property/rentals?sort=1&propertyType=2%2C3&rentalType=2&limit=100000&offset=0&layer=0'
    data = requests.get(api)
    dataJson = json.loads(data.content)
    n = 0
    uniq = 0

    nest = NestiaEstate() # Initialize model
    for property in dataJson['properties']:
        try:
            id = dataJson['properties'][n]['id']
            nest.id = dataJson['properties'][n]['id']
            url = 'https://property.nestia.com/rental/detail/' + str(id)
            nest.url = 'https://property.nestia.com/rental/detail/' + str(id)
            print(nest.url)
            nest.save()
        except:
            id = ''
            nest.id = ''
            url =''
            nest.url =''
        #     Checking if id is already in output. If not, adding it and other values.
        if str(id) not in list:
            uniq +=1
            try:
                propertyLeaseId = dataJson['properties'][n]['propertyLeaseId']
                nest.propertyLeaseId = dataJson['properties'][n]['propertyLeaseId']
            except:
                propertyLeaseId = ''
                nest.propertyLeaseId = ''
            try:
                name = dataJson['properties'][n]['name'].replace(',',';')
                nest.name = dataJson['properties'][n]['name'].replace(',',';')
            except:
                name = ''
                nest.name = ''
            try:
                street = dataJson['properties'][n]['street'].replace(',',';')
                nest.street = dataJson['properties'][n]['street'].replace(',',';')
            except:
                street = ''
                nest.street = ''
            try:
                block = dataJson['properties'][n]['block'].replace(',',';')
                nest.block = dataJson['properties'][n]['block'].replace(',',';')
            except:
                block = ''
                nest.block = ''
            try:
                propertyTypeName = dataJson['properties'][n]['propertyType']['name']
                nest.propertyTypeName = dataJson['properties'][n]['propertyType']['name']
            except:
                propertyTypeName = ''
                nest.propertyTypeName = ''
            try:
                propertyTypeCode = dataJson['properties'][n]['propertyType']['code']
                nest.propertyTypeCode = dataJson['properties'][n]['propertyType']['code']
            except:
                propertyTypeCode = ''
                nest.propertyTypeCode = ''
            try:
                rentalTypeName = dataJson['properties'][n]['rentalType']['name']
                nest.rentalTypeName = dataJson['properties'][n]['rentalType']['name']
            except:
                rentalTypeName = ''
                nest.rentalTypeName = ''
            try:
                rentalTypeCode = dataJson['properties'][n]['rentalType']['code']
                nest.rentalTypeCode = dataJson['properties'][n]['rentalType']['code']
            except:
                rentalTypeCode = ''
                nest.rentalTypeCode = ''
            try:
                bedroomNumberName = dataJson['properties'][n]['bedroomNumber']['name']
                nest.bedroomNumberName = dataJson['properties'][n]['bedroomNumber']['name']
            except:
                bedroomNumberName = ''
                nest.bedroomNumberName = ''
            try:
                bedroomNumberCode = dataJson['properties'][n]['bedroomNumber']['code']
                nest.bedroomNumberCode = dataJson['properties'][n]['bedroomNumber']['code']
            except:
                bedroomNumberCode = ''
                nest.bedroomNumberCode = ''
            try:
                bathroomNumberName = dataJson['properties'][n]['bathroomNumber']['name']
                nest.bathroomNumberName = dataJson['properties'][n]['bathroomNumber']['name']
            except:
                bathroomNumberName = ''
                nest.bathroomNumberName = ''
            try:
                bathroomNumberCode = dataJson['properties'][n]['bathroomNumber']['code']
                nest.bathroomNumberCode = dataJson['properties'][n]['bathroomNumber']['code']
            except:
                bathroomNumberCode = ''
                nest.bathroomNumberCode = ''
            try:
                roomTypeName = dataJson['properties'][n]['roomType']['name']
                nest.roomTypeName = dataJson['properties'][n]['roomType']['name']
            except:
                roomTypeName = ''
                nest.roomTypeName = ''
            try:
                roomTypeCode = dataJson['properties'][n]['roomType']['code']
                nest.roomTypeCode = dataJson['properties'][n]['roomType']['code']
            except:
                roomTypeCode = ''
                nest.roomTypeCode = ''
            try:
                bathroomTypeName = dataJson['properties'][n]['bathroomType']['name']
                nest.bathroomTypeName = dataJson['properties'][n]['bathroomType']['name']
            except:
                bathroomTypeName = ''
                nest.bathroomTypeName = ''
            try:
                bathroomTypeCode = dataJson['properties'][n]['bathroomType']['code']
                nest.bathroomTypeCode = dataJson['properties'][n]['bathroomType']['code']
            except:
                bathroomTypeCode = ''
                nest.bathroomTypeCode = ''
            try:
                price = dataJson['properties'][n]['price']
                nest.price = dataJson['properties'][n]['price']
            except:
                price = ''
                nest.price = ''
            try:
                ImageURL1 = dataJson['properties'][n]['images'][0]['path']
                nest.ImageURL1 = dataJson['properties'][n]['images'][0]['path']
            except:
                ImageURL1 = ''
                nest.ImageURL1 = ''
            try:
                ImageURL2 = dataJson['properties'][n]['images'][1]['path']
                nest.ImageURL2 = dataJson['properties'][n]['images'][1]['path']
            except:
                ImageURL2 = ''
                nest.ImageURL2 = ''
            try:
                ImageURL3 = dataJson['properties'][n]['images'][2]['path']
                nest.ImageURL3 = dataJson['properties'][n]['images'][2]['path']
            except:
                ImageURL3 = ''
                nest.ImageURL3 = ''
            try:
                ImageURL4 = dataJson['properties'][n]['images'][3]['path']
                nest.ImageURL4 = dataJson['properties'][n]['images'][3]['path']
            except:
                ImageURL4 = ''
                nest.ImageURL4 = ''
            try:
                ImageURL5 = dataJson['properties'][n]['images'][4]['path']
                nest.ImageURL5 = dataJson['properties'][n]['images'][4]['path']
            except:
                ImageURL5 = ''
                nest.ImageURL5 = ''
            try:
                isLike = dataJson['properties'][n]['isLike']
                nest.isLike = dataJson['properties'][n]['isLike']
            except:
                isLike = ''
                nest.isLike = ''
            try:
                tags = '; '.join(dataJson['properties'][n]['tags'])
                nest.tags = '; '.join(dataJson['properties'][n]['tags'])
            except:
                tags = ''
                nest.tags = ''
            try:
                subDistrictId = dataJson['properties'][n]['subDistrictId']
                nest.subDistrictId = dataJson['properties'][n]['subDistrictId']
            except:
                subDistrictId = ''
                nest.subDistrictId = ''
            try:
                latitude = dataJson['properties'][n]['latitude']
                nest.latitude = dataJson['properties'][n]['latitude']
            except:
                latitude = ''
                nest.latitude = ''
            try:
                longitude = dataJson['properties'][n]['longitude']
                nest.longitude = dataJson['properties'][n]['longitude']
            except:
                longitude = ''
                nest.longitude = ''
            try:
                projectId = dataJson['properties'][n]['projectId']
                nest.projectId = dataJson['properties'][n]['projectId']
            except:
                projectId = ''
                nest.projectId = ''
            try:
                isRecommendAgent = dataJson['properties'][n]['isRecommendAgent']
                nest.isRecommendAgent = dataJson['properties'][n]['isRecommendAgent']
            except:
                isRecommendAgent = ''
                nest.isRecommendAgent = ''
            date = (time.strftime("%d/%m/%Y")) +' '+ (time.strftime("%H:%M:%S"))
            
            nest.save()
            # Forming variable for output line
            mainData = (
            url,id, propertyLeaseId, name, street, block, propertyTypeName, propertyTypeCode, rentalTypeName, rentalTypeCode,
            bedroomNumberName, bedroomNumberCode, bathroomNumberName, bathroomNumberCode, roomTypeName, roomTypeCode,
            bathroomTypeName, bathroomTypeCode, price, ImageURL1,ImageURL2,ImageURL3,ImageURL4,ImageURL5, isLike, tags, subDistrictId, latitude, longitude, projectId,
            isRecommendAgent,date)
            # Calling function save_csv to append new line to output file.
            save_csv(mainData,url)
        n += 1