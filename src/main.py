import requests

def main():
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        print('Your IP is', response.json()['origin'])

if __name__ == '__main__':
    main()
