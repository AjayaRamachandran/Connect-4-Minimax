# Connect-4-Minimax
A Connect Four program and bot that uses a variation of the minimax algorithm to play the game.
---

## Hallmark Features
### 1. Interface
This program has an interface that allows users to play against the bot by clicking.

### 2. Win Detection
The program can detect if either the player or bot has achieved 4 in a row. It can complete the full board analysis in ~5ms, which isn't fast, but most likely fast enough for now.

### 3. Minimax
The module `minimax.py` contained within this program features an implementation of the Minimax algorithm (see function `minimax()`). It is recursive and self-referencing.

### 4. Alpha-Beta Pruning
The module `minimax.py` also contains an implementation of the alpha-beta pruning optimization, which allows the algorithm to simulate far less of the tree than without.

|                              |Iterations    |Time           |
|Crude Minimax (depth: 5)      |approx. 90k   |approx. 4 sec  |
|Crude Minimax (depth: 3)      |approx. 2k    |approx. 0.3 sec|
|Minimax w/AB pruning (d: 5)
