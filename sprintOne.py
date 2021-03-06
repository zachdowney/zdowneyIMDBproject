import requests
import pprint
import secrets
import sys


def get_data(url):
    # https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c
    # showed me how to use a secrets file
    # https://www.youtube.com/watch?v=QovKok-2u9k
    # showed me how to get data and what pprint is
    response = requests.get(url + secrets.apiKey)
    data_list = response.json()
    data = data_list['items']
    return data


def user_ratings(self):
    shows = get_data("https://imdb-api.com/en/API/Top250TVs/")
    user_url = "https://imdb-api.com/en/API/UserRatings/"
    for i in range(0, 200):
        if shows[i]['rank'] == '1' or shows[i]['rank'] == '50' \
                or shows[i]['rank'] == '100' or shows[i]['rank'] == '200':
            r = requests.get(user_url + secrets.apiKey + "/" + shows[i]['id'])
            info = r.json()
            print("User rating data for the number " + shows[i]['rank'] + " ranked show:")
            pprint.pprint(info)
            print('\n')


def wheel_user_ratings():
    user_url = "https://imdb-api.com/en/API/UserRatings/"
    wheel_of_time_id = 'tt0331080'
    w = requests.get(user_url + secrets.apiKey + "/" + wheel_of_time_id)
    wheel_info = w.json()
    print("User rating data for Wheel of Time:")
    pprint.pprint(wheel_info)


def list_shows(self):
    shows = get_data("https://imdb-api.com/en/API/Top250TVs/")
    print('\n')
    print("List of Top 250 shows:")
    print('\n')
    for i in range(0, len(shows)):
        print(shows[i])
        print('\n')


# https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python
# that website showed me how to get my data onto my text file.
def save_data(data, filename='data.txt'):
    sys.stdout = open(filename, "w")

    user_ratings(data)
    wheel_user_ratings()
    # list_shows(data)

    sys.stdout.close()
