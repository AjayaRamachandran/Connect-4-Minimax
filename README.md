<p align="center">
  <img alt="Nodes" src="https://i.ibb.co/JrTT8sh/nodes.png" width="140px" />
  <h1 align="center">Connect 4 AI</h1>
</p>

#### A Connect Four program and bot that uses a variation of the minimax algorithm to play the game.

---

## Hallmark Features
### 1. Interface
This program has an interface that allows users to play against the bot by clicking. It uses the PyGame library to draw a very simple board to the screen.

### 2. Minimax (Initial Depth: 4)
The module `minimax.py` contained within this program features an implementation of the Minimax algorithm (see function `minimax()`). It is recursive and self-referencing. After searching the tree, all possible choices the AI can make are given a specific score based on how they are for the AI. 2 leads to an AI win, -1 leads to an AI loss, and 0 means that either the game is full or the tree cannot search far enough down that branch to determine who wins. If there are multiple optimal paths to take, then the AI defaults to a predetermined move order. Initially this move order is just from left to right, but this is in most cases not the most efficient order to search. Without any other optimizations, we can only look 4 moves ahead in a reasonable amount of time.

### 3. Alpha-Beta Pruning - Optimization (Depth: 4 -> 5)
The module `minimax.py` also contains an implementation of the alpha-beta pruning optimization, which allows the algorithm to simulate far less of the tree while not affecting the gameplay decisions. It uses values Alpha and Beta in order to skip searching branches of the tree if the extremes of the values contained within a branch are greater than alpha (maximum value known so far) or less than beta (minimum). This optimization reduces the number of nodes to search, and allows us to increase our search depth from 4 to 5.

### 4. Naive Move Ordering - Optimization (Depth: 5 -> 5)
Since on average better moves are played in the middle of the board, when searching the game tree the algorithm searches the middle columns first, then moves out to the edges. This often finds better moves first, and reduces the size of the game tree searched on average. Because this optimization can be wrong, as in the hard-coded move order is not always the best order to search in either, and that the optimization provides only a 1.5-2x speed boost, it is not enough to increase the simulation depth.

### 5. Optimized Win Detection (Depth: 5 -> 6)
The program can detect if either the player or bot has achieved 4 in a row. The original win detection program (slicing sections of the board and comparing them against hard-coded matrices) completed one full board analysis in ~5 ms, which is not that fast on its own and extremely slow when dealing with the hundreds, or even thousands of analyses we have to do each time we play. With heavy optimization (needle slicing method, removing redundant searches) can complete the full board analysis in ~0.5ms, which is faster. A faster win detection module means that larger portions of the game tree can be searched in less time, allowing us to look more moves ahead. Specifically in this case, the upgrade in speed in the win detection module allowed us to go from looking 5 moves ahead to 6.

### 6. Realistic Win Countering
When the minimax algorithm has declared that all possible AI moves will lead to a player win (we'll call this a "surefire loss"), it will return the same score for each choice it could possibly make. This means that it will default to the Naive Move Order on the occasion of a surefire loss, and the Naive Move Ordering, due to the fact that it is independent from the current game state, will only rarely give the best countering move or even just a good one. In practice, this often looks like the AI has "given up" and just lets the player win once it knows it's going to lose, and this is often not fun for the player. Moreover, this can actually be game-breaking because the AI detects the win assuming optimal play from the player - but the player does not always play optimally, and thus may be given a win that they did not even plan for.

To fix this, if the AI sees a surefire loss when searching `N` moves ahead, it will repeat the search while looking `N - 1` moves ahead. This is done until a surefire loss is no longer detected. Altogether this addition ensures that the AI will now try its best to attempt a victory even when one is not possible, enchancing the experience for the player. However, this is still a problem so we must at the end of the process default to a Naive Win Prevention function, which simply checks to see if any columns on the very next turn can be used for wins and if so blocks them. These failsafes ensure more immersive and realistic play.


## Optimization Specs Chart
|                                  |Nodes Searched|Time Taken             |
|---                               |---           |---                    |
|Crude Minimax (depth: 6)          |approx. 130k  |approx. 71 sec         |
|Crude Minimax (depth: 5)          |approx. 20k   |approx. 10 sec         |
|Crude Minimax (depth: 4)          |approx. 2.8k  |approx. 1.6 sec        |
|Minimax w/AB pruning (depth: 6)   |approx. 2.0k  |approx. 1.3 sec        |
|Minimax w/AB pruning (depth: 5)   |approx. 550   |approx. 550 ms         |
|Minimax w/AB pruning (depth: 4)   |approx. 200   |approx. 200 ms         |
