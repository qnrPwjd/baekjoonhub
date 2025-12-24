import sys
input = sys.stdin.readline

class Set:
    def __init__(self):
        self.s = [0 for _ in range(21)]
        self.size = 0

    def add(self, x):
        if self.s[x] == 0:
            self.s[x] = 1
            self.size += 1
    
    def remove(self, x):
        if self.s[x] == 1:
            self.s[x] = 0
            self.size -= 1
    
    def check(self, x):
        print(self.s[x])
    
    def toggle(self, x):
        if self.s[x] == 1:
            self.s[x] = 0
            self.size -= 1
        else:
            self.s[x] = 1
            self.size += 1
    
    def all(self):
        self.s = [1 for _ in range(21)]
        self.size = 20
    
    def empty(self):
        self.s = [0 for _ in range(21)]
        self.size = 0

my_set = Set()
n = int(input())

commands = {
    'add' : my_set.add,
    'remove' : my_set.remove,
    'check' : my_set.check,
    'toggle' : my_set.toggle,
    'all' : my_set.all,
    'empty' : my_set.empty
}

for _ in range(n):
    command = input().strip().split()
    if len(command) == 2:
        cmd, x = command[0], int(command[1])
        commands[cmd](x)
    else:
        cmd = command[0]
        commands[cmd]()