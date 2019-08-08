#!/usr/bin/python

import os
import webbrowser
import shutil
import optparse
import random
import string
import click
import hashlib
import re
from multiprocessing import Pool
from cryptography.fernet import Fernet

apps_list = ['slack', 'webstorm', 'github desktop']

url = [
    'https://www.icloud.com/#mail',
    'https://mail.google.com/mail/u/0/#inbox',
    'https://app.zeplin.io/project/5c82cb40af86007b4377b013',
    'https://calendar.google.com/calendar/r?tab=mc',
    'https://stockx-services.atlassian.net/secure/RapidBoard.jspa?rapidView=71&projectKey=WEB&selectedIssue=BS-19&sprint=553',
    'https://stockx-services.atlassian.net/secure/RapidBoard.jspa?rapidView=71&projectKey=WEB&sprint=557',
    'https://www.youtube.com/',
    'https://github.com/stockx/iron'
]


# Used for looping through urls and opening them in browser
def open_url(urls):
    for u in urls:
        webbrowser.open_new_tab(u)


# User for Running processes
def run_process(process):
    os.system(f'python apps/{process}')


# Used for creating/writing and moving files in folder
def automate_file_creation(i):
    with open(f"open_{i}.py", "w+") as f:
        f.write(
            f'''
            import subprocess

            def open_app():
                subprocess.call(
                    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/{i.capitalize()}.app"]
                )

            open_app()''')
        f.close()
        shutil.move(f"open_{i}.py", f"./apps/open_{i}.py")
        # processes = f"open_{i}.py"
        # with Pool(processes=3) as pool:
        #     pool.map(run_process, processes)
        # open_url(url)


def get_arguments():
    return click.prompt('Enter the name of the apps you want Convinence to open')
    # parser = optparse.OptionParser()
    # parser.add_option("-n", "--name", dest="app_name", help="Enter name for the app you want to generate password for")
    # (options, arguments) = parser.parse_args()
    # if not options.open_apps:
    #     parser.error('''
    #     [-] Please enter the name of the app that you want to generate password for, and we will take care of the rest
    #     ''')
    # return options


def create_random_password(for_length=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(for_length))


def encrypt_password():
    return create_random_password(10)


def make_it(app_name):
    if os.path.isfile('password_keeper.txt'):
        with open(f"password_keeper.txt", "a+") as f:
            f.write(f'{app_name}: {encrypt_password()}')
            f.close()
    else:
        with open(f"password_keeper.txt", "w+") as f:
            f.write(f'{app_name}: {encrypt_password()}')
            f.close()


def main():
    if os.path.isdir('./apps'):
        print("Directory exist")
    else:
        app_name = get_arguments()
        make_it(app_name)
        # text = os.system('openssl rand -base64 16 | colrm 17')
        # a_list = []
        # a_list.append(text)
        # print(a_list)

        # os.mkdir('./apps')
        # text = click.prompt('Enter the name of the apps you want Convinence to open', apps)
        # apps_list.append(f"{text}")
        # print(apps_list)
        # for i in apps_list:
        #     automate_file_creation(i)


if __name__ == "__main__":
    main()


