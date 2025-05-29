import random

def pick_six_pairs() -> list[tuple[int, int]]:
    # 1~16 중 서로 다른 12개 숫자 추출, 중복없이 12개 한번에 뽑기
    nums = random.sample(range(1, 17), k=12)
    print(nums) # [9, 3, 11, 5, 4, 1, 15, 7, 14, 10, 12, 2]
    # 인접한 두 개씩 묶어 6개의 (a, b) 형태 튜플 생성
    return list(zip(nums[::2], nums[1::2]))
    # [(9, 3), (11, 5), (4, 1), (15, 7), (14, 10), (12, 2)]

if __name__ == "__main__":
    pairs = pick_six_pairs()
    print(pairs)



