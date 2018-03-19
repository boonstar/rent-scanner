import json
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# import utils_propertyguru
# import utils_iproperty


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

    
def set_query_iproperty(q="west coast"):
    dlink = "https://www.iproperty.com.sg/rent/private-apartment/?q={}".format(q)
    
    # call firefox for answer
    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Firefox(capabilities=caps)
    driver.get(dlink)
    
    property_list = []
    selector = "li[class^=rent-]"
    
    while not property_list:
        property_list = driver.find_elements_by_css_selector(selector)
    # driver.quit() # cannot close here. close after scrape
    
    return q, property_list, driver

    
def set_query_propertyguru(q="west coast"):
    q = q.replace(' ', '+')
    dlink = "https://www.propertyguru.com.sg/singapore-property-listing/property-for-rent?market=residential&property_type_code%5B%5D=CONDO&property_type_code%5B%5D=APT&property_type_code%5B%5D=WALK&property_type_code%5B%5D=CLUS&property_type_code%5B%5D=EXCON&property_type=N&freetext={}".format(q)
    
    # call firefox for answer

    driver = webdriver.Firefox()
    driver.get(dlink)
    
    property_list = []
    selector = "li[class^=listing-item]"
    
    while not property_list:
        property_list = driver.find_elements_by_css_selector(selector)
        
    # driver.quit() # cannot close here. close after scrape
    
    return q, property_list, driver
    

    
    
# # TODO: only works for iproperty now.
# def scrape(search="west coast"):
#     q, property_list, driver = set_query_iproperty(search)
#     data_iproperty = {}
# 
#     q = q.replace(' ', '-')
# 
#     for i in range(len(property_list)):
#         print("The ith in property_list: {}".format(i))
#         data_iproperty[q + '_' + str(i)] = {}
#         data_iproperty[q + '_' + str(i)]['link'] = utils_iproperty.get_link(property_list[i])
#         data_iproperty[q + '_' + str(i)]['rent'] = utils_iproperty.get_rent(property_list[i])
#         data_iproperty[q + '_' + str(i)]['area'] = utils_iproperty.get_area(property_list[i])
# 
#     # save answer
#     save_obj(data_iproperty, "data_iproperty")
# 
#     driver.quit()
# 
# 
#     # load answer and print
#     try:
#         data_iproperty = load_obj("data_iproperty")
#         print(json.dumps(data_iproperty, indent=4))
#     except:
#         print('pickle is empty')
####################################################################


if __name__ == "__main__":
    # scrape("kallang")
    q, xx, driver = set_query_propertyguru()

    print(xx)
