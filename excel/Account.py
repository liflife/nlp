class Account():
    def __init__(self, no, mark, opposite_account, opposite_name, jie_money, dai_money, money, use_purpose, remark,
                 date):
        self.no = no
        self.mark = mark
        self.opposite_account = opposite_account
        self.opposite_name = opposite_name
        self.jie_money = self.parse_money(jie_money)
        self.dai_money = self.parse_money(dai_money)
        self.money = self.parse_money(money)
        self.use_purpose = use_purpose
        self.remark = remark
        self.date = date

    def parse_money(self, money: str):
        if type(money) == str:
            money = money.replace(',', '')
        if money == '':
            return float(0)
        else:
            return float(money)

    def __str__(self):
        return '序号：%s 借贷标志：%s 对方账号：%s  对方户名：%s  借方发生额：%s  贷方发生额：%s  余额：%s  用途：%s  摘要：%s   日期：%s                            ' % (
            self.no, self.mark, self.opposite_account, self.opposite_name, self.jie_money, self.dai_money, self.money,
            self.use_purpose, self.remark, self.date)

    def to_string(self):
        return '借贷标志：%s 对方账号：%s  对方户名：%s  借方发生额：%s  贷方发生额：%s 余额：%s  ' % (
            self.mark, self.opposite_account, self.opposite_name, self.jie_money, self.dai_money, self.money)

    def to_string2(self):
        return '对方户名：%s  借方发生额：%s  贷方发生额：%s ' % (
            self.opposite_name, self.jie_money, self.dai_money)
