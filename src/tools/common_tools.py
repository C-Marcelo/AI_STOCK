def get_yahoo_code(stock_code):
    """
    根据 A 股代码自动识别并返回 Yahoo Finance 格式的代码
    :param stock_code: A 股代码（字符串或数字）
    :return: Yahoo Finance 格式的代码（如 "600519.SS"）
    """
    # 将代码转换为字符串并去除空格
    stock_code = str(stock_code).strip()
    
    # 检查代码长度是否为 6 位
    if len(stock_code) == 6:
         # 根据代码开头判断交易所
        if stock_code.startswith(('6', '5')):  # 上海证券交易所
            return f"{stock_code}.SS"
        elif stock_code.startswith(('0', '2', '3')):  # 深圳证券交易所
            return f"{stock_code}.SZ"
        else:
            raise ValueError("可能是无法识别的 A 股代码，请确认")
    else:
        return stock_code
