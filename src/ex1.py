from ValidationException import ValidationException
import csv

def validate_file(file_name):
    with open(file_name) as f:
        file_reader = csv.reader(f)
        next(file_reader, None)
        for row in file_reader:
            num = float(row[1])
            if not num.is_integer():
                raise ValidationException(f"Invalid mileage: {row[1]}")
        print("File is valid.")



def ex1():
    try:
        validate_file("files\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()