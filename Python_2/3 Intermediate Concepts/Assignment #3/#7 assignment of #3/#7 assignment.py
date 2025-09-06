import requests


#1
# youtube_eminem = requests.get('https://www.youtube.com/watch?v=OOKMf-kMEdg&ab_channel=VibeTribe')
#
# if youtube_eminem.status_code == 200:
#     print(f'{youtube_eminem.text[:300]}')
# else:
#     print('NOT AVAILABLE')



#2

# A
# response = requests.get("https://api.github.com/users/octocat")
# data = response.json()
# print(data['login'])


# B

try:
    response1 = requests.get("https://www.google.com")
    var = response1.status_code
    print(var)
except requests.exceptions.RequestException as x:
    print(f'Error {x}')
