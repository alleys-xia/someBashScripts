#这条命令会将 pip 的全局代理设置为本地（127.0.0.1，即 localhost）的 8800 端口。设置后，pip 在下载和安装 Python 包时会通过这个代理服务器进行网络连接。
pip config set global.proxy http://127.0.0.1:8800