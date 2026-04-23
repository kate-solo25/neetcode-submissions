class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tags_dictionary = {
        ")": "(",
        "]": "[", 
        "}":"{"
        }
    
        for tag in s:
            if tag in tags_dictionary.values():
                stack.append(tag)
            elif tag in tags_dictionary.keys():
                if stack == [] or tags_dictionary[tag] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        