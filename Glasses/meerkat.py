import os
import json

component=input("What component are building? -> ")
file=open("output.txt", "w")

directory = os.getcwd()

lines = []

print('-- --')

lines.append(component+'_uncommon: [\n')
for entry in os.scandir(directory+'/uncommon'):
    if entry.path.endswith(".png"):
        name = input('What should "'+entry.name+'" be called? -> ')
        print('-- --')
        comp = '{ "image": require("'+'../static/assets/img/'+component+'/uncommon/'+entry.name+'"),"rarity": "uncommon","name": "'+name+'" },'
        lines.append(comp)
lines.append("\n],")

lines.append(component+'_common: [\n')
for entry in os.scandir(directory+'/common'):
    if entry.path.endswith(".png"):
        name = input('What should "'+entry.name+'" be called? -> ')
        print('-- --')
        comp = '{ "image": require("'+'../static/assets/img/'+component+'/common/'+entry.name+'"),"rarity": "common","name": "'+name+'" },'
        lines.append(comp)
lines.append('\n],')

lines.append(component+'_legendary: [\n')
for entry in os.scandir(directory+'/legendary'):
    if entry.path.endswith(".png"):
        name = input('What should "'+entry.name+'" be called? -> ')
        print('-- --')
        comp = '{ "image": require("'+'../static/assets/img/'+component+'/legendary/'+entry.name+'"),"rarity": "legendary","name": "'+name+'" },'
        lines.append(comp)
lines.append('\n],')

for entry in os.scandir(directory+'/rare'):
    lines.append(component+'_rare: [\n')
    if entry.path.endswith(".png"):
        name = input('What should "'+entry.name+'" be called? -> ')
        print('-- --')
        comp = '{ "image": require("'+'../static/assets/img/'+component+'/rare/'+entry.name+'"),"rarity": "rare","name": "'+name+'" },'
        lines.append(comp)
    lines.append('\n]')

print(lines)


file.writelines(lines)

file.close()

print("Complete!")
