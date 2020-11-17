import requests

google_apikey = 'youer api key'

Nearby_search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=22.880716929671433,120.47941071080224&radius=500&type=restaurant" + google_apikey

restaurantApi = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + '842高雄市旗山區中山南街145號' + '+restaurant&radius=30000' + google_apikey

pictureApi = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='

restaurantData = requests.get(Nearby_search_url).json()

msg = ""
if restaurantData['status'] == 'OK':
    allRestaurantList = list()
    for item in restaurantData['results'][0:5]:
        RestaurantList = list()
        RestaurantList.append(item['name'])
        RestaurantList.append(item['vicinity'])
        RestaurantList.append(str(item['rating']))
        RestaurantList.append(str(item['opening_hours']['open_now']))
        RestaurantList.append(str(item['user_ratings_total']))
        RestaurantList.append(pictureApi + item['photos'][0]['photo_reference'] + google_apikey)
        allRestaurantList.append(RestaurantList)
    print(allRestaurantList)
    print(restaurantData['results'][0]['name'])
else:
    print('找不到資料')
