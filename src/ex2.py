import csv

def find_total_visits():
    all_weeks = ["files\week-1.csv", "files\week-2.csv", "files\week-3.csv"]
    total = 0

    for week in all_weeks:
        with open(week) as f:
            w = csv.reader(f)
            next(w, None)
            for person in w:
                total += sum(map(lambda x: int(x), person[1:]))
    
    return total
    

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()