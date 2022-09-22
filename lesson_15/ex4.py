
from urllib.parse import urlparse

url_data = urlparse('https://www.youtube.com/watch?v=RRW2aUSw5vU')
print(url_data.query[2::])

# url_data = 'https://www.youtube.com/watch?v=kwj8i2TOmgE'
# print(url_data[url_data.index('=') + 1:])


