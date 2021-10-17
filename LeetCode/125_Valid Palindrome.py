class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = collections.deque()
        
        for word in s:
            if word.isalnum():
                sentence.append(word.lower())
        
        while len(sentence) > 1:
            if sentence.popleft() != sentence.pop():
                return False
            
        return True