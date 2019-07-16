#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'yooongchun'

import sys
import importlib

importlib.reload(sys)
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

from translation.translation import *

'''
解析pdf文件，获取文件中包含的各种对象
'''


def changePdfToText(filePath, fileName):
    file = open(filePath, 'rb')  # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    praser = PDFParser(file)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)
    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()
    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    # 创建PDf 资源管理器 来管理共享资源
    rsrcmgr = PDFResourceManager()
    # 创建一个PDF设备对象
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pdfStr = ''
    dict = {}
    # 循环遍历列表，每次处理一个page的内容
    for inx, page in enumerate(doc.get_pages()):  # doc.get_pages()         获取page列表
        if 1 <= inx < 10:
            continue

        if inx > 12:
            break
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        for x in layout:
            if hasattr(x, "get_text"):
                before = x.get_text()  # type:str
                before = before.replace('\n', '')
                text = tran(before)
                dict[before] = text
                ret = before + ':' + text + '\n'
                print(ret)
                with open(fileName + '.txt', mode='a', encoding='utf-8') as f:
                    f.write(ret)

        # break
        # with open(fileName + '.txt', 'wb') as f:
        #     for key, value in dict.items():
        #         ret = key + ':' + value + '\n'
        #         print(ret)
        #         # ret = str(ret, 'utf-8')
        #         f.write(bytes(ret, encoding='utf-8'))


if __name__ == '__main__':
    init()
    pdf_path = r'H:\迅雷下载\ed3book2.pdf'
    fileName = r'H:\迅雷下载\test.txt'
    changePdfToText(pdf_path, fileName)
