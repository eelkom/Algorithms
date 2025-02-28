import sys

e, s, m = map(int, sys.stdin.readline().strip().split())
year = e

while year:
    # 잘못된 방식: year % 28 == s
    # 이 방식은 "나머지가 s와 정확히 같아야 함" 을 의미합니다.
    # 문제는 나머지 연산의 결과는 항상 0부터 27까지 이므로, s = 28일 때 이 조건은 절대 참이 될 수 없습니다.
    if (year - s) % 28 == 0 and (year - m) % 19 == 0:
        break
    year += 15

print(year)