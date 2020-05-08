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
-------------------------------from version 1.1-------------------------
@version * - at the beggining, on its own line; causes error if interpreter version is lower than specified at the place of *
! - nextchar; break c - '0' loops
~ - adds not into while (~[] - while look == 0; ~{} - while stack is empty)
-------------------------------from version 1.2------------------------
e - executes stack
---------------------------------------------------------FUTURE-------------------------------------------------------------
-------------------------------from version 2.0------------------------
p
  ...
  elif c == 's':
    nextchar;
    if c == '"':
      sbuff = <chars to next '"'>
      for ch in sbuff:
        push ch to stack
    elif c == 'r':
    nextchar;
      if c == '"':
        sbuff = <chars to next '"'>
        for ch in sbuff.reverse():
          push ch to stack
^ - inserts a new place for stack after current stack and increments stack pointer
x - deletes current stack and decrements stack pointer
!ROUTINES!
r<name<code> - creates new routine
rc<name> - runs a routine
</pre>
## syntax:
just write commands, use ? as one-line comment
