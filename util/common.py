# _*_ coding:utf-8 _*_


def statistics_category(data={}, category='category'):

    """
    给定一个数据集，返回字典形式的每个类目的数目
    :param data:
    :param category:
    :return:
    """
    if not data:
        return None
    p = {}
    count = 0
    for item in data:
        count += 1
        p.setdefault(item[category], 0)
        p[item[category]] += 1
    return p, count


