import paramiko

# 获取私钥
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
# 实例化transport对象
transport_obj = paramiko.Transport(('127.0.0.1', 22))
# 建立连接
transport_obj.connect(username='root', pkey=private_key)
# 创建ssh对象
ssh_obj = paramiko.SSHClient()
# 指定 ssh_obj的transport 为 transport_obj
ssh_obj._transport = transport_obj
# 执行命令
stdin, stdout, stderr = ssh_obj.exec_command('pwd', timeout=15)
# 获取结果
res, err = stdout.read(), stderr.read()
result = res.decode() if res else err.decode()
print(result)
# 关闭连接
ssh_obj.close()
