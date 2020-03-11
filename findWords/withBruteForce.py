
import time

def brute_find_words(N,words,x):
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
        
        if ((sum1 == words[k]) or #right 1
            (sum2 == words[k]) or #bottom 2
            (sum3 == words[k]) or #right bottom 3
            (sum4 == words[k]) or #left 4
            (sum5 == words[k]) or #top 5
            (sum6 == words[k]) or #left top 6
            (sum7 == words[k]) or #left bottom 7
            (sum8 == words[k])):  #right top 8
          match.add(words[k])
    # print(match)
  return match

def main():
  N = int(input())
  words = list(input().split(" "))
  x = [list(input().split(" ")) for y in range(N)]
  brute_find_words(N,words,x)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

