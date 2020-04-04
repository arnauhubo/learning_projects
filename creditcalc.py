import math
import sys

class Credit:
    def __init__(self, types, prin, per, math_pay, inte):
        self.P = prin
        self.types = types
        self.n = per
        self.i = inte
        self.A = math_pay
        self.tot_pay = 0.0
        self.O = 0.0

    def count_months(self):
        x = self.A / (self.A - self.i * self.P)
        self.n = math.log(x, 1 + self.i)
        self.n = math.ceil(self.n)
        self.tot_pay = self.A * self.n
        years = self.n // 12
        months = self.n % 12
        y = True
        m = True
        y_plur = True
        m_plur = True
        if years == 0:
            y = False
        if months == 0:
            m = False
        if years == 1:
            y_plur = False
        if months == 1:
            m_plur = False
        if y and m and y_plur and m_plur:
            return "You need {} years and {} months to repay this credit!".format(years, months)
        if y and m and m_plur:
            return "You need {} year and {} months to repay this credit!".format(years, months)
        if y and m and y_plur:
            return "You need {} years and {} month to repay this credit!".format(years, months)
        if y and y_plur:
            return "You need {} years to repay this credit!".format(years)
        if y:
            return "You need {} year to repay this credit!".format(years)
        if m and m_plur:
            return "You need {} months to repay this credit!".format(months)
        if m:
            return "You need {} month to repay this credit!".format(months)

    def annuity_payment(self):
        self.A = self.P * self.i * math.pow(1 + self.i, self.n)
        self.A = self.A / (math.pow(1 + self.i, self.n) - 1)
        self.tot_pay = math.ceil(self.A) * self.n
        return "Your annuity payment = {}!".format(math.ceil(self.A))


    def crd_principal(self):
        a = self.i * math.pow(1 + self.i, self.n)
        b = math.pow(1 + self.i, self.n) - 1
        d = a / b
        self.P = self.A / d
        self.tot_pay = self.A * self.n
        return "Your credit principal = {}!".format(math.floor(self.P))

    def diff_payment(self):
        for m in range(1, self.n + 1):
            d = self.P / self.n + self.i * self.P * (1 - (m - 1) / self.n)
            d = math.ceil(d)
            print("Month {}: paid out {}".format(m, d))
            self.tot_pay += d

    def overpayment(self):
        self.O = self.tot_pay - self.P
        return "Overpayment = {}".format(math.ceil(self.O))


def get_inputs(args):
    types = ""
    prin = 0
    per = 0
    math_pay = 0
    inte = 0
    if len(args) < 5:
        print("Parameters are incorrect.")
        sys.exit()
    for i in range(1, len(args)):
        if "type" in args[i]:
            types = args[i].split("=")[-1]
            if types not in ["annuity", "diff"]:
                print("Parameters are incorrect.")
                sys.exit()
                #raise ValueError("Incorrect parameters")
        if "principal" in args[i]:
            prin = float(args[i].split("=")[-1])
            if prin <= 0.0:
                print("Parameters are incorrect.")
                sys.exit()
        if "periods" in args[i]:
            per = int(args[i].split("=")[-1])
            if per <= 0.0:
                print("Parameters are incorrect.")
                sys.exit()
        if "payment" in args[i]:
            math_pay = float(args[i].split("=")[-1])
            if math_pay <= 0.0:
                print("Parameters are incorrect.")
                sys.exit()
            if types == "diff":
                print("Parameters are incorrect.")
                sys.exit()
                #raise ValueError("Incorrect parameters")
        if "interest" in args[i]:
            inte = float(args[i].split("=")[-1]) / 100 / 12
            if inte <= 0.0:
                print("Parameters are incorrect.")
                sys.exit()
    if inte == 0:
        print("Parameters are incorrect.")
        sys.exit()
    if types == "diff":
        if prin == 0 or per == 0:
            print("Parameters are incorrect.")
            sys.exit()

    return types, prin, per, math_pay, inte

#------------------START MAIN--------------------------------------
types, prin, per, math_pay, inte = get_inputs(sys.argv)
my_credit = Credit(types, prin, per, math_pay, inte)

if my_credit.types == "diff":
    print(my_credit.diff_payment())
elif my_credit.P == 0:
    print(my_credit.crd_principal())
elif my_credit.n == 0:
    print(my_credit.count_months())
elif my_credit.A == 0:
    print(my_credit.annuity_payment())

print(my_credit.overpayment())
#------------------END MAIN----------------------------------------

