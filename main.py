# import re
# from bs4 import BeautifulSoup
# import urllib.request

# def get_corona_usd():
#     headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
#     url = "https://online.unistream.ru/card2cash/?country=GEO&payout_branch=&amount=10&currency=USD&profile=unistream"
#     request = urllib.request.Request(url, headers=headers)
#     response = urllib.request.urlopen(request)
#     soup = BeautifulSoup(response, 'lxml')
#     item = soup.find_all('div', class_='fee-result__label')

#     # course = re.findall(r"[-+]?\d*\.?\d+|\d+", course_str)
#     # return float(course[1])
#     print(item)

# get_corona_usd()

# # print(get_corona_gel())
# print(get_corona_usd())

# a1 = 76.2294
# b1 = 76.0032
# print(b1/a1*-100+100)
# a2 = 29.59184
# b2 = 29.54661
# print(b2/a2*-100+100)
# a3 = 80.598
# b3 = 80.4783
# print(b3/a3*-100+100)
# # 0.29673590504449976
# # 0.1528461900307576
# # 0.14851485148513177

# a1 = 76.10003
# b1 = 76.10003
# print(b1/a1*-100+100)
# a2 = 29.69387
# b2 = 29.6485
# print(b2/a2*-100+100)
# a3 = 81.204
# b3 = 81.0834
# print(b3/a3*-100+100)
# 0.0
# 0.15279247871698942
# 0.14851485148514598

# a1 = 76.836  # USD
# b1 = 76.608
# print(b1/a1*-100+100)
# a2 = 29.69387  # GEL
# b2 = 29.6485
# print(b2/a2*-100+100)
# a3 = 81.305  # EURO
# b3 = 81.18425
# print(b3/a3*-100+100)
# 0.29673590504449976
# 0.15279247871698942
# 0.14851485148514598

a1 = 76.836  # USD
b1 = 76.608
print(b1/a1*-100+100)
a2 = 29.69387  # GEL
b2 = 29.6485
print(b2/a2*-100+100)
a3 = 81.305  # EURO
b3 = 81.18425
print(b3/a3*-100+100)
0.29673590504449976
0.15279247871698942
0.14851485148514598