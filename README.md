# ATM_Machine
This is a Python code that simulates an Automated Teller Machine (ATM) system. The code provides a simple and intuitive interface for users to perform various banking transactions, including checking their account balance, withdrawing cash, depositing funds, and transferring money to other accounts.  
Functionality of the Code:

The code provides the following functionality:

PIN Verification:
                The user is prompted to enter their 4-digit PIN. If the PIN is correct, the user is granted access to the ATM system. If the PIN is incorrect, the user is prompted to try again. After three incorrect attempts, the system locks out the user for 12 hours.
Menu Options: The user is presented with a menu of options, including:
Check Balance: 
             Displays the user's current account balance.
Withdraw Cash:
             Allows the user to withdraw a specified amount of cash from their account.
Deposit Funds:
             Allows the user to deposit a specified amount of cash into their account.
Transfer Funds: 
               Allows the user to transfer a specified amount of cash to another account.
Exit:
     Terminates the ATM session.
Transaction Processing: 
                      The code processes each transaction request, including:
Validating the user's account balance to ensure sufficient funds for withdrawals and transfers.
Updating the user's account balance accordingly.
Displaying a success message and the new account balance after each transaction.
Error Handling: 
               The code includes error handling mechanisms to handle invalid user input, such as:
Invalid PIN attempts.
Insufficient account balance for withdrawals and transfers.
Invalid account numbers for transfers.
Overall, this code provides a basic ATM system that simulates real-world banking transactions, with a focus on simplicity and ease of use.

