# Connect-4-Minimax
#### A Connect Four program and bot that uses a variation of the minimax algorithm to play the game.
---

## Hallmark Features
### 1. Interface
This program has an interface that allows users to play against the bot by clicking. It uses the PyGame library to draw a very simple board to the screen.

### 2. Win Detection
The program can detect if either the player or bot has achieved 4 in a row. It can complete the full board analysis in ~0.5ms, which is faster than the previous 5ms.

### 3. Minimax
The module `minimax.py` contained within this program features an implementation of the Minimax algorithm (see function `minimax()`). It is recursive and self-referencing.

### 4. Alpha-Beta Pruning
The module `minimax.py` also contains an implementation of the alpha-beta pruning optimization, which allows the algorithm to simulate far less of the tree while not affecting the gameplay negatively. 

|                                  |Nodes Searched|Time (w/ Win Detection)|
|---                               |---           |---                    |
|Crude Minimax (depth: 6)          |approx. 130k  |approx. 71 sec         |
|Crude Minimax (depth: 5)          |approx. 20k   |approx. 10 sec         |
|Crude Minimax (depth: 4)          |approx. 2.8k  |approx. 1.6 sec        |
|Minimax w/AB pruning (depth: 6)   |approx. 2.0k  |approx. 1.3 sec        |
|Minimax w/AB pruning (depth: 5)   |approx. 550   |approx. 550 ms         |
|Minimax w/AB pruning (depth: 4)   |approx. 200   |approx. 200 ms         |
