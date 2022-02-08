import imaplib
import email.header
import chardet

conn = imaplib.IMAP4_SSL(port=993, host='imap.qq.com')
print('已连接服务器')
conn.login('2748652229@qq.com', 'bdbaiwgnpgkjddde')
print('登录成功')

conn.select()

type, data = conn.search(None, 'ALL')

newlist = data[0].split()
type, data = conn.fetch(newlist[-4], '(RFC822)')
msg = email.message_from_string(data[0][1].decode('utf-8'))
sub = msg.get('subject')
subdecode,charset=email.header.decode_header(sub)[0]
if charset is not None:
    subdecode=subdecode.decode(charset)
print(subdecode)

for part in msg.walk():
    if not part.is_multipart():
        print(part.get_payload())
        print(part.get_payload(decode=True).decode("ISO-8859-1"))