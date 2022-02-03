import requests
import pprint
import secrets
import sys

base_url = "https://imdb-api.com/en/API/Top250TVs/"
user_url = "https://imdb-api.com/en/API/UserRatings/"
# https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c
# showed me how to use a secrets file
# https://www.youtube.com/watch?v=QovKok-2u9k
# showed me how to get data and what pprint is
response = requests.get(base_url + secrets.apiKey)
shows = response.json()


def user_ratings(data):
    for i in range(0, 200):
        if data['items'][i]['rank'] == '1' or data['items'][i]['rank'] == '50' \
                or data['items'][i]['rank'] == '100' or data['items'][i]['rank'] == '200':
            r = requests.get(user_url + secrets.apiKey + "/" + data['items'][i]['id'])
            info = r.json()
            print("User rating data for the number " + data['items'][i]['rank'] + " ranked show:")
            pprint.pprint(info)
            print('\n')


def wheel_user_ratings():
    wheel_of_time_id = 'tt0331080'
    w = requests.get(user_url + secrets.apiKey + "/" + wheel_of_time_id)
    wheel_info = w.json()
    print("User rating data for Wheel of Time:")
    pprint.pprint(wheel_info)


def list_shows(data):
    print('\n')
    print("List of Top 250 shows:")
    print('\n')
    for i in range(0, 250):
        print(data['items'][i])
        print('\n')


# https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python
# that website showed me how to get my data onto my text file.
def save_data(data, filename='data.txt'):
    sys.stdout = open(filename, "w")

    user_ratings(data)
    wheel_user_ratings()
    list_shows(data)

    sys.stdout.close()


def main():
    save_data(shows)


if __name__ == '__main__':
    main()

