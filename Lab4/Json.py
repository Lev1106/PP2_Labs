import json

def parse():
    with open('Lab4/json/sample-data.json', 'r') as file:
        data = json.load(file)

    print("Interface Status\n" + ('=' * 80))
    print("DN" + (' ' * 49) + "Description" + (' ' * 11) + "Speed" + (' ' * 4) + "MTU")
    print(('-' * 50) + ' ' + ('-' * 20) + '  ' + ('-' * 6) + '  ' + ('-' * 6))

    for l1PhysIf in data['imdata']:
        attr = l1PhysIf["l1PhysIf"]["attributes"]

        dn = attr['dn']
        num = dn[-3:-1]
        if not num.isnumeric() or int(num) < 33 or int(num) > 35:
            continue
        print(dn, end='')
        
        descr = attr['descr']
        print(descr, end=(' ' * 30))
        
        speed = attr['speed']
        print(speed, end=(' ' * 3))
        
        mtu = attr['mtu']
        print(mtu)