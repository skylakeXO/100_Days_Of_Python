import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import PIL.Image

text = open('lyrics.txt', 'r').read()
pic_python = np. array(PIL.Image.open('heart.png'))

fig = plt.figure(figsize=(8,8))
wc = WordCloud(stopwords=STOPWORDS,
               mask = pic_python,
               background_color='white').generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()
