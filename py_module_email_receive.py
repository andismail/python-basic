import poplib
from email.header import decode_header
from email.parser import Parser


def decode_str(s):
    if not s:
        return None
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)# value.decode(charset, 'ignore') 有时有decode异常，可以用ignore
    return value


def receive(email_name):
    send_address = 'sender_address@gmail.com'
    send_password = 'sender_password'
    receive_server = 'imap.exmail.qq.com'

    # 连接到邮箱
    server = poplib.POP3(receive_server)
    server.user(send_address)
    server.pass_(send_password)

    # 获得邮件
    messages = [server.retr(i) for i in range(1, len(server.list()[1]) + 1)]
    messages = [b'\r\n'.join(msg[1]).decode() for msg in messages]# .decode('utf-8', 'ignore') 有时会decode异常，可以这样处理
    messages = [Parser().parsestr(msg) for msg in messages]
    messages = messages[::-1]

    for msg in messages:
        subject = decode_str(msg.get('Subject'))
        if subject != email_name: continue

        for part in msg.walk():
            file_name = decode_str(part.get_filename())
            if not file_name: continue

            # 保存EXCEL
            with open('~/Desktop/' + file_name, 'wb') as f:
                data = part.get_payload(decode=True)
                f.write(data)
    server.quit()

# receive('BI_report-钱帮催收数据-2017-04-25')
