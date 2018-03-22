import re

def preprocess(txt):
    return re.sub(r'(?<=sqft).*', '', txt)
    
    
    

def get_link(i):
    return i.find_element_by_css_selector('a').get_attribute('href')

    
def get_rent(i):
    txt = preprocess(i.text)
    # print('\n\n' + txt + '\n\n')
    try:
        rent = re.search('(?<=\$\s)\d+[\,\.]?\d*', txt).group(0)
        rent = float(rent.replace(',', ''))
        return rent
        
    except:
        print('perhaps rent value does not exist')

        
def get_area(i):
    try:
        area = re.search('\d+[\,\.]?(?=\ssqft)', i.text).group(0)
        area = float(area.replace(',', ''))
        return area
    except:
        print('perhaps area value does not exist')

        
def get_location(i):
    txt = i.text.split('\n')
    if txt[0] == 'FEATURED AGENT':
        return txt[1]
    else:
        return txt[0]
    # try:
    #     location = re.search('(.*?)\\n', i.text).group(0)
    #     return location
    # except:
    #     print('perhaps location value does not exist')
        
    
    
xx = "Woodsvale\nFully Furnished Condominium\n1 Woodlands Drive 72\n1292 sqft · Ready to move\n3 2\nS$ 2,600 / mo\nMessage\nAlex Chia 12 hours"

location = re.search('(.*?)\\n', xx).group(0)
print(location)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# test