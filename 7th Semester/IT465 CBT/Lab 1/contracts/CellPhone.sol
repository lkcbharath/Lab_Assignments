// SPDX-License-Identifier: MIT

pragma solidity >=0.4.19;
//pragma solidity ^0.4.19;

import "./DateTime.sol";

contract CellPhone {
    address company;
    address subscriber;
    uint256 balance;

    DateTime dt;

    // monthly charge
    uint256 monthly_charge;

    uint start_date;

    // dates paid

    struct Payment {
        uint256 amount;
        uint date;
    }

    Payment[] payments;

    constructor(address subscriber_, uint256 monthly_charge_) {
        company = msg.sender;
        balance = 0;
        subscriber = subscriber_;
        monthly_charge = monthly_charge_;

        // current time
        start_date = block.timestamp;

        dt = new DateTime();
    }

    function pay(uint date) public payable {
        require(date >= start_date);
        require(msg.sender == subscriber);

        // if previous payment exists
        if (payments.length > 0) {
            uint last_paid_date = payments[payments.length - 1].date;
            require(date >= last_paid_date);
        }

        payments.push(Payment(msg.value, date));
        balance += msg.value;
    }


    function verify_payment(uint256 date) public view returns(bool) {
        uint256 arr_length = payments.length;

        uint256 i = 0;

        uint256 charge_for_month = 0;

        // no support for NULL hence
        uint256 prev_payment_init = 0;

        Payment memory prev_payment = Payment(0,0);

        Payment storage current_payment;

        while(i < arr_length) {
            current_payment = payments[i];

            if(current_payment.date > date) {
                break;
            }

            if (prev_payment_init == 0) {
                prev_payment_init = 1;
                charge_for_month += current_payment.amount;
            }
            else {

                // on month change, monthly payment should be atleast minimum
                if (dt.getMonth(current_payment.date) != dt.getMonth(prev_payment.date) && (charge_for_month < monthly_charge)) {
                    return false;
                }  
                else {
                    charge_for_month = current_payment.amount;
                }

            }
            prev_payment = current_payment;
        }

        // early exit or end of array check
        if (charge_for_month < monthly_charge) {
            return false;
        }

        return true;
    }

    // only company can access
    function withdraw_funds() public {
        require(msg.sender == company);

        msg.sender.transfer(address(this).balance);
    }
}