import boto3
from botocore.exceptions import ClientError

def calculate():
    log = open("files\log.txt", "a")
    while True:
        num1 = input("Enter first number: ")
        if num1 == "q": break
        num2 = input("Enter second number: ")
        print(f"{int(num1)} + {int(num2)} = {int(num1) + int(num2)}")
        print(f"{int(num1)} + {int(num2)} = {int(num1) + int(num2)}", file=log)
    print("Andrew MacMaster", file = log)
    # s3 implementation hidden due to lack of valid credentials
    # s3 = boto3.resource("s3")
    # BUCKET = "test"
    # s3.Bucket(BUCKET).upload_file("files\log.txt", "file\location")

def ex4():
    calculate()

ex4()
