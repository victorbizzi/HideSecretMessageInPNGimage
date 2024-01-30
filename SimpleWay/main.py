end_hex = b"\xfe\x35\x52\xa5\x4a\x27\x77\xa8\x15\xeb\xff\xd9"
#with open('imagedog.png', 'ab') as f:
#    f.write(b"Message")


with open('imagedog.png', 'rb') as f:
   content = f.read()
   offset = content.index(end_hex)
   f.seek(offset + len(end_hex))
   print(f.read())