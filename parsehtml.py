from pyquery import PyQuery as pq
import re
def parseHtml(html):
    try:
        title = re.findall('<title>(.+信用卡)', html)[0]
        if title:
            print(title)
            return title
    except Exception as e:
        return e
    # res = pq(html)
    # fromName = res('#tipFromAddr_readmail').text()
    # print(fromName)
    # if '光大银行信用卡' in html:
    #     print('找到光大的账单')
    #     date = re.findall('\((\d{4}年\d{2})', html)[0]
    #     print(date)
    #     num = re.findall('￥(\d{1,3},\d{3})',html)
    #     zong = num[0]
    #     yinghuan = num[1]
    #     zuidi = num[2]
    #     print(num)
    #     res = {
    #         'from':fromName,
    #         'month':date,
    #         'zong':zong,
    #         'yinghuan':yinghuan,
    #         'zuidi':zuidi
    #     }
    #     print(res)
    # elif '中信银行信用卡' in html:
    #     print('找到中心的账单')
    #     date = re.findall('(\d{4}年\d{2})月账单', html)[0]
    #     print(date)
    #     # <font face="华文细黑" style="font-size:16px;line-height:120%;">1,456.47</font>
    #     num = re.findall('(\d{1,3}?,?\d{1,3}\.\d{2})</font>', html)
    #     print(num)
    #     # zong = num[0]
    #     # yinghuan = num[1]
    #     # zuidi = num[2]
    #     # res = {
    #     #   : fromName,
    #     #     'month': date,
    #     #     'zong': zong,
    #     #     'yinghuan': yinghuan,
    #     #     'zuidi': zuidi
    #     # }
