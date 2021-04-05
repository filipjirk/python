import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QScreen
from PySide6.QtGui import QGuiApplication

class CsgoBindGenerator(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("CS:GO Bind Generator")
		self.setFixedSize(1700, 500)

		self.centralWidget = QWidget(self)
		self.setCentralWidget(self.centralWidget)
		self.layout = QGridLayout(self.centralWidget)
		self.centralWidget.setLayout(self.layout)

		self.create_GUI()

	def create_GUI(self) -> None:
		self.commands_display = QTextEdit(self)
		font = self.commands_display.font()
		font.setPointSize(10)
		self.commands_display.setFont(font)

		self.commands_display.setReadOnly(True)
		place_holder: str = "1. Choose Action | 2. Pick a Key to be Bound | 3. Select a Gun/Equipment"
		self.commands_display.setPlaceholderText(place_holder)
	
		self.f1 = QPushButton(self.centralWidget)
		self.f2 = QPushButton(self.centralWidget)
		self.f3 = QPushButton(self.centralWidget)
		self.f4 = QPushButton(self.centralWidget)
		self.f5 = QPushButton(self.centralWidget)
		self.f6 = QPushButton(self.centralWidget)
		self.f7 = QPushButton(self.centralWidget)
		self.f8 = QPushButton(self.centralWidget)
		self.f9 = QPushButton(self.centralWidget)
		self.f10 = QPushButton(self.centralWidget)
		self.f11 = QPushButton(self.centralWidget)
		self.f12 = QPushButton(self.centralWidget)
		
		self.acute = QPushButton(self.centralWidget)
		self.one = QPushButton(self.centralWidget)
		self.two = QPushButton(self.centralWidget)
		self.three = QPushButton(self.centralWidget)
		self.four = QPushButton(self.centralWidget)
		self.five = QPushButton(self.centralWidget)
		self.six = QPushButton(self.centralWidget)
		self.seven = QPushButton(self.centralWidget)
		self.eight = QPushButton(self.centralWidget)
		self.nine = QPushButton(self.centralWidget)
		self.zero = QPushButton(self.centralWidget)
		self.minus = QPushButton(self.centralWidget)
		self.equal = QPushButton(self.centralWidget)
		self.backspace = QPushButton(self.centralWidget)

		self.tab = QPushButton(self.centralWidget)
		self.q = QPushButton(self.centralWidget)
		self.w = QPushButton(self.centralWidget)
		self.e = QPushButton(self.centralWidget)
		self.r = QPushButton(self.centralWidget)
		self.t = QPushButton(self.centralWidget)
		self.y = QPushButton(self.centralWidget)
		self.u = QPushButton(self.centralWidget)
		self.i = QPushButton(self.centralWidget)
		self.o = QPushButton(self.centralWidget)
		self.p = QPushButton(self.centralWidget)
		self.open_bracket = QPushButton(self.centralWidget)
		self.closed_bracket = QPushButton(self.centralWidget)
		self.backslash = QPushButton(self.centralWidget)

		self.capslock = QPushButton(self.centralWidget)
		self.a = QPushButton(self.centralWidget)
		self.s = QPushButton(self.centralWidget)
		self.d = QPushButton(self.centralWidget)
		self.f = QPushButton(self.centralWidget)
		self.g = QPushButton(self.centralWidget)
		self.h = QPushButton(self.centralWidget)
		self.j = QPushButton(self.centralWidget)
		self.k = QPushButton(self.centralWidget)
		self.l = QPushButton(self.centralWidget)
		self.semicolon = QPushButton(self.centralWidget)
		self.apostrophe = QPushButton(self.centralWidget)
		self.enter = QPushButton(self.centralWidget)

		self.left_shift = QPushButton(self.centralWidget)
		self.z = QPushButton(self.centralWidget)
		self.x = QPushButton(self.centralWidget)
		self.c = QPushButton(self.centralWidget)
		self.v = QPushButton(self.centralWidget)
		self.b = QPushButton(self.centralWidget)
		self.n = QPushButton(self.centralWidget)
		self.m = QPushButton(self.centralWidget)
		self.comma = QPushButton(self.centralWidget)
		self.dot = QPushButton(self.centralWidget)
		self.slash = QPushButton(self.centralWidget)
		self.right_shift = QPushButton(self.centralWidget)

		self.left_ctrl = QPushButton(self.centralWidget)
		self.right_alt = QPushButton(self.centralWidget)
		self.space = QPushButton(self.centralWidget)
		self.left_alt = QPushButton(self.centralWidget)
		self.right_ctrl = QPushButton(self.centralWidget)
	
		self.insert = QPushButton(self.centralWidget)
		self.home = QPushButton(self.centralWidget)
		self.pgup = QPushButton(self.centralWidget)
		self.delete = QPushButton(self.centralWidget)
		self.end = QPushButton(self.centralWidget)
		self.pgdn = QPushButton(self.centralWidget)
		self.uparrow = QPushButton(self.centralWidget)
		self.leftarrow = QPushButton(self.centralWidget)
		self.downarrow = QPushButton(self.centralWidget)
		self.rightarrow = QPushButton(self.centralWidget)

		self.numlock = QPushButton(self.centralWidget)
		self.kp_slash = QPushButton(self.centralWidget)
		self.kp_multiply = QPushButton(self.centralWidget)
		self.kp_minus = QPushButton(self.centralWidget)
		self.kp_home = QPushButton(self.centralWidget)
		self.kp_uparrow = QPushButton(self.centralWidget)
		self.kp_pgup = QPushButton(self.centralWidget)
		self.kp_plus = QPushButton(self.centralWidget)
		self.kp_plus.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
		self.kp_leftarrow = QPushButton(self.centralWidget)
		self.kp_five = QPushButton(self.centralWidget)
		self.kp_rightarrow = QPushButton(self.centralWidget)
		self.kp_end = QPushButton(self.centralWidget)
		self.kp_downarrow = QPushButton(self.centralWidget)
		self.kp_pgdn = QPushButton(self.centralWidget)
		self.kp_enter = QPushButton(self.centralWidget)
		self.kp_enter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
		self.kp_insert = QPushButton(self.centralWidget)
		self.kp_delete = QPushButton(self.centralWidget)

		self.buy = QPushButton(self.centralWidget)
		self.buy.setStyleSheet("QPushButton"
		"{"
		"font-size: 17px;"
		"}"		
		)
		self.buy.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
		self.hand_switch = QPushButton(self.centralWidget)
		self.clear_decals = QPushButton(self.centralWidget)
		self.bind_grenade = QPushButton(self.centralWidget)
		self.voice_mute = QPushButton(self.centralWidget)
		self.bomb_drop = QPushButton(self.centralWidget)
		self.copy = QPushButton(self.centralWidget)
		self.reset = QPushButton(self.centralWidget)

		self.ak47 = QPushButton(self.centralWidget)
		self.ak47.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
		self.m4s = QPushButton(self.centralWidget)
		self.m4s.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
		self.aug = QPushButton(self.centralWidget)
		self.sg = QPushButton(self.centralWidget)
		self.awp = QPushButton(self.centralWidget)
		self.ssg = QPushButton(self.centralWidget)
		self.famas = QPushButton(self.centralWidget)
		self.galil = QPushButton(self.centralWidget)

		self.mac10 = QPushButton(self.centralWidget)
		self.mp9 = QPushButton(self.centralWidget)
		self.mp7 = QPushButton(self.centralWidget)
		self.ump = QPushButton(self.centralWidget)
		self.bizon = QPushButton(self.centralWidget)
		self.p90 = QPushButton(self.centralWidget)
		self.mp5 = QPushButton(self.centralWidget)

		self.xm = QPushButton(self.centralWidget)
		self.sawedoff = QPushButton(self.centralWidget)
		self.mag7 = QPushButton(self.centralWidget)

		self.p250 = QPushButton(self.centralWidget)
		self.cz75 = QPushButton(self.centralWidget)
		self.tec9 = QPushButton(self.centralWidget)
		self.fiveseven = QPushButton(self.centralWidget)
		self.deagle = QPushButton(self.centralWidget)
		self.revolver = QPushButton(self.centralWidget)

		self.nade = QPushButton(self.centralWidget)
		self.flash = QPushButton(self.centralWidget)
		self.double_flash = QPushButton(self.centralWidget)
		self.smoke = QPushButton(self.centralWidget)
		self.molotov = QPushButton(self.centralWidget)
		self.inc_grenade = QPushButton(self.centralWidget)

		self.vest = QPushButton(self.centralWidget)
		self.vest.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
		self.vest_helmet = QPushButton(self.centralWidget)
		self.vest_helmet.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
		self.defuse_kit = QPushButton(self.centralWidget)

		self.mouse3 = QPushButton(self.centralWidget)
		self.mouse3.setStyleSheet(
		"margin-top: 25px;"
		"margin-bottom: 10px;"	
		)
		self.mouse4 = QPushButton(self.centralWidget)
		self.mouse4.setStyleSheet(
		"margin-top: 25px;"
		"margin-bottom: 10px;"
		)
		self.mouse5 = QPushButton(self.centralWidget)
		self.mouse5.setStyleSheet(
		"margin-top: 25px;"
		"margin-bottom: 10px;"
		)

		self.f1.setText("F1")
		self.f2.setText("F2")
		self.f3.setText("F3")
		self.f4.setText("F4")
		self.f5.setText("F5")
		self.f6.setText("F6")
		self.f7.setText("F7")
		self.f8.setText("F8")
		self.f9.setText("F9")
		self.f10.setText("F10")
		self.f11.setText("F11")
		self.f12.setText("F12")
		self.acute.setText("`")
		self.one.setText("1")
		self.two.setText("2")
		self.three.setText("3")
		self.four.setText("4")
		self.five.setText("5")
		self.six.setText("6")
		self.seven.setText("7")
		self.eight.setText("8")
		self.nine.setText("9")
		self.zero.setText("0")
		self.minus.setText("-")
		self.equal.setText("=")
		self.backspace.setText("Backspace")
		self.tab.setText("TAB")
		self.q.setText("Q")
		self.w.setText("W")
		self.e.setText("E")
		self.r.setText("R")
		self.t.setText("T")
		self.y.setText("Y")
		self.u.setText("U")
		self.i.setText("I")
		self.o.setText("O")
		self.p.setText("P")
		self.open_bracket.setText("[")
		self.closed_bracket.setText("]")
		self.backslash.setText("\\")
		self.capslock.setText("Caps Lock")
		self.a.setText("A")
		self.s.setText("S")
		self.d.setText("D")
		self.f.setText("F")
		self.g.setText("G")
		self.h.setText("H")
		self.j.setText("J")
		self.k.setText("K")
		self.l.setText("L")
		self.semicolon.setText(";")
		self.apostrophe.setText("'")
		self.enter.setText("Enter")
		self.left_shift.setText("Shift")
		self.z.setText("Z")
		self.x.setText("X")
		self.c.setText("C")
		self.v.setText("V")
		self.b.setText("B")
		self.n.setText("N")
		self.m.setText("M")
		self.comma.setText(",")
		self.dot.setText(".")
		self.slash.setText("/")
		self.right_shift.setText("Shift")
		self.left_ctrl.setText("Ctrl")
		self.left_alt.setText("Alt")
		self.space.setText("Space")
		self.right_alt.setText("Alt")
		self.right_ctrl.setText("Ctrl")
		self.insert.setText("Insert")
		self.home.setText("Home")
		self.pgup.setText("PgUp")
		self.delete.setText("Del")
		self.end.setText("End")
		self.pgdn.setText("PgDn")
		self.uparrow.setText("↑")
		self.leftarrow.setText("←")
		self.downarrow.setText("↓")
		self.rightarrow.setText("→")
		self.numlock.setText("Num Lock")
		self.kp_slash.setText("/")
		self.kp_multiply.setText("*")
		self.kp_minus.setText("-")
		self.kp_home.setText("7")
		self.kp_uparrow.setText("8")
		self.kp_pgup.setText("9")
		self.kp_plus.setText("+")
		self.kp_leftarrow.setText("4")
		self.kp_five.setText("5")
		self.kp_rightarrow.setText("6")
		self.kp_end.setText("1")
		self.kp_downarrow.setText("2")
		self.kp_pgdn.setText("3")
		self.kp_enter.setText("Enter")
		self.kp_insert.setText("0")
		self.kp_delete.setText(".")

		self.buy.setText("BUY")
		self.bind_grenade.setText("Bind Grenades")
		self.voice_mute.setText("Mute Voice Chat")
		self.bomb_drop.setText("Bomb Drop")
		self.reset.setText("RESET")
		self.clear_decals.setText("Clear Decals")
		self.hand_switch.setText("Switch Hands")
		self.copy.setText("Copy to Clipboard")
		self.mouse3.setText("Mouse 3")
		self.mouse4.setText("Mouse 4")
		self.mouse5.setText("Mouse 5")

		self.ak47.setText("AK-47")
		self.m4s.setText("M4A4/1-S")
		self.aug.setText("AUG")
		self.sg.setText("SG 553")
		self.awp.setText("AWP")
		self.galil.setText("Galil AR")
		self.famas.setText("FAMAS")
		self.ssg.setText("SSG 08")

		self.mac10.setText("MAC-10")
		self.mp9.setText("MP9")
		self.mp7.setText("MP7")
		self.bizon.setText("PP-Bizon")
		self.p90.setText("P90")
		self.ump.setText("UMP-45")
		self.mp5.setText("MP5-SD")

		self.mag7.setText("MAG-7")
		self.sawedoff.setText("Sawed-Off")
		self.xm.setText("XM1014")

		self.p250.setText("P250")
		self.cz75.setText("CZ75-Auto")
		self.fiveseven.setText("Five-SeveN")
		self.tec9.setText("Tec-9")
		self.deagle.setText("Desert Eagle")
		self.revolver.setText("R8 Revolver")

		self.vest.setText("Kevlar Vest")
		self.vest_helmet.setText(f"Kevlar\n +\nHelmet")
		self.defuse_kit.setText("Defuse Kit")

		self.flash.setText("Flash")
		self.double_flash.setText("2x Flash")
		self.nade.setText("Grenade")
		self.smoke.setText("Smoke")
		self.inc_grenade.setText("INC-Grenade")
		self.molotov.setText("Molotov")

		self.layout.addWidget(self.commands_display, 0, 5, 5, 7)

		self.layout.addWidget(self.bind_grenade, 0, 0, 1, 2)
		self.layout.addWidget(self.bomb_drop, 1, 0, 1, 2)
		self.layout.addWidget(self.voice_mute, 2, 0, 1, 2)
		self.layout.addWidget(self.hand_switch, 3, 0, 1, 2)
		self.layout.addWidget(self.clear_decals, 4, 0, 1, 2)

		self.layout.addWidget(self.buy, 0, 3, 2, 2)
		self.layout.addWidget(self.reset, 3, 3, 1, 2)
		self.layout.addWidget(self.copy, 4, 3, 1, 2)

		self.layout.addWidget(self.ak47, 0, 12, 2, 1)
		self.layout.addWidget(self.m4s, 0, 13, 2, 1)
		self.layout.addWidget(self.vest, 2, 12, 2, 1)
		self.layout.addWidget(self.vest_helmet, 2, 13, 2, 1)
		self.layout.addWidget(self.defuse_kit, 4, 12)
		self.layout.addWidget(self.double_flash, 4, 13)

		self.layout.addWidget(self.flash, 0, 14)
		self.layout.addWidget(self.smoke, 1, 14)
		self.layout.addWidget(self.nade, 2, 14)
		self.layout.addWidget(self.inc_grenade, 3, 14)
		self.layout.addWidget(self.molotov, 4, 14)

		self.layout.addWidget(self.awp, 0, 15)
		self.layout.addWidget(self.deagle, 1, 15)

		self.layout.addWidget(self.aug, 0, 16)
		self.layout.addWidget(self.sg, 1, 16)
		self.layout.addWidget(self.famas, 3, 16)
		self.layout.addWidget(self.galil, 2, 16)
		self.layout.addWidget(self.ssg, 4, 16)

		self.layout.addWidget(self.fiveseven, 0, 17)
		self.layout.addWidget(self.tec9, 1, 17)
		self.layout.addWidget(self.cz75, 3, 17)
		self.layout.addWidget(self.p250, 2, 17)
		self.layout.addWidget(self.revolver, 4, 17)

		self.layout.addWidget(self.mac10, 0, 18)
		self.layout.addWidget(self.mp9, 1, 18)
		self.layout.addWidget(self.mp7, 2, 18)
		self.layout.addWidget(self.ump, 3, 18)
		self.layout.addWidget(self.p90, 4, 18)

		self.layout.addWidget(self.mp5, 0, 19)
		self.layout.addWidget(self.bizon, 1, 19)
		self.layout.addWidget(self.mag7, 2, 19)
		self.layout.addWidget(self.sawedoff, 3, 19)
		self.layout.addWidget(self.xm, 4, 19)

		self.layout.addWidget(self.mouse3, 5, 7)
		self.layout.addWidget(self.mouse4, 5, 8)
		self.layout.addWidget(self.mouse5, 5, 9)
		
		self.layout.addWidget(self.f1, 6, 0)
		self.layout.addWidget(self.f2, 6, 1)
		self.layout.addWidget(self.f3, 6, 2)
		self.layout.addWidget(self.f4, 6, 3)
		self.layout.addWidget(self.f5, 6, 4)
		self.layout.addWidget(self.f6, 6, 5)
		self.layout.addWidget(self.f7, 6, 6)
		self.layout.addWidget(self.f8, 6, 7)
		self.layout.addWidget(self.f9, 6, 8)
		self.layout.addWidget(self.f10, 6, 9)
		self.layout.addWidget(self.f11, 6, 10)
		self.layout.addWidget(self.f12, 6, 11)

		self.layout.addWidget(self.acute, 7, 0)
		self.layout.addWidget(self.one, 7, 1)
		self.layout.addWidget(self.two, 7, 2)
		self.layout.addWidget(self.three, 7, 3)
		self.layout.addWidget(self.four, 7, 4)
		self.layout.addWidget(self.five, 7, 5)
		self.layout.addWidget(self.six, 7, 6)
		self.layout.addWidget(self.seven, 7, 7)
		self.layout.addWidget(self.eight, 7, 8)
		self.layout.addWidget(self.nine, 7, 9)
		self.layout.addWidget(self.zero, 7, 10)
		self.layout.addWidget(self.minus, 7, 11)
		self.layout.addWidget(self.equal, 7, 12)
		self.layout.addWidget(self.backspace, 7, 13)
		self.layout.addWidget(self.insert, 7, 14)
		self.layout.addWidget(self.home, 7, 15)
		self.layout.addWidget(self.pgup, 7, 16)
		self.layout.addWidget(self.numlock, 7, 17)
		self.layout.addWidget(self.kp_slash, 7, 18)
		self.layout.addWidget(self.kp_multiply, 7, 19)
		self.layout.addWidget(self.kp_minus, 7, 20)

		self.layout.addWidget(self.tab, 8, 0)
		self.layout.addWidget(self.q, 8, 1)
		self.layout.addWidget(self.w, 8, 2)
		self.layout.addWidget(self.e, 8, 3)
		self.layout.addWidget(self.r, 8, 4)
		self.layout.addWidget(self.t, 8, 5)
		self.layout.addWidget(self.y, 8, 6)
		self.layout.addWidget(self.u, 8, 7)
		self.layout.addWidget(self.i, 8, 8)
		self.layout.addWidget(self.o, 8, 9)
		self.layout.addWidget(self.p, 8, 10)
		self.layout.addWidget(self.open_bracket, 8, 11)
		self.layout.addWidget(self.closed_bracket, 8, 12)
		self.layout.addWidget(self.backslash, 8, 13)
		self.layout.addWidget(self.delete, 8, 14)
		self.layout.addWidget(self.end, 8, 15)
		self.layout.addWidget(self.pgdn, 8, 16)
		self.layout.addWidget(self.kp_home, 8, 17)
		self.layout.addWidget(self.kp_uparrow, 8, 18)
		self.layout.addWidget(self.kp_pgup, 8, 19)
		self.layout.addWidget(self.kp_plus, 8, 20, 2, 1)

		self.layout.addWidget(self.capslock, 9, 0)
		self.layout.addWidget(self.a, 9, 1)
		self.layout.addWidget(self.s, 9, 2)
		self.layout.addWidget(self.d, 9, 3)
		self.layout.addWidget(self.f, 9, 4)
		self.layout.addWidget(self.g, 9, 5)
		self.layout.addWidget(self.h, 9, 6)
		self.layout.addWidget(self.j, 9, 7)
		self.layout.addWidget(self.k, 9, 8)
		self.layout.addWidget(self.l, 9, 9)
		self.layout.addWidget(self.semicolon, 9, 10)
		self.layout.addWidget(self.apostrophe, 9, 11)
		self.layout.addWidget(self.enter, 9, 12, 1, 2)
		self.layout.addWidget(self.kp_leftarrow, 9, 17)
		self.layout.addWidget(self.kp_five, 9, 18)
		self.layout.addWidget(self.kp_rightarrow, 9, 19)

		self.layout.addWidget(self.left_shift, 10, 0, 1, 2)
		self.layout.addWidget(self.z, 10, 2)
		self.layout.addWidget(self.x, 10, 3)
		self.layout.addWidget(self.c, 10, 4)
		self.layout.addWidget(self.v, 10, 5)
		self.layout.addWidget(self.b, 10, 6)
		self.layout.addWidget(self.n, 10, 7)
		self.layout.addWidget(self.m, 10, 8)
		self.layout.addWidget(self.comma, 10, 9)
		self.layout.addWidget(self.dot, 10, 10)
		self.layout.addWidget(self.slash, 10, 11)
		self.layout.addWidget(self.right_shift, 10, 12, 1, 2)
		self.layout.addWidget(self.uparrow, 10, 15)
		self.layout.addWidget(self.kp_end, 10, 17)
		self.layout.addWidget(self.kp_downarrow, 10, 18)
		self.layout.addWidget(self.kp_pgdn, 10, 19)
		self.layout.addWidget(self.kp_enter, 10, 20, 2, 1)

		self.layout.addWidget(self.left_ctrl, 11, 0)
		self.layout.addWidget(self.left_alt, 11, 2)
		self.layout.addWidget(self.space, 11, 3, 1, 7)
		self.layout.addWidget(self.right_alt, 11, 10)
		self.layout.addWidget(self.right_ctrl, 11, 13)
		self.layout.addWidget(self.leftarrow, 11, 14)
		self.layout.addWidget(self.downarrow, 11, 15)
		self.layout.addWidget(self.rightarrow, 11, 16)
		self.layout.addWidget(self.kp_insert, 11, 17, 1, 2)
		self.layout.addWidget(self.kp_delete, 11, 19)

		self.f1.clicked.connect(lambda: self.key_clicked("f1"))
		self.f2.clicked.connect(lambda: self.key_clicked("f2"))
		self.f3.clicked.connect(lambda: self.key_clicked("f3"))
		self.f4.clicked.connect(lambda: self.key_clicked("f4"))
		self.f5.clicked.connect(lambda: self.key_clicked("f5"))
		self.f6.clicked.connect(lambda: self.key_clicked("f6"))
		self.f7.clicked.connect(lambda: self.key_clicked("f7"))
		self.f8.clicked.connect(lambda: self.key_clicked("f8"))
		self.f9.clicked.connect(lambda: self.key_clicked("f9"))
		self.f10.clicked.connect(lambda: self.key_clicked("f10"))
		self.f11.clicked.connect(lambda: self.key_clicked("f11"))
		self.f12.clicked.connect(lambda: self.key_clicked("f12"))

		self.acute.clicked.connect(lambda: self.key_clicked("`"))
		self.one.clicked.connect(lambda: self.key_clicked("1"))
		self.two.clicked.connect(lambda: self.key_clicked("2"))
		self.three.clicked.connect(lambda: self.key_clicked("3"))
		self.four.clicked.connect(lambda: self.key_clicked("4"))
		self.five.clicked.connect(lambda: self.key_clicked("5"))
		self.six.clicked.connect(lambda: self.key_clicked("6"))
		self.seven.clicked.connect(lambda: self.key_clicked("7"))
		self.eight.clicked.connect(lambda: self.key_clicked("8"))
		self.nine.clicked.connect(lambda: self.key_clicked("9"))
		self.zero.clicked.connect(lambda: self.key_clicked("0"))
		self.minus.clicked.connect(lambda: self.key_clicked("-"))
		self.equal.clicked.connect(lambda: self.key_clicked("="))
		self.backspace.clicked.connect(lambda: self.key_clicked("Backspace"))
		self.insert.clicked.connect(lambda: self.key_clicked("ins"))
		self.home.clicked.connect(lambda: self.key_clicked("Home"))
		self.pgup.clicked.connect(lambda: self.key_clicked("pgup"))
		self.numlock.clicked.connect(lambda: self.key_clicked("numlock"))
		self.kp_slash.clicked.connect(lambda: self.key_clicked("kp_slash"))
		self.kp_multiply.clicked.connect(lambda: self.key_clicked("kp_multiply"))
		self.kp_minus.clicked.connect(lambda: self.key_clicked("kp_minus"))

		self.tab.clicked.connect(lambda: self.key_clicked("Tab"))
		self.q.clicked.connect(lambda: self.key_clicked("Q"))
		self.w.clicked.connect(lambda: self.key_clicked("W"))
		self.e.clicked.connect(lambda: self.key_clicked("E"))
		self.r.clicked.connect(lambda: self.key_clicked("R"))
		self.t.clicked.connect(lambda: self.key_clicked("T"))
		self.y.clicked.connect(lambda: self.key_clicked("Y"))
		self.u.clicked.connect(lambda: self.key_clicked("U"))
		self.i.clicked.connect(lambda: self.key_clicked("I"))
		self.o.clicked.connect(lambda: self.key_clicked("O"))
		self.p.clicked.connect(lambda: self.key_clicked("P"))
		self.open_bracket.clicked.connect(lambda: self.key_clicked("["))
		self.closed_bracket.clicked.connect(lambda: self.key_clicked("]"))
		self.backspace.clicked.connect(lambda: self.key_clicked("\\"))
		self.delete.clicked.connect(lambda: self.key_clicked("del"))
		self.end.clicked.connect(lambda: self.key_clicked("End"))
		self.pgdn.clicked.connect(lambda: self.key_clicked("pgdn"))
		self.kp_home.clicked.connect(lambda: self.key_clicked("kp_home"))
		self.kp_uparrow.clicked.connect(lambda: self.key_clicked("kp_uparrow"))
		self.kp_pgup.clicked.connect(lambda: self.key_clicked("kp_pgup"))
		self.kp_plus.clicked.connect(lambda: self.key_clicked("kp_plus"))

		self.capslock.clicked.connect(lambda: self.key_clicked("CapsLock"))
		self.a.clicked.connect(lambda: self.key_clicked("A"))
		self.s.clicked.connect(lambda: self.key_clicked("S"))
		self.d.clicked.connect(lambda: self.key_clicked("D"))
		self.f.clicked.connect(lambda: self.key_clicked("F"))
		self.g.clicked.connect(lambda: self.key_clicked("G"))
		self.h.clicked.connect(lambda: self.key_clicked("H"))
		self.j.clicked.connect(lambda: self.key_clicked("J"))
		self.k.clicked.connect(lambda: self.key_clicked("K"))
		self.l.clicked.connect(lambda: self.key_clicked("L"))
		self.semicolon.clicked.connect(lambda: self.key_clicked("semicolon"))
		self.apostrophe.clicked.connect(lambda: self.key_clicked("'"))
		self.enter.clicked.connect(lambda: self.key_clicked("Enter"))
		self.kp_leftarrow.clicked.connect(lambda: self.key_clicked("kp_leftarrow"))
		self.kp_five.clicked.connect(lambda: self.key_clicked("kp_5"))
		self.kp_rightarrow.clicked.connect(lambda: self.key_clicked("kp_rightarrow"))

		self.left_shift.clicked.connect(lambda: self.key_clicked("Shift"))
		self.z.clicked.connect(lambda: self.key_clicked("Z"))
		self.x.clicked.connect(lambda: self.key_clicked("X"))
		self.c.clicked.connect(lambda: self.key_clicked("C"))
		self.v.clicked.connect(lambda: self.key_clicked("V"))
		self.b.clicked.connect(lambda: self.key_clicked("B"))
		self.n.clicked.connect(lambda: self.key_clicked("N"))
		self.m.clicked.connect(lambda: self.key_clicked("M"))
		self.comma.clicked.connect(lambda: self.key_clicked(","))
		self.dot.clicked.connect(lambda: self.key_clicked("."))
		self.slash.clicked.connect(lambda: self.key_clicked("/"))
		self.right_shift.clicked.connect(lambda: self.key_clicked("Shift"))
		self.uparrow.clicked.connect(lambda: self.key_clicked("uparrow"))
		self.kp_end.clicked.connect(lambda: self.key_clicked("kp_end"))
		self.kp_downarrow.clicked.connect(lambda: self.key_clicked("kp_downarrow"))
		self.kp_pgdn.clicked.connect(lambda: self.key_clicked("kp_pgdn"))
		self.kp_enter.clicked.connect(lambda: self.key_clicked("kp_enter"))

		self.left_ctrl.clicked.connect(lambda: self.key_clicked("Ctrl"))
		self.left_alt.clicked.connect(lambda: self.key_clicked("Alt"))
		self.space.clicked.connect(lambda: self.key_clicked("Space"))
		self.right_alt.clicked.connect(lambda: self.key_clicked("Alt"))
		self.right_ctrl.clicked.connect(lambda: self.key_clicked("Ctrl"))
		self.leftarrow.clicked.connect(lambda: self.key_clicked("leftarrow"))
		self.downarrow.clicked.connect(lambda: self.key_clicked("downarrow"))
		self.rightarrow.clicked.connect(lambda: self.key_clicked("rightarrow"))
		self.kp_insert.clicked.connect(lambda: self.key_clicked("kp_ins"))
		self.kp_delete.clicked.connect(lambda: self.key_clicked("kp_del"))

		self.mouse3.clicked.connect(lambda: self.key_clicked("mouse3"))
		self.mouse4.clicked.connect(lambda: self.key_clicked("mouse4"))
		self.mouse5.clicked.connect(lambda: self.key_clicked("mouse5"))

		self.buy.clicked.connect(self.buy_clicked)
		self.reset.clicked.connect(self.reset_clicked)
		self.bomb_drop.clicked.connect(self.bomb_drop_clicked)
		self.clear_decals.clicked.connect(self.clear_decals_clicked)
		self.bind_grenade.clicked.connect(self.bind_grenade_clicked)
		self.voice_mute.clicked.connect(self.voice_mute_clicked)
		self.hand_switch.clicked.connect(self.hand_switch_clicked)
		self.copy.clicked.connect(self.copy_clicked)

		self.ak47.clicked.connect(lambda: self.gear_clicked('"buy ak47; buy m4a1";'))
		self.m4s.clicked.connect(lambda: self.gear_clicked('"buy m4a1; buy ak47";'))
		self.vest.clicked.connect(lambda: self.gear_clicked("buy vest;"))
		self.vest_helmet.clicked.connect(lambda: self.gear_clicked("buy vesthelm;"))
		self.defuse_kit.clicked.connect(lambda: self.gear_clicked("buy defuser;"))
		self.double_flash.clicked.connect(lambda: self.gear_clicked('"buy flashbang; buy flashbang";'))

		self.flash.clicked.connect(lambda: self.gear_clicked("buy flashbang;"))
		self.smoke.clicked.connect(lambda: self.gear_clicked("buy smokegrenade;"))
		self.nade.clicked.connect(lambda: self.gear_clicked("buy hegrenade;"))
		self.inc_grenade.clicked.connect(lambda: self.gear_clicked('"buy incgrenade; buy molotov;"'))
		self.molotov.clicked.connect(lambda: self.gear_clicked('"buy molotov; "buy incgrenade;"'))

		self.awp.clicked.connect(lambda: self.gear_clicked("buy awp;"))
		self.deagle.clicked.connect(lambda: self.gear_clicked('"buy deagle; buy revolver;"'))

		self.aug.clicked.connect(lambda: self.gear_clicked('"buy aug; buy sg556;"'))
		self.sg.clicked.connect(lambda: self.gear_clicked('"buy sg556; buy aug;"'))
		self.galil.clicked.connect(lambda: self.gear_clicked('"buy galilar; buy famas;"'))
		self.famas.clicked.connect(lambda: self.gear_clicked('"buy famas; buy galilar";'))
		self.ssg.clicked.connect(lambda: self.gear_clicked("buy ssg08;"))
		
		self.fiveseven.clicked.connect(lambda: self.gear_clicked('"buy fiveseven; buy tec9";'))
		self.tec9.clicked.connect(lambda: self.gear_clicked('"buy tec9; buy fiveseven";'))
		self.p250.clicked.connect(lambda: self.gear_clicked("buy p250;"))
		self.cz75.clicked.connect(lambda: self.gear_clicked('"buy fiveseven; buy tec9";'))
		self.revolver.clicked.connect(lambda: self.gear_clicked('"buy revolver; buy deagle";'))

		self.mac10.clicked.connect(lambda: self.gear_clicked('"buy mac10; buy mp9";'))
		self.mp9.clicked.connect(lambda: self.gear_clicked('"buy mp9; buy mac10";'))
		self.mp7.clicked.connect(lambda: self.gear_clicked("buy mp7;"))
		self.ump.clicked.connect(lambda: self.gear_clicked("buy ump;"))
		self.p90.clicked.connect(lambda: self.gear_clicked("buy p90;"))

		self.mp5.clicked.connect(lambda: self.gear_clicked("buy mp7;"))
		self.bizon.clicked.connect(lambda: self.gear_clicked("buy bizon;"))
		self.mag7.clicked.connect(lambda: self.gear_clicked('"buy mag7; buy sawedoff";'))
		self.sawedoff.clicked.connect(lambda: self.gear_clicked('"buy sawedoff; buy mag7";'))
		self.xm.clicked.connect(lambda: self.gear_clicked("buy xm1014;"))	

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------	

		self.command: str = ""
		self.bind: Union[NoneType, bool] = None
		self.action: Union[NoneType, str] = None
		self.grenade_keys: tuple = (self.flash, self.smoke, self.nade, self.inc_grenade, self.molotov)
		self.bound_keys: list = () #TODO bound keys

#------------------------------------------------------------------------------------------

	def buy_clicked(self) -> None:
		self.action = "buy"
				
	def key_clicked(self, key_value: str) -> None:
		if self.action and not self.bind:
			if self.action == "buy":
				self.command += f"bind { key_value } "
				self.bind = True

			elif self.action == "bind_grenade": #bind z "use weapon_flashbang";
				self.command += f"bind { key_value} "
				self.bind = True
				for key in self.grenade_keys:
					key.setStyleSheet("background-color: #3f3f3f;")
				
			elif self.action == "bomb_drop":
				self.command += f'bind { key_value } "use weapon_knife; use weapon_c4; drop; slot1;"\n'
				self.commands_display.setText(self.command)
				self.action = None

			elif self.action == "voice_mute":
				self.command += f"bindtoggle { key_value } voice_enable;\n"
				self.commands_display.setText(self.command)
				self.action = None
			
			elif self.action == "hand_switch":
				self.command += f'bind { key_value } "cl_righthand 0 1";\n'
				self.commands_display.setText(self.command)
				self.action = None

			elif self.action == "clear_decals":
				self.command += f"bind { key_value } r_cleardecals;\n"
				self.commands_display.setText(self.command)
				self.action = None
		else:
			pass
			
	def gear_clicked(self, key_value: str) -> None:
		if self.action and self.bind:
			if self.action == "buy":
				self.command += f"{ key_value }\n"
				self.commands_display.setText(self.command)
				self.action = None
				self.bind = None

			elif self.action == "bind_grenade":
				new_key_value = key_value.replace("buy ", "use weapon_")
				self.command += f"{ new_key_value }\n"
				self.commands_display.setText(self.command)
				self.action = None
				self.bind = None
				for key in self.grenade_keys:
					key.setStyleSheet("background-color: #2F2F2F;")
		else:
			pass

#------------------------------------------------------------------------------------------	

	def bind_grenade_clicked(self) -> None:
		self.action = "bind_grenade"

	def bomb_drop_clicked(self) -> None:
		self.action = "bomb_drop"
		
	def voice_mute_clicked(self) -> None:
		self.action = "voice_mute"
		
	def hand_switch_clicked(self) -> None:
		self.action = "hand_switch"
		
	def clear_decals_clicked(self) -> None:
		self.action = "clear_decals"
		
	def copy_clicked(self) -> None:
		QApplication.clipboard().setText(self.command[0:-1])

	def reset_clicked(self) -> None:
		self.commands_display.setText("")
		self.command = ""
		self.action = None
		self.bind = None
		self.action = None
		for key in self.grenade_keys:
			key.setStyleSheet("background-color: #2F2F2F;")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

STYLESHEET = """
		QWidget {
			background-color: #2F2F2F;
			color: white;
			font-family: "Calibri";
		}
		QTextEdit {
			border: 1px solid #92B4A7;
			background-color: grey;
			color: #2F2F2F;
		}
		QPushButton {
			min-height: 30px;
		}
		"""


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyleSheet(STYLESHEET)
	window = CsgoBindGenerator()
	window.show()
	center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
	geo = window.frameGeometry()
	geo.moveCenter(center)	
	window.move(geo.topLeft())
	sys.exit(app.exec_())