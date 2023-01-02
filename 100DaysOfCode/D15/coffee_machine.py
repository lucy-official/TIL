quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

class CoffeeMachine:
    def __init__(self, water=300, milk=200, coffee=100, money=0.0, **menu):
        self._water = water
        self._milk = milk
        self._coffee = coffee
        self._money = money
        self._menu = menu['menu']
        self._choice = ''
        self._inputmoney = 0

    # 0. get choice
    def choose_menu(self, choice):
        if choice not in self._menu.keys():
            return False
        self._choice = choice
        return True

    # 1. report
    def report(self):
        report_text = f' \
        Water: {self._water}ml\n \
        Milk: {self._milk}ml\n \
        Coffee: {self._coffee}g\n \
        Money: ${self._money}\n'
        print(report_text)

    # 2. Check resources sufficient
    def check_resources(self):
        if self._choice == '':
            print('What is your menu..?')
            return False
        if self._menu[self._choice]['water'] > self._water:
            print('Sorry there is not enough water.')
            return False
        if self._menu[self._choice]['milk'] > self._milk:
            print('Sorry there is not enough water.')
            return False
        if self._menu[self._choice]['coffee'] > self._coffee:
            print('Sorry there is not enough water.')
            return False
        return True 

    # 5. Make coffee
    def make_coffee(self):
        if self._choice == '':
            return False
        self._water = self._water - self._menu[self._choice]['water']
        self._milk = self._milk - self._menu[self._choice]['milk']
        self._coffee = self._coffee - self._menu[self._choice]['coffee']
        print(f"Here is your {self._choice.lower()}. Enjoy!")
        self._choice = ''
        self._inputmoney = 0
        return True


    # 3. Process coins
    # Return
    # [1] Success : return changes
    # [2] Fail : return False
    def process_coins(self):
        if self._choice == '':
            print('What is your menu..?')
            return False
        self._inputmoney = float(input('quarters : ')) * quarters
        self._inputmoney += float(input('dimes : ')) * dimes
        self._inputmoney += float(input('nickles : ')) * nickles
        self._inputmoney += float(input('pennies : ')) * pennies
        return True
    
    # 4. Check tx successful  
    def process_tx(self):
        if self._menu[self._choice]['money'] <= self._inputmoney:
            # add profit
            self._money += self._menu[self._choice]['money']
            print(f"Here is ${self._inputmoney - self._menu[self._choice]['money']} dollars in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
