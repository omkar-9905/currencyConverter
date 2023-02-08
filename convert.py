import requests


class currency_converter():
    
    def currency(self, currency_type_1,currency_type_2):
        self.currency_type_1 = currency_type_1
        self.currency_type_2 = currency_type_2
        default = "invalid choice"
        return getattr(self,"case_"+str(currency_type_1), lambda:default)()

    def case_1(self):
        url = "https://v6.exchangerate-api.com/v6/YOURAPIKEY/latest/USD"
        value = float(input("Please Enter Amount To Convert: "))
        response = requests.get(url)
        data = response.json()
        if self.currency_type_2 == 1:
            return value*float(data['conversion_rates']['USD'])
        elif self.currency_type_2 == 2:
            return value*float(data['conversion_rates']['INR'])

    def case_2(self):
        url = "https://v6.exchangerate-api.com/v6/1a740d5d7c07a2b23f879e9e/latest/INR"
        value = float(input("Please Enter Amount To Convert: "))
        response = requests.get(url)
        data = response.json()
        if self.currency_type_2 == 1:
            return value*float(data['conversion_rates']['USD'])
        elif self.currency_type_2 == 2:
            return value*float(data['conversion_rates']['INR'])

currency_switch = currency_converter()

print(currency_switch.currency(currency_type_1=int(input("Please Enter Which Currency To Convert From Below Options \n1.USD\n2.INR\n ")),
                               currency_type_2=int(input("Please Enter Which Currency To Convert From Below Options \n1.USD\n2.INR\n ")))
                               )