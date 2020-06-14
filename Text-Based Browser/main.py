import sys
import os
from collections import deque

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
args = sys.argv
folder_name = str(args[1])
os.makedirs(folder_name, exist_ok=True)

my_stack = deque()

while True:
    website = input()
    if website == 'exit':
        break
    elif website == 'back':
        my_stack.pop()
        if my_stack[0] == 'bloomberg':
            print(bloomberg_com)
        else:
            print(nytimes_com)
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
        if website == 'bloomberg.com':
            with open(f'{folder_name}/{formatted_website}.txt', 'w') as web_page:
                web_page.write(bloomberg_com)
            print(bloomberg_com)
            my_stack.append(formatted_website)
        elif website == 'nytimes.com':
            with open(f'{folder_name}/{formatted_website}.txt', 'w') as web_page:
                web_page.write(nytimes_com)
            print(nytimes_com)
            my_stack.append(formatted_website)
        else:
            print('Error: Unknown website')
