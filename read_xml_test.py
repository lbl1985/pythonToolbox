import xml.etree.ElementTree as ET

def printChild(obj):
	for child in obj:
		print child.tag, child.text

tree = ET.parse("country_data.xml")
root = tree.getroot()
print root.tag
print root.attrib
for child in root:
	print child.tag, child.text, child.attrib

print root[1][1].text

# for neighbor in root.iter('neighbor'):
# 	print neighbor.attrib

for country in root.findall('country'):
	rank = country.find('rank').text
	name = country.get('name')
	print name, rank