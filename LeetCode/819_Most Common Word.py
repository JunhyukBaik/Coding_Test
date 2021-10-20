class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        count_dic = collections.defaultdict(int)
        words = [word for word in paragraph.lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        return counts.most_common()[0][0]