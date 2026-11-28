# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        


        def getHostname(url):
            return url.split("/")[2]
        visited = {startUrl}
        queue = deque([startUrl])
        result = []
        hostname = getHostname(startUrl)
        while queue:
            url = queue.popleft()
            result.append(url)

            other_urls = htmlParser.getUrls(url)

            for u in other_urls:
                if u not in visited and getHostname(u) == hostname:
                    queue.append(u)
                    visited.add(u)

        return result
