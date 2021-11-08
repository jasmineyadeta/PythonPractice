# first non repeating character question
# input type = string
# string contains only lowercase english letters
# not worrying about empty strings, but there can be strings with no repeating characters
# length 1 - n
# ex. input: abcbad output: c
# brute force, double for loop with if statement identify first character, compare with upcoming indexes (O(n^2))
# a hashmap??

def firstNonRepeatingChar(string_provided):
   char_order = []
   counts = {}
   for c in string_provided:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
       if counts[c] == 1:
        return c
   return None

print(firstNonRepeatingChar('abcbad'))
print(firstNonRepeatingChar('applebottomjeansbootswiththefur'))
print(firstNonRepeatingChar('abcdabcd'))
