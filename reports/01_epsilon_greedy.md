
# Experiment 01: Epsilon-Greedy

## 1. Objective
Understand the trade-off between exploration
and exploitation.

## 2. Algorithm
Epsilon-greedy.

## 3. Experimental Settings
- Actions: Attack, Heal, Move
- Action values: 0.6, 0.8, 0.4
- Number of decisions: 10,000

## 4. Results

| Epsilon | Attack | Heal | Move |
|---|---:|---:|---:|
| 0.0 | 0% | 100% | 0% |
| 0.1 | 3.42% | 93.46% | 3.12% |
| 1.0 | 33.46% | 33.73% | 32.81% |

## 5. Conclusion

A larger epsilon increases the probability
of exploration.

When epsilon equals 0, the agent always
chooses the action with the highest estimated value.

When epsilon equals 1, the agent selects
actions randomly.

## 6. Limitations

The action values are manually predefined.
The agent does not update its estimates
based on environmental feedback.
