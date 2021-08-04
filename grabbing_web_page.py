import requests
from zipfile import ZipFile

scipy_url = "https://www.python.org/"

response = requests.get(scipy_url)

if response.status_code == requests.codes.OK:
    page_source = response.text
    print(response.text[:1000])
print('-' * 60)

python_doc_url = "https://docs.python.org/3/archives/python-3.9.6-docs-pdf-letter.zip"

response = requests.get(python_doc_url)
if response.status_code == requests.codes.OK:
    with open('pydocs.zip', 'wb') as pydocs_out:
        pydocs_out.write(response.content)
    pyzip = ZipFile('pydocs.zip')
    for member in pyzip.namelist():
        print(member)

    pyzip.extract('docs-pdf/whatsnew.pdf')

