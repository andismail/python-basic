import smtplib
from datetime import datetime as _datetime
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


# 发带附件的邮件
def send():
    # 发件人
    send_address = 'sender_address@gmail.com'
    send_password = 'sender_password'

    # 发送服务器：smtp.exmail.qq.com(使用SSL)
    send_server = 'smtp.exmail.qq.com'

    # 收件人
    to_me = 'me@163.com'

    email_obj = MIMEMultipart()
    email_obj['From'] = formataddr(('张三', send_address))
    email_obj['To'] = formataddr(('李四', to_me))
    email_obj['Subject'] = Header('扯皮专用图片' + _datetime.now().date().strftime('%Y-%m-%d'), 'utf-8')  # 邮件标题

    email_obj.attach(MIMEText('测试发送带附件邮件_扯皮专用', 'plain', 'utf-8'))  # 邮件正文内容

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('~/Desktop/WX20170428-102853@2x.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='WX20170428-102853@2x.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='扯皮专用.png')  # 中文名会乱码
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        email_obj.attach(mime)

    server = smtplib.SMTP(send_server, 25)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(send_address, send_password)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(send_address, [to_me, ], email_obj.as_string())  # 括号中对应的是发件人邮箱账号

    server.quit()  # 关闭连接

# 注：具体实现不太清楚，如encode
