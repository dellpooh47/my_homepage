import random

print("じゃんけん、ぽん")

janken_ai = random.randint(0, 2)

if janken_ai == 0:
　print("じゃんけんAI：グーです。")
elif janken_ai == 1:
　print("じゃんけんAI：チョキです。")
elif janken_ai == 2:
　print("じゃんけんAI：パーです。")