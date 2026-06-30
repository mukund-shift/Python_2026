import urllib.request

my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
print(my_request.read())