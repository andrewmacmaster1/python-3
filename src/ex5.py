from pprint import pprint
import csv

def build_car_list():
    models = {}
    with open('files\car-ids.txt') as c:
        reader = csv.reader(c)
        for car in reader:
            models[int(car[0])] = car[1]
    mileages = {}
    with open('files\input.txt') as m:
        reader = csv.reader(m)
        next(reader, None)
        for car in reader:
            num = float(car[1])
            if num.is_integer():
                mileages[int(car[0])] = int(num)
    
    return [{'id': id, 'miles': mileages[id], 'model': models[id]} for id in mileages.keys()]

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
