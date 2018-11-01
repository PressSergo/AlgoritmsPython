import xml.etree.ElementTree as etree
tree = etree.parse("/Users/sergei/Library/Preferences/PyCharm2018.2/scratches/scratch.xml")
root = tree.getroot()
print root
for i in root:
    print str(i.tag) + str(i.attrib) + str(i.text)
k = root.findall('{Basense}Putin')
print k