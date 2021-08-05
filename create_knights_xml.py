import lxml.etree as et
# import xml.etree.ElementTree as et

root = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_element = et.SubElement(root, "knight", name=name)
        title_element = et.SubElement(knight_element, 'title')
        title_element.text = title
        et.SubElement(knight_element, 'color').text = color
        et.SubElement(knight_element, 'quest').text = quest
        et.SubElement(knight_element, 'comment').text = comment

print(
    et.tostring(
        root,
        xml_declaration=True,
        pretty_print=True
    ).decode()
)

doc = et.ElementTree(root)
print(doc)
doc.write('knights.xml', pretty_print=True, xml_declaration=True)
