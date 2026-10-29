# Q-Learning Gridworld
One line: what the agent learns.

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
