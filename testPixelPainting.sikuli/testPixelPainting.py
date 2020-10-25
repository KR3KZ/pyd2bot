from java.awt import Color, Rectangle
from java.awt.event import *
from java.awt.image import BufferedImage
from java.swing import JFrame, JPanel, ImageIcon, JLabel


class ScreenHighlighter(JFrame):
    _opened = set()
    bi = None
    _lastTarget = None
    _anim = None
    TARGET_SIZE = 80
    MARGIN = 20

    def __init__(self, screen):
        self._native_transparent = True
        self.double_buffered = True
        self._overlayColor = Color(0, 0, 0, 0, 0)
        self._transparentColor = Color(0, 0, 0, 0.0)
        self._targetColor = Color(1, 0, 0, 0.7)
        self._opened.add(self)
        self.srcx, self.srcy, self.destx, self.desty = None
        self._lastTarget = None
        self._native_transparent = False
        self.double_buffered = False
        self._StrokeCross = BasicStroke(1, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND, 1, lambda x:2, 0)
        self._StrokeBorder = BasicStroke(3)
        self._screen = screen
        self.setVisible(False)
        self.setAlwaysOnTop(True)
        self.setOpaque(False)
        self.setUndecorated(True)
        if self._native_transparent:
            self.setBackground(self._transparentColor)
        self.getRootPane().putClientProperty("Window.shadow", False)
        self.getContentPane().setDoubleBuffered(True)
        self.addMouseListener(self)

    def mouseClicked(self, e):
        self.dispose()

    def closeAfter(self, secs):
        try:
            time.sleep(secs * 1000)
        except InterruptedError as e:
            self.close()
            traceback.print_stack()
        self.close()

    def captureScreen(self, x, y, w, h):
        img = self.screen.capture(x, y, w, h)
        self._screen = img.getImage()
        scaleFactor = .6
        op = RescaleOp(scaleFactor, 0, None)

    def drawCircle(self, x, y, radius, g):
        g.drawOval(x - radius, y - radius, radius * 2, radius * 2)

    def drawTarget(self, g2d):
        cx = (self.srcx + self.destx) / 2
        cy = (self.srcy + self.desty) / 2

        if self._anim.running():
            g2d.setColor(self._targetColor)
            g2d.setStroke(self._StrokeBorder)
            size = self._anim.step()
            size2 = 0 if size == 0 else size - 5
            self.drawCircle(cx, cy, size, g2d)
            self.drawCircle(cx, cy, size2, g2d)
            self.repaint()

    def drawBorder(self, g2d):
        g2d.setColor(self._targetColor)
        g2d.setStroke(self._StrokeBorder)
        w = self._StrokeBorder.getLineWidth()
        g2d.drawRect(w / 2, w / 2, self.getWidth() - w, self.getHeight() - w)

    def paint(self, g):
        super.paint(g)
        if not self.bi or self.bi.getWidth(self) != self.getWidth() or self.bi.getHeight(self) != self.getHeight():
            self.bi = BufferedImage(self.getWidth(), self.getHeight(), BufferedImage.TYPE__RGB)

        bfG2 = self.bi.createGraphics()
        g2d = None

        if self.double_buffered:
            g2d = bfG2

        else:
            g2d = g
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.CLEAR, 0.0))
            g2d.fillRect(0, 0, self.getWidth(), self.getHeight())
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 1.0))
            g2d.setRenderingH(RenderingHs.KEY_ANTIALIASING, RenderingHs.VALUE_ANTIALIAS_ON)

        self.drawTarget(g2d)

        if self.double_buffered:
            g.drawImage(self.bi, 0, 0, self)
            if not self.isVisible():
                self.setVisible(True)

        elif self.isVisible():
            self.setVisible(False)

    def close(self):
        self.setVisible(False)
        for it in self._opened:
            it.remove(self)
        self.dispose()

    def closeAll(self):
        log.info(3, "close all ScreenHighlighter")
        for s in self._opened:
            if s.self.isVisible():
                s.self.setVisible(False)
                s.dispose()
        self._opened.clear()

    def highlight(self, r_, secs=None):
        r = None
        if self._native_transparent:
            r = r_
        else:
            r = Region(r_)
            r.setROI(Rectangle(r_.x - 3, r_.y - 3, r_.w + 6, r_.h + 6))
            self.captureScreen(r.x, r.y, r.w, r.h)
        self.setLocation(r.x, r.y)
        self.setSize(r.w, r.h)
        self.setBackground(self._transparentColor)
        self.setVisible(True)
        self.toFront()
        if secs:
            self.closeAfter(secs)

    def showWindow(self, x, y, w, h, secs):
        self.setLocation(x, y)
        self.setSize(w, h)
        self.setVisible(True)
        self.toFront()
        self.closeAfter(secs)


scr = r.getScreen()
_overlay = ScreenHighlighter(scr)
_overlay.highlight(r)