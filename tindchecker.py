#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import requests
except ModuleNotFoundError:
    print("requests modulen er ikke installert, installer ved aa skrive: 'pip install requests'")
    sys.exit()

import sys, requests, time, platform



if not (int(platform.python_version().split('.')[0]) == 3 and int(platform.python_version().split('.')[1]) >= 5):
    print("For gammel versjon av python, kjor med versjon storre enn 3.5")
    print("versjon: ", platform.python_version())
    sys.exit()

def bibreader(inputtext):
    outputelement = {}
    for line in inputtext.split('\n'):
        tmpsplit = line.split('=')
        if len(tmpsplit) > 1:
            outputelement[tmpsplit[0].strip()] = tmpsplit[1].strip()[1:-2]
    return outputelement

def read_many_bibs(inputtext):
    list_of_matches = []
    for elem in inputtext.split('\n@'):
        if elem != '':
            list_of_matches.append(bibreader(elem))
    return list_of_matches
    
if len(sys.argv) != 3:
  print("\nMangler inputfil og/eller outputfil")
  print("Kjor scriptet slik:\n")
  print("python tindchecker.py inputfil outputfil\n\n")
  sys.exit()
count = 0
with open (sys.argv[2], 'w', encoding='UTF-8') as output:
    with open(sys.argv[1], 'r') as input:
        for line in input:
            r = requests.get(
                url='https://ntnu.tind.io/search?of=btex&p=' + line.strip()
            )
            if r.ok and r.text != '':
                output_row = line.strip() 
                for matches in read_many_bibs(r.text):
                    output_row += ';' + str(matches.get('recid')) + ';' + str(matches.get('title')) + ';' + str(matches.get('author'))
                output.write(output_row + '\n')
            count += 1
            time.sleep(0.5)
            output.flush()
print('prosseserte ', count, ' antall rader')