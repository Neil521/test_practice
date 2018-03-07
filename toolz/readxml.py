#coding utf-8
from lxml import etree

import json
import csv
with open(r'D:\abcd\toolz\myxml.xml') as xml:
    x=xml.read().replace('encoding="gbk"','encoding="utf-8"')

# get bbox
print(x)
for event,element in etree.iterparse(BytesIO(x.encode('utf-8'))):

