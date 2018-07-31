from requests_html import HTMLSession
import json
import matplotlib.pyplot as plt


session = HTMLSession()
response = session.get('https://www.dcard.tw/_api/forums/mood/posts?popular=true')  #抓心情版的熱門文章
mood_load = json.loads(response.text) # 把json 格式轉為 python格式
mood_gender = {"F":0 , "M":0}  #創建性別dic，計算男女分文比例
mood_like = []
mood_comment = []
mood_title = []


            #計算男女分文比例
for i in mood_load:
    mood_gender[i['gender']]+=1   


            # 算出愛心分佈
for i in mood_load:
    mood_like.append(i['likeCount'])
        
            # 算出留言分佈
for i in mood_load:
    mood_comment.append(i['commentCount'])

for i in mood_load:
    L = len(i['title'])
    mood_title.append(L)   




# 畫長條圖
    def data_gender():
        
        plt.xlabel('gender')
        plt.ylabel('number')
        plt.title('sex ratio')
        kind = ['Female' , 'male'] 
        plt.bar(kind , list(mood_gender.values()), align = 'center' , facecolor = '#9999ff'  , width = 0.3)
        plt.xticks(range(len(mood_gender)),list(mood_gender.keys()))
        plt.savefig('data_gender.png')       
        plt.show()
       


# 畫線圖
    def data_like():
        plt.plot(range(1,31) , mood_like)
        plt.xlabel('ranking')
        plt.ylabel('number of like')
        plt.title('distributed of likes ')
        plt.savefig('data_like.png')
        plt.show() 


# 畫線圖
#data_comment 
    def data_comment():
        plt.plot(range(1,31) , mood_comment)
        plt.xlabel('ranking')
        plt.ylabel('number of comments')
        plt.title('distributed of comments')
        plt.savefig('data_comment.png')
        plt.show() 


# 畫線圖
    def data_title():
        plt.plot(range(1,31) , mood_title)
        plt.xlabel('ranking')
        plt.ylabel('length of title')
        plt.title('tltle length about ranking')
        plt.savefig('data_title.png')
        plt.show() 



print('男女性發文數量：',mood_gender)
print('愛心數排行',mood_like)
print('留言數量排行',mood_comment)
print('標題長度分佈',mood_title)

data_gender()
data_like()
data_comment()
data_title()


#算出 like 
#算出 comment
#算出平均熱度維持