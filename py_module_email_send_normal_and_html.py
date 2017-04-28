import smtplib
from datetime import datetime as _datetime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

# 发送普通文本邮件和Html格式邮件
# MIMEText _subtype 参数设置成plain(默认)就是普通文本邮件
def send():
    html_email_content = '<p>数据处理成功，若有问题请及时联系。</p><p>出催：91 件</p><p>入催：27 件</p>'

    # 发送服务器：smtp.exmail.qq.com(使用SSL)
    send_server = 'smtp.exmail.qq.com'

    # 发件人
    send_address = 'sender_address@gmail.com'
    send_password = 'sender_password'

    # 收件人
    to_me = 'me@163.com'

    email_obj = MIMEText(html_email_content, _subtype='html', _charset='utf-8')# _subtype默认是plain
    email_obj['From'] = formataddr(('张三', send_address))
    email_obj['To'] = formataddr(('李四', to_me))
    email_obj['Subject'] = Header('闪银PayDay每日数据处理结果' + _datetime.now().date().strftime('%Y-%m-%d'), 'utf-8')

    server = smtplib.SMTP(send_server, 25)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(send_address, send_password)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(send_address, [to_me, ], email_obj.as_string())  # 括号中对应的是发件人邮箱账号

    server.quit()  # 关闭连接
