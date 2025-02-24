import asyncio
import base64
import json
import re
from tonutils.client import TonapiClient
from tonutils.wallet import WalletV5R1
from pytonapi import AsyncTonapi
import requests
from tgbot import config


# 创建 Session
session = requests.Session()
session.headers.update({'Cookie': config.cookies})


# 获取用户信息
async def huoquuser(username, months):
    url = f"https://fragment.com/api?hash={config.hash_value}"

    data = {
        "query": username,
        "months": months,
        "method": "searchPremiumGiftRecipient"
    }

    response = session.post(url, data=data)

    if response.status_code == 200:
        json_response = response.json()
        if json_response.get('ok', False):
            user_name = json_response['found'].get('name', "未知")
            recipient = json_response['found'].get('recipient', "未知")
            photo = json_response['found'].get('photo', "未知")

            # print(f"用户昵称：{user_name}")
            # print(f"唯一标识：{recipient}")
            return user_name, recipient, photo
        else:
            print("未找到用户信息")
            print(f"错误信息: {response.text}")
    else:
        print(f"请求失败，状态码: {response.status_code}")
        print(f"错误信息: {response.text}")


# 创建订单
async def dingdan(username, months):
    user_info = huoquuser(username, months)
    if not user_info:
        return None
    _, recipient, _ = await user_info

    url = f"https://fragment.com/api?hash={config.hash_value}"

    data = {
        "recipient": recipient,
        "months": months,
        "method": "initGiftPremiumRequest"
    }

    response = session.post(url, data=data)
    # print(response.json())
    if response.status_code == 200:
        json_response = response.json()
        if "req_id" in json_response:
            req_id = json_response["req_id"]
            amount = json_response["amount"]
            # print("reqID：", req_id)
            # print("开通金额：", amount)
            return req_id
        else:
            print("订单创建失败:", json_response)
    else:
        print(f"请求失败，状态码: {response.status_code}")
        print(f"错误信息: {response.text}")

    return None


# 确认订单
async def queren_dingdan(username: str, months: int):
    req_id = await dingdan(username, months)
    if not req_id:
        print("无法获取 req_id，终止流程。")
        return

    url = f"https://fragment.com/api?hash={config.hash_value}"

    data = {
        "transaction": 1,
        "id": req_id,
        "show_sender": 1,
        "method": "getGiftPremiumLink"
    }

    response = session.post(url, data=data)
    # print(response.json())
    # payload(req_id)
    if response.status_code == 200:
        json_response = response.json()
        # print("第三步", json_response)
        # 检查 'ok' 是否为 True
        if json_response.get("ok"):
            # print("执行下一步逻辑...")
            zhifu_amount = int(json_response['transaction']['messages'][0]['amount'])
            zhifu_dizhi = str(json_response['transaction']['messages'][0]['address'])
            zhifu_payload = str(json_response['transaction']['messages'][0]['payload'])
            if zhifu_dizhi == config.huiyuandizhi:
                # print("支付金额：", zhifu_amount)
                # print("支付地址：", zhifu_dizhi)
                # print("支付payload：", zhifu_payload)
                # 先补足 Base64 可能缺失的 `=` 进行解码
                padding = len(zhifu_payload) % 4
                if padding:
                    zhifu_payload += "=" * (4 - padding)
                # print(zhifu_payload)
                # Base64 解码
                jiema_dizhis = base64.b64decode(zhifu_payload)
                decoded_text = jiema_dizhis.decode("utf-8", errors="ignore")
                filtered_text = re.sub(r'[\x00-\x1F\x7F]', '', decoded_text)  # 过滤控制字符
                # print("过滤后的内容:", filtered_text)

                # 使用正则表达式匹配目标内容
                premium_match = re.search(r'Telegram Premium.*?\d+ (months|year)', filtered_text)
                ref_match = re.search(r'Ref#(\S+)', filtered_text)

                # 提取匹配的文本
                # if premium_match:
                    # print("Premium Text:", premium_match.group(0))
                # else:
                    # print("Premium Text: None")

                # if ref_match:
                    # print("Ref Code:", ref_match.group(1))
                # else:
                    # print("Ref Code: None")

                # 组合明文信息
                mingwen = f"{premium_match.group(0) if premium_match else ''} Ref#{ref_match.group(1) if ref_match else ''}"
                # print("明文信息:", mingwen)
                # print(f"支付地址：https://app.tonkeeper.com/transfer/{zhifu_dizhi}?amount={zhifu_amount}&bin={zhifu_payload}")
                print("-----执行支付-----")
                # result = await send_ton(req_id, zhifu_amount, zhifu_dizhi, mingwen)
                return result

    else:
        print(f"请求失败，状态码: {response.status_code}")
        print(f"错误信息: {response.text}")
