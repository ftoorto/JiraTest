import imaplib
import email.header
import chardet

conn = imaplib.IMAP4_SSL(port=993, host='imap.qq.com')
print('已连接服务器')
conn.login('2748652229@qq.com', '#TODO')
print('登录成功')

conn.select()

type, data = conn.search(None, 'qq')

newlist = data[0].split()
type, data = conn.fetch(newlist[-3], '(RFC822)')
msg = email.message_from_string(data[0][1].decode('utf-8'))
sub = msg.get('subject')
subdecode=email.header.decode_header(sub)[0][0]
result=chardet.detect(subdecode)
print(result)
print(subdecode.decode('GB2312'))

for part in msg.walk():
    if not part.is_multipart():
        print(part.get_payload(decode=True).decode('GB2312'))