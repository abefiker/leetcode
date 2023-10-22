class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_count = {}
        magazine_count = {}
        for char in ransomNote:
            ransomNote_count[char] = ransomNote_count.get(char , 0) + 1
        for char in magazine:
            magazine_count[char] = magazine_count.get(char , 0) + 1   
        for char , count in ransomNote_count.items():
            if magazine_count.get(char , 0 ) < count:
                return False
        return True        