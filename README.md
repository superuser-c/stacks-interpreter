# stacks-interpreter
intepreter of my new ezoteric? language in Python<br/>
there is a list of stacks and one variable and code manipulates with them to create output

## commands:
<pre>
c - creates a new stack/clears stack at stack pointer
n - increments stack pointer
b - decrements stack pointer
p
  nextchar;
  if c == 'c':
    nextchar; push c to actual stack  elif c == 'i':
    nextchar; push (c - '0') to actual stack
  elif c == 'l':
    push (look at actual stack) to actual stack -> duplicate item at top of actual stack
  elif c == '$':
    push value of tmp var to actual stack
  elif c == '<':
    push input to actual stack
  nextchar;
s - shoots from actual stack
w
  nextchar;
  if c == 'l':
    write look at actual stack
  elif c == 's':
    write shoot from actual stack
  elif c == '#':
    write and clear full stack
$
  nextchar;
  if c == 'l':
    tmp = look at actual stack
  elif c == 's':
    tmp = shoot from actual stack
i - increment top of actual stack
d - decrement top of actual stack
[] - while look at actual stack != 0
{} - while actual stack isn't empty
t - terminates program
</pre>
## syntax:
just write commands, use ? as one-line comment
