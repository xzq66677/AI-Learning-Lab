This is the first note about ai agent learning.
$$Date:2026.11.24$$
Basic Concepts:1.Agent 2.State 3.action 4.reward

1.policy: How to find the optimal solution in a specific environment？
policy acts as a function: action=policy under state  
$$\pi(a=\pi(s)$$
first kind:(确定性策略) Deterministic$$ $$Strategy
the second kind:(随机性决策)Stochastic Policy
$$\pi(a\mid s)=P(A=a\mid S=s)$$

2.find a balance	  
        Exploration（探索）	Exploitation（利用）
行为	尝试其他动作	     选择目前最好的动作
目的	获取新的信息	     获取更好的当前收益
优点	可能发现更优策略	 利用已有经验
缺点	可能损失当前收益	 可能错过更优策略

3.first algorithm： greedy algorithm
\epsilon is a number between 0 and 1
algorithm is simple：
- 以 \(\varepsilon\) 的概率choose an action randomly。(also the action includes current best action )
- 以 \(1-\varepsilon\) 的概率选择current best action。

Pseudocode:
Generate a random number r between 0 and 1

IF r < epsilon:
    Choose a random action
ELSE:
    Choose the best known action

    Epsilon Decay:
    初期：多探索，积累经验。
中期：逐渐减少探索，利用已有经验。
后期：更多利用已经学到的策略，但仍可以保留少量探索。
当前算法的一个重要局限：它只会利用已有估计，却不会主动纠正错误估计