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
        q = {}
        if count == 0:
            return
        for key, value in category.items():
            q.setdefault(key, .0)
            q[key] = value/float(count)
        return q

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
            result.setdefault(category_key, {})
            for category, value in category_value.items():
                if category != 'category':
                    result[category_key].setdefault(category, {})
                for key, count in value.items():
                    if category == 'category':
                        continue
                    print('P(%s = %s|category=%s) = %s' %(category,key,category_key,float(count)/category_count))
                    result[category_key][category][key] = float(count)/category_count
        return result

    @classmethod
    def classify(cls, result={}, record={}):

        """
        返回类

        :param result:
        :param record:
        :return:
        """
        p = {}
        for category, item in result.items():
            p.setdefault(category, 0)
            for key, value in record.items():
                if p[category] == 0:
                    p[category] = item[key][value]
                else:
                    p[category] *= item[key][value]

        return p
        pass
bayes = Bayes()
pro, count = bayes.get_category()
print(pro)
p_total = bayes.get_p(count, pro)
print(p_total)
data = bayes.statistics_condition_p(data=test_data)
result = bayes.calculate(data)
X = {'age': 'y', 'income': 'm', 'student': 'y', 'credit_rating': 'f'}
final_p = bayes.classify(result, X)

final = {}
for key, value in final_p.items():
    final[key] = value*p_total[key]
