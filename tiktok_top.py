import requests
import json
import pymongo
def get_top(url):
    headers = {
        "Referer": "https://www.iesdouyin.com/share/billboard/?id=1",
        "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_13_6) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.131Safari / 537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    html = requests.get(url=url,headers = headers)
    print(html.text)
    return html
def foo(var):
    return {
            '0': "",
            '1': "新",
            '3': "热",
    }.get(var,'error')
def parce_top(html):
    top_list = json.loads(html.text)
    time = top_list['active_time']
    print(time)
    word_list = top_list['word_list']
    for rank,word in enumerate(word_list):
        words = word['word']
        hot_value = word['hot_value']
        tag = word['label']
        tags = foo(str(tag))
        print(rank,words,hot_value,tags)

def get_hot_video(url):
    headers = {
        "Referer": "https://www.iesdouyin.com/share/billboard/?id=1",
        "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_13_6) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.131Safari / 537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    html = requests.get(url=url, headers=headers)
    print(html.text)
    return html

def save_mongo(name,dictitem):
    sta = 'Tik_Tok' + name
    myclient = pymongo.MongoClient(host='localhost', port=27017)
    mydb = myclient.Tik_Tok
    mycol = mydb[sta]
    mycol.update_one(dictitem, {'$set': dictitem}, upsert=True)

def parce_hot_video(html):
    hot_list = json.loads(html.text)
    time = hot_list['active_time']
    print(time)
    aweme_list = hot_list.get('aweme_list')
    for rank,awemes in enumerate(aweme_list):
        aweme= awemes.get('aweme_info')
        aweme_id = aweme.get('aweme_id')
        create_time = aweme.get('create_time')
        desc = aweme.get('desc')
        url = aweme['video']['play_addr']['url_list'][0]
        hot_value = awemes.get('hot_value')
        print(rank,aweme_id,create_time,desc,hot_value,url)
def parce_music(html):
    mc_list = json.loads(html.text)
    time = mc_list.get('active_time')
    music_list = mc_list.get('music_list')
    for rank,music in enumerate(music_list):
        hot_value = music.get('hot_value')
        is_new = music.get('is_new')
        music_info = music.get('music_info')
        author = music_info.get('author')
        title = music_info.get('title')
        url = music_info['play_url']['url_list'][0]
        print(rank,title,author,hot_value,is_new,url)

def parce_cat(html):
    list = json.loads(html.text)
    weekly_info = list.get('weekly_info')
    print(weekly_info)
    brand_list = list.get('brand_list')
    for brand in brand_list:
        id = brand.get('id')
        heat = brand.get('heat')
        name = brand.get('name')
        rank = brand.get('rank')
        rank_diff = brand.get('rank_diff')
        url = brand.get('logo_url')
        print(rank,id,name,heat,rank_diff,url)

def parce_star(html):
    list = json.loads(html.text)
    active_time = list.get('active_time')
    print(active_time)
    star_list = list.get('star_list')
    stars = []
    for rank,star in enumerate(star_list):
        hot_value = star.get('hot_value')
        is_new = star.get('is_new')
        rank_diff = star.get('rank_diff')
        star_info = star.get('star_info')
        uid = star_info.get('uid')
        nickname = star_info.get('nickname')
        signature = star_info.get('signature')
        url = star_info.get('avatar_thumb')
        print(rank,nickname,signature,rank_diff,hot_value,is_new,url,uid,)
        star_dic = {
            'rank':rank,
            'nickname':nickname,
            'signature':signature,
            'rank_diff': rank_diff,
            'hot_value': hot_value,
            'is_new': is_new,
            'url': url,
            'uid': uid,
            'active_time': active_time,
        }
        save_mongo('star',star_dic)
    return stars


#明星榜
star = 'https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/star/'
#热搜榜地址
top = 'https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/'
#视频榜地址
hot = 'https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/aweme/'
#正能量
positive = 'https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/aweme/?type=positive'
#音乐
music = 'https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/music/'
#汽车榜
car = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/billboard/?version_code=6.0.0&category_id=1'
#手机榜
phone = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/billboard/?version_code=6.0.0&category_id=2'
#美妆榜
meiz = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/billboard/?version_code=6.0.0&category_id=3'
# a = get_top(star)
# parce_star(a)
#
# def save_mongo(name,dictitem):
#     myclient = pymongo.MongoClient(host='localhost', port=27017)
#     mydb = myclient.Tik_Tok
#     mycol = mydb[name]
#     mycol.update_one(dictitem, {'$set': dictitem}, upsert=True)

def main():
    a = get_top(star)
    dic = parce_star(a)


if __name__ == "__main__":
    main()