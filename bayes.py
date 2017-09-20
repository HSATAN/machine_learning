# _*_ coding:utf-8 _*_

from util.common import statistics_category
from data_util.data import test_data_3 as test_data


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
                total_property.setdefault(category, {})
                total_property[category].setdefault(property, {})
                total_property[property].setdefault(item[property], {})

                total_property[property][item[property]].setdefault(item['category'], 0)
                total_property[property][item[property]][item['category']] += 1
        return total_property

bayes = Bayes()
p, count = bayes.get_category()
print(p)
print(count)
p_total = bayes.get_p(count, p)
print(p_total)
print(bayes.statistics_condition_p(test_data))