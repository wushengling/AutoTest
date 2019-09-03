#闭包  事例
# 现场
# 尽可能少的使用全局变量
#非闭包操作
origin = 0
def go(step):
    global origin    # global 声明为全局变量
    new_pos = origin + step
    origin = new_pos
    return origin

print(go(2))
print(go(3))
print(go(6))

# 闭包操作
def factory(pos):
    def go(step):
        nonlocal pos     # nonlocal 声明为本地变量
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go
f = factory(0)
print(f(2))
print(f(3))
print(f(6))
