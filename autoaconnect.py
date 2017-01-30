#! /usr/local/bin/python3
import subprocess, re
from time import sleep

def connectall():
    for i in (re.findall("client (\d+): '(?!(?:Midi Through)|(?:FLUID Synth))", subprocess.run(["aconnect", "-o"], universal_newlines=True, stdout=subprocess.PIPE).stdout, re.I)):
        subprocess.run(["aconnect", i + ":0", (re.findall("client (\d+): '(?=FLUID Synth)", subprocess.run(["aconnect", "-o"], universal_newlines=True, stdout=subprocess.PIPE).stdout, re.I))[0] + ":0"])
        #print("Connected " + str(i))

connectall()

prev = ""
 
while True:
    sleep(5)
    new = subprocess.run(["aconnect", "-o"], universal_newlines=True, stdout=subprocess.PIPE).stdout
    if prev != new:
        connectall()
    prev = new
