from django.shortcuts import render


# Create your views here.


def index(request):
    img_list = [
        'https://haski-mana.ru/wp-content/uploads/4/a/7/4a7ea44468120dc95b5bc4edf0f66987.jpeg',
        'https://steamuserimages-a.akamaihd.net/ugc/535124313182101052/20B71045D1FCB3DB406D1B2077532CAE9FF49760/',
        'https://www.technocracy.news/wp-content/uploads/2022/09/Screen-Shot-2022-09-01-at-7.09.30-AM.png',
        'https://cdn1.ozone.ru/multimedia/1020857860.jpg',
        'https://witchnest.ru/uploads/posts/2022-07/steampunk-fly.webp',
        'https://i.ytimg.com/vi/0z4UR-Db0ao/maxresdefault.jpg',
        'https://otvet.imgsmail.ru/download/50227636_f53f5f9a6f9f68bae1d8680e5b8fa519_800.jpg'
    ]
    data = {'img_list': img_list}
    return render(request, 'home/index.html', data)
