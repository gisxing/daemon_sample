"""
Python Remote Daemon Example
可以在远程服务器上运行并根据不同消息请求进行分支处理的守护程序
"""

import socketserver
import json
import signal
import sys
import time
from threading import Thread

class RequestHandler(socketserver.BaseRequestHandler):
    """处理来自客户端的请求"""
    
    def handle(self):
        try:
            # 接收客户端数据
            raw_data = self.request.recv(1024).strip()
            data = json.loads(raw_data.decode('utf-8'))
            
            # 获取消息类型和参数
            msg_type = data.get('type')
            params = data.get('params', {})
            
            # 根据消息类型路由处理
            if msg_type == 'status':
                response = self.handle_status(params)
            elif msg_type == 'execute':
                response = self.handle_execute(params)
            elif msg_type == 'config':
                response = self.handle_config(params)
            else:
                response = {'error': 'Unknown message type'}
                
            # 发送响应
            self.request.sendall(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            self.request.sendall(json.dumps({'error': str(e)}).encode('utf-8'))

    def handle_status(self, params):
        """处理状态请求"""
        return {
            'status': 'running',
            'uptime': time.time() - server.start_time,
            'params_received': params
        }

    def handle_execute(self, params):
        """处理执行请求"""
        command = params.get('command')
        if not command:
            return {'error': 'No command specified'}
            
        # 这里应该是实际执行命令的逻辑
        # 示例仅返回接收到的命令
        return {
            'executed': command,
            'params': params,
            'result': 'simulated_execution'
        }

    def handle_config(self, params):
        """处理配置请求"""
        if 'key' not in params or 'value' not in params:
            return {'error': 'Missing key or value'}
            
        # 这里应该是实际修改配置的逻辑
        # 示例仅返回新的配置
        return {
            'config_updated': params['key'],
            'new_value': params['value']
        }

class DaemonServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """多线程TCP服务器"""
    daemon_threads = True
    allow_reuse_address = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = time.time()

def run_server():
    """启动服务器"""
    HOST, PORT = "0.0.0.0", 9999
    
    with DaemonServer((HOST, PORT), RequestHandler) as server:
        print(f"Daemon running on {HOST}:{PORT}")
        
        # 处理优雅退出
        def signal_handler(sig, frame):
            print("\nShutting down server...")
            server.shutdown()
            sys.exit(0)
            
        signal.signal(signal.SIGINT, signal_handler)
        server.serve_forever()

if __name__ == "__main__":
    print("Starting remote daemon...")
    run_server()