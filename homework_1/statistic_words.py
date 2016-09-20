import heapq
import re
from collections import OrderedDict

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority,  item))

    def pop(self):
        return heapq.heappop(self._queue)


def para_file(file_name,lang):
    if lang == 'en':
        com = re.compile(r'\w+\b')
    else:
        com = re.compile(r'\w')
    with open(file_name) as f:
        words_count={}
        for i in f.readlines():
            words = com.findall(i)
            for i in words:
                if i not in words_count.keys():
                    words_count[i] = 1
                else:
                    words_count[i] +=1
    return words_count


def words_to_queue(words):
    pq = PriorityQueue()
    for k ,v in words.items():
        pq.push(k,v)
    return pq

def get_top_k(k,pq):
    topk = OrderedDict()
    for _ in range(k):
        i = pq.pop()
        topk[i[1]] = i[0] * -1
    return topk


if __name__ == '__main__':
    words_dict=para_file('words_cn.txt','chin')
    words_pq = words_to_queue(words_dict)
    print(get_top_k(10,words_pq))

