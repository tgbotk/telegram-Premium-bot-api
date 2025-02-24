async def kkkkkkk():
    # 🚀 你的 TonAPI API Key（从 https://tonconsole.com 获取）
    api_key = "AELZK********************MNNH64XV5KKW74NIQ"

    tonapi = AsyncTonapi(api_key=api_key)
    haxi = await tonapi.blockchain.get_transaction_data("319e88fbf36bec9**************b718c4fae35698be38ae575b8ee278898")
    # 判断交易是否成功
    if is_transaction_successful(haxi):
        print("交易成功！")
    else:
        print("交易失败！")

# 🚀 运行异步任务
if __name__ == "__main__":
    asyncio.run(kkkkkkk())
