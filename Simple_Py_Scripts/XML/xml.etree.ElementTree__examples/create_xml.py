#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://docs.python.org/3/library/xml.etree.elementtree.html

import io
import xml.etree.ElementTree as ET

from pretty_print import indent


root = ET.Element('data')

country = ET.Element('country', name="Liechtenstein")

rank = ET.Element('rank', updated="yes")
rank.text = '2'
country.append(rank)

year = ET.Element('year')
year.text = '2008'
country.append(year)

gdppc = ET.Element('gdppc')
gdppc.text = '141100'
country.append(gdppc)

country.append(ET.Element('neighbor', name="Austria", direction="E"))
country.append(ET.Element('neighbor', name="Switzerland", direction="W"))

root.append(country)

country = ET.Element('country', name="Singapore")
root.append(country)

...

indent(root)

xml_str = ET.tostring(root, encoding="utf-8", method="xml")
print(xml_str.decode(encoding="utf-8"))
# <data>
#   <country name="Liechtenstein">
#     <rank updated="yes">2</rank>
#     <year>2008</year>
#     <gdppc>141100</gdppc>
#     <neighbor direction="E" name="Austria" />
#     <neighbor direction="W" name="Switzerland" />
#   </country>
#   <country name="Singapore" />
# </data>

etree = ET.ElementTree(root)
f = io.BytesIO()
etree.write(f, encoding='utf-8', xml_declaration=True)
print(f.getvalue().decode(encoding="utf-8"))
# <?xml version='1.0' encoding='utf-8'?>
# <data>
#   <country name="Liechtenstein">
#     <rank updated="yes">2</rank>
#     <year>2008</year>
#     <gdppc>141100</gdppc>
#     <neighbor direction="E" name="Austria" />
#     <neighbor direction="W" name="Switzerland" />
#   </country>
#   <country name="Singapore" />
# </data>
