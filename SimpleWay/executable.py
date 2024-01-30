end_hex = b"\xfe\x35\x52\xa5\x4a\x27\x77\xa8\x15\xeb\xff\xd9"
#First insert the executable inside the image

#with open('ExecutableBATimagedog.png', 'ab') as f, open('message.bat', 'rb') as e:
#    f.write(e.read())


#Then
with open('ExecutableBATimagedog.png', 'rb') as f:
    content = f.read()
    offset = content.index(end_hex)
    f.seek(offset + len(end_hex))

    with open ('newmessage.exe', 'wb') as e:
        e.write(f.read())
