#import camelot by installing the following in your terminal :
# pip install tk
#pip install ghostscript
#pip install camelot-py

import camelot
tables = camelot.read_pdf("foo.pdf",pages='1')
print(tables)

#to convert and store in CSV file

tables.export('foo.csv',compress=True)

