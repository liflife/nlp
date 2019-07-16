import xlrd
from Account import Account


def read_excel(filePath, type=1):
    # 打开文件
    workbook = xlrd.open_workbook(filePath)
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    # sheet的名称，行数，列数
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    if type == 1:
        return parse1(sheet1)
    elif type == 2:
        return parse2(sheet1)
    else:
        print('无效的类型')
        return []


def parse1(sheet1):
    rows = sheet1.nrows
    list = []
    for row in range(6, rows):
        no = sheet1.cell(row, 0).value
        date = sheet1.cell(row, 1).value
        mark = sheet1.cell(row, 2).value
        opposite_account = sheet1.cell(row, 3).value
        opposite_name = sheet1.cell(row, 4).value
        jie_money = sheet1.cell(row, 5).value
        dai_money = sheet1.cell(row, 6).value
        money = sheet1.cell(row, 7).value
        use_purpose = sheet1.cell(row, 8).value
        remark = sheet1.cell(row, 9).value
        a = Account(no=no, date=date, mark=mark, opposite_account=opposite_account, opposite_name=opposite_name,
                    jie_money=jie_money, dai_money=dai_money, money=money, use_purpose=use_purpose, remark=remark)
        list.append(a)
    return list


def parse2(sheet1):
    rows = sheet1.nrows
    list = []
    for row in range(6, rows):
        mark = ''
        date = sheet1.cell(row, 1).value
        no = sheet1.cell(row, 2).value
        opposite_account = sheet1.cell(row, 3).value
        opposite_name = sheet1.cell(row, 4).value
        jie_money = sheet1.cell(row, 5).value
        dai_money = sheet1.cell(row, 6).value
        money = sheet1.cell(row, 7).value
        use_purpose = ''
        remark = sheet1.cell(row, 8).value
        a = Account(no=no, date=date, mark=mark, opposite_account=opposite_account, opposite_name=opposite_name,
                    jie_money=jie_money, dai_money=dai_money, money=money, use_purpose=use_purpose, remark=remark)
        list.append(a)
    return list


def evencut(aList: list, bList: list):
    alistnull = []
    blistnull = []
    adict = {}
    bdict = {}
    for a in aList:
        key = a.opposite_name
        if key == '':
            alistnull.append(a.to_string2())
            continue
        print('adict' + key)
        lsitvalue = adict.get(key)
        if lsitvalue is None:
            adict[a.opposite_name] = [a]
        else:
            lsitvalue.append(a)
    for b in bList:
        key = b.opposite_name
        if key == '':
            blistnull.append(b.to_string2())
            continue
        print('bList' + key)
        lsitvalue = bdict.get(key)
        if lsitvalue is None:
            bdict[b.opposite_name] = [b]
        else:
            lsitvalue.append(b)

    listok = []
    listwaring = []
    listmut = []
    listerror = []
    countTmp = 0
    for key, valueA in adict.items():
        valueB = bdict.get(key)

        if valueB is not None:
            if len(valueB) == 1 and len(valueA) == 1:
                countTmp += 1
                a = valueA[0]  # type:Account
                b = valueB[0]
                if a.jie_money == b.dai_money or a.dai_money == b.jie_money:
                    listok.append(a.to_string2() + '->' + b.to_string2())
                    print('对账一致：%s,%s' % (a.opposite_name, b.opposite_name))
                else:
                    listerror.append(a.to_string2() + '->' + b.to_string2())
                    print('对账不一致：银行：%s,%s,%s,明细：%s,%s%s,' % (
                        a.opposite_name, a.jie_money, a.dai_money, b.opposite_name, b.jie_money, b.dai_money))
            else:
                countTmp += len(valueA)
                adictChid = {}
                bdictChid = {}
                for a in valueA:
                    if a.jie_money != float(0):
                        key = a.opposite_name + str(a.jie_money)
                    else:
                        key = a.opposite_name + str(a.dai_money)
                    adictChid[key] = a
                for a in valueB:
                    if a.jie_money != float(0):
                        key = a.opposite_name + str(a.jie_money)
                    else:
                        key = a.opposite_name + str(a.dai_money)
                    bdictChid[key] = a

                for key, valueA in adictChid.items():
                    valueB = bdictChid.get(key)
                    if valueB is None:
                        listwaring.append('在账户明细没有找到：%s' % (key))
                        print('在账户明细没有找到：%s' % (key))
                    else:
                        listok.append(valueA.to_string2() + '->' + valueB.to_string2())
                        print('对账一致：%s,%s' % (valueA.opposite_name, valueB.opposite_name))
        else:
            listwaring.append('在账户明细没有找到：%s' % (key))
            print('在账户明细没有找到：%s' % (key))
    print('总条数：%s,countTmp：%s' % (len(aList), countTmp))
    print('总条数：%s,对账一致：%s' % (len(aList), len(listok)))
    print('总条数：%s,对账名为null：%s' % (len(aList), len(alistnull)))
    # saveFile('D:\对账\对账一致.txt', listok)
    # for a in listok:
    #     print(a)
    print('总条数：%s,对账不知一致：%s' % (len(aList), len(listerror)))
    # saveFile('D:\对账\对账不知一致.txt', listerror)
    # for a in listerror:
    #     print(a)
    print('总条数：%s,在账户明细没有找到：%s' % (len(aList), len(listwaring)))
    # saveFile('D:\对账\在账户明细没有找到.txt', listwaring)
    # for a in listwaring:
    #     print(a)
    print('总条数：%s,存在多条账目的：%s' % (len(aList), len(listmut)))
    # saveFile('D:\对账\存在多条账目的.txt', listmut)
    # for a in listmut:
    #      print(a)
    return listok, listwaring, listmut, listerror


