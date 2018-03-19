import datetime
import json
import numpy as np
import re
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


###############################################################################
# functions
def save_obj(obj, name):
    directory = 'obj'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open('obj/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def get_link(i):
    return i.find_element_by_css_selector('a').get_attribute('href')

def get_rent(i):
    try:
        rent = re.search('(?<=SGD\s)\d+[\,\.]?\d*', i.text).group(0)
        rent = float(rent.replace(',',''))
        return rent
        
    except:
        print('perhaps rent value does not exist')

def get_area(i):
    try:
        area = re.search('(\d+\,?\d*)\ssq', i.text).group(1)
        area = float(area.replace(',',''))
        return area
    except:
        print('perhaps area value does not exist')
    
def set_query(q="west coast"):
    dlink = "https://www.iproperty.com.sg/rent/private-apartment/?q={}".format(q)
    
    # call firefox for answer
    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Firefox(capabilities=caps)
    driver.get(dlink)
    
    selector = "li[class^=rent-]"
    property_list = driver.find_elements_by_css_selector(selector)
    # driver.quit() # cannot close here. close after scrape
    
    return q, property_list, driver
    
def scrape(search="west coast"):
    q, property_list, driver = set_query(search)
    data_iproperty = {}
    q = q.replace(' ', '-')
    
    # import pdb; pdb.set_trace()
    
    for i in range(len(property_list)):
        print("The ith in property_list: {}".format(i))
        data_iproperty[q + '_' + str(i)] = {}
        data_iproperty[q + '_' + str(i)]['link'] = get_link(property_list[i])
        data_iproperty[q + '_' + str(i)]['rent'] = get_rent(property_list[i])
        data_iproperty[q + '_' + str(i)]['area'] = get_area(property_list[i])
        
        

    # save answer
    save_obj(data_iproperty, "data_iproperty")
    
    driver.quit()
    

    # load answer and print
    try:
        data_iproperty = load_obj("data_iproperty")
        print(json.dumps(data_iproperty, indent=4))
    except:
        print('pickle is empty')

####################################################################

if __name__ == "__main__":
    scrape("kallang")