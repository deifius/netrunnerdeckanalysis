#/usr/bin/env python

from glob import glob
from time import sleep

#download all of your decks from cardgamedb and put them in the "allofthedecks" folder
runners = ["Andromeda","Chaos Theory","Edward Kim","Exile","Gabriel Santiago","Hayley Kaplan","Iain Stirling",'Kate "Mac" McCaffrey','Ken "Express" Tenma',"Laramy Fisk","Leela Patel","MaxX","Nasir Meidan","Noise","Quetzal","Reina Roja",'Rielle "Kit" Peddler',"Silhouette","The Collective","The Masque","The Professor","Valencia Estevez","Whizzard"]

corps = set(["Argus Security: Protection Guaranteed","Blue Sun: Powering the Future","Cerebral Imaging: Infinite Frontiers","Chronos Protocol: Selective Mind-mapping","Chronos Protocol: Selective Mind-mapping","Custom Biotics: Engineered for Success","Gagarin Deep Space: Expanding the Horizon","GRNDL: Power Unleashed","Haas-Bioroid: Engineering the Future","Haas-BioroiArgus Security: Protection Guaranteed","Blue Sun: Powering the Future","Cerebral Imaging: Infinite Frontiers","Chronos Protocol: Selective Mind-mapping","Chronos Protocol: Selective Mind-mapping","Custom Biotics: Engineered for Success","Gagarin Deep Space: Expanding the Horizon","GRNDL: Power Unleashed","Haas-Bioroid: Engineering the Future","Haas-Bioroid: Stronger Together","Harmony Medtech: Biomedical Pioneer","Industrial Genomics: Growing Solutions","Jinteki Biotech: Life imagined","Jinteki: Personal Evolution","Jinteki: Replicating Perfection","NBN: Making News","NBN: The World is Yours*","Near-Earth Hub: Broadcast Center","NEXT Design: Guarding the Net","Nisei Division: The Next Generation","Tennin Institute: The Secrets Within","The Foundry: Refining the Process","The Shadow: Pulling the Strings","Titan Transnational: Investing In Your Future","Weyland Consortium: Because We Built It","Weyland Consortium: Building a Better World","d: Stronger Together","Harmony Medtech: Biomedical Pioneer","Industrial Genomics: Growing Solutions","Jinteki Biotech: Life imagined","Jinteki: Personal Evolution","Jinteki: Replicating Perfection","NBN: Making News","NBN: The World is Yours*","Near-Earth Hub: Broadcast Center","NEXT Design: Guarding the Net","Nisei Division: The Next Generation","Tennin Institute: The Secrets Within","The Foundry: Refining the Process","The Shadow: Pulling the Strings","Titan Transnational: Investing In Your Future","Weyland Consortium: Because We Built It","Weyland Consortium: Building a Better World"])

alldecks = {}
deckfiles = glob("allofthedecks/*")
for decktxt in deckfiles:
# the data structure is a dict of decks of cards that have the properties 'name' and 'set'
	detective = open(decktxt).read().split('\n')
	shuffleable = []
	for each in detective:		
		#print each
		shuffleable.append([each.split(' (')[0],each.split('(')[1].split(')')[0],int(each.split(') x')[-1].rstrip())])
		#print shuffleable[-1]
		#sleep(.25)
	#sleep(2)
	alldecks[decktxt.split("/")[1].split(".txt")[0]] = shuffleable

setdecks = {}
for deck in alldecks.keys():
	setlist = []	
	for card in alldecks[deck]:
		setlist.append(card[1])
	setlist = set(setlist)
	setdecks[deck] = setlist

#divide the decks into corps and runners.  Pull all the corps out of allthedecks, and what is left is runners!
corpdecks = {}
runnerdecks = {}
for deck in alldecks:
	for card in alldecks[deck]:
		if card[0] in corps:
			corpdecks[deck] = alldecks[deck]

for keys in corpdecks.keys():
	alldecks.pop(keys,)

runnerdecks = alldecks

#iterate through all the corp and runner combinations
corpandrunner = {}
for runner in runnerdecks:
	for corp in corpdecks:
		corpandrunner[corp + "+" + runner] = []
		for card in runnerdecks[runner]:
			corpandrunner[corp + "+" + runner].append(card[1])
		for card in corpdecks[corp]:
			corpandrunner[corp + "+" + runner].append(card[1])
		#print corpandrunner.keys()
		#sleep(.25)
		corpandrunner[corp + "+" + runner] = list(set(corpandrunner[corp + "+" + runner]))

count = 0
ezbuilds = []
corpandrunnerlist = []
while len(ezbuilds) < 6: 
	for each in corpandrunner:
		if len(corpandrunner[each]) < count:
			ezbuilds.append(each + " needs " + str(len(corpandrunner[each])) + " sets to build")
			corpandrunnerlist.append(corpandrunner[each])
	count += 1

count = 0
for sentence in ezbuilds:
	print str(count) + ". " + sentence
	count += 1

#select deck pairing, and review set +data packs required
while 1 is 1:
	review = input("which build?:") 
#add number of cards in each set
	for setpresence in corpandrunnerlist[review]:
		presencevalue = 0
		for card in corpdecks[ezbuilds[review].split('+')[0]]:
			if card[1] == setpresence:
				presencevalue += card[2]
		for card in runnerdecks[ezbuilds[review].split('+')[1].split(' needs ')[0]]:
			if card[1] == setpresence:
				presencevalue += card[2]
		print setpresence + ": " + str(presencevalue) + " cards"
		sleep(.25)
	print "to build " + ezbuilds[review]

