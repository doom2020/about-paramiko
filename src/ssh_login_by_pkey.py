import paramiko

"""
基于公钥的免密登陆
原理：
    1.本机生成公钥与私钥------》 命令 $ ssh-keygen
    2.将本机公钥发送给要远程的服务器(有几种方法,其一)------》 命令 $ ssh-copy-id root@127.0.0.1
    3.本机登陆远程服务器，服务器向本机发送随机字符串，本机接收并通过私钥加密，发送给远程服务器，
    远程服务器通过本机存储在服务器里的公钥进行解密，解密成功，则信任本机，可直接登陆无需密码
说明：
    本机公钥存储在远程服务器中的authorized_keys文件中
    远程服务器~/.ssh/known_hosts文件中存储着每个访问过服务器的计算机公钥（允许里面的计算机访问）
    可通过设置‘ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())’
"""

# 获取私钥
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
# 创建ssh连接对象
ssh_obj = paramiko.SSHClient()
# 允许不在known_hosts文件中的主机连接
ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 建立连接
ssh_obj.connect(hostname='127.0.0.1', port=22, username='root', pkey=private_key, timeout=15)
# 执行命令
stdin, stdout, stderr = ssh_obj.exec_command('pwd', timeout=15)
# 获取结果
res, err = stdout.read(), stderr.read()
result = res.decode() if res else err.decode()
print(result)
# 关闭连接
ssh_obj.close()

