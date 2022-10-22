University of Queensland || COMP3702 A3 HexBot

## Reinforcement Learning

Using Q-Learning and SARSA algorithms to compute an optimal path to solve the a non-deterministic environment.

### Components
**Solution**: An environment is solved when HexBot reaches the target cells.

**Environment**: A hexagonal grid, indexed by (row, col) coordinates.

<img width="266" alt="image" src="https://user-images.githubusercontent.com/92434786/197333598-8600f2c0-9169-48a3-bd4b-afc15eb9dafe.png">

- Obstacles & Hazards: collisions with these cells result in a penalty/negative reward. Represented with 'X', '!' respectively.
- Targets: Cells marked with 'tgt', in which the agent is to occupy.

**Robot**: HexBot, the agent, occupies a single cell. It has four possible nominal actions: forwards, reverse, spin left, spin right.
