import re


def get_link(i):
    return i.find_element_by_css_selector('a').get_attribute('href')

    
def get_rent(i):
    try:
        rent = re.search('(?<=SGD\s)\d+[\,\.]?\d*', i.text).group(0)
        rent = float(rent.replace(',', ''))
        return rent
        
    except:
        print('perhaps rent value does not exist')

        
def get_area(i):
    try:
        area = re.search('(\d+\,?\d*)\ssq', i.text).group(1)
        area = float(area.replace(',', ''))
        return area
    except:
        print('perhaps area value does not exist')
        
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
    
def get_location(i):
    txt = i.text.split('\n')
    if hasNumbers(txt[5]):
        return txt[6]
    else:
        return txt[5]
            
xx = "16\nEric Tay - ORANGETEE & TIE PTE LTD\nPosted today 12:15 AM\nSave\nSGD 3,000\n(Price PSF SGD 4.89)\nThe Nexus\nBukit Timah Road\nCondominium\nBuilt-up : 613 sq. ft.\n1\n1"
xx = xx.split('\n')
for i in xx:
    print(i)
