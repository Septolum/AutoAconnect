#! /bin/python3
import subprocess, re
for i in (re.findall("client (\d+): '(?!(?:Midi Through)|(?:FLUID Synth))", subprocess.run(["aconnect", "-o"], universal_newlines=True, stdout=subprocess.PIPE).stdout, re.I)):
    subprocess.run(["aconnect", i + ":0", (re.findall("client (\d+): '(?=FLUID Synth)", subprocess.run(["aconnect", "-o"], universal_newlines=True, stdout=subprocess.PIPE).stdout, re.I))[0] + ":0"])
