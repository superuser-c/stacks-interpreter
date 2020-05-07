# stacks-interpreter
intepreter of my new ezoteric? language in Python<br/>
there is a list of stacks and one variable and code manipulates with them to create output

## commands:
c - creates a new stack/clears stack at stack pointer<br/>
n - increments stack pointer<br/>
b - decrements stack pointer<br/>
p<br/>
  nextchar;<br/>
  if c == 'c':<br/>
    nextchar; push c to actual stack<br/>
  elif c == 'i':<br/>
    nextchar; push (c - '0') to actual stack<br/>
  elif c == 'l':<br/>
    push (look at actual stack) to actual stack -> duplicate item at top of actual stack<br/>
  elif c == '$':<br/>
    push value of tmp var to actual stack<br/>
  elif c == '<':<br/>
    push input to actual stack<br/>
  nextchar;<br/>
s - shoots from actual stack<br/>
w<br/>
  nextchar;<br/>
  if c == 'l':<br/>
    write look at actual stack<br/>
  elif c == 's':<br/>
    write shoot from actual stack<br/>
  elif c == '#':<br/>
    write and clear full stack<br/>
$<br/>
  nextchar;<br/>
  if c == 'l':<br/>
    tmp = look at actual stack<br/>
  elif c == 's':<br/>
    tmp = shoot from actual stack<br/>
i - increment top of actual stack<br/>
d - decrement top of actual stack<br/>
[] - while look at actual stack != 0<br/>
{} - while actual stack isn't empty<br/>
t - terminates program<br/>
## syntax:
just write commands, use ? as one-line comment
