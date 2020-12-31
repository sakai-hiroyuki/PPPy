import re
from typing import List


def header_decomposition(header: List[str]) -> List[dict]:
    info = []
    for name in header:
        d = dict()
        label = re.findall('\A[^<]+', name)[0]
        d['label'] = label
        params = re.findall('<[a-z]+=[a-z]+>', name)
        for param in params:
            p = re.findall('[a-z]+', param)
            d[p[0]] = p[1]
    
        info.append(d)

    return info
