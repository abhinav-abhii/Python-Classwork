import random
appleJuice=15.5
orangeJuice=20
grapeJuice=10.25
totalvolume=appleJuice+orangeJuice+grapeJuice
print("TOTAL VOLUME=",totalvolume)

inttotalvolume=int(totalvolume)
print("Total volume in Integer=",inttotalvolume)

strtotalvolume=str(totalvolume)
print("Total volume in String=",strtotalvolume)

additionalbonus=random.randint(5,10)
print("Additional Bonus=",totalvolume+additionalbonus)
