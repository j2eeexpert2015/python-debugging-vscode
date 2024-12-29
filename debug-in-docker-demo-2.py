from time import sleep
import subprocess

subprocess.run(['hostname'])
counter = 0
while True:
    print("The demo 2 counter:", counter)
    counter = counter +1
    sleep(1)
