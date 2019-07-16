import jieba

text = '据俄罗斯卫星网7月9日报道，塔吉克斯坦国防部新闻中心负责人奥里夫·诺济米延周二表示，塔吉克斯坦和中国军方将于7月底在塔吉克斯坦戈尔诺-巴达赫尚自治州举行联合演习。'
wordlist_jieba = jieba.cut(text, cut_all=False)
wl_space_split = " ".join(wordlist_jieba)
print(wl_space_split)


dic={}
dic['a']='a'
dic['a']='a'
dic['a']='a'
dic['a']='a'
dic['a']='a'

print(dic)