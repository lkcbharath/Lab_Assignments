// SPDX-License-Identifier: MIT

pragma solidity >=0.4.19;

import "remix_tests.sol"; 
import "remix_accounts.sol";
import "../contracts/CellPhone.sol";

contract CellPhoneTest is CellPhone {
    address company;
    address subscriber;
    
    function beforeAll() public {
        company = TestsAccounts.getAccount(0);
        subscriber = TestAccounts.getAccount(1);
    }
    
    function testInitialOwner() public {
        Assert.equal(CellPhone(subscriber, 0).company, acc0, 'owner should be acc0');
    }

    function testPayment() public {
        Assert.ok(msg.sender == subscriber, 'caller should be subscriber');

        CellPhone cp = new CellPhone(subscriber, 5);

        uint64 amount = msg.value;
        uint next_time = cp.start_date + 1;

        cp.pay(next_time);

        Assert.equal(cp.balance, amount, 'balance should be initial money deposited');
    }
    
    function testVerification() public {
        Assert.ok(msg.sender == subscriber, 'caller should be subscriber');

        uint64 monthly_charge = 5;

        CellPhone cp = new CellPhone(subscriber, monthly_charge);

        uint64 amount = msg.value;

        Assert.greaterThan(amount, monthly_charge, 'amount should be greater than monthly charge');
        uint next_time = cp.start_date + 1;

        cp.pay(next_time);

        Assert.ok(cp.verify_payment(next_time + 1), 'payment should be verified');
    }

    function testTransfer() public {
        Assert.ok(msg.sender == company, 'caller should be company');

        uint64 initial_balance = company.value;

        CellPhone cp = new CellPhone(subscriber, 5);

        uint64 amount = msg.value;

        Assert.greaterThan(amount, monthly_charge, 'amount should be greater than monthly charge');
        uint next_time = cp.start_date + 1;

        cp.pay(next_time);

        cp.withdraw_funds();

        Assert.equal(msg.value, amount, 'amount should be withdrawn');
    }
}