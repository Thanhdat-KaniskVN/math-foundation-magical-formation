from vending_machine import VendingMachine

def test_buy_success():
    vm = VendingMachine()
    vm.insert_coin(10000)
    vm.insert_coin(10000)
    assert vm.money == 20000
    result = vm.buy()
    assert "Change: 10000đ" in result
    assert vm.money == 0
    assert vm.check_invariant()

def test_not_enough_money():
    vm = VendingMachine()
    vm.insert_coin(5000)
    result = vm.buy()
    assert "Not enough money" in result
    assert vm.check_invariant()

def test_cancel():
    vm = VendingMachine()
    vm.insert_coin(5000)
    result = vm.cancel()
    assert "5000đ" in result
    assert vm.money == 0