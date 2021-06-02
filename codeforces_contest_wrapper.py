from lxml import html 
import requests 


def parse_contest(contest_link):
    page = requests.get(contest_link)
    tree = html.fromstring(page.content)
    contest = {
        "contest_id": get_contest_id(tree),
        "contest_name": get_contest_name(tree),
        "contest_link": get_contest_link(tree),
        "problems": get_problems(tree),
        "editorial": get_editorial(tree),
        "announcement": get_announcement(tree),
    }
    return contest

def get_announcement(tree):
    announcement = tree.xpath('//*[@id="sidebar"]/div[4]/ul/li[1]/span[1]/a/@href')
    return announcement[0] if len(announcement) else ""

def get_editorial(tree):
    editorial = tree.xpath('//*[@id="sidebar"]/div[4]/ul/li[2]/span[1]/a/@href')
    return editorial[0] if len(editorial) else ""

def get_contest_name(tree):
    contest_name = tree.xpath('//*[@id="sidebar"]/div[1]/table/tbody/tr[1]/th/a/text()')
    return contest_name[0] if len(contest_name) else ""

def get_contest_link(tree):
    contest_link = tree.xpath('//*[@id="sidebar"]/div[1]/table/tbody/tr[1]/th/a/@href')
    return contest_link[0] if len(contest_link) else ""

def get_contest_id(tree):
    contest_link = tree.xpath('//*[@id="sidebar"]/div[1]/table/tbody/tr[1]/th/a/@href')
    return int(contest_link[0].split('/')[2]) if len(contest_link) else 0

def get_problems(tree):
    problems = []

    problem_links = tree.xpath('//*[@class="problems"]/tr/td[2]/div/div[1]/a/@href')
    problem_names = tree.xpath('//*[@class="problems"]/tr/td[2]/div/div[1]/a/text()')

    for i in range(len(tree.xpath('//*[@class="problems"]/tr/td[2]/div/div[1]/a/text()'))):
        problem = {}
        problem["problem_id"] = problem_links[i].split('/')[4]
        problem["contest_id"] = int(problem_links[i].split('/')[2])
        problem["name"] = problem_names[i]
        problem["problem_link"] = problem_links[i]
        
        problems.append(problem)
    
    return problems
