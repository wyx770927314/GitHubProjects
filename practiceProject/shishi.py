def shixiangshigedashabi(list):
    sum = 0
    jishu_sum = 0
    for i in list:
        sum += i
    for index, value in enumerate(list):
        if index % 2 == 0:
            jishu_sum += value
    if sum - jishu_sum > jishu_sum:
        return sum - jishu_sum
    else:
        return jishu_sum


if __name__ == '__main__':
    a = shixiangshigedashabi([5,6,7,8])
    print(a)
