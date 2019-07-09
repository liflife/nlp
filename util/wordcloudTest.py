# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image
import os
import numpy as np

import jieba

text = '据俄罗斯卫星网7月9日报道，塔吉克斯坦国防部新闻中心负责人奥里夫·诺济米延周二表示，塔吉克斯坦和中国军方将于7月底在塔吉克斯坦戈尔诺-巴达赫尚自治州举行联合演习。'
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)
d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
# 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='C:/Windows/Fonts/FZSTK.TTF').generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
