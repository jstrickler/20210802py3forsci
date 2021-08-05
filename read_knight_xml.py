import lxml.etree as et

doc = et.parse('knights.xml')
print("doc: {}\n".format(doc))

root = doc.getroot()

print("root: {}\n".format(root))

for knight in root:  # iterate over children
    print(knight.get('name'))  # get XML attribute
print()

for knight in doc.findall('knight'):
    name = knight.get('name')
    title = knight.findtext('title')
    print(f"{title} {name}")
print()


for knight in doc.findall('knight'):   # doc.getroot().findall()
    name = knight.get('name')
    title = knight.findtext('title')
    print(f"{title} {name}")
print()

for knight in doc.findall('.//knight'):  # xpath
    name = knight.get('name')
    title = knight.findtext('title')
    comment = knight.findtext('comment')
    print(f"{title} {name} <<{comment}>>")
print()
