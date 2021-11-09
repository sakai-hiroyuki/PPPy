import re
from typing import Dict, List


def header_decomposition(header: List[str]) -> List[dict]:
    '''
    Decompose the header and return the List of the dictionaries.
    The decomposition is::

        string<key1=value1><key2=value2>
        -> {'label': 'string', 'key1': 'value1', 'key2': 'value2'}
    
    The key of the string not in <> is 'label'.
    Meanwhile the string inside <>, the part before '=' is the key,
    and the part after '=' is the value.
    
    Parameters
    ----------
    header : List[str]
        Header to decompose.
    
    Returns
    -------
    info : List[dict]
        List of the decomposed header.

    Examples
    --------
    >>> h = [AAA<V=W><X=Y>,BBB<X=Z>]
    >>> info = header_decomposition(h)
    >>> info
    [{'label': 'AAA', 'V': 'W', 'X': 'Y'}, {'label': 'BBB', 'X': 'Z'}]
    '''
    info : List[dict] = []
    for name in header:
        d : Dict[str, str] = dict()
        label = re.findall('\A[^<]+', name)[0]
        d['label'] = label
        params : List[str] = re.findall('<[a-z]+=[a-z]+>', name)
        for param in params:
            p : List[str] = re.findall('[a-z]+', param)
            d[p[0]] = p[1]
    
        info.append(d)

    return info
