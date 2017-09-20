# _*_ coding:utf-8 _*_

from util.common import statistics_category
from data_util.data import test_data_3 as test_data
import copy

class Bayes(object):

    def __init__(self):
        pass
    @classmethod
    def get_category(cls):

        return statistics_category(test_data)

    @classmethod
    def get_p(cls, count=0, category={}):
        p = {}
        if count == 0:
            return
        for key, value in category.items():
            p.setdefault(key, .0)
            p[key] = value/float(count)
        return p

    @classmethod
    def statistics_condition_p(cls, attribute_list=None, data={}, category=None):

        total_property = {}
        if not category:
            category = 'category'
        for item in data:
            for property in item.keys():
                total_property.setdefault(item[category], {})
                total_property[item[category]].setdefault(property, {})
                total_property[item[category]][property].setdefault(item[property], 0)

                total_property[item[category]][property][item[property]] += 1
        return total_property
    @classmethod
    def calculate(cls, count_p={}):
        result = {}
        p = copy.deepcopy(count_p)
        for category_key, category_value in p.items():
            category_count = sum(category_value['category'].values())
            for category, value in category_value.items():
                for key, count in value.items():
                    if key == 'category':
                        return
                    print('P(%s = %s|category=%s) = %s' %(category,key,category_key,count/category_count))
bayes = Bayes()
p, count = bayes.get_category()
print(p)
print(count)
p_total = bayes.get_p(count, p)
print(p_total)
data = bayes.statistics_condition_p(data=test_data)
bayes.calculate(data)