#!/usr/bin/python

import os
import webbrowser
import shutil
import click
import psutil
from os import listdir
from os.path import isfile, join
from multiprocessing import Pool


apps_list = []

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


def who_am_i():
    return os.popen('whoami').read().strip().capitalize()


def open_apps(app_name):
    with open(f"{app_name}.py", "w+") as f:
        f.write(f'''
import subprocess


def open_app():
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/{app_name}.app"])


if __name__ == '__main__':
    open_app()''')
        f.close()


def write_automation(i):
    app_name = i.lower()
    prog_name = i.title()
    if ' ' in i:
        open_apps(prog_name)
    else:
        open_apps(prog_name)
    if os.path.isdir('./apps'):
        if ' ' in app_name:
            remove_space = app_name.lower().split(' ')
            new_app_name = "_".join(remove_space)
            return shutil.move(f"{app_name}.py", f"./apps/{new_app_name}.py")
        else:
            return shutil.move(f"{app_name}.py", f"./apps/{app_name}.py")
    else:
        os.mkdir('./apps')
        if ' ' in app_name:
            remove_space = app_name.lower().split(' ')
            new_app_name = "_".join(remove_space)
            return shutil.move(f"{app_name}.py", f"./apps/{new_app_name}.py")
        else:
            return shutil.move(f"{app_name}.py", f"./apps/{app_name}.py")


# Used for looping through urls and opening them in browser
def open_url(urls):
    for u in urls:
        webbrowser.open_new_tab(u)


# User for Running processes
def run_process(process):
    os.system(f'python ./apps/{process}')


def main():
    if not os.path.isdir('./apps'):
        add_to_apps = click.prompt(f'Hi {who_am_i()}, please type the name of the app you want to open')
        write_automation(add_to_apps)
        open_now = click.prompt(f'Would you like {add_to_apps} to open now (Y) or (N)')
        if open_now.lower() == 'y':
            get_apps_to_open = [f for f in listdir('apps') if isfile(join('apps', f))]
            pool = Pool(processes=len(get_apps_to_open))
            pool.map(run_process, get_apps_to_open)
            open_url(url)
            print('Opening...')
        else:
            continue_adding_apps = click.prompt('Would you like to add more (Y) or (N)')
            while continue_adding_apps.lower() == 'y':
                names_to_add = click.prompt('Please tell me the name of the app you want to add or (D) for Done')
                if names_to_add.lower() == 'd':
                    break
                else:
                    write_automation(names_to_add)
            print('Thank you, I have created files for the names of the apps you requested')
    else:
        add_to_apps = click.prompt(f'Hi {who_am_i()}, would you like to add to your current list of Apps to open (Y) or (N)')
        if add_to_apps.lower() == 'y':
            names_to_add = click.prompt('Please tell me the name of the app you want to add')
            write_automation(names_to_add)
            continue_adding_apps = click.prompt('Would you like to add more (Y) or (N)')
            while continue_adding_apps.lower() == 'y':
                names_to_add = click.prompt('Please tell me the name of the app you want to add or (D) for Done')
                if names_to_add.lower() == 'd':
                    break
                else:
                    write_automation(names_to_add)
            print('Thank you, I have created files for the names of the apps you requested')
        else:
            open_the_apps = click.prompt('Would you like to open current apps (Y) or (N)')
            if open_the_apps.lower() == 'y':
                print('Opening apps....')
                open_url(url)
                get_apps_to_open = [f for f in listdir('apps') if isfile(join('apps', f))]
                pool = Pool(processes=len(get_apps_to_open))
                pool.map(run_process, get_apps_to_open)
            else:
                print('Thank you, enjoy your day')


if __name__ == '__main__':
    main()
