# Vending Machine FSM 🥤

A Finite State Machine (FSM) model of an automated vending machine, inspired by **MIT 6.1200J Lecture 04 (Mathematics for Computer Science)**.

## State Machine Definition
*   **States:** `IDLE`, `HAS_MONEY`, `READY`
*   **Initial state:** `IDLE` (money = 0)
*   **Transitions:** `insert_coin`, `buy`, `cancel`
*   **Invariant:** `money >= 0` AND `stock >= 0`

## State Diagram
```mermaid
stateDiagram-v2
    [*] --> IDLE
    IDLE --> HAS_MONEY: Insert 2k/5k
    HAS_MONEY --> READY: Insert enough coins
    READY --> IDLE: Buy
    HAS_MONEY --> IDLE: Cancel
    READY --> IDLE: Cancel