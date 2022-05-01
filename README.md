
# RENDER - OFFENSIVE SECURITY SOLUTIONS - "GREYCRAK"
# MADE BY: "Grey."
# // : BTC : 3Mf37GhjYfrjTG59hmT3rAe5ntWDCgeDVg
-----------------------------------------

This is a simple bitcoin Cracker. It looks for private keys then matches it to a working address, which is found in GREYCRAK/database then matches it to common keywords.
Giving you access to take their funds.


This is compatible for any operating system that supports Python3.


The database currently holds `19,216,420 Bitcoin addresses`. This is the total number of P2PKH Bitcoin addresses with a balance that exist in the blockchain.

# - NOTES:

 > Join the discord : https://discord.gg/3qKxa48n4E

 Also, The database was created using a third-party program: "https://github.com/graymauser/btcposbal2csv"
 which generates a csv file of all Bitcoin addresses with a positive balance.
It works by analyzing the current unspent transaction output set (UTXO), aggregating outputs to same addresses together and writes them to csv file.
 Please be sure to refresh this if need be.

-----------------------------------------
# - Installation:

git clone https://github.com/RealGreyDB/GREYCRAK.git GREYCRAK

cd GREYCRAK && pip3 install -r requirements.txt

python3 GREYCRAK.py

Then just wait it out, all outputs of verified hits will be displayed in GREYCRAK.txt

-----------------------------------------

STATISTICS:

It takes 0.003 seconds for this program to brute force a single Bitcoin address.

But. through multiprocessing, a concurrent process is created for every CPU your computer has. So this program can brute force addresses at a speed of 0.003 Divided by the cpu count
Every time this program checks the balance of a generated address, it will print the result to the user. If an empty wallet is found, then the wallet address will be printed to the terminal.

-----------------------------------------

An example is:

1Kz2CTvjzkZ3p2BQb5x5DX6GEoHX2jFS45

-----------------------------------------

However, if a wallet with a balance is found, it will be put in GREYCRAK.txt.

An example is:

Hex private key: 5A4F3F1CAB44848B2C2C515AE74E9CC487A9982C9DD695810230EA48B1DCEADD
WIF private key: 5JW4RCAXDbocFLK9bxqw5cbQwuSn86fpbmz2HhT9nvKMTh68hjm
Public key: 04393B30BC950F358326062FF28D194A5B28751C1FF2562C02CA4DFB2A864DE63280CC140D0D540EA1A5711D1E519C842684F42445C41CB501B7EA00361699C320
Address: 1Kz2CTvjzkZ3p2BQb5x5DX6GEoHX2jFS45

=
