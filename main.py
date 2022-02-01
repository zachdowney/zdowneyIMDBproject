import requests
import pprint
import config
import sys

baseurl = "https://imdb-api.com/en/API/Top250TVs/"
userurl = "https://imdb-api.com/en/API/UserRatings/"
# https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c
# showed me how to use a secrets file
# https://www.youtube.com/watch?v=QovKok-2u9k
# showed me how to get data and what pprint is
response = requests.get(baseurl + config.apiKey)
shows = response.json()


def user_ratings(self):
    for i in range(0, 200):
        if shows['items'][i]['rank'] == '1' or shows['items'][i]['rank'] == '50' \
                or shows['items'][i]['rank'] == '100' or shows['items'][i]['rank'] == '200':
            r = requests.get(userurl + config.apiKey + "/" + shows['items'][i]['id'])
            info = r.json()
            print("User rating data for the number " + shows['items'][i]['rank'] + " ranked show:")
            pprint.pprint(info)
            print('\n')


def wheel_user_ratings():
    wheel_of_time_id = 'tt0331080'
    w = requests.get(userurl + config.apiKey + "/" + wheel_of_time_id)
    wheel_info = w.json()
    print("User rating data for Wheel of Time:")
    pprint.pprint(wheel_info)

def list_shows(self):
    print('\n')
    print("List of Top 250 shows:")
    print('\n')
    for i in range(0, 250):
        print(shows['items'][i])
        print('\n')


# https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python
# that website showed me how to get my data onto my text file.
sys.stdout = open("data.txt", "w")

user_ratings(shows)
wheel_user_ratings()
list_shows(shows)

sys.stdout.close()
