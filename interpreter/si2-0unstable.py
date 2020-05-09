import sys
import traceback

class SRuntimeException(RuntimeError):
  pass
class SIndexOutOfRangeErr(SRuntimeException):
  pass
class SStackEmptyErr(SRuntimeException):
  pass

class Stack:
  def __init__(self):
    self._sl = []
  def push(self, item):
    self._sl.append(item)
  def look(self):
    if self.empty():
      raise SStackEmptyErr("Can't look at empty stack!")
    return self._sl[-1]
  def shoot(self):
    if self.empty():
      raise SStackEmptyErr("Can't shoot from empty stack!")
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
    self.version = "2.0"
    self.versions = ["1.0", "1.1", "1.2", "2.0"]
    self.getchar = lambda: sys.stdin.read(1)
    self.s = []
    self.cycles = Stack()
    self.t = 0
    self.sp = 0
    self.rs = {}
  def runi(self, i, nam):
    pp = 0
    try:
      running = True
      def testlen():
        if pp >= len(i):
            raise
      def nextc():
        nonlocal pp
        pp += 1
        testlen()
      testlen()
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
          if self.sp >= len(self.s):
            while self.sp > len(self.s):
              self.s.appent(None)
            self.s.append(Stack())
          elif self.s[self.sp] is None:
            self.s[self.sp] = Stack()
          else:
            self.s[self.sp].clear()
        elif i[pp] == 'n':
          self.sp += 1
        elif i[pp] == 'b':
          self.sp -= 1
          if self.sp < 0:
            raise SIndexOutOfRangeErr("Stack pointer can't go below 0!")
        elif i[pp] == 'p':
          nextc()
          if i[pp] == 'c':
            nextc()
            self.s[self.sp].push(ord(i[pp]))
          elif i[pp] == 'i':
            nextc()
            self.s[self.sp].push(ord(i[pp]) - ord('0'))
          elif i[pp] == 'l':
            self.s[self.sp].push(self.s[self.sp].look())
          elif i[pp] == '$':
            self.s[self.sp].push(t)
          elif i[pp] == '<':
            self.s[self.sp].push(ord(self.getchar()))
          elif i[pp] == 's':
            nextc()
            if i[pp] == '"':
              nextc()
              while i[pp] != '"':
                self.s[self.sp].push(ord(i[pp]))
                nextc()
            elif i[pp] == 'r':
              nextc()
              if i[pp] == '"':
                nextc()
                sbuff = ""
                while i[pp] != '"':
                  sbuff += i[pp]
                  nextc()
                for ch in sbuff[::-1]:
                  self.s[self.sp].push(ord(ch))
        elif i[pp] == 's':
          self.s[self.sp].shoot()
        elif i[pp] == 'w':
          nextc()
          if i[pp] == 'l':
            print(chr(self.s[self.sp].look()), end="")
          elif i[pp] == 's':
            print(chr(self.s[self.sp].shoot()), end="")
          elif i[pp] == '#':
            self.s[self.sp].print()
          elif i[pp] == 'i':
            print(self.s[self.sp].look(), end="")
        elif i[pp] == '$':
          nextc()
          if i[pp] == 'l':
            t = self.s[self.sp].look()
          elif i[pp] == 's':
            t = self.s[self.sp].shoot()
          elif i[pp] == '<':
            t = ord(self.getchar())
        elif i[pp] == 'i':
          self.s[self.sp].push(self.s[self.sp].shoot() + 1)
        elif i[pp] == 'd':
          self.s[self.sp].push(self.s[self.sp].shoot() - 1)
        elif i[pp] == '[':
          if self.s[self.sp].look() == 0:
            brs = -1
            while i[pp] != ']' and brs < 1:
              if i[pp] == '[':
                brs += 1
              elif i[pp] == ']':
                brs -= 1
              nextc()
          else:
            self.cycles.push(pp)
        elif i[pp] == ']':
          if self.cycles.look() > 0:
            if self.s[self.sp].look() != 0:
              pp = self.cycles.look()
            else:
              self.cycles.shoot()
          else:
            if self.s[self.sp].look() == 0:
              pp = -self.cycles.look()
            else:
              self.cycles.shoot()
        elif i[pp] == '{':
          if self.s[self.sp].empty():
            brs = -1
            while i[pp] != '}' and brs < 1:
              if i[pp] == '{':
                brs += 1
              elif i[pp] == '}':
                brs -= 1
              nextc()
          else:
            self.cycles.push(pp)
        elif i[pp] == '}':
          if self.cycles.look() > 0:
            if not self.s[self.sp].empty():
              pp = self.cycles.look()
            else:
              self.cycles.shoot()
          else:
            if self.s[self.sp].empty():
              pp = -self.cycles.look()
            else:
              self.cycles.shoot()
        elif i[pp] == '?':
          while i[pp] != '\n':
            nextc()
        elif i[pp] == 't':
          running = False
        elif i[pp] == '!':
          nextc()
          cc = ord(i[pp]) - ord('0')
          for _ in range(cc):
            self.cycles.shoot()
          while cc > 0:
            nextc()
            if i[pp] == ']' or i[pp] == '}':
              cc -= 1
            elif i[pp] == '[' or i[pp] == '{':
              cc += 1
        elif i[pp] == '~':
          nextc()
          if i[pp] == '[':
            if self.s[self.sp].look() != 0:
              brs = -1
              while i[pp] != ']' and brs < 1:
                if i[pp] == '[':
                  brs += 1
                elif i[pp] == ']':
                  brs -= 1
                nextc()
            else:
              self.cycles.push(-pp)
          if i[pp] == '{':
            if not self.s[self.sp].empty():
              brs = -1
              while i[pp] != '}' and brs < 1:
                if i[pp] == '{':
                  brs += 1
                elif i[pp] == '}':
                  brs -= 1
                nextc()
            else:
              self.cycles.push(-pp)
        elif i[pp] == 'e':
          code = ""
          while not self.s[self.sp].empty():
            code += chr(self.s[self.sp].shoot())
          self.runi(code, "<stack exec()>")
        elif i[pp] == '^':
          self.sp += 1
          self.s.insert(self.sp, None)
        elif i[pp] == 'x':
          del self.s[self.sp]
          self.sp -= 1
        elif i[pp] == 'r':
          nextc()
          if i[pp] == '<':
            nextc()
            nbuff = ""
            while i[pp] != '<':
              nbuff += i[pp]
              nextc()
            nextc()
            buff = ""
            while i[pp] != '>':
              buff += i[pp]
              nextc()
            self.rs[nbuff] = buff
          elif i[pp] == 'c':
            nextc()
            if i[pp] == '<':
              nextc()
              nbuff = ""
              while i[pp] != '<':
                nbuff += i[pp]
                nextc()
            self.runi(self.rs[nbuff], "<routine> " + nbuff + "()")
        pp += 1
    except Exception as e:
      sys.stderr.write("Exception: " + str(type(e)) + "\n")
      self.printErr(i, pp, nam)
      if "-InterpreterTraceback" in sys.argv and "-Debug" in sys.argv:
        traceback.print_exception(type(e), e, sys.exc_info()[2])
      if nam != "<main>":
        raise SRuntimeException()
      return
  def printErr(self, i, pp, name):
    sys.stderr.write("in " + name + ": \n")
    lns = i.split('\n')
    tl = 0
    ln = 0
    for iln, line in enumerate(lns):
      tl += len(line)
      if tl >= pp:
        ln = iln
        tl -= len(line)
        break
    if len(lns) > 0 and ln > 0:
      sys.stderr.write("\t" + lns[ln - 1] + "\n")
    sys.stderr.write("\t" + lns[ln] + "\n")
    sys.stderr.write("\t" + " " * (pp - tl - 2) + "^ here!\n")
    if ln + 1 < len(lns):
      sys.stderr.write("\t" + lns[ln + 1] + "\n")

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
  si.runi(inp, "<main>")
  input()
