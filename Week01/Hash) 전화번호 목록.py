# https://programmers.co.kr/learn/courses/30/lessons/42577
# Solved.

def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book, key=len)

    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]: return False

    return answer


if __name__ == "__main__":
    print(solution(['119', '97674223', '1195524421']))
    print(solution(['123', '456', '789']))