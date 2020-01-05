'''A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.'''

def analyze_the_number(num):
    number = str(num)
    res = [[1, number[0]]]
    
    for i in range(len(str(num))-1):
        current = number[i]
        fnext = number[i+1]
        
        if fnext == current:
            res[-1][0] += 1
        else:
            res.append([1, fnext])
    
    return ''.join([str(figure) for sublist in res for figure in sublist])

def look_and_say(n):
    
    start = 1
    
    for _ in range(n-1):
        res = analyze_the_number(start)
        start = res
    
    return start 

# Other solution:
# ---------------------------------------------------------------------
def look_and_say2(num):
  result = '1'
  
  for _ in range(1, num):
    new_result = ''
    chr = result[0]
    count = 0
    for c in result:
      if chr == c:
        count += 1
      else:
        new_result += str(count) + chr
        count = 1
        chr = c

    result = new_result + str(count) + chr

  return result


print(look_and_say(5))