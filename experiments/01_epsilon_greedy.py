import random
# Available actions
actions=["move","attack","heal"]
# Estimated action values
actions_values={
    "move":0.4,
    "attack":0.6,
    "heal":0.8
}
# Exploration probability
EPSILON = 1
# epsilon,1-epsilon
def select_action(action_values, epsilon):
    r=random.random()
    if r<epsilon:
       return random.choice(list(action_values.keys()))
    #list(action_values.key())is an element in the item
    else:return max(action_values, key=action_values.get)
for _ in range(10):
    action = select_action(actions_values, EPSILON)
    print(action)

from collections import Counter

results = Counter()

for _ in range(10000):
    action = select_action(actions_values, EPSILON)
    results[action] += 1

for action, count in results.items():
    print(f"{action}: {count / 10000:.2%}")
