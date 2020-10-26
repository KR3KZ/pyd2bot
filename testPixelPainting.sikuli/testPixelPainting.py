from java.awt import Color, Rectangle, AlphaComposite, RenderingHints, BasicStroke
from javax.swing import JFrame, JPanel, ImageIcon, JLabel
from java.awt.event import MouseListener
import traceback


class ScreenHighlighter(JFrame):
    opened = set()

    def __init__(self):
        super(ScreenHighlighter, self).__init__()
        self.target_color = Color(1, 0, 0, 0.7)
        self.setAlwaysOnTop(True)
        self.setUndecorated(True)
        self.setBackground(Color(0, 0, 0, 0.0))
        self.roi = set()
        self.opened.add(self)
        self.setVisible(False)
        self.getRootPane().putClientProperty("Window.shadow", False)

    def closeAfter(self, secs):
        try:
            sleep(secs)
        except InterruptedError as e:
            self.close()
            traceback.print_stack()
        self.close()

    def drawBorder(self, g):
        stroke = BasicStroke(3)
        g.setColor(self.target_color)
        g.setStroke(stroke)
        w = stroke.getLineWidth()
        g.drawRect(int(w / 2), int(w / 2), int(self.getWidth() - w), int(self.getHeight() - w))

    def drawRoi(self, g):
        print('yep')
        g.setColor(self.target_color)
        for loc in self.roi:
            g.drawLine(loc.x, loc.y, loc.x, loc.y)

    def paint(self, g):
        super(ScreenHighlighter, self).paint(g)
        if not self.roi:
            self.drawBorder(g)
        else:
            self.drawRoi(g)

    def close(self):
        self.setVisible(False)
        self.opened.remove(self)
        self.dispose()

    def highlight(self, r, secs=None, roi=None, color=None):
        self.setLocation(r.x, r.y)
        self.setSize(r.w, r.h)
        if roi:
            self.roi = roi
        if color:
            self.targetColor = color
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


r = Region(696, 395, 460, 255)
r = Region(1270, 653, 273, 131)
overlay = ScreenHighlighter()
overlay.setSize(r.w, r.h)
overlay.setLocation(r.x, r.y)
overlay.setVisible(True)
for x in range(100):
    overlay.roi.add(Location(x, x))
    overlay.repaint()
    overlay.repaint()
    wait(0.05)
overlay.close()
sleep(2)


