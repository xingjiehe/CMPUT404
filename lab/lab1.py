import requests
r = requests.get('https://raw.githubusercontent.com/xingjiehe/CMPUT404/master/lab/lab1.py')
print(r.text)