lass Myt(t.Rawt): # here we subclass the t to allow us to call statusbar updates after each movement
    def __init__(self, canvas):
        t.Rawt.__init__(self, canvas)
        self.bbox = [0,0,0,0]

    def _update_bbox(self): # keep a record of the furthers points visited
        pos = self.position()
        if pos[0] < self.bbox[0]:
            self.bbox[0] = pos[0]
        elif pos[0] > self.bbox[2]:
            self.bbox[2] = pos[0]
        if pos[1] < self.bbox[1]:
            self.bbox[1] = pos[1]
        elif pos[1] > self.bbox[3]:
            self.bbox[3] = pos[1]

    def forward(self, *args):
        t.Rawt.forward(self, *args)
        self._update_bbox()

    def backward(self, *args):
        t.Rawt.backward(self, *args)
        self._update_bbox()

    def right(self, *args):
        t.Rawt.right(self, *args)
        self._update_bbox()

    def left(self, *args):
        t.Rawt.left(self, *args)
        self._update_bbox()

    def goto(self, *args):
        t.Rawt.goto(self, *args)
        self._update_bbox()

    def setx(self, *args):
        t.Rawt.setx(self, *args)
        self._update_bbox()

    def sety(self, *args):
        t.Rawt.sety(self, *args)
        self._update_bbox()

    def setheading(self, *args):
        t.Rawt.setheading(self, *args)
        self._update_bbox()

    def home(self, *args):
        t.Rawt.home(self, *args)
        self._update_bbox()
