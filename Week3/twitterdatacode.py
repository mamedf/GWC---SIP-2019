'''
In this program, we print out all the text data from our twitter JSON file.

Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
# textblobb
# tweetFile = open("tweets_small.json", "r")
# tweetData = json.load(tweetFile)
# tweetFile.close()
listoftweets = []
for tweet in range(len(tweetData)):
	subtweet = tweetData[tweet]["text"]
	listoftweets.append(subtweet)
print(listoftweets)
def wordcount(stringoftweet, string1):
	counter= 0
	string1 = string1.lower()
	wordList = stringoftweet.split(' ')
	for item in wordList:
		if item.lower() == string1:
			counter += 1
	return counter

wordcountlist = []
for item in listoftweets:
	wordoccurence = wordcount(item, "the")
	wordcountlist.append(wordoccurence)
print(wordcountlist)
print (min(wordcountlist), max(wordcountlist))
plt.hist(wordcountlist)
plt.axis([min(wordcountlist), max(wordcountlist), 0, 15])
plt.show()

# tweetstr = ""
# for subtweet in listoftweets:
# 	tweetstr += subtweet + " "
# print(tweetstr)

'''
def countLetter(string, letter):
	count = 0
	for let in string:
		if let.lower() == letter:
			count += 1
	return count
print(countLetter, "a")
alpha = "qwertyuiopasdfghjklzxcvbnmmmmmmm"
letters = (set(sorted(alpha)))

for letter in letters:
	print(f"letter:{letter} occurrences:{countLetter(tweetstr, letter)}")
occurrences = []
for letter in letters:
	occurrences.append(countLetter(tweetstr, letter))
print(occurrences)
print (min(occurrences), max(occurrences))
plt.hist(occurrences)
plt.axis([min(occurrences), max(occurrences), 0, 10])
plt.show()
'''


# import wordcloud
# from wordcloud import WordCloud
# wordcloud = WordCloud().generate(tweetstr)
# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud, interpolation = 'bilinear')
# plt.axis('off')
# plt.tight_layout(pad = 0)
# plt.show()
# polaritylist = []
# for tweet in listoftweets:
# 	blob1 = TextBlob(tweet)
# 	polar1 = blob1.polarity
# 	polaritylist.append(polar1)
# print(polaritylist)
# print(listoftweets)


# for i in range(len(tweetData)):
# 	dictionaree = {}
# 	dictionaree["tid"] = tweetData[i][id]
# 	dictionaree["polarity"] = polaritylist[i]
# 	dictionaree[tweet]=text[i]
# print(tweetData[0])
# sum=0
# for tweet in range(len(tweetData)):
# # 	if "favorite_count" in tweetData[tweet]:
# # 		sum += tweetData[tweet]["favorite_count"]
# # avg = sum/ len(tweetData)
# # print (avg)

#
# We can close the file now that we have locally stored the data.
# tweetFile.close()
#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
