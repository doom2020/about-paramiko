import paramiko

__author__ = 'doom'

class ConnectionBySSH:
    def __init__(self,hostname,port,username,password,pkey_file,timeout):
        self._hostname = hostname
        self._port = port
        self._username = username
        self._password = password
        self._pkey_file = pkey_file
        # 设置超时时间(ssh连接使用,命令执行使用)
        self._timeout = timeout
        # 创建ssh对象
        self._client = paramiko.SSHClient()
        # 设置known_hosts中不存在host也允许连接
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 实例化transport对象
        self._transport = paramiko.Transport((self._hostname, self._port))

    def _connect_by_password(self):
        # 建立连接
        self._client.connect(hostname=self._hostname, port=self._port, username=self._username\
                            , password=self._password, timeout=self._timeout)


    def _connect_by_pkey(self):
        # 建立连接
        _private_key = paramiko.RSAKey.from_private_key_file(self._pkey_file)
        self._client.connect(hostname=self._hostname, port=self._port, username=self._username\
                             , pkey=_private_key)

    def _use_transport_by_password(self):
        # 建立连接
        self._transport.connect(username=self._username, password=self._password)
        # 指定ssh对象的transport为self._transport
        self._client._transport = self._transport

    def _use_transport_by_pkey(self):
        # 建立连接
        _private_key = paramiko.RSAKey.from_private_key_file(self._pkey_file)
        self._transport.connect(username=self._username, pkey=_private_key)
        # 指定ssh对象的transport为self._transport
        self._client._transport = self._transport

    def _execute_command(self, cmd):
        stdin, stdout, stderr = self._client.exec_command(cmd, timeout=self._timeout)
        res, err = stdout.read(), stderr.read()
        result = res.decode() if res else err.decode()
        # print(result)
        return result

    def _close_connect(self):
        if self._client:
            self._client.close()

