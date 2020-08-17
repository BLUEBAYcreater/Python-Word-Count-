with open("Python.txt", 'r') as fh:  
    filedata = fh.read()

#check contents
print("File data sample : ", filedata[:200])

# Create stopword list:
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

#Generate wordcloud data
wordcloud = WordCloud(stopwords=stopwords, max_words=15, \
                      background_color="white").generate(filedata)




displsaying



import matplotlib.pyplot as mpLib
mpLib.imshow(wordcloud)
mpLib.axis("off")
mpLib.show()


stopwords.update(["many","using", "want", "value"])

#Redo stop words. Limit number of words
wordcloud = WordCloud(stopwords=stopwords, max_words=10, \
                      background_color="azure").generate(filedata)

mpLib.imshow(wordcloud)
mpLib.axis("off")
mpLib.show()