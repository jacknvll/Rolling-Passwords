# Roll yourself a password
Idea has been provided by:
https://gist.github.com/zdw/2571473#file-rolling_passwords-md
## Required Equipment

 * One d4  Nibble die <http://www.amazon.com/gp/product/B001AV9C0M/>
 * One d8  Octal die <http://www.amazon.com/gp/product/B001AV9C0W/>
 * One d10 Decimal die <http://www.amazon.com/gp/product/B001AVEIOW>
 * One d16 Hexadecimal die <http://www.amazon.com/gp/product/B0012YVYXU/> 
 * One d30 Alphanumeric die (26 letters + 4 wild spaces) <http://www.amazon.com/dp/B001BIZD02/>
 * Paper or some way of recording the password

 
## Decide how long of a password to use
 
 Current best recommendations are to use passwords of at least 12 characters.  
 To randomize password length, add 10 to the sum of two rolls the nibble die.
 
 UpperLimit = D4 + D4 + 10

## Rolling a password

Roll the Nibble Die.  

Depending on what you roll, perform the following actions:

 1 or 2 - Lower (1) or Upper (2) Case Letter - For either of these, roll the Alphanumeric die.  
 Record the letter given in the appropriate case.   
 If you roll a "wild", roll the Octal die, look up a symbol in the chart below and record: 

     1 - `[`
     2 - `]`
     3 - `\`
     4 - `<`
     5 - `>`
     6 - `+`
     7 - `=`
     8 - `_`
   
 3 - Decimal Number - Roll the Decimal die, record the number.  

 4 - Symbol - Roll the Hexadecimal die, use the chart given below to look up a 
 symbol and record:

     1 - `-`
     2 - `/`
     3 - `;`
     4 - `.`
     5 - `,`
     6 - `'`
     7 - `:`
     8 - `(`
     9 - `)`
     A - `$`
     B - `&`
     C - `@`
     D - `"`
     E - `?`
     F - `!`

Repeat until you have a password of the length desired. 

## Optional instructions

To speed up the rolling process, you may want to roll all the dice every time, 
or just the dice that contributed data to that roll. 

# Defining the flow
Pre-requisites:
  import random, string, itertools
  initial variables: Password = "", Dice_D#, 
 1. Create UpperLimit
 2. Create switch case for D4 results
   - 1: lower(roll D30), and if 'wild': roll D8, add char to Password var
   - 2: upper(roll D30), and if 'wild': roll D8, add char to Password var
   - 3: roll D10, add char to Password var
   - 4: roll D16, add char to Password var
 Possible solution for PART2, to create a dictionary of definitions as switch 
 statements are not supported in Python.
 https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
 3. Check: len(Password) == UpperLimit
   if YES: STOP and print(Password)
   if NO: continue to next roll of D4