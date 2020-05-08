import sys

class Stack:
  def __init__(self):
    self._sl = []
  def push(self, item):
    self._sl.append(item)
  def look(self):
    return self._sl[-1]
  def shoot(self):
    x = self._sl[-1]
    del self._sl[-1]
    return x
  def clear(self):
    self._sl = []
  def print(self):
    while not self.empty():
      print(chr(self.shoot()), end="")
  def empty(self):
    return len(self._sl) < 1

class SInterpreter:
  def __init__(self):
    self.name = "Stacks interpreter"
    self.version = "1.1"
    self.versions = ["1.0", "1.1", "1.2"]
    self.getchar = lambda: sys.stdin.read(1)
  def runi(self, i):
    s = []
    cycles = Stack()
    t = 0
    sp = 0
    pp = 0
    running = True
    def testlen():
      if pp >= len(i):
          sys.stderr.write("Program is not terminated!")
          sys.exit(-1)
    def nextc():
      nonlocal pp
      pp += 1
      testlen()
    testlen()
    buff = ""
    while i[pp] == '@':
      nextc()
      for ch in "version ":
        if i[pp] != ch:
          break
        nextc()
      else:
        vbuff = ""
        while i[pp] != '\n':
          vbuff += i[pp]
          nextc()
        nextc()
        if vbuff in self.versions:
          if vbuff not in self.versions[:self.versions.index(self.version) + 1]:
            sys.stderr.write("Uncompatible program version specified in @version! (" + vbuff + ")")
            sys.exit(-1)
        else:
          sys.stderr.write("Unknown version specified in @version! (or program is for future version) (" + vbuff + ")")
          sys.exit(-1)
    while running:
      testlen()
      if i[pp] == 'c':
        if sp > len(s):
          sys.stderr.write("Can't leave gaps between stacks!")
          sys.exit(-1)
        elif sp == len(s):
          s.append(Stack())
        else:
          s[sp].clear()
      elif i[pp] == 'n':
        sp += 1
      elif i[pp] == 'b':
        sp -= 1
        if sp < 0:
          sys.stderr.write("Stack pointer can't go below 0!")
          sys.exit(-1)
      elif i[pp] == 'p':
        nextc()
        if i[pp] == 'c':
          nextc()
          s[sp].push(ord(i[pp]))
        elif i[pp] == 'i':
          nextc()
          s[sp].push(ord(i[pp]) - ord('0'))
        elif i[pp] == 'l':
          s[sp].push(s[sp].look())
        elif i[pp] == '$':
          s[sp].push(t)
        elif i[pp] == '<':
          s[sp].push(ord(self.getchar()))
      elif i[pp] == 's':
        s[sp].shoot()
      elif i[pp] == 'w':
        nextc()
        if i[pp] == 'l':
          print(chr(s[sp].look()), end="")
        elif i[pp] == 's':
          print(chr(s[sp].shoot()), end="")
        elif i[pp] == '#':
          s[sp].print()
      elif i[pp] == '$':
        nextc()
        if i[pp] == 'l':
          t = s[sp].look()
        elif i[pp] == 's':
          t = s[sp].shoot()
        elif i[pp] == '<':
          t = ord(self.getchar())
      elif i[pp] == 'i':
        s[sp].push(s[sp].shoot() + 1)
      elif i[pp] == 'd':
        s[sp].push(s[sp].shoot() - 1)
      elif i[pp] == '[':
        if s[sp].look() == 0:
          brs = -1
          while i[pp] != ']' and brs < 1:
            if i[pp] == '[':
              brs += 1
            elif i[pp] == ']':
              brs -= 1
            nextc()
        else:
          cycles.push(pp)
      elif i[pp] == ']':
        if cycles.look() > 0:
          if s[sp].look() != 0:
            pp = cycles.look()
          else:
            cycles.shoot()
        else:
          if s[sp].look() == 0:
            pp = -cycles.look()
          else:
            cycles.shoot()
      elif i[pp] == '{':
        if s[sp].empty():
          brs = -1
          while i[pp] != '}' and brs < 1:
            if i[pp] == '{':
              brs += 1
            elif i[pp] == '}':
              brs -= 1
            nextc()
        else:
          cycles.push(pp)
      elif i[pp] == '}':
        if cycles.look() > 0:
          if not s[sp].empty():
            pp = cycles.look()
          else:
            cycles.shoot()
        else:
          if s[sp].empty():
            pp = -cycles.look()
          else:
            cycles.shoot()
      elif i[pp] == '?':
        while i[pp] != '\n':
          nextc()
      elif i[pp] == 't':
        running = False
      elif i[pp] == '!':
        nextc()
        cc = ord(i[pp]) - ord('0')
        for _ in range(cc):
          cycles.shoot()
        while cc > 0:
          nextc()
          if i[pp] == ']' or i[pp] == '}':
            cc -= 1
          elif i[pp] == '[' or i[pp] == '{':
            cc += 1
      elif i[pp] == '~':
        nextc()
        if i[pp] == '[':
          if s[sp].look() != 0:
            brs = -1
            while i[pp] != ']' and brs < 1:
              if i[pp] == '[':
                brs += 1
              elif i[pp] == ']':
                brs -= 1
              nextc()
          else:
            cycles.push(-pp)
        if i[pp] == '{':
          if not s[sp].empty():
            brs = -1
            while i[pp] != '}' and brs < 1:
              if i[pp] == '{':
                brs += 1
              elif i[pp] == '}':
                brs -= 1
              nextc()
          else:
            cycles.push(-pp)
      pp += 1

if __name__ == "__main__":
  if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as f:
      inp = f.read()
  else:
    inp = input("give me food: ")
    import os
    if os.path.exists(inp):
      print("Assuming that food is filename.")
      with open(inp, "r") as f:
        inp = f.read()
    else:
      print("Assuming that food is code.")
  si = SInterpreter()
  print("------------------Running " + si.name + " " + si.version + "--------------")
  si.runi(inp)
  input()
