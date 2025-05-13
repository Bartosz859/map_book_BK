def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')


def added_user(users_data: str) -> None:
    new_name: str = input('podaj imię nowego znajomego: ')
    new_location: str = input('podaj lokalizację: ')
    new_posts: str = input('podaj liczbę postów: ')
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts})


def remove_user(users_data: list):
    user_name: str = input('podaj imię zmajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)

def get_coordinates(city_name:str)->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/{city_name}"
    response=requests.get(url).text
    response_html=BeautifulSoup(response,"html.parser")
    longitude=response_html.select(".longitude")[1].text.replace(",",".")
    latitude=response_html.select(".latitude")[1].text.replace(",",".")
    print(longitude)
    print(latitude)
    return [latitude,longitude]

def get_map(users_data:list)->None:
    import folium
    m = folium.Map(location=(52.23, 21.0), zoom_start=6)
    for user in users_data:
        folium.Marker(location=(get_coordinates(user['location'])),popup='<img src="https://geoforum.pl/upload3/news_pl/picture/328_geodeta_artykul6.jpg"/>').add_to(m)
    m.save("index.html")