def evencut2(aList: list, bList: list):
    alistnull = []
    blistnull = []
    adict = {}
    bdict = {}
    for a in aList:
        key = a.opposite_name
        if key == '':
            alistnull.append(a.to_string2())
            continue
        date = a.date.replace('-', '')[:8]
        if a.jie_money != float(0):
            key = a.opposite_name + str(a.jie_money)
        else:
            key = a.opposite_name + str(a.dai_money)
        adict[key + date] = a
    for a in bList:
        key = a.opposite_name
        date = a.date.replace('-', '')[:8]
        if key == '':
            blistnull.append(a.to_string2())
            continue
        if a.jie_money != float(0):
            key = a.opposite_name + str(a.jie_money)
        else:
            key = a.opposite_name + str(a.dai_money)
        bdict[key + date] = a

    listok = []
    listwaring = []
    listmut = []
    listerror = []
    countTmp = 0
    for key, valueA in adict.items():
        valueB = bdict.get(key)
        if valueB is None:
            listwaring.append('在账户明细没有找到：%s' % (key))
            print('在账户明细没有找到：%s' % (key))
        else:
            listok.append(valueA.to_string2())
            print('对账一致：%s,%s' % (valueA.opposite_name, valueB.opposite_name))

    print('总条数：%s,总条数：%s,对账一致：%s' % (len(aList), len(adict.items()), len(listok)))
    print('总条数：%s,对账名为null：%s' % (len(aList), len(alistnull)))
    # saveFile('D:\对账\对账一致.txt', listok)
    # for a in listok:
    #     print(a)
    print('总条数：%s,对账不一致：%s' % (len(aList), len(listerror)))
    # saveFile('D:\对账\对账不知一致.txt', listerror)
    # for a in listerror:
    #     print(a)
    print('总条数：%s,在账户明细没有找到：%s' % (len(aList), len(listwaring)))
    # saveFile('D:\对账\在账户明细没有找到.txt', listwaring)
    # for a in listwaring:
    #     print(a)
    return listok, listwaring, listmut, listerror


def evencut3(aList: list, bList: list):
    alistnull = []
    blistnull = []

    listok = []
    listerror = []

    aListStr = []
    for a in aList:
        key = a.opposite_name
        if key == '':
            alistnull.append(a.to_string2())
            continue
        if a.jie_money != float(0):
            key = a.opposite_name + '_' + str(a.jie_money)
        else:
            key = a.opposite_name + '_' + str(a.dai_money)
        print(key)
        aListStr.append(key)

    bListStr = []
    for a in bList:
        key = a.opposite_name
        if key == '':
            blistnull.append(a.to_string2())
            continue
        if a.jie_money != float(0):
            key = a.opposite_name + '_' + str(a.jie_money)
        else:
            key = a.opposite_name + '_' + str(a.dai_money)
        bListStr.append(key)
    bListStrTmp = bListStr
    for a in aListStr:
        if a in bListStrTmp:
            bListStrTmp.remove(a)
            listok.append(a)
            print('对账一致：%s' % (a))
        else:
            listerror.append('对账不一致：%s' % (a))
            print('对账不一致：%s' % (a))

    print('总条数：%s,对账一致：%s' % (len(aList), len(listok)))
    print('总条数：%s,对账名为null：%s' % (len(aList), len(alistnull)))
    print('总条数：%s,对账不一致：%s' % (len(aList), len(listerror)))

    return listok, listerror,alistnull,len(aList)


def saveFile(filePath, data: list):
    with open(filePath, 'a+') as f:
        for a in data:
            f.write(a.to_string() + '\n')


if __name__ == '__main__':
    filePath1 = r'D:\对账\4月银行明细账李.xls'
    filePath2 = r'D:\对账\4月账户明细账.xls'
    yinhang = read_excel(filePath1, 1)
    listB = read_excel(filePath2, 2)
    # for yh in yinhang:
    #     print(yh)
    # for yh in listB:
    #     print(yh)
    evencut3(yinhang, listB)
