#-*- coding:utf-8 -*-
# @Author : Target
# @Date :2023-7-30
# @Function: get_ip_city

import sys
import asyncio
import aiohttp


# 获取IP所在地址信息及运营商
async def get_ip_city(ip) :
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    params = {
        'ip': ip
    }
    url = 'https://api.vore.top/api/IPdata'
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers, params=params, timeout=10) as response:
            if response != None :
                res_json = await response.json()
                if 'adcode' not in res_json :
                    print(ip + ' 该IP格式有误,错误代码： ' + str(res_json['code'])+' '+ res_json['msg'])
                else:
                    ip_info = res_json['adcode']['o']
                    print(ip + '\t地址信息：' + ip_info)

def get_help():
    print('\n参数有误,查询单个IP格式：python get_ip_info.py 127.0.0.1')
    print('查询多个IP格式：python get_ip_info.py 127.0.0.1,202.96.134.122')


if __name__ == '__main__' :
    tasks = []
    if len(sys.argv[0:]) != 2:
        get_help()
        quit()
    else:
        print('\r\n查询结果\r\n-------------------------------------------------------------------')
        try:
            ip = sys.argv[1]
            if ',' in ip:
                ips = ip.split(',')
                for ip in ips:
                    c = get_ip_city(ip)
                    task = asyncio.ensure_future(c)
                    tasks.append(task)
            else:
                c = get_ip_city(ip)
                task = asyncio.ensure_future(c)
                tasks.append(task)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))
        except:
            print('\n'+ip + '该IP有误')
            get_help()
