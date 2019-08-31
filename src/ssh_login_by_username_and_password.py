import paramiko

# 创建ssh连接对象
ssh_obj = paramiko.SSHClient()
# 允许连接不在know_hosts 文件中的主机
ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程服务器
ssh_obj.connect(hostname='localhost', port=22, username='root', password='123456',pkey=None, timeout=15)
# 执行命令
stdin, stdout, stderr = ssh_obj.exec_command('pwd', timeout=15)
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res.decode() if res else err.decode()
print(result)
ssh_obj.close()


