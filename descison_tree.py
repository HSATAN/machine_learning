# _*_ coding:utf-8 _*_
import math
import copy
from  data_util.data import *
test_data = test_data_3

DATA_LENTH = len(test_data)
if test_data:
    ATTRIBUTE_LIST = test_data[0].keys()
    ATTRIBUTE_LIST.remove('category')

print(ATTRIBUTE_LIST)

def get_property(data={}):
    property_category = {}
    for property in data.keys():
        property_category.setdefault()

def get_category(attribute_list=None, property=None):
    if property:
        total_property = {}
        for item in test_data:
            for property in attribute_list:
                total_property.setdefault(property, {})
                total_property[property].setdefault(item[property], {})

                total_property[property][item[property]].setdefault(item['category'], 0)
                total_property[property][item[property]][item['category']] += 1
        return total_property
    p = {}
    count = 0
    for item in test_data:
        count += 1
        p.setdefault(item['category'], 0)
        p[item['category']] += 1

    return p
def get_entropy(property=None):
    p = copy.deepcopy(property)
    if not p or not isinstance(p, dict):
        return
    count = .0
    for value in p.values():
        count += value
    if count == 0:
        return
    for key, value in p.items():
        temp = float(value / count)
        p[key] = -(temp * math.log(temp, 2))
    return sum(p.values())*(count/DATA_LENTH)

def get_info(data={}, property=None):
    if property:
        data = data[property]
        info_property = 0
        for property in data.values():
            resullt = get_entropy(property)
            info_property += resullt
        return info_property
    info = {}
    for key in data.keys():
        data_property = data[key]
        info_property = 0
        for property in data_property.values():
            resullt = get_entropy(property)
            info_property += resullt
        info[key] = info_property
    return info
total_probability = get_category(ATTRIBUTE_LIST)
print(total_probability)
total_info = get_entropy(total_probability)
print(total_info)
house_count = get_category(ATTRIBUTE_LIST, property=True)
print(house_count)

info = get_info(house_count)
print(info)

for key, value in info.items():
    info[key] = total_info - value
    print(total_info - value)
print info

def SplitInfo(data={}):
    splitinfo = {}
    for attribute, value in data.items():
        splitinfo.setdefault(attribute, 0)
        for key_temp, value_temp in value.items():
            count = sum(value_temp.values())
            splitinfo[attribute] += (-math.log(float(count)/DATA_LENTH, 2)*count/DATA_LENTH)

    return splitinfo

splitinfo = SplitInfo(house_count)

for key ,value in splitinfo.items():
    print info[key],value
    print '%s  = ' % key, info[key] / value
    print '%s  = '%key, round(info[key]/value,3)

