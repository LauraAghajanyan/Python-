import csv
import sys


def laptops():
    with open('laptops.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            yield Laptop(
                manufacturer=row['Manufacturer'],
                model_name=row['Model Name'],
                category=row['Category'],
                screen_size=row['Screen Size'],
                screen=row['Screen'],
                cpu=row['CPU'],
                ram=row['RAM'],
                storage=row['Storage'],
                gpu=row['GPU'],
                operating_system=row['Operating System'],
                operating_system_version=row['Operating System Version'],
                weight=row['Weight'],
                price=row['Price (Euros)'],
            )


class Laptop:
    def __init__(self, manufacturer, model_name, category, screen_size, screen, cpu, ram, storage, gpu,
                 operating_system, operating_system_version, weight, price):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.category = category
        self.screen_size = screen_size
        self.screen_size = float(self.screen_size.replace('"', ''))
        self.screen = screen
        self.cpu = cpu
        self.ram = ram
        self.ram = float(self.ram.replace('GB', ''))
        self.storage = storage
        self.gpu = gpu
        self.operating_system = operating_system
        self.operating_system_version = operating_system_version
        self.weight = weight
        self.weight = float(self.weight.replace('kg', '').replace('s', ''))
        self.price = price
        self.price = float(self.price.replace(',', '.'))


# Helper function to find the most expensive and cheapest computers
def pr(prices):
    for p in laptops():
        if p.price == prices:
            return p


# 1
# 5 most expensive computers
def expensive():
    lst = []
    for lap in laptops():
        lst.append(lap.price)
    lst.sort(reverse=True)
    for p in lst[:5]:
        print(f'{func(p).manufacturer} {func(p).model_name} {func(p).price}')


# 2
# 5 cheapest computers
def cheapest():
    lst = []
    for lap in laptops():
        lst.append(lap.price)
    lst.sort()
    for p in lst[:5]:
        print(f'{func(p).manufacturer} {func(p).model_name} {func(p).price}')


# 3
# All operation systems and their quantity
def all_os():
    names_os = {}
    for lap in laptops():
        if lap.operating_system in names_os.keys():
            names_os[lap.operating_system] += 1
        else:
            names_os[lap.operating_system] = 1
    return names_os


# Helper function to find heaviest computers
def weight(weights):
    for w in laptops():
        if w.weight == weights:
            return w


# 4
# 5 heaviest computers
def heaviest():
    lst = []
    for lap in laptops():
        lst.append(lap.weight)
    lst.sort(reverse=True)
    for w in lst[:5]:
        print(f'{weight(w).manufacturer} {weight(w).model_name} {weight(w).weight}')


# Helper function to find the most powerful computers
def ram(rams):
    for r in laptops():
        if r.ram == rams:
            return r


# 5
# 5 most powerful computers
def str_ram():
    lst = []
    for lap in laptops():
        lst.append(lap.ram)
    lst.sort(reverse=True)
    for r in lst[:5]:
        print(f'{ram(r).manufacturer} {ram(r).model_name} {ram(r).ram}')


# 6
# All rams and their quantity
def all_rams():
    names_ram = {}
    for lap in laptops():
        if lap in names_ram.keys():
            names_ram[lap.ram] += 1
        else:
            names_ram[lap.ram] = 1
    print(names_ram)


# Helper function to print all screen sizes grouped
# All screen sizes
def all_size():
    screen_size = {}
    for lap in laptops():
        if lap.screen_size in screen_size.keys():
            screen_size[lap.screen_size] += 1
        else:
            screen_size[lap.screen_size] = 1
    print(screen_size)


# 7
# All screen sized grouped
def all_sizes_grouped():
    new_d = {'Less than 10': 0, '10-13': 0, '13-15': 0, 'More than 15': 0}
    sizes = []
    for lap in laptops():
        sizes.append(lap.screen_size)
    for key in sizes:
        if key < 10:
            new_d['Less than 10'] += 1
        elif key >= 10 and key < 13:
            new_d['10-13'] += 1
        elif key >= 13 and key <= 15:
            new_d['13-15'] += 1
        elif key > 15:
            new_d['More than 15'] += 1
    print(new_d)


# 8
# All brands
def brands():
    brand = {}

    for lap in laptops():
        if lap.manufacturer in brand.keys():
            brand[lap.manufacturer] += 1
        else:
            brand[lap.manufacturer] = 1
    print(brand)

# brands()


# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         print(
#             'Type one of the following commands.\n'
#               '1. 5_most_expensive\n'
#               '2. 5_cheapest\n'
#               '3. All_OS\n'
#               '4. 5_heaviest\n'
#               '5. 5_most_powerful\n'
#               '6. All_rams\n'
#               '7. Screen_sizes\n'
#               '8. All_brands'
#         )
#         command = sys.argv[1]
#         if command not in ['5_most_expensive',
#                            '5_cheapest',
#                            'All_OS',
#                            '5_heaviest',
#                            '5_most_powerful',
#                            'All_rams',
#                            'Screen_sizes',
#                            'All_brands']:
#             print('No such command!')
#             commands = {
#                 '5_most_expensive': expensive,
#                 '5_cheapest': cheapest,
#                 'All_OS': all_os,
#                 '5_heaviest': heaviest,
#                 '5_most_powerful': str_ram,
#                 'All_rams': all_rams,
#                 'Screen_sizes': all_sizes_grouped,
#                 'All_brands': brands
#             }
#
#             func = commands[command]
#             print(func)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Type one of the following commands.\n 5_most_expensive\n 5_cheapest\n all_OS\n 5_heaviest\n 5 most_powerful'
              '\nall_rams\nscreen_sizes\nall_brands')
    elif len(sys.argv) >= 1:
        command = sys.argv[1]
        if command in ['5_most_expensive\n 5_cheapest\n all_OS\n 5_heaviest\n 5 most_powerful'
                       '\n all_rams\n screen_sizes\n all_brands']:
            commands = {
                '5_most_expensive': expensive,
                '5_cheapest': cheapest,
                'all_OS': all_os,
                '5_heaviest': heaviest,
                '5_most_powerful': str_ram,
                'all_rams': all_rams,
                'screen_sizes': all_sizes_grouped,
                'all_brands': brands
            }
            func = commands[command]
            print(func)





