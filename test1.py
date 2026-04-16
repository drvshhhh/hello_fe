import time

for i in range(10):
    print(f"i={i} ", end="") # 0 - 9

for i in range(101):
    print(f"\r正在加载{i}% ", end="")
    time.sleep(0.02)

print("\n加载完成！")
