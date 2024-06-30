from zipfile import *
f = ZipFile('images.zip', 'w', ZIP_DEFLATED)

f.write('c++.png')
f.write('download.png')
f.write('csharp.png')
f.write('javascrpit.png')

f.close()
