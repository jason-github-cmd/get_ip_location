# get_ip_location
用于批量获取IP位置信息

使用方法：

查询单个IP格式：python get_ip_info.py 127.0.0.1'

查询多个IP格式：python get_ip_info.py 127.0.0.1,202.96.134.122'

注意：采用异步协程的方法加快批量查询，导致入参ip的顺序与返回的结果的顺序会不一致。
