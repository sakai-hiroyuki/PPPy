import re


def name_decomposition(name: str):
    d = dict()
    label = re.findall('\A[^<]+', name)[0]
    d['label'] = label
    params = re.findall('<[a-z]+=[a-z]+>', name)
    for param in params:
        p = re.findall('[a-z]+', param)
        d[p[0]] = p[1]

    return d
