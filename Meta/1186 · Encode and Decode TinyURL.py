import random
class Solution:
    def __init__(self):
        self.l2id = dict()
        self.s2l = dict()
    """
    @param longUrl: 
    @return: nothing
    """
    def encode(self, longUrl):
        # 
        url_id = str(random.randint(1, 100))
        short_url = 'http://tinyurl.com/' + url_id
        self.l2id[longUrl] = url_id
        self.s2l[short_url] = longUrl
        return short_url


    """
    @param shortUrl: 
    @return: nothing
    """
    def decode(self, shortUrl):
        #
        return self.s2l[shortUrl]
