from collections import Counter


class Solution:
    # Time: O(nm) m: the length of magazine, n: the length of ransomNote
    # Space: O(m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteLength = len(ransomNote)
        magazineLength = len(magazine)

        if noteLength > magazineLength:
            return False

        for char in ransomNote:
            if char not in magazine:
                return False
            index = magazine.find(char)
            if index > 0:
                magazine = magazine[0:index] + magazine[index + 1 :]
            elif index == 0:
                magazine = magazine[1:]

        return True

    # Time: O(m) m: the length of magazine, n: the length of ransomNote
    # Space: O(1)
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        noteLength = len(ransomNote)
        magazineLength = len(magazine)

        if noteLength > magazineLength:
            return False

        occurrenceNote = {}

        for char in ransomNote:
            if char in occurrenceNote:
                occurrenceNote[char] += 1
            else:
                occurrenceNote[char] = 1

        for char in magazine:
            if char in occurrenceNote:
                occurrenceNote[char] -= 1

        for key in occurrenceNote:
            if occurrenceNote[key] > 0:
                return False

        return True

    # Time: O(m) m: the length of magazine
    # Space: O(1)
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        noteLength = len(ransomNote)
        magazineLength = len(magazine)

        if noteLength > magazineLength:
            return False

        ransomNoteCounter = Counter(ransomNote)
        magazineCouneter = Counter(magazine)

        for char in ransomNote:
            if ransomNoteCounter[char] > magazineCouneter[char]:
                return False
        return True

    # Time: O(m) m: the length of magazine
    # Space: O(1)
    def canConstruct4(self, ransomNote: str, magazine: str) -> bool:
        noteLength = len(ransomNote)
        magazineLength = len(magazine)

        if noteLength > magazineLength:
            return False

        magazineCouneter = Counter(magazine)

        for char in ransomNote:
            if magazineCouneter[char] <= 0:
                return False
            magazineCouneter[char] -= 1

        return True

    # Time: O(mlogm) m: the length of magazine
    # Space: O(m)
    def canConstruct5(self, ransomNote: str, magazine: str) -> bool:
        noteLength = len(ransomNote)
        magazineLength = len(magazine)

        if noteLength > magazineLength:
            return False

        ransomNoteList = sorted(ransomNote, reverse=True)
        magazineList = sorted(magazine, reverse=True)

        while ransomNoteList and magazineList:

            if ransomNoteList[-1] == magazineList[-1]:
                ransomNoteList.pop()
                magazineList.pop()

            elif ransomNoteList[-1] > magazineList[-1]:
                magazineList.pop()

            else:
                return False

        return len(ransomNoteList) == 0
