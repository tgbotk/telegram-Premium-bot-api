# Telegram24小时自助开通会员机器人 bot

# 项目简介

开发人员： https://t.me/kdawang

演示机器人 ： https://t.me/ruankebot

这是一个基于 Go语言 和 python 的 Telegram自助开通会员机器人，支持24小时自动处理会员开通流程。用户通过 USDT 进行支付，机器人自动验证支付并开通会员服务。系统采用 Redis 用于缓存和会话管理，MySQL 存储用户数据和交易记录。

# 功能特点
![image](https://github.com/user-attachments/assets/9b5632f1-576e-4fbb-88cb-7c3655d2fbfb)

![image](https://github.com/user-attachments/assets/770e5e03-c324-4e96-bd2e-1eaf79995e73)

![image](https://github.com/user-attachments/assets/407e4300-6a52-4d14-89a1-1ae23c93fed2)


24小时自动开通会员：用户通过支付USDT，系统会自动检测到账情况，并开通会员服务。

支付网关：使用 Go语言 开发的支付网关处理所有的支付请求，确保支付验证的安全性和准确性。

自动化流程：用户支付后，机器人会自动检测支付情况，进行开通会员操作，并向用户发送确认消息。

MySQL数据库管理：使用 MySQL 数据库存储用户数据、订单信息和支付记录。

Redis缓存管理：使用 Redis 缓存会话和用户状态信息，提高系统性能。

# 项目架构

支付网关：基于Go语言的支付接口，支持USDT支付的接收和验证。

Telegram机器人：基于 Pyrogram 库开发的Telegram机器人，用于与用户交互，处理命令和支付信息。

数据库：使用 MySQL 存储用户信息、订单记录以及交易状态。

缓存系统：使用 Redis 管理用户会话状态，提高系统的响应速度。

# 技术栈

Go语言：用于开发支付网关，处理支付验证和与外部API的交互。

python：用于开发Telegram机器人，处理机器人命令和用户交互。

Redis：用于缓存用户状态和会话信息，提高响应速度。

MySQL：用于存储用户数据、订单记录以及支付相关信息。

# 使用说明

## 环境准备

安装 Go、Python 和 MySQL。

安装 Redis 用于缓存管理。

配置 .env 文件，设置所需的API密钥、数据库连接信息和Telegram机器人令牌。

## 安装依赖

### 在Go项目中，运行以下命令安装所需依赖：

go mod tidy

### 在Python项目中，运行以下命令安装依赖：

pip install -r requirements.txt

## 配置文件

Go语言部分：在Go项目根目录下创建 .env 文件，配置API密钥、回调地址、支付网关相关信息。

Python部分：在Python项目根目录下创建 .env 文件，配置Telegram机器人令牌和其他所需的环境变量。

## 启动项目

启动 Go支付网关：

go run main.go

启动 Pyrogram Telegram机器人：

python bot.py

# 系统工作流程

用户在Telegram中通过机器人发送支付请求。

用户支付USDT后，支付网关会回调机器人，验证支付状态。

如果支付成功，机器人会更新数据库中的订单状态，并为用户开通会员。

机器人会向用户发送开通成功消息，并通知管理员。


## 请确保你的API密钥和支付网关相关信息存放在 .env 文件中，并且不要公开这些文件。

对于敏感信息（如用户数据和支付记录），请确保采取适当的加密和安全措施。

# 常见问题

Q: 支付后没有收到开通会员消息怎么办？

A: 请检查支付网关和机器人日志，确保支付信息已经被正确处理。如果仍然有问题，请联系管理员。

Q: 如何增加新的支付方式？

A: 可以在Go语言部分的支付网关中增加新的支付方式处理逻辑，修改相应的支付验证和回调接口。
