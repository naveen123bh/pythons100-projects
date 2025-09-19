import hashlib
from difflib import SequenceMatcher

def hash_file(filename1, filename2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()
    with open(filename1, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            h1.update(chunk)
        while chunk != b'':
            chunk = f.read(1024)
            h2.update(chunk)
        return h1.hexdigest(), h2.hexdigest()

msg1,msg2 = hash_file('C:\\Users\\ABC\\Downloads\\lefl113.pdf', 'C:\\Users\\ABC\\Downloads\\Who_Am_I_English.pdf')
if(msg1 != msg2):
    print("Files are different")
else:
    print("Files are the same")
    