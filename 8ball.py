import random

q = input("Please input your question:")
while q[-1] is not "?":
	q = input("A question must end by '?'. Please input your question again.:")

r = random.randint(1, 21)

dic = { 
	
1: "It is certain",
2:"It is decidedly so",
3:"Without a doubt",
4:"Yes, definitely",
5:"You may rely on it",
6:"As I see it, yes",
7:"Most likely",
8:"Outlook good",
9:"Yes",
10:"Signs point to yes",
11:"Reply hazy try again",
12:"Ask again later",
13:"Better not tell you now",
14:"Cannot predict now",
15:"Concentrate and ask again",
16:"Don't count on it",
17:"My reply is no",
18:"My sources say no",
19:"Outlook not so good",
20:"Very doubtful"

}

print(dic[r])
while r in range(11,16):
	print("The answer is not clear, Try again.")
	r = random.randint(1, 21)
	print(dic[r])
