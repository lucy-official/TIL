from coffee_machine import CoffeeMachine

MENU = {'espresso'  :{'water':50,'milk':0,'coffee':18, 'money':1.50},
        'latte'     :{'water':50,'milk':150,'coffee':24, 'money':2.50},
        'cappuccino':{'water':50,'milk':100,'coffee':24, 'money':3.00}}

if __name__ == '__main__':
    cm = CoffeeMachine(menu = MENU)
    # loop - off : break
    # user input
    while True:
        m = input('What would you like? (espresso/latte/cappuccino):')
        if m == 'off':
            break
        elif m in MENU.keys():
            if not cm.choose_menu(m):
                continue
            if not cm.check_resources():
                continue
            if not cm.process_coins():
                continue
            if not cm.process_tx():
                continue
            cm.make_coffee()
        elif m.lower() == 'report':
            cm.report()
        else:
            print('Invalid menu...:(') 
        
