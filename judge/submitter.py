from urllib.request import urlopen

from bs4 import BeautifulSoup

from utils.exceptions import *

import requests

class Submitter(object):
    def __init__(self):
        pass

    def login(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def is_login_in(self):
        raise NotImplementedError

    def submit(self, *args, **kwargs):
        raise NotImplementedError


class HduSubmitter(Submitter):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        }
        self.session.headers.update(headers)

    def login(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        url = 'http://acm.hdu.edu.cn/userloginex.php?action=login'
        data = {
            "username": username,
            "userpass": password,
            'login': 'Sign In',
        }
        ret = self.session.post(url, data=data)
        return ret.status_code

    @property
    def is_login_in(self):
        r = self.session.get("http://acm.hdu.edu.cn/control_panel.php")
        return r.status_code == 200

    def submit(self, *args, **kwargs):
        print('submit')
        url = 'http://acm.hdu.edu.cn/submit.php?action=submit'
        language = kwargs['language']
        code = kwargs['code']
        problem = kwargs['problem']
        print(language)
        print(code)
        print(problem)
        data = {
            'check': 0,
            'problemid': str(problem),
            'language': str(language),
            'usercode': code
        }
        ret = self.session.post(url, data=data)
        print(ret.status_code)
        return ret.status_code

    def get_run_id(self, username):
        url = 'http://acm.hdu.edu.cn/status.php?user=' + username
        print(url)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        try:
            run_id = int(soup.findAll('table')[-2].findAll("tr")[1].td.string)
            return run_id
        except:
            raise GetRunIdFailed("BS4ERROR")
