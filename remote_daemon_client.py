"""
Python Remote Daemon Client Example
演示如何向远程守护程序发送不同消息请求的客户端
"""

import socket
import json
import time

def send_request(host, port, message_type, params=None):
    """发送请求到远程守护程序"""
    if params is None:
        params = {}
        
    # 创建请求数据
    request = {
        'type': message_type,
        'params': params
    }
    
    # 创建socket连接
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # 发送请求
        s.sendall(json.dumps(request).encode('utf-8'))
        
        # 接收响应
        response = s.recv(1024)
        return json.loads(response.decode('utf-8'))

if __name__ == "__main__":
    HOST = "localhost"  # 远程服务器地址
    PORT = 9999         # 守护程序端口
    
    # 1. 发送状态请求
    print("Sending status request...")
    status_response = send_request(HOST, PORT, 'status', {'detail': 'full'})
    print("Status Response:", status_response)
    
    # 2. 发送执行请求
    print("\nSending execute request...")
    execute_response = send_request(HOST, PORT, 'execute', {
        'command': 'process_data',
        'args': ['file1.txt', 'file2.txt'],
        'timeout': 60
    })
    print("Execute Response:", execute_response)
    
    # 3. 发送配置请求
    print("\nSending config request...")
    config_response = send_request(HOST, PORT, 'config', {
        'key': 'log_level',
        'value': 'debug'
    })
    print("Config Response:", config_response)
    
    # 4. 发送无效请求
    print("\nSending invalid request...")
    invalid_response = send_request(HOST, PORT, 'unknown_type')
    print("Invalid Response:", invalid_response)