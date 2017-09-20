# _*_ coding:utf-8 _*_

from util.common import statistics_category
from data_util.data import test_data_3 as test_data


class Bayes(object):

    def __init__(self):
        pass

    def get_category(self):

        return statistics_category(test_data)

    def get_p(self, count=0, category={}):
        p = {}
        if count == 0:
            return
        for key, value in category.items():
            p.setdefault(key, .0)
            p[key] = value/float(count)
        return p

    def statistics_condition_p(attribute_list=None, property=None, data={}):
        if property:
            total_property = {}
            for item in data:
                for property in attribute_list:
                    total_property.setdefault(property, {})
                    total_property[property].setdefault(item[property], {})

                    total_property[property][item[property]].setdefault(item['category'], 0)
                    total_property[property][item[property]][item['category']] += 1
            return total_property
        p = {}
        count = 0
        for item in data:
            count += 1
            p.setdefault(item['category'], 0)
            p[item['category']] += 1

        return p

bayes = Bayes()
p, count = bayes.get_category()
print(p)
print(count)
p_total = bayes.get_p(count, p)
print(p_total)