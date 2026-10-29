import numpy as np
import pandas as pd

# ---------- design (same as before) ----------
rewards = np.full((4, 4), -2)
rewards[1, 1] = -4
rewards[2, 1] = -3
rewards[2, 2] = -3
rewards[3, 3] = 10

gamma = 0.9
alpha = 0.1        # learning rate
epsilon = 0.2     # chance of exploring original 0.2
actions = ["up", "down", "left", "right"]

def next_cell(row, col, action):
    if action == "up":
        row = row - 1
    elif action == "down":
        row = row + 1
    elif action == "left":
        col = col - 1
    elif action == "right":
        col = col + 1
    row = max(0, min(3, row))
    col = max(0, min(3, col))
    return row, col

# ---------- Q-learning ----------
rng = np.random.default_rng(0)
Q = np.zeros((4, 4, 4))            # Q[row, col, action]

for episode in range(3000):
    r, c = 0, 0                    # every trip starts at (0,0)
    for step in range(200):
        # explore or exploit (epsilon-greedy)
        if rng.random() < epsilon:
            a = int(rng.integers(4))           # random move
        else:
            a = int(np.argmax(Q[r, c]))        # best known move

        nr, nc = next_cell(r, c, actions[a])
        reward = rewards[nr, nc]

        if (nr, nc) == (3, 3):
            target = reward                    # trip ends, nothing after
        else:
            target = reward + gamma * np.max(Q[nr, nc])  # Bellman target: reward + discounted best next value

        Q[r, c, a] = Q[r, c, a] + alpha * (target - Q[r, c, a])  # Q-update: move old value toward target by alpha

        r, c = nr, nc
        if (r, c) == (3, 3):
            break

# ---------- read the result ----------
V = Q.max(axis=2)
V[3, 3] = 0

print("Best value per cell:")
print(pd.DataFrame(np.round(V, 1)))
policy = [["GOAL" if (r, c) == (3, 3) else actions[int(np.argmax(Q[r, c]))]
           for c in range(4)] for r in range(4)]
print("Best action per cell:")
print(pd.DataFrame(policy))
