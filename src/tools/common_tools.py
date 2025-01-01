def get_yahoo_code(stock_code):
    """
    根据 A 股代码自动识别并返回 Yahoo Finance 格式的代码
    :param stock_code: A 股代码（字符串或数字）
    :return: Yahoo Finance 格式的代码
    
    规则：
    - 以 6/5 开头的为上交所，添加 .SS 后缀
    - 以 0/1/2/3 开头的为深交所，添加 .SZ 后缀
    """
    # 将代码转换为字符串并去除空格
    stock_code = str(stock_code).strip()
    
    # 检查代码长度是否为 6 位
    if len(stock_code) != 6:
        return stock_code
    
    # 上海证券交易所
    if stock_code.startswith(('5', '6')):
        return f"{stock_code}.SS"
    # 深圳证券交易所
    elif stock_code.startswith(('0', '1', '2', '3')):
        return f"{stock_code}.SZ"
    else:
        raise ValueError(f"无法识别的交易所代码: {stock_code}")

def get_currency_symbol(ticker):
    """
    根据股票代码判断对应的货币单位
    """
    # 美股
    if "." not in ticker:
        return "USD"
    # 港股
    elif ticker.endswith(".HK"):
        return "HKD"
    # A股
    elif ticker.endswith(".SS") or ticker.endswith(".SZ"):
        return "CNY"
    # 台股
    elif ticker.endswith(".TW"):
        return "TWD"
    # 其他市场可以继续添加
    else:
        return None
    