from time import sleep

# the program will print hello world every 1 second
count = 0
while True:
    count = count + 1
    print("Count value:",count)
    sleep(1)