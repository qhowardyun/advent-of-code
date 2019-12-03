lines = open("day13.in").read().splitlines()

grid = [[" " for i in range(150)] for j in range(150)]

class Cart:

    x, y = 0, 0
    #0 left, 1 straight, 2 right
    currentdir = 0
    #0 up, 1 right, 2 down, 3 left
    drive = 0

    xmod = [0, 1, 0, -1]
    ymod = [-1, 0, 1, 0]
    
    def __init__(self, x, y, drive):
        self.x = x
        self.y = y
        self.drive = drive

    def move(self):

        self.x += self.xmod[self.drive]
        self.y += self.ymod[self.drive]

        #print("current {} x {} y {}".format(grid[self.x][self.y], self.x, self.y))

        if grid[self.x][self.y] == "/":
            if self.drive == 0:
                self.drive = 1
            elif self.drive == 1:
                self.drive = 0
            elif self.drive == 2:
                self.drive = 3
            elif self.drive == 3:
                self.drive = 2
        elif grid[self.x][self.y] == "\\":
            if self.drive == 0:
                self.drive = 3
            elif self.drive == 3:
                self.drive = 0
            elif self.drive == 2:
                self.drive = 1
            elif self.drive == 1:
                self.drive = 2
        elif grid[self.x][self.y] == "+":
            #print("dir {} next {}".format(self.drive, self.currentdir))
            #0 left, 1 straight, 2 right
            #0 up, 1 right, 2 down, 3 left
            if self.drive == 0:
                if self.currentdir == 0:
                    self.drive = 3
                elif self.currentdir == 1:
                    self.drive = 0
                elif self.currentdir == 2:
                    self.drive = 1
            elif self.drive == 1:
                if self.currentdir == 0:
                    self.drive = 0
                elif self.currentdir == 1:
                    self.drive = 1
                elif self.currentdir == 2:
                    self.drive = 2
            elif self.drive == 2:
                if self.currentdir == 0:
                    self.drive = 1
                elif self.currentdir == 1:
                    self.drive = 2
                elif self.currentdir == 2:
                    self.drive = 3
            elif self.drive == 3:
                if self.currentdir == 0:
                    self.drive = 2
                elif self.currentdir == 1:
                    self.drive = 3
                elif self.currentdir == 2:
                    self.drive = 0

            self.currentdir += 1
            self.currentdir %= 3


        
carts = []

for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        if cell == "v":
            carts.append(Cart(j, i, 2))
        elif cell == "^":
            carts.append(Cart(j, i, 0))
        elif cell == "<":
            carts.append(Cart(j, i, 3))
        elif cell == ">":
            carts.append(Cart(j, i, 1))
        else:
            grid[j][i] = cell

def sim():
    global carts
    ticks = 0
    while True:
        ticks += 1
        #print(carts[15].x, carts[15].y, grid[carts[15].x][carts[15].y])
        #input()
        for i, cart in enumerate(carts):
            cart.move()
            for j in carts:
                if cart.x == j.x and cart.y == j.y and cart != j:
                    print(ticks)
                    return cart.x, cart.y

print(sim())

#83, 121
#141, 94