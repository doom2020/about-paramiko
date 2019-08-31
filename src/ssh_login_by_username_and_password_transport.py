import paramiko

#实例化一个transport 对象
transport_obj = paramiko.Transport(('127.0.0.1', 22))
# 建立连接
transport_obj.connect(username='root', password='123456')
# 创建ssh对象
ssh_obj = paramiko.SSHClient()
# 将ssh_obj transport 指定为transport_obj
ssh_obj._transport = transport_obj
# 执行命令
stdin, stdout, stderr = ssh_obj.exec_command('pwd', timeout=15)
#获取结果
res, err = stdout.read(), stderr.read()
result = res.decode() if res else err.decode()
print(result)
# 关闭连接
transport_obj.close()


