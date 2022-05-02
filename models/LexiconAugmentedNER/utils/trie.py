import collections


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        '''
        这个地方的插入，输入的是一个词组，如“二十四史”,通过遍历，将单个字依次插入。
        然后设置is_word属性是True
        '''
        current = self.root
        for letter in word:
            # print("type{},letter:{}".format(type(letter), letter))
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        '''
        search word list中每一个汉字是否属于一个word
        返回Boolean值：如果get(letter)没有从self.children字典中找到word，返回false，否则True；
        '''
        current = self.root
        # open('/home/lixu/baseline_ner/LexiconAugmentedNER/data/children.json', 'w').write(str(current.children.items()))
        for letter in word:
            # print("special current:{}".format(current.children.items()))
            current = current.children.get(letter)
            # current 返回查询后的一个对象<元，"one source">
            # print("search letter {}, rest {}".format(letter, type(current)))
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

    def enumerateMatch(self, word, space="_", backward=False):  #space=‘’
        matched = []

        while len(word) > 0:
            # print("search result {}".format((word)))
            if self.search(word):
                # search的结果都是返回false，只有到“陈元”的时候才返回false，进而控制matched的结果
                matched.append(space.join(word[:]))
                # print("each time value{}".format(matched))
            del word[-1]
        # 返回样例： ['我是中国人', '我是中国', '我是中', '我是', '我']
        return matched
