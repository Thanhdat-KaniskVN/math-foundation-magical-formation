from enum import Enum
from dataclasses import dataclass

class State(Enum):
    IDLE = "idle"              # money == 0
    HAS_MONEY = "has_money"    # 0 < money < price
    READY = "ready"            # money >= price

@dataclass
class VendingMachine:
    price: int = 10000
    stock: int = 10
    money: int = 0
    state: State = State.IDLE

    def insert_coin(self, amount: int) -> str:
        if amount not in (2000, 5000, 10000):
            return "❌ Only accept 2k, 5k, 10k coins."
        self.money += amount
        self._update_state()
        return f"💰 Inserted {amount}đ. Total: {self.money}đ"

    def buy(self) -> str:
        if self.state != State.READY:
            return f"❌ Not enough money (requires {self.price}đ)"
        if self.stock == 0:
            return "❌ Out of stock"
        
        change = self.money - self.price
        self.money = 0
        self.stock -= 1
        self._update_state()
        return f"🥤 Dispensed water + Change: {change}đ"

    def cancel(self) -> str:
        refund = self.money
        self.money = 0
        self._update_state()
        return f"↩️ Transaction cancelled. Refunded {refund}đ"

    def _update_state(self):
        if self.money == 0:
            self.state = State.IDLE
        elif self.money < self.price:
            self.state = State.HAS_MONEY
        else:
            self.state = State.READY

    def check_invariant(self) -> bool:
        """Invariant: money >= 0 and stock >= 0"""
        return self.money >= 0 and self.stock >= 0