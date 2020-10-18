// SPDX-License-Identifier: MIT

pragma solidity >=0.4.19;

import "remix_tests.sol"; 
import "remix_accounts.sol";
import "../contracts/Bank.sol";

contract BankTest is Bank {
    address acc0;
    address acc1;
    
    function beforeAll() public {
        acc0 = TestsAccounts.getAccount(0);
        acc1 = TestsAccounts.getAccount(1);
    }
    
    function testInitialOwner() public {
        Assert.equal(Bank(), acc0, 'owner should be acc0');
    }

    function testBalanceDeposit() public {
        Assert.ok(msg.sender == acc0, 'caller should be default account i.e. acc0');
        Bank bank = new Bank();
        uint64 balance = msg.value;
        bank.deposit();
        Assert.equal(bank.balance(), balance, 'balance should be initial money deposited');
    }
    
    function testWithdraw() public {
        Assert.ok(msg.sender == acc1, 'caller should be default account i.e. acc1');
        Bank bank = new Bank();
        uint64 balance = msg.value;
        bank.deposit();
        Assert.equal(bank.withdraw(), balance, 'withdraw amount should be initial money deposited');
    }
}