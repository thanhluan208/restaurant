import random

random_jp = ["A","I","U","E","O","Ka","Ki","Ku","ke","ko","Sa","Si","Se","Su","so","Ta","Chi","Tsu","Te","To","Ga","Gi","Gu","Ge","Go","Za","Zi","Zu","Ze","Zo"]
number = random.randrange(0,len(random_jp),1)
print(number)
print(random_jp[number])