import requests
import random

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]
# URL
url = 'http://detected.altervista.org/ATTLOGIN/login.php'
# Number of spam calls
spamcalls = 100

# Payload format
def makePayload(user, pwd):
    return {
        "email": user,
        "password": pwd
    }


def adjustPasswords(pwd):
    while len(pwd) < 8:
        pwd = pwd + str(int(random.uniform(0,100)))
    if pwd[0].isalpha():
        return pwd[0].upper() + pwd[1:];
    return "Password" + pwd

with open('first-names.txt') as f:
    firstnames = list(f)
with open('last-names.txt') as f:
    lastnames = list(f)
with open('1000-most-common-passwords.txt') as f:
    passwords = list(f)
firstnames = list(map((lambda s: s.replace('\n','').lower()), firstnames))
lastnames = list(map((lambda s: s.replace('\n','').lower()), lastnames))
passwords = list(map(adjustPasswords, map((lambda s: s.replace('\n','')), passwords)))

joining=['','.','-','_']
providers=['gmail','yahoo','aol','mail','outlook', 'icloud']

def makeRandomMailAddress():
    fst = random.choice(firstnames)
    snd = random.choice(lastnames)
    join = random.choice(joining)
    provider = random.choice(providers)
    m = ""
    if random.uniform(0,1) > 0.75:
        m = m + fst[0] + snd
    else:
        m = m + fst + join + snd

    if random.uniform(0,1) > 0.75:
        if random.uniform(0,1) > 0.5:
            ryear = str(int(random.uniform(1950, 2010)))
        else:
            ryear = str(int(random.uniform(0,99)))
        m = m + ryear

    return m + "@" + provider + ".com"


for i in range(0,spamcalls):
    
    mail = makeRandomMailAddress()
    pwd = random.choice(passwords)
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    data = makePayload(mail,pwd)
    response = requests.post(url, data=data, headers=headers).status_code
    i += 1
    print("%s - %s %s (%s)" % (i, mail, pwd, response))
