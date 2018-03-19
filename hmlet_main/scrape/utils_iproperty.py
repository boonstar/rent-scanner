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
