# Daemon Sample

一个Python远程守护程序示例，包含服务端和客户端实现。

## 功能概述

- **服务端** (`remote_daemon_example.py`):
  - 监听TCP端口(默认9999)
  - 处理三种类型的请求:
    - `status`: 获取服务状态
    - `execute`: 执行命令
    - `config`: 修改配置
  - 支持JSON格式的参数传递
  - 多线程处理并发请求
  - 优雅退出处理

- **客户端** (`remote_daemon_client.py`):
  - 演示如何发送不同类型的请求
  - 展示参数传递方式
  - 处理服务端响应

## 快速开始

1. 启动服务端:
   ```bash
   python3 remote_daemon_example.py
   ```

2. 运行客户端测试:
   ```bash
   python3 remote_daemon_client.py
   ```

## 扩展指南

1. 添加新的请求类型:
   - 在`RequestHandler`类中添加新的处理方法
   - 更新消息类型判断逻辑

2. 修改监听端口:
   - 修改`remote_daemon_example.py`中的`PORT`常量
   - 相应更新客户端连接端口

3. 增强安全性:
   - 添加认证机制
   - 实现SSL/TLS加密通信

## 文件结构

```
daemon_sample/
├── remote_daemon_example.py   # 服务端守护程序
├── remote_daemon_client.py    # 客户端示例
└── README.md                  # 项目说明
```

## 贡献

欢迎提交Pull Request或Issue报告问题。