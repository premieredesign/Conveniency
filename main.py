#!/usr/bin/python

import os
import webbrowser
import shutil
from multiprocessing import Pool


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


def who_am_i():
    return os.popen('whoami').read().strip()


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
        processes = f"open_{i}.py"
        with Pool(processes=3) as pool:
            pool.map(run_process, processes)
        open_url(url)



