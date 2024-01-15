import heapq
from collections import Counter

class Pair:
  def __init__(self,word,freq):
    self.word = word
    self.freq = freq
  
  def __lt__(self,pair):
    
    if self.freq==pair.freq:
      return self.word<pair.word # lexical order
    
    return self.freq<pair.freq


if __name__=="__main__":
    lst = ["i","love","leetcode","i","love","coding"]
    lstCnts = Counter(lst)
    min_heap = []
    heapq.heapify(min_heap)

    for word,cnt in lstCnts.items():
        heapq.heappush(min_heap,Pair(word,cnt))

    while min_heap:
       elem = heapq.heappop(min_heap)
       print(elem.word,elem.freq)
    


