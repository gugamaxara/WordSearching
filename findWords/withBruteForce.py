# N = int(input())
# wordArray = list(input().split(" "))
# matrix = [list(input().split(" ")) for y in range(N)]
# print(matrix[0][0])
# for i in range(N):
#   for j in range(N):
#     for k in range(N):
#       print (matrix[i][j][j : k])

# words = ["fe", "ae", "eq", "ef", 'af', 'afe', 'abc', 'c', 'qfc', 'efa', 'ad', 'ab', 'ac', 'cb', 'bc', 'da']
# words = ['ad']
# N = 3
# x = [['a', 'b', 'c'], 
#     ['e', 'f', 'g'],
#     ['q', 'w', 'e']]
# x = [['a', 'b'],
#       ['c', 'd']]
# for i in range(N):
#   for j in range(len(words)):
#     if ((i < N and (x[i][0] + x[i + 1][0] == words[j]) or
#        (i < N and x[i][0] + x[i][1] == words[j]) or
#        (i < N  and x[i][0] + x[i + 1][1] == words[j]))):

#       match.append(words[j])
import time

def main():
  N = int(input())
  words = list(input().split(" "))
  x = [list(input().split(" ")) for y in range(N)]
  match = set()

  for i in range(N):
    for j in range(N):
      for k in range(len(words)):
            # print('------------')
        sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8 = "", "", "", "", "", "", "", ""
        for z in range(len(words[k])):
          if j < N - z:
            sum1 += x[i][j + z]
          if i < N - z:
            sum2 += x[i + z][j]
          if i < N - z and j < N - z:
            sum3 += x[i + z][j + z]
          if j >= z:
            sum4 += x[i][j - z]
          if i >= z:
            sum5 += x[i - z][j]
          if i >= z and j >= z:
            sum6 += x[i - z][j - z]
          if i >= z and j < N - z:
            sum7 += x[i - z][j + z]
          if i < N - z and j >= z:
            sum8 += x[i + z][j - z]
        
        if ((sum1 == words[k]) or #marjvena 1
            (sum2 == words[k]) or #qveda 2
            (sum3 == words[k]) or #marjvena qveda 3
            (sum4 == words[k]) or #marcxena 4
            (sum5 == words[k]) or #zeda 5
            (sum6 == words[k]) or #marcxena zeda 6
            (sum7 == words[k]) or #marcxena qveda 7
            (sum8 == words[k])):  #marjvena zeda 8
          match.add(words[k])
  print(match)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

# if ((j < N - 1 and x[i][j] + x[i][j + 1] == words[k]) or #marjvena 1
#           (i < N - 1 and x[i][j] + x[i + 1][j] == words[k]) or #qveda 2
#           (i < N - 1 and j < N - 1 and x[i][j] + x[i + 1][j + 1] == words[k]) or #marjvena qveda 3
#           (j > 1 and x[i][j] + x[i][j - 1] == words[k]) or #marcxena 4
#           (i > 1 and x[i][j] + x[i - 1][j] == words[k]) or #zeda 5
#           (i > 1 and j > 1 and x[i][j] + x[i - 1][j - 1] == words[k]) or #marcxena zeda 6
#           (i > 1 and j < N - 1 and x[i][j] + x[i - 1][j + 1] == words[k]) or #marcxena qveda 7
#           (i < N - 1 and j > 1 and x[i][j] + x[i + 1][j - 1] == words[k])):  #marjvena zeda 8