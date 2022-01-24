import re


def H2M(text):
    # 剪切头尾
    pattern1 = r'<tr.*?>.*</tr>'
    result = re.search(pattern1, text)
    # 分割row
    # TODO
    pattern2 = r'<tr.*?>.*?</tr>'
    # b="adbc<tr class=b><td></td></tr>hhhyfda<tr class=a>fag</tr>ee<tr>bb</tr>"
