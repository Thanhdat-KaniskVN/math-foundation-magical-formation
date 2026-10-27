# Core Concepts from MIT 6.1200J (Lecture 04)

This document summarizes the theoretical foundations applied in this project, based on **MIT 6.1200J Lecture 04: State Machines**.

## 1. State Machine Definition
> *"A state machine is defined by a collection of states, a specified initial state, and for each state a list of possible transitions."* (MIT Lecture 04)

In our Python implementation:
*   **States:** `IDLE` (money = 0), `HAS_MONEY` (0 < money < price), `READY` (money >= price).
*   **Initial State:** `IDLE`.
*   **Transitions:** `insert_coin`, `buy`, `cancel`.

## 2. Preserved Predicate & Invariant
*   **Preserved Predicate:** A property \(P\) is preserved if, whenever \(P(s)\) is true for a state \(s\), and there is a transition \(s \to t\), then \(P(t)\) is also true.
*   **Invariant:** A property that is true for *all* reachable states. (Theorem: If \(P\) is true for the initial state, and \(P\) is a preserved predicate, then \(P\) is an invariant).

### Application in our code:
The function `check_invariant()` ensures that `money >= 0` and `stock >= 0`.
*   *Proof:* Initially, money = 0 and stock = 10 (satisfies the condition).
*   *Transitions:* `insert_coin` adds positive amounts; `buy` deducts exactly the price; `cancel` resets to 0. None of these operations can make money or stock negative. Thus, the invariant is preserved.

## 3. Reachability & The Invariant Principle
*   **Reachability:** A state is reachable if there exists an execution from the initial state to that state.
*   **The Invariant Principle:** If a property \(P\) is an invariant, and \(P(s)\) is false for some state \(s\), then \(s\) is **unreachable**.

### Application: The 8-Puzzle
In the classic 8-puzzle, we use the **parity of inversions** as an invariant. The start state has an odd number of inversions, and the goal state has an even number. Because horizontal and vertical moves preserve this parity, the goal is unreachable.

## 4. Termination & Derived Variables (Potential Functions)
*   **Termination:** A state machine terminates if there are no infinite executions.
*   **Potential Function:** A function \(f\) mapping states to real numbers that is strictly decreasing (\(f(t) < f(s)\) for all transitions \(s \to t\)). If such a function exists, the machine must terminate.

### Application:
In sorting algorithms (like Bubble Sort), the *number of inversions* acts as a strictly decreasing potential function, proving the algorithm will always terminate.

---
*“Mathematics is the music of reason.”*