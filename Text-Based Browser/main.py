import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

args = sys.argv
folder_name = str(args[1])
os.makedirs(folder_name, exist_ok=True)

my_stack = deque()

while True:
    website = input()
    if website == 'exit':
        break
    elif website == 'back':
        try:
            my_stack.pop()
        except IndexError:
            continue
        try:
            with open(f'{folder_name}/{my_stack[0]}.txt', 'r') as web_page:
                content = web_page.read()
                print(content)

        except IndexError:
            continue
    elif website[-4] != '.':
        try:
            with open(f'{folder_name}/{website}.txt', 'r') as web_page:
                content = web_page.read()
                print(content)
                my_stack.append(website)
        except:
            print('Error: Incorrect URL')
    else:
        formatted_website = website[:-4]

        r = requests.get(f'https://{website}')
        soup = BeautifulSoup(r.text, 'html.parser')
        if not r:
            print('Error: Request fail')

        with open(f'{folder_name}/{formatted_website}.txt', 'w') as web_page:
            for tag in soup.find_all(['p', 'h1', 'a', 'ul', 'ol', 'li']):
                web_page.write(f'\n{tag.get_text()}')
                if tag.name == 'a':
                    print(Fore.BLUE + f'{tag.get_text()}')
                else:
                    print(Fore.WHITE + f'{tag.get_text()}')
        my_stack.append(formatted_website)
