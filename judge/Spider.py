import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from submission.models import Submission, JudgeStatus


class Spider(object):
    def __init__(self, username):
        self.username = username

    def check_database(self):
        """
        check the database to confirm all the submissions have been judged
        :return: the list of unfinished submissions
        """
        raise NotImplementedError

    def get_result(self, *args, **kwargs):
        raise NotImplementedError


class HduSpider(Spider):

    def check_database(self):
        submissions = Submission.objects.filter(result=JudgeStatus.STATUS[JudgeStatus.PENDING])
        print(submissions)
        if submissions:
            return self.get_result(submissions)
        else:
            return 1000

    def get_result(self, dest):
        """
        update the database
        :param dest:
        :return:
        """
        url = 'http://acm.hdu.edu.cn/status.php?user=' + self.username
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.findAll('table')[-2].findAll("tr")
        tds = BeautifulSoup(str(trs), 'lxml').findAll('td')
        cnt = dest.count()
        print(url)
        for i in range(9, len(tds), 9):
            print(i)
            run_id = tds[i].string
            judge_status = tds[i + 2].string
            exe_time = tds[i + 4].string
            exe_memory = tds[i + 5].string
            code_len = tds[i + 6].string
            obj = dest.filter(hdusubmission__hdu_run_id=run_id)
            if obj:
                obj.update(
                    result=judge_status,
                    exe_memory=exe_memory,
                    exe_time=exe_time,
                    code_len=code_len)
                cnt -= 1
        return cnt
