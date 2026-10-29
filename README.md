# Q-Learning Gridworld
```
Best value per cell:
     0    1     2     3
0 -2.3 -0.3   1.9   4.3
1 -0.3  1.9   4.3   7.0
2  1.9  4.3   7.0  10.0
3  4.3  7.0  10.0   0.0

Best action per cell:
       0      1      2     3
0  right  right   down  down
1   down  right  right  down
2   down   down  right  down
3  right  right  right  GOAL
```

## Problem
4x4 grid, start (0,0), goal (3,3) = +10, step cost -2,
hazards: (1,1) = -4, (2,1) and (2,2) = -3.

## Method
Q-learning, epsilon-greedy (0.2), alpha 0.1, gamma 0.9, 3000 episodes.
Update rule: Q = Q + alpha * (target - Q)

## Sample run
(paste the two printed tables here, inside a code block)

## Possible improvements
Decaying epsilon, a larger grid, compare with SARSA.
