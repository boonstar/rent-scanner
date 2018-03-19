import re

def preprocess(txt):
    return re.sub(r'(?<=sqft).*', '', txt)
    
    
    

def get_link(i):
    return i.find_element_by_css_selector('a').get_attribute('href')

    
def get_rent(i):
    txt = preprocess(i.text)
    print('\n\n' + txt + '\n\n')
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

        
if __name__ == "__main__":
    raw_text ="""Changi Court
Fully Furnished Condominium
698-708 Upper Changi Road East
1162 sqft · S$ 2.15 psf
3 3
S$ 2,500 / mo
Message
Mostapha Kamal 3 days
"""

    print(raw_text)
    print('#####################################')
    print(re.sub(r'(?<=sqft).*','bbbbbbbbbbbbbbbbbbbbb', raw_text))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# test