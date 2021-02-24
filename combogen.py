# coding: UTF-8
import sys
l1lll1ll = sys.version_info [0] == 2
l1lll1l1 = 2048
l11l1l1 = 7
def l11lllll (l111l11):
    global l1l11
    l1l1l1 = ord (l111l11 [-1])
    l1ll111l = l111l11 [:-1]
    l1lll1l = l1l1l1 % len (l1ll111l)
    l1ll1l = l1ll111l [:l1lll1l] + l1ll111l [l1lll1l:]
    if l1lll1ll:
        l1l1l1l1 = unicode () .join ([unichr (ord (char) - l1lll1l1 - (l111ll11 + l1l1l1) % l11l1l1) for l111ll11, char in enumerate (l1ll1l)])
    else:
        l1l1l1l1 = str () .join ([chr (ord (char) - l1lll1l1 - (l111ll11 + l1l1l1) % l11l1l1) for l111ll11, char in enumerate (l1ll1l)])
    return eval (l1l1l1l1)
while 1:
	try:
		import sys, time, os, re, colorama, requests, random, bs4, threading, lxml, base64, getpass, hashlib
		from requests import Session, Request
		from bs4 import BeautifulSoup
		from urllib.parse import quote
		from distutils.util import strtobool
		from colorama import Fore, Back, Style
		from selectmenu import SelectMenu
		from threading import Lock
		from lxml import html
		break
	except ImportError:
		print(l11lllll (u"ࠫࠥࡄࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡘࡣ࡬ࡸࠥ࡝ࡨࡪ࡮ࡨࠤࡹ࡮ࡥࠡࡒࡵࡳ࡬ࡸࡡ࡮ࠢࡌࡲࡸࡺࡡ࡭࡮ࡶࠤࡹ࡮ࡥࠡࡆࡨࡴࡪࡴࡤࡦࡰࡦ࡭ࡪࡹ࠮ࠡࡖࡋࡍࡘࠦࡍࡊࡉࡋࡘ࡚ࠥࡁࡌࡇࠣࡅࠥࡒࡏࡏࡉࠣࡘࡎࡓࡅ࠯ࠩࠀ"))
		os.system(l11lllll (u"ࠬࡧࡰࡵࠢࡸࡴࡩࡧࡴࡦࠢࠩࠪࠥࡧࡰࡵࠢࡸࡴ࡬ࡸࡡࡥࡧࠣࠪࠫࠦࡡࡱࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡷࡵ࡯ࡵ࠯ࡵࡩࡵࡵࠠࡶࡰࡶࡸࡦࡨ࡬ࡦ࠯ࡵࡩࡵࡵࠠ࠮ࡻࠪࠁ"))
		os.system(l11lllll (u"࠭ࡡࡱࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡨࡲࡡ࡯ࡩࠣࡴࡾࡺࡨࡰࡰࠣࡰ࡮ࡨࡸࡴ࡮ࡷࠤࡱ࡯ࡢࡪࡥࡲࡲࡻࠦ࡬ࡪࡤ࡬ࡧࡴࡴࡶࠡ࠯ࡼࠫࠂ"))
		os.system(l11lllll (u"ࠧࡱ࡫ࡳࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡲࡸ࡮࡮ࠪࠃ"))
		os.system(l11lllll (u"ࠨࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦ࠭ࡳࠢࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳࠨࠄ"))
		os.system(l11lllll (u"ࠩࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡴࡧ࡯ࡩࡨࡺ࡭ࡦࡰࡸࠤࠬࠅ"))
		print(l11lllll (u"ࠪࡠࡳࡢ࡮ࠡࡀࠣࡈࡪࡶࡥ࡯ࡦࡨࡲࡨ࡯ࡥࡴࠢࡌࡲࡸࡺࡡ࡭࡮ࡨࡨ࠳ࠦࡒࡦࡵࡷࡥࡷࡺࡩ࡯ࡩ࠱࠲࠳࠭ࠆ"))
		os.system(l11lllll (u"ࠫࡨࡲࡥࡢࡴࠪࠇ"))
		continue
colorama.init(autoreset=True)
l = Lock()
l1ll = []
l111111 = l11lllll (u"ࠬ࠵ࡤࡢࡶࡤ࠳ࡩࡧࡴࡢ࠱ࡦࡳࡲ࠴ࡴࡦࡴࡰࡹࡽ࠵ࡦࡪ࡮ࡨࡷ࠴࡮࡯࡮ࡧ࠲ࠫࠈ")
l11111 = l11lllll (u"࠭࠯ࡥࡣࡷࡥ࠴ࡪࡡࡵࡣ࠲ࡧࡴࡳ࠮ࡵࡧࡵࡱࡺࡾ࠯ࡧ࡫࡯ࡩࡸ࠵ࡨࡰ࡯ࡨ࠳ࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴࠭ࠉ")
class l1l1lll1(Exception):
	pass
class l1l1l111(Exception):
	pass
class l11lll1l(Exception):
	pass
class l111llll(Exception):
	pass
class l1l1l11(Exception):
	pass
class l1l1l11l(Exception):
	pass
class l1llllll:
	def __init__(self, l1l11l11):
		self.l111lll = l1l11l11
		self.l1l1ll1 = {l11lllll (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫࠊ"):l11lllll (u"ࠨࡏࡲࡾ࡮ࡲ࡬ࡢ࠱࠸࠲࠵ࠦࠨࡂࡰࡧࡶࡴ࡯ࡤࠡ࠻࠾ࠤࡒࡵࡢࡪ࡮ࡨ࠿ࠥࡸࡶ࠻࠸࠺࠲࠵࠯ࠠࡈࡧࡦ࡯ࡴ࠵࠶࠸࠰࠳ࠤࡋ࡯ࡲࡦࡨࡲࡼ࠴࠼࠷࠯࠲ࠪࠋ"),
		 l11lllll (u"ࠩࡄࡧࡨ࡫ࡰࡵࠩࠌ"):l11lllll (u"ࠪࡸࡪࡾࡴ࠰ࡺࡰࡰ࠱ࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼࡲࡲࠬࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾࡨࡵ࡯࡯࠯ࡽࡳ࡬࠭ࡶࡨࡼࡹ࠵ࡨࡵ࡯࡯࠿ࡶࡃ࠰࠯࠻࠯ࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴ࠻ࡲ࠿࠳࠲࠽࠲ࡩ࡮ࡣࡪࡩ࠴ࡶ࡮ࡨ࠮࠭࠳࠯ࡁࡱ࠾࠲࠱࠹ࠬࠍ"),
		 l11lllll (u"ࠫࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨࠎ"):l11lllll (u"ࠬࡱࡥࡦࡲ࠰ࡥࡱ࡯ࡶࡦࠩࠏ"),
		 l11lllll (u"࠭ࡋࡦࡧࡳ࠱ࡆࡲࡩࡷࡧࠪࠐ"):l11lllll (u"ࠧ࠲࠳࠸ࠫࠑ"),
		 l11lllll (u"ࠨࡃࡦࡧࡪࡶࡴ࠮ࡅ࡫ࡥࡷࡹࡥࡵࠩࠒ"):l11lllll (u"ࠩࡌࡗࡔ࠳࠸࠹࠷࠼࠱࠶࠲ࡵࡵࡨ࠰࠼ࡀࡷ࠽࠱࠰࠺࠰࠯ࡁࡱ࠾࠲࠱࠻ࠬࠓ"),
		 l11lllll (u"ࠪࡅࡨࡩࡥࡱࡶ࠰ࡐࡦࡴࡧࡶࡣࡪࡩࠬࠔ"):l11lllll (u"ࠫࡪࡴ࠭ࡶࡵ࠯ࡩࡳࡁࡱ࠾࠲࠱࠹ࠬࠕ")}
		self.l11llll1 = []
		self.l11l1ll = 4
		self.l1l1llll = 6
		self.cookie = l11lllll (u"ࠬ࠭ࠖ")
		self.l1l1ll1 = l11lllll (u"࠭ࠧࠗ")
		self.ei = l11lllll (u"ࠧࠨ࠘")
		self.s = Session()
		self.s.headers.update(self.l1l1ll1)
		self.l1l1ll = None
		self.l1ll1l11 = False
		self.l1l111ll = False
	def l1ll1l1l(self, l1l11ll1):
		l1l11111 = requests.cookies.create_cookie(name=l11lllll (u"ࠨࡉࡒࡓࡌࡒࡅࡠࡃࡅ࡙ࡘࡋ࡟ࡆ࡚ࡈࡑࡕ࡚ࡉࡐࡐࠪ࠙"), value=l1l11ll1)
		self.s.cookies.set_cookie(l1l11111)
		self.l1ll1l11 = False
		self.l1l111ll = False
	def l11ll(self, url):
		req = Request(l11lllll (u"ࠩࡊࡉ࡙࠭ࠚ"), url)
		prep = req.prepare()
		l1lll1 = self.s.send(prep, timeout=30)
		return l1lll1
	def l11ll1l1(self):
		time.sleep(random.choice([self.l11l1ll, self.l1l1llll]))
	def l11ll1l(self):
		l1l111 = self.l11ll(l11lllll (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰࠫࠛ"))
		self.l11ll1l1()
		self.l11ll(l11lllll (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯ࡩࡲࡳ࡬ࡲࡥ࠯ࡥࡲࡱ࠴ࡴࡣࡳࠩࠜ"))
	def l11ll1ll(self):
		l1l111 = self.l11ll(l11lllll (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡪࡳࡴ࡭࡬ࡦ࠰ࡦࡳࡲ࠵ࡰࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࡃ࡭ࡲ࠽ࡦࡰࠪࠝ"))
		soup = BeautifulSoup(l1l111.content, l11lllll (u"࠭ࡨࡵ࡯࡯࠲ࡵࡧࡲࡴࡧࡵࠫࠞ"))
		l1lll = soup.find(l11lllll (u"ࠧࡪࡰࡳࡹࡹ࠭ࠟ"), {l11lllll (u"ࠨࡰࡤࡱࡪ࠭ࠠ"): l11lllll (u"ࠩࡶ࡭࡬࠭ࠡ")})
		self.l11ll1l1()
		self.l11ll(l11lllll (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰ࠳ࡸ࡫ࡴࡱࡴࡨࡪࡸࡅࡳࡪࡩࡀࠫࠢ") + quote(l1lll[l11lllll (u"ࠫࡻࡧ࡬ࡶࡧࠪࠣ")]) + l11lllll (u"ࠬࠬࡨ࡭࠿ࡨࡲࠫࡲࡲ࠾࡮ࡤࡲ࡬ࡥࡥ࡯ࠨࡶࡥ࡫࡫ࡵࡪ࠿࡬ࡱࡦ࡭ࡥࡴࠨࡶࡹ࡬࡭࡯࡯࠿࠵ࠪࡳ࡫ࡷࡸ࡫ࡱࡨࡴࡽ࠽࠱ࠨࡱࡹࡲࡃ࠱࠱࠲ࠩࡵࡂࠬࡰࡳࡧࡹࡁ࡭ࡺࡴࡱࠧ࠶ࡅࠪ࠸ࡆࠦ࠴ࡉࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰࠩ࠷ࡌࠦࡴࡷࡥࡱ࡮ࡺ࠲࠾ࡕࡤࡺࡪ࠱ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶ࠯ࠬࠤ"))
	def l11l1l1l(self, l1l111l1=None):
		while 1:
			try:
				l111ll1l = l11lllll (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡷࡸࡹ࠱࡫ࡴࡵࡧ࡭ࡧ࠱ࡧࡴࡳ࠯ࡴࡧࡤࡶࡨ࡮࠿ࡲ࠿ࠪࠥ") + str(quote(self.l111lll)) + l11lllll (u"ࠧࠧࡶࡥࡷࡂࡷࡤࡳ࠼ࠪࠦ") + l1l111l1 + l11lllll (u"ࠨࠨࡱࡹࡲࡃ࠱࠱࠲ࠩ࡬ࡱࡃࡥ࡯ࠨࡥ࡭ࡼࡃ࠱࠳࠺࠳ࠪࡧ࡯ࡨ࠾࠸࠴࠶ࠫࡶࡲ࡮ࡦࡀ࡭ࡻࡴࡳࠧࡧ࡬ࡁࠬࠧ") + str(quote(self.ei)) + l11lllll (u"ࠩࠩࡷࡦࡃࡎࠨࠨ")
				l1l111 = self.l11ll(l111ll1l)
				soup = BeautifulSoup(l1l111.text, l11lllll (u"ࠪ࡬ࡹࡳ࡬࠯ࡲࡤࡶࡸ࡫ࡲࠨࠩ"))
				l1llll1l = soup.findAll(l11lllll (u"ࠫ࡫ࡵࡲ࡮ࠩࠪ"))
				if not l1llll1l is not None:
					if l1llll1l != []:
						if l1llll1l[0][l11lllll (u"ࠬ࡯ࡤࠨࠫ")] == l11lllll (u"࠭ࡣࡢࡲࡷࡧ࡭ࡧ࠭ࡧࡱࡵࡱࠬࠬ"):
							raise l1l1lll1
				links = soup.findAll(l11lllll (u"ࠧࡢࠩ࠭"))
				for link in links:
					l111l1 = link[l11lllll (u"ࠨࡪࡵࡩ࡫࠭࠮")]
					if l11lllll (u"ࠩ࠲ࡹࡷࡲ࠿ࡲ࠿࡫ࡸࡹࡶࡳ࠻࠱࠲ࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮ࠩ࠯") in l111l1:
						self.l11llll1.append(l111l1[7:])
				break
			except l1l1lll1:
				print(Fore.RED + Style.DIM + l11lllll (u"ࠪࡠࡳࠦ࠾࡛ࠡࡲࡹࠥ࡮ࡡࡷࡧࠣࡆࡪ࡫࡮ࠡࡄ࡯ࡥࡨࡱ࡬ࡪࡵࡷࡩࡩࠦࡦࡳࡱࡰࠤࡌࡵ࡯ࡨ࡮ࡨ࠲ࠥࡕࡰࡦࡰࠣࠫ࠰") + Style.BRIGHT + l111ll1l + Style.DIM + l11lllll (u"ࠫࠥ࡯࡮ࠡࡈ࡬ࡶࡪ࡬࡯ࡹࠢࡤࡲࡩࠦࡅ࡯ࡶࡨࡶࠥࡺࡨࡦࠢࡆࡳࡳࡺࡥ࡯ࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࡋࡔࡕࡇࡍࡇࡢࡅࡇ࡛ࡓࡆࡡࡈ࡜ࡊࡓࡐࡕࡋࡒࡒࠥࡉ࡯ࡰ࡭࡬ࡩ࠳ࠦࡃࡐࡑࡎࡍࡊ࡙ࠠࡏࡑࡗࠤ࡜ࡕࡒࡌࡋࡑࡋ࠳࠭࠱") + Style.RESET_ALL)
				break
	def l1l1lll(self):
		chars = l11lllll (u"ࠬ࠵࠭࡝࡞ࡿࠫ࠲")
		for char in chars:
			sys.stdout.write(l11lllll (u"࠭࡜ࡳࠩ࠳") + Fore.GREEN + Style.DIM + l11lllll (u"ࠧࠡࡀࠣࡗࡨࡸࡡࡱ࡫ࡱ࡫࠳࠴࠮ࠨ࠴") + str(char))
			time.sleep(0.2)
			sys.stdout.flush()
	def l1l11lll(self):
		global l1ll
		for link in self.l11llll1:
			l11lll = link.index(l11lllll (u"ࠨࠨࠪ࠵"))
			l11l11l1 = link[0:l11lll]
			if l11lllll (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮࠱ࡸ࠳ࠬ࠶") not in l11l11l1:
				l1ll.append(link[0:l11lll])
	def l11(self, l1l111l1):
		self.l11ll1l()
		self.l11ll1l1()
		self.l11ll1ll()
		self.l11ll1l1()
		self.l11l1l1l(l1l111l1)
		self.l1l11lll()
class l111lll1:
	def __init__(self, filename):
		self.l1llll1 = l11lllll (u"ࠪࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮࠱ࡵࡥࡼ࠭࠷")
		self.s = Session()
		self.l1l1ll1 = {l11lllll (u"࡚ࠫࡹࡥࡳ࠯ࡄ࡫ࡪࡴࡴࠨ࠸"):l11lllll (u"ࠬࡓ࡯ࡻ࡫࡯ࡰࡦ࠵࠵࠯࠲ࠣࠬࡆࡴࡤࡳࡱ࡬ࡨࠥ࠿࠻ࠡࡏࡲࡦ࡮ࡲࡥ࠼ࠢࡵࡺ࠿࠼࠷࠯࠲ࠬࠤࡌ࡫ࡣ࡬ࡱ࠲࠺࠼࠴࠰ࠡࡈ࡬ࡶࡪ࡬࡯ࡹ࠱࠹࠻࠳࠶ࠧ࠹"),
		 l11lllll (u"࠭ࡁࡤࡥࡨࡴࡹ࠭࠺"):l11lllll (u"ࠧࡵࡧࡻࡸ࠴ࡾ࡭࡭࠮ࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࡯࡯࠰ࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࡬ࡹࡳ࡬ࠬࡺࡰࡰ࠱ࡺࡥࡹࡶ࠲࡬ࡹࡳ࡬࠼ࡳࡀ࠴࠳࠿ࠬࡵࡧࡻࡸ࠴ࡶ࡬ࡢ࡫ࡱ࠿ࡶࡃ࠰࠯࠺࠯࡭ࡲࡧࡧࡦ࠱ࡳࡲ࡬࠲ࠪ࠰ࠬ࠾ࡵࡂ࠶࠮࠶ࠩ࠻"),
		 l11lllll (u"ࠨࡅࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬ࠼"):l11lllll (u"ࠩ࡮ࡩࡪࡶ࠭ࡢ࡮࡬ࡺࡪ࠭࠽"),
		 l11lllll (u"ࠪࡏࡪ࡫ࡰ࠮ࡃ࡯࡭ࡻ࡫ࠧ࠾"):l11lllll (u"ࠫ࠶࠷࠵ࠨ࠿"),
		 l11lllll (u"ࠬࡇࡣࡤࡧࡳࡸ࠲ࡉࡨࡢࡴࡶࡩࡹ࠭ࡀ"):l11lllll (u"࠭ࡉࡔࡑ࠰࠼࠽࠻࠹࠮࠳࠯ࡹࡹ࡬࠭࠹࠽ࡴࡁ࠵࠴࠷࠭ࠬ࠾ࡵࡂ࠶࠮࠸ࠩࡁ"),
		 l11lllll (u"ࠧࡂࡥࡦࡩࡵࡺ࠭ࡍࡣࡱ࡫ࡺࡧࡧࡦࠩࡂ"):l11lllll (u"ࠨࡧࡱ࠱ࡺࡹࠬࡦࡰ࠾ࡵࡂ࠶࠮࠶ࠩࡃ")}
		self.s.headers.update(self.l1l1ll1)
		self.l1l1ll11 = re.compile(l11lllll (u"ࠩࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࠮ࡠ࠯ࡠ࠯ࡅࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࠯ࡠ࠯ࡡࡢ࠮࡜ࡣ࠰ࡾࡆ࠳࡚࠯࡟ࡾ࠶࠱࠿ࡽࠥࠩࡄ"), re.IGNORECASE)
		self.l1l1l = re.compile(l11lllll (u"ࠪࡢࡠ࠶࠭࠺ࡃ࠰࡞ࡦ࠳ࡺࠢࡂࠦࠨࡄࠫ࠮ࡠ࠯ࡠࡿ࠷࠲࠳࠳ࡿࠧࠫࡅ"), re.IGNORECASE)
		self.l11l = re.compile(l11lllll (u"ࠫࡣ࠮ࡨࡵࡶࡳࢀ࡭ࡺࡴࡱࡵࠬ࠾࠴࠵ࡰࡢࡵࡷࡩࡧ࡯࡮࠯ࡥࡲࡱ࠴ࡢࡷࠬࠦࠪࡆ"), re.IGNORECASE)
		self.filename = filename
		self.n = 0
	def l1l1111l(self, links):
		self.n = 0
		l1ll1l1 = []
		for link in links:
			if link != l11lllll (u"ࠬ࠭ࡇ") and link is not None: # and self.l11l.match(link):
				l1ll1l1.append(link)
		with open(self.filename, l11lllll (u"࠭ࡡࠨࡈ")) as l11l11l:
			for link in l1ll1l1:
				print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠧࠡࡀࠣࡐࡪ࡫ࡣࡩ࡫ࡱ࡫ࠥ࠭ࡉ") + link + l11lllll (u"ࠨ࠰࠱࠲ࠬࡊ"))
				l1111l = link.replace(l11lllll (u"ࠩࡳࡥࡸࡺࡥࡣ࡫ࡱ࠲ࡨࡵ࡭ࠨࡋ"), self.l1llll1, 1)
				req = Request(l11lllll (u"ࠪࡋࡊ࡚ࠧࡌ"), l1111l)
				prep = req.prepare()
				l1lll1 = self.s.send(prep, timeout=30)
				soup = BeautifulSoup(l1lll1.content, l11lllll (u"ࠫ࡭ࡺ࡭࡭࠰ࡳࡥࡷࡹࡥࡳࠩࡍ"))
				l11ll1 = l11lllll (u"ࠬ࠭ࡎ").join(soup.findAll(text=True))
				l1ll111 = l11ll1.split(l11lllll (u"࠭࡜࡯ࠩࡏ"))
				i = 0
				for line in l1ll111:
					if l11lllll (u"ࠧࡽࠩࡐ") in line:
						line = line.split(l11lllll (u"ࠨࡾࠪࡑ"))[0]
					if l11lllll (u"ࠩ࠽ࠫࡒ") in line:
						if l11lllll (u"ࠪࡄࠬࡓ") in line:
							try:
								l1lll111, l1lllll = line.split(l11lllll (u"ࠫ࠿࠭ࡔ"))
							except ValueError:
								l1111l1 = line.split(l11lllll (u"ࠬࡀࠧࡕ"))
								l1lll111 = l1111l1[0]
								l1lllll = l1111l1[1]
							l1lll111 = l1lll111.strip()
							l1lllll = l1lllll.strip()
							if self.l1l1ll11.match(l1lll111):
								if self.l1l1l.match(l1lllll):
									l1l111l = l1lll111 + l11lllll (u"࠭࠺ࠨࡖ") + l1lllll
									print(Fore.GREEN + Style.DIM + l11lllll (u"ࠧࠡ࡞ࡷࡂࠥࡉ࡯࡮ࡤࡲࠤࡋࡵࡵ࡯ࡦࠣ࠾ࠥ࠭ࡗ") + l1l111l)
									l11l11l.write(l1l111l + l11lllll (u"ࠨ࡞ࡱࠫࡘ"))
									i = i + 1
									self.n = self.n + 1
				print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠩࠣࡂࠥࡌ࡯ࡶࡰࡧࠤ࡙ࠬ") + str(i) + l11lllll (u"ࠪࠤࡈࡵ࡭ࡣࡱࡶࠤ࡮ࡴࠠࡕࡪ࡬ࡷࠥࡒࡩ࡯࡭࠱࡚ࠫ"))
				#print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠫࠥࡄࠠࡕࡱࡷࡥࡱࠦࡃࡰ࡯ࡥࡳࡸࠦ࠺࡛ࠡࠩ") + Style.BRIGHT + str(self.n))
				print(Fore.YELLOW + Style.DIM + l11lllll (u"ࠬࠦ࠾ࠡࡒࡵࡩࡸࡹࠠࡄࡖࡕࡐࠥ࠱ࠠࡄࠢࡤࡸࠥࡇ࡮ࡺࠢࡓࡳ࡮ࡴࡴࠡࡶࡲࠤࡈࡧ࡮ࡤࡧ࡯ࠤࡦࡴࡤࠡࡕࡤࡺࡪࠦࡃࡰ࡯ࡥࡳࡸ࠴ࠠ࡝ࡰࠪ࡜"))
		l1llll11 = 0
		with open(self.filename, l11lllll (u"࠭ࡲࠨ࡝")) as l11l111l:
			for line in l11l111l:
				l1llll11 = l1llll11 + 1
		print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠧ࡝ࡰࠣࡂࠥࡌ࡯ࡶࡰࡧࠤࠬ࡞") + Style.BRIGHT + str(l1llll11) + Style.NORMAL + l11lllll (u"ࠨࠢࡆࡳࡲࡨ࡯ࡴ࠰ࠪ࡟"))
		print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠩࠣࡂ࡙ࠥࡡࡷࡧࡧࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻ࠱ࠫࡠ"))
		print(Fore.CYAN + Style.BRIGHT + l11lllll (u"ࠪࠤࡃࠦࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠡࡤࡼࠤࡅ࡮ࡥࡸࡪࡲࡱࡺࡹࡴ࡯࠲ࡷࡦࡪࡴࡡ࡮ࡧࡧ࠲ࠥࡖࡥࡢࡥࡨࠥࠬࡡ"))
def l11111l():
	if os.path.isfile(l11lllll (u"ࠫ࠳࡬ࡩࡳࡵࡷࠫࡢ")):
		l11lll11 = strtobool(open(l11lllll (u"ࠬ࠴ࡦࡪࡴࡶࡸࠬࡣ"), l11lllll (u"࠭ࡲࠨࡤ")).read().strip())
	else:
		l11lll11 = True
	return l11lll11
def l1ll1ll():
	print(Fore.CYAN + l11lllll (u"ࠧࠡࡀࠣࡔࡱ࡫ࡡࡴࡧࠣࡅࡱࡲ࡯ࡸࠢࡖࡸࡴࡸࡡࡨࡧࠣࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠡࡋࡩࠤࡆࡹ࡫ࡦࡦࠣࡸࡴࠦࡤࡰࠢࡖࡳ࠳࠭ࡥ"))
	time.sleep(2)
	if not os.path.isdir(l111111 + l11lllll (u"ࠨࡵࡷࡳࡷࡧࡧࡦࠩࡦ")):
		os.system(l11lllll (u"ࠩࡷࡩࡷࡳࡵࡹ࠯ࡶࡩࡹࡻࡰ࠮ࡵࡷࡳࡷࡧࡧࡦࠩࡧ"))
	if os.path.isdir(l111111 + l11lllll (u"ࠪࡷࡹࡵࡲࡢࡩࡨࠫࡨ")):
		print(Fore.GREEN + l11lllll (u"ࠫࠥࡄࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡅࡴࡶࡤࡦࡱ࡯ࡳࡩࡧࡧࠤࡘࡺ࡯ࡳࡣࡪࡩ࠳࠭ࡩ"))
		if not os.path.isdir(l111111 + l11lllll (u"ࠬࡹࡴࡰࡴࡤ࡫ࡪ࠵ࡳࡩࡣࡵࡩࡩ࠵ࡖࡰ࡮ࡧࡩࡲࡵࡲࡵࡅࡲࡱࡲࡻ࡮ࡪࡶࡼ࠳ࡈࡵ࡭ࡣࡱࡊࡩࡳ࠭ࡪ")):
			os.makedirs(l111111 + l11lllll (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴࠧ࡫"))
		if not os.path.isdir(l111111 + l11lllll (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮࠰ࡍࡨࡽࡼࡵࡲࡥࡵࠪ࡬")):
			os.makedirs(l111111 + l11lllll (u"ࠨࡵࡷࡳࡷࡧࡧࡦ࠱ࡶ࡬ࡦࡸࡥࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯࠱ࡎࡩࡾࡽ࡯ࡳࡦࡶࠫ࡭"))
		if not os.path.isdir(l111111 + l11lllll (u"ࠩࡶࡸࡴࡸࡡࡨࡧ࠲ࡷ࡭ࡧࡲࡦࡦ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡇࡴࡳࡢࡰࡎ࡬ࡷࡹࡹࠧ࡮")):
			os.makedirs(l111111 + l11lllll (u"ࠪࡷࡹࡵࡲࡢࡩࡨ࠳ࡸ࡮ࡡࡳࡧࡧ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡈࡵ࡭ࡣࡱࡏ࡭ࡸࡺࡳࠨ࡯"))
		print(Fore.GREEN + l11lllll (u"ࠫࠥࡄࠠࡊࡰࡷࡩࡷࡴࡡ࡭ࠢࡖࡸࡴࡸࡡࡨࡧ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹࠡࡅࡵࡩࡦࡺࡥࡥࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹ࠯ࠩࡰ"))
		print(Fore.GREEN + l11lllll (u"ࠬࠦ࠾ࠡࡔࡨࡷࡹࡧࡲࡵ࡫ࡱ࡫࠳࠭ࡱ"))
		time.sleep(1.5)
		os.system(l11lllll (u"࠭ࡣ࡭ࡧࡤࡶࠬࡲ"))
		open(l11lllll (u"ࠧ࠯ࡨ࡬ࡶࡸࡺࠧࡳ"), l11lllll (u"ࠨࡹࠪࡴ")).write(l11lllll (u"ࠩࡉࡥࡱࡹࡥࠨࡵ"))
def l111l1l(l11l11):
	if l11l11 != l11lllll (u"ࠪࡥ࡛ࡧࡄࡂࠢ࡮ࡉࡉࡧࡖࡳࡃࠪࡶ"):
		l11l11 = float(l11l11)
		l1l11l1 = float(requests.get(l11lllll (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡸࡡࡸ࠰ࡪ࡭ࡹ࡮ࡵࡣࡷࡶࡩࡷࡩ࡯࡯ࡶࡨࡲࡹ࠴ࡣࡰ࡯࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡱࡦࡹࡴࡦࡴ࠲࠲ࡻ࡫ࡲࡴ࡫ࡲࡲࠬࡷ")).text.strip())
		if l1l11l1 > l11l11:
			l1lll11l = str(requests.get(l11lllll (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡲࡢࡹ࠱࡫࡮ࡺࡨࡶࡤࡸࡷࡪࡸࡣࡰࡰࡷࡩࡳࡺ࠮ࡤࡱࡰ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡲࡧࡳࡵࡧࡵ࠳࠳ࡩࡨࡢࡰࡪࡩࡱࡵࡧࠨࡸ")).text.strip())
			print(Fore.GREEN + Style.BRIGHT + l11lllll (u"࠭ࠠ࠿ࠢࡘࡴࡩࡧࡴࡦࠢࡄࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠳ࡢ࡮ࠨࡹ"))
			time.sleep(0.7)
			l1l1l1ll = input(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠧࠡࡀࠣࡇ࡭ࡧ࡮ࡨࡧ࡯ࡳ࡬ࡀࠠ࡝ࡰ࡟ࡲࠬࡺ") + Style.DIM + l1lll11l + Fore.YELLOW + Style.BRIGHT + l11lllll (u"ࠨ࡞ࡱࡠࡳࠦ࠾ࠡࡆࡲࠤ࡞ࡵࡵ࡙ࠡࡤࡲࡹࠦࡴࡰࠢࡘࡴࡩࡧࡴࡦࠢࡑࡳࡼࡅࠠ࡜ࠩࡻ") + Fore.GREEN + l11lllll (u"ࠩ࡜ࠫࡼ") + Fore.YELLOW + l11lllll (u"ࠪ࠳ࠬࡽ") + Fore.RED + l11lllll (u"ࠫࡓ࠭ࡾ") + Fore.YELLOW + l11lllll (u"ࠬࡣࠠࠨࡿ") + Style.RESET_ALL)
			if l1l1l1ll.lower() == l11lllll (u"࠭ࡹࠨࢀ"):
				print(Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠧࠡࡀࠣࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡖࡲࡧࡥࡹ࡫࠮ࠨࢁ"))
				os.system(l11lllll (u"ࠨࡩ࡬ࡸࠥࡸࡥࡴࡧࡷࠤ࠲࠳ࡨࡢࡴࡧࠫࢂ"))
				os.system(l11lllll (u"ࠩࡪ࡭ࡹࠦࡰࡶ࡮࡯ࠤࡴࡸࡩࡨ࡫ࡱࠤࡲࡧࡳࡵࡧࡵࠫࢃ"))
				time.sleep(5)
				print(Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠪࠤࡃࠦࡕࡱࡦࡤࡸࡪࠦࡃࡰ࡯ࡳࡰࡪࡺࡥ࠯ࠩࢄ"))
				print(Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠫࠥࡄࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡓࡧࡶࡸࡦࡸࡴࠡࡶ࡫ࡩࠥࡖࡲࡰࡩࡵࡥࡲࠦࡴࡰࠢࡌࡲࡨࡵࡲࡱࡱࡵࡥࡹ࡫ࠠࡵࡪࡨࠤ࡚ࡶࡤࡢࡶࡨ࠲ࠬࢅ"))
		elif l1l11l1 == l11l11:
			print(Fore.GREEN + Style.DIM + l11lllll (u"ࠧࠦ࠾࡛ࠡࡲࡹࠬࡸࡥࠡࡃ࡯ࡶࡪࡧࡤࡺࠢࡲࡲࠥࡺࡨࡦࠢࡏࡥࡹ࡫ࡳࡵ࡙ࠢࡩࡷࡹࡩࡰࡰ࠱ࠤࡈ࡮ࡥࡦࡴࡶࠥࠧࢆ"))
		elif l1l11l1 < l11l11:
			l11lll1 = os.getcwd()
			os.system(l11lllll (u"࠭ࡲ࡮ࠢ࠰ࡶ࡫ࠦࠧࢇ") + l11lll1)
			os.system(l11lllll (u"ࠧࡳ࡯ࠣ࠱ࡷ࡬ࠠ࠰ࡵࡧࡧࡦࡸࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠨ࢈"))
			print(Fore.RED + Style.BRIGHT + l11lllll (u"ࠨࠢࡁࠤࡒࡵࡤࡪࡨ࡬ࡧࡦࡺࡩࡰࡰࡶࠤࡹࡵࠠࡵࡪࡨࠤࡋ࡯࡬ࡦࡵࡼࡷࡹ࡫࡭ࠡࡊࡤࡺࡪࠦࡂࡦࡧࡱࠤࡉ࡫ࡴࡦࡥࡷࡩࡩ࠴ࠠࡂ࡮࡯ࠤࡉࡧࡴࡢࠢ࡫ࡥࡸࠦࡂࡦࡧࡱࠤࡊࡸࡡࡴࡧࡧࠤࡦࡹࠠࡢࡰࠣࡅࡳࡺࡩࠡࡒ࡬ࡶࡦࡩࡹࠡࡏࡨࡥࡸࡻࡲࡦ࠰ࠪࢉ"))
			exit()
	else:
		print(l11lllll (u"ࠩࠣࡂࠥࡊࡥࡷࡧ࡯ࡳࡵ࡫ࡲࠡࡇࡻࡩࡲࡶࡴࡪࡱࡱ࠲ࠬࢊ"))
def l111ll():
	if not os.path.isdir(l111111 + l11lllll (u"ࠪࡷࡹࡵࡲࡢࡩࡨࠫࢋ")):
		os.system(l11lllll (u"ࠫࡹ࡫ࡲ࡮ࡷࡻ࠱ࡸ࡫ࡴࡶࡲ࠰ࡷࡹࡵࡲࡢࡩࡨࠫࢌ"))
	if os.path.isdir(l111111 + l11lllll (u"ࠬࡹࡴࡰࡴࡤ࡫ࡪ࠭ࢍ")):
		if not os.path.isdir(l111111 + l11lllll (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴࠧࢎ")):
			os.makedirs(l111111 + l11lllll (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠨ࢏"))
		if not os.path.isdir(l111111 + l11lllll (u"ࠨࡵࡷࡳࡷࡧࡧࡦ࠱ࡶ࡬ࡦࡸࡥࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯࠱ࡎࡩࡾࡽ࡯ࡳࡦࡶࠫ࢐")):
			os.makedirs(l111111 + l11lllll (u"ࠩࡶࡸࡴࡸࡡࡨࡧ࠲ࡷ࡭ࡧࡲࡦࡦ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬ࢑"))
		if not os.path.isdir(l111111 + l11lllll (u"ࠪࡷࡹࡵࡲࡢࡩࡨ࠳ࡸ࡮ࡡࡳࡧࡧ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡈࡵ࡭ࡣࡱࡏ࡭ࡸࡺࡳࠨ࢒")):
			os.makedirs(l111111 + l11lllll (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡉ࡯࡮ࡤࡲࡐ࡮ࡹࡴࡴࠩ࢓"))
		if not os.path.isdir(l111111 + l11lllll (u"ࠬࡹࡴࡰࡴࡤ࡫ࡪ࠵ࡳࡩࡣࡵࡩࡩ࠵ࡖࡰ࡮ࡧࡩࡲࡵࡲࡵࡅࡲࡱࡲࡻ࡮ࡪࡶࡼ࠳ࡈࡵ࡭ࡣࡱࡊࡩࡳ࠵ࡐࡳࡱࡻࡽࡑ࡯ࡳࡵࡵࠪ࢔")):
			os.makedirs(l111111 + l11lllll (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴ࠯ࡑࡴࡲࡼࡾࡒࡩࡴࡶࡶࠫ࢕"))
def l11ll11():
	print(Fore.CYAN + " > " + Back.CYAN + Fore.BLACK + "ComboGen is no longer freely accessible.")
	print(Fore.CYAN + " > " + Back.CYAN + Fore.BLACK + "Authorization can be Purchased for 5$.")
	print(Fore.CYAN + " > " + Back.CYAN + Fore.BLACK + "To Purchase, contact @hewhomustn0tbenamed.")
	print(Fore.CYAN + " > " + Back.CYAN + Fore.BLACK + "( Telegram : https://t.me/hewhomustn0tbenamed )." + Style.RESET_ALL)
	l11l1l = b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2REMXNQTEJ4'
	print(Fore.RED + Style.BRIGHT + l11lllll (u"ࠨࠢࡁࠤࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠤࡗ࡫ࡱࡶ࡫ࡵࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡗࡧࡵ࡭࡫ࡿ࡚ࠠࡱࡸࡶࠥࡉࡲࡦࡦࡨࡲࡹ࡯ࡡ࡭ࡵ࠱ࠫࢗ"))
	uname = input(Fore.GREEN + Style.DIM + l11lllll (u"ࠩࠣࡂ࡛ࠥࡳࡦࡴࡱࡥࡲ࡫ࠠ࠻ࠢࠪ࢘") + Fore.RESET + Style.DIM)
	pwd = hashlib.sha256(getpass.getpass(Fore.GREEN + Style.DIM + l11lllll (u"ࠪࠤࡃࠦࡐࡢࡵࡶࡻࡴࡸࡤࠡ࠼࢙ࠣࠫ") + Fore.RESET + Style.DIM).encode(l11lllll (u"ࠫࡦࡹࡣࡪ࡫࢚ࠪ"))).hexdigest()
	l1ll1ll1 = requests.get(base64.b64decode(l11l1l).decode(l11lllll (u"ࠬࡧࡳࡤ࡫࡬࢛ࠫ"))).text
	for x in l1ll1ll1.split(l11lllll (u"࠭࡜࡯ࠩ࢜")):
		if uname in x:
			if pwd.strip() == x.split(l11lllll (u"ࠢ࠻ࠤ࢝"))[1].strip():
				print(Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠨࠢࡁࠤࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࠯ࠩ࢞"))
				return
	print(Fore.RED + Style.BRIGHT + l11lllll (u"ࠩࠣࡂࠥࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲ࡛ࠥ࡮ࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯࠲ࠥࡖࡲࡰࡩࡵࡥࡲࠦࡔࡦࡴࡰ࡭ࡳࡧࡴࡦࡦ࠱ࠫ࢟"))
	print(Fore.RED + Style.DIM + l11lllll (u"ࠪࠤࡃࠦࡃࡰ࡯ࡥࡳࡸࠦࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢ࠽ࠤ࠵࠭ࢠ"))
	os.system(l11lllll (u"ࠫࡰ࡯࡬࡭ࠢࠪࢡ") + str(os.getpid()))
	exit()
try:
	l11ll11()
	l11l11 = open(l11lllll (u"ࠬ࠴ࡶࡦࡴࡶ࡭ࡴࡴࠧࢢ"), l11lllll (u"࠭ࡲࠨࢣ")).read().strip()
	l111ll()
	if l11111l():
		l1ll1ll()
	print(Fore.CYAN + Style.NORMAL + l11lllll (u"ࠧ࡝ࡰ࡟ࡸࡡࡺࠠࡠࡡࡢࡣࡤࡥࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡣࠥࠦࠠࠡࠢࠣࠤࠥࡥ࡟ࡠࡡࡢࡣࡡࡴ࡜ࡵ࡞ࡷࢀࠥࠦࠠࠡࠢࠣࢀࡤࡥ࡟ࠡࡡࡢࡣࡤࡥࡼࠡࡾࡢࡣࠥࡥ࡟ࡠࡾࠣࠤࠥࡥ࡟ࡠࡾࡢࡣࡤࠦ࡟ࡠࡡ࡟ࡲࡡࡺ࡜ࡵࡾࠣࠤࠥ࠳࠭࠮ࡾࠣ࠲ࠥࢂ࡜ࡵࠢࡿࠤ࠳ࠦࠠࡽࠢ࠱ࠤࢁࠦࠠࡽࠢࠣࠤࢁࠦ࠭ࡠࡾࠣࠤࠥࢂ࡜࡯࡞ࡷࡠࡹࢂ࡟ࡠࡡࡢࡣࡤࢂ࡟ࡠࡡࡿࡣࢁࡥࡼࡠࡾࡢࡣࡤࡥࡼࡠࡡࡢࢀࡤࡥ࡟ࡠࡡࡢࢀࡤࡥ࡟ࡽࡡࡿࡣࢁࡢ࡮࡝ࡰ࡟ࡸࡡࡺ࡜ࡵ࡞ࡷࡠࡹࡢࡴ࡝ࡶࠪࢤ") + Style.DIM + l11lllll (u"ࠨ࡞ࡷࠤࡻ࠭ࢥ") + l11l11 + l11lllll (u"ࠩࠣࡦࡾࠦࡀࡩࡧࡺ࡬ࡴࡳࡵࡴࡶࡱ࠴ࡹࡨࡥ࡯ࡣࡰࡩࡩࡢ࡮࡝ࡰ࡟ࡲࠥࡄࠠࡈ࡫ࡷ࡬ࡺࡨ࠺ࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡪ࡭ࡹ࡮ࡵࡣ࠰ࡦࡳࡲ࠵ࡖࡰ࡮ࡧࡩࡲࡵࡲࡵࡅࡲࡱࡲࡻ࡮ࡪࡶࡼ࠳ࡈࡵ࡭ࡣࡱࡊࡩࡳࡢ࡮࡝ࡶࠪࢦ"))
	time.sleep(2)
	print(Fore.GREEN + Style.DIM + l11lllll (u"ࠪࠤࡃࠦࡶࠨࢧ") + l11l11 + l11lllll (u"ࠫࠥࡊࡥࡷࡧ࡯ࡳࡵ࡫ࡤࠡࡤࡼࠤࠬࢨ") + Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠬࡆࡨࡦࡹ࡫ࡳࡲࡻࡳࡵࡰ࠳ࡸࡧ࡫࡮ࡢ࡯ࡨࡨࠬࢩ") + Style.RESET_ALL + Fore.GREEN + Style.DIM + l11lllll (u"࠭ࠠࠩࡖࡨࡰࡪ࡭ࡲࡢ࡯ࠬ࠲ࠬࢪ"))
	time.sleep(1)
	print(Fore.GREEN + Style.DIM + l11lllll (u"ࠧࠡࡀࠣࡊࡴࡸࠠࡖࡲࡧࡥࡹ࡫ࡳࠡࠨࠣࡑࡴࡸࡥ࠭ࠢࡆ࡬ࡪࡩ࡫ࠡࡱࡸࡸࠬࢫ") + Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠨࠢࡃ࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡔࡥࡸࡵ࡯ࡩࡹࡺࡥࡳࠩࢬ") + Style.RESET_ALL + Fore.GREEN + Style.DIM + l11lllll (u"࡙ࠩࠣࠬ࡫࡬ࡦࡩࡵࡥࡲ࠯࠮ࠨࢭ"))
	time.sleep(2)
	l111l1l(l11l11)
	l111l = input(Fore.GREEN + Style.DIM + l11lllll (u"ࠪࠤࡃࠦࡐࡳࡧࡶࡷࠥࡋ࡮ࡵࡧࡵࠤࡹࡵࠠࡄࡱࡱࡸ࡮ࡴࡵࡦ࠰ࠪࢮ") + Style.RESET_ALL)
	print(Fore.GREEN + Style.DIM + l11lllll (u"ࠫࡡࡴࠠ࠿ࠢࡏࡳࡦࡪࡩ࡯ࡩࠣࡏࡪࡿࡷࡰࡴࡧࡷ࠳ࡢ࡮ࠡࡀࠣࡔࡱ࡫ࡡࡴࡧࠣࡑࡴࡼࡥࠡࡶ࡫ࡩࠥࡑࡥࡺࡹࡲࡶࡩࡹࠠࡇ࡫࡯ࡩࠥࡺ࡯ࠨࢯ") + Style.BRIGHT + l11lllll (u"ࠬࠦࡉ࡯ࡶࡨࡶࡳࡧ࡬ࠡࡕࡷࡳࡷࡧࡧࡦ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯࠱ࡎࡩࡾࡽ࡯ࡳࡦࡶࠫࢰ"))
	time.sleep(4)
	l1l1ll1l = l11lllll (u"࠭ࠧࢱ")
	l11l1ll1 = []
	while 1:
		try:
			l1lllll1 = SelectMenu()
			l1l = os.listdir(l11111 + l11lllll (u"ࠧࡌࡧࡼࡻࡴࡸࡤࡴࠩࢲ"))
			l11l1111 = {}
			l11ll111 = []
			for file in l1l:
				if os.path.isfile(l11111 + l11lllll (u"ࠨࡍࡨࡽࡼࡵࡲࡥࡵ࠲ࠫࢳ") + file):
					l1llll = {l11lllll (u"ࠩࡱࡥࡲ࡫ࠧࢴ"):file,
					 l11lllll (u"ࠪࡴࡦࡺࡨࠨࢵ"):l11111 + l11lllll (u"ࠫࡐ࡫ࡹࡸࡱࡵࡨࡸ࠵ࠧࢶ") + file}
					l11l1111[file] = l1llll
					l11ll111.append(l1llll[l11lllll (u"ࠬࡴࡡ࡮ࡧࠪࢷ")])
			l11ll111.append(l11lllll (u"࠭ࡒࡦࡨࡵࡩࡸ࡮ࠠࡇ࡫࡯ࡩࠥࡒࡩࡴࡶࠪࢸ"))
			l11ll111.append(l11lllll (u"ࠧࡆࡰࡷࡩࡷࠦࡋࡦࡻࡺࡳࡷࡪࡳࠡࡏࡤࡲࡺࡧ࡬࡭ࡻࠪࢹ"))
			l1lllll1.add_choices(l11ll111)
			l1l1ll1l = l1lllll1.select(l11lllll (u"ࠨࠢࡁࠤࡕࡲࡥࡢࡵࡨࠤࡘ࡫࡬ࡦࡥࡷࠤࡹ࡮ࡥࠡࡆࡨࡷ࡮ࡸࡥࡥࠢࡉ࡭ࡱ࡫࠮ࠨࢺ"))
			if l1l1ll1l == l11lllll (u"ࠩࡕࡩ࡫ࡸࡥࡴࡪࠣࡊ࡮ࡲࡥࠡࡎ࡬ࡷࡹ࠭ࢻ"):
				raise l11lll1l
			else:
				if l1l1ll1l == l11lllll (u"ࠪࡉࡳࡺࡥࡳࠢࡎࡩࡾࡽ࡯ࡳࡦࡶࠤࡒࡧ࡮ࡶࡣ࡯ࡰࡾ࠭ࢼ"):
					raise l111llll
				print(Fore.GREEN + Style.DIM + l11lllll (u"ࠫࠥࡄࠠࡍࡱࡤࡨ࡮ࡴࡧࠡࡍࡨࡽࡼࡵࡲࡥࡵࠣࡪࡷࡵ࡭ࠡࡈ࡬ࡰࡪࠦ࠺ࠡࠩࢽ") + Style.NORMAL + l1l1ll1l)
				time.sleep(1)
				try:
					with open(l11l1111[l1l1ll1l][l11lllll (u"ࠬࡶࡡࡵࡪࠪࢾ")], l11lllll (u"࠭ࡲࠨࢿ")) as key_file:
						l1l11ll = key_file.readlines()
						for x in l1l11ll:
							l11l1ll1.append(x.strip())
						if l11l1ll1 == []:
							raise l1l1l11
				except l1l1l11:
					print(Fore.RED + Style.NORMAL + l11lllll (u"ࠧࠡࡀࠣࡊ࡮ࡲࡥࠡ࡫ࡶࠤࡊࡳࡰࡵࡻ࠱ࠤࠬࣀ") + Style.RESET_ALL)
					continue
			break
		except l11lll1l:
			print(Fore.GREEN + Style.DIM + l11lllll (u"ࠨࠢࡁࠤࡗ࡫ࡦࡳࡧࡶ࡬࡮ࡴࡧࠡࡈ࡬ࡰࡪࠦࡌࡪࡵࡷ࠲ࠬࣁ"))
			time.sleep(1)
			continue
		except l111llll:
			try:
				l1 = input(Fore.GREEN + Style.DIM + l11lllll (u"ࠩࠣࡂࠥࡋ࡮ࡵࡧࡵࠤࡐ࡫ࡹࡸࡱࡵࡨࡸࠦࡓࡦࡲࡨࡶࡦࡺࡥࡥࠢࡥࡽࠥࡉ࡯࡮࡯ࡤࡷࠥ࠮ࠬࠪࠢ࠽ࠤࠬࣂ") + Fore.RESET + Style.DIM)
				l1 = l1.strip()
				l1 = l1.strip(l11lllll (u"ࠪ࠰ࠬࣃ"))
				if l1 == l11lllll (u"ࠫࠬࣄ") or l1 == None:
					raise l1l1l11
				else:
					l1l11ll = l1.split(l11lllll (u"ࠬ࠲ࠧࣅ"))
					print(Style.RESET_ALL)
					for x in l1l11ll:
						l11l1ll1.append(x.strip())
				break
			except l1l1l11:
				print(Fore.RED + Style.NORMAL + l11lllll (u"࠭ࠠ࠿ࠢࡌࡲࡻࡧ࡬ࡪࡦࠣࡍࡳࡶࡵࡵ࠰ࠣࠫࣆ") + Style.RESET_ALL)
				continue
	#l1l1111 = l1ll1111()
	l1l11l = 0
	l1ll1lll = [l11lllll (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠢࣇ")]
	l1ll11 = {}
	l111 = {l11lllll (u"ࠨࡉࡲࡳ࡬ࡲࡥࠨࣈ"):[
	  l11lllll (u"ࠩࡄࡲࡾࠦࡔࡪ࡯ࡨࠫࣉ"), l11lllll (u"ࠪࡔࡦࡹࡴࠡࡊࡲࡹࡷ࠭࣊"), l11lllll (u"ࠫࡕࡧࡳࡵࠢ࠵࠸ࠥࡎ࡯ࡶࡴࡶࠫ࣋"), l11lllll (u"ࠬࡖࡡࡴࡶ࡛ࠣࡪ࡫࡫ࠨ࣌"), l11lllll (u"࠭ࡐࡢࡵࡷࠤࡒࡵ࡮ࡵࡪࠪ࣍"), l11lllll (u"ࠧࡑࡣࡶࡸࠥ࡟ࡥࡢࡴࠪ࣎")],
	 l11lllll (u"ࠨࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳ࣏ࠬ"):[l11lllll (u"ࠩࡄࡲࡾࠦࡔࡪ࡯ࡨ࣐ࠫ")]}
	for l1ll11l in l1ll1lll:
		l11ll11l = SelectMenu()
		l11ll11l.add_choices(l111[l1ll11l])
		l11l111 = l11ll11l.select(l11lllll (u"ࠪࠤࡃ࡛ࠦࠨ࣑") + l1ll11l + l11lllll (u"ࠫࡢࠦࡆࡪࡰࡧࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠥࡵࡦࠡ࠼࣒ࠣࠫ"))
		if l11l111 == l11lllll (u"ࠬࡇ࡮ࡺࠢࡗ࡭ࡲ࡫࣓ࠧ"):
			l1ll11[l1ll11l] = l11lllll (u"࠭ࡺࠨࣔ")
		elif l11l111 == l11lllll (u"ࠧࡑࡣࡶࡸࠥࡎ࡯ࡶࡴࠪࣕ"):
			l1ll11[l1ll11l] = l11lllll (u"ࠨࡪࠪࣖ")
		elif l11l111 == l11lllll (u"ࠩࡓࡥࡸࡺࠠ࠳࠶ࠣࡌࡴࡻࡲࡴࠩࣗ"):
			l1ll11[l1ll11l] = l11lllll (u"ࠪࡨࠬࣘ")
		elif l11l111 == l11lllll (u"ࠫࡕࡧࡳࡵ࡚ࠢࡩࡪࡱࠧࣙ"):
			l1ll11[l1ll11l] = l11lllll (u"ࠬࡽࠧࣚ")
		elif l11l111 == l11lllll (u"࠭ࡐࡢࡵࡷࠤࡒࡵ࡮ࡵࡪࠪࣛ"):
			l1ll11[l1ll11l] = l11lllll (u"ࠧ࡮ࠩࣜ")
		elif l11l111 == l11lllll (u"ࠨࡒࡤࡷࡹ࡙ࠦࡦࡣࡵࠫࣝ"):
			l1ll11[l1ll11l] = l11lllll (u"ࠩࡼࠫࣞ")
		else:
			l1ll11[l1ll11l] = l11lllll (u"ࠪࡾࠬࣟ")
		print(Fore.GREEN + Style.DIM + l11lllll (u"ࠫࠥࡄࠠࡇ࡫ࡱࡨ࡮ࡴࡧࠡࡔࡨࡷࡺࡲࡴࡴࠢࡲࡪࠥ࠭࣠") + Style.NORMAL + l11l111 + Style.DIM + l11lllll (u"ࠬࠦࡦࡰࡴࠣࠫ࣡") + Fore.GREEN + Style.NORMAL + l1ll11l + Fore.GREEN + Style.DIM + l11lllll (u"࠭࠮ࠨ࣢"))
	while True:
		try:
			l1l1l1l = input(Fore.GREEN + Style.DIM + l11lllll (u"ࠧࠡࡀࠣࡉࡳࡺࡥࡳࠢࡉ࡭ࡱ࡫ࠠࡏࡣࡰࡩࠥࡺ࡯ࠡࡕࡷࡳࡷ࡫ࠠࡄࡱࡰࡦࡴࠦࡌࡪࡵࡷࠤ࠿ࣣࠦࠧ") + Style.RESET_ALL + Style.DIM)
			if l1l1l1l == l11lllll (u"ࠨࠩࣤ") or l1l1l1l == None:
				raise l1l1l11
			else:
				if l11lllll (u"ࠩ࠱ࡸࡽࡺࠧࣥ") not in l1l1l1l:
					l1l1l1l = l1l1l1l.strip() + l11lllll (u"ࠪ࠲ࡹࡾࡴࠨࣦ")
				l1111ll = l11111 + l11lllll (u"ࠫࡈࡵ࡭ࡣࡱࡏ࡭ࡸࡺࡳ࠰ࠩࣧ") + l1l1l1l
				if os.path.isfile(l1111ll):
					raise l1l1l11l
			break
		except l1l1l11l:
			l1111 = input(Fore.RED + Style.DIM + l11lllll (u"ࠬࠦ࠾ࠡࡈ࡬ࡰࡪࠦࡁ࡭ࡴࡨࡥࡩࡿࠠࡆࡺ࡬ࡷࡹࡹ࠮ࠡࡑࡹࡩࡷࡽࡲࡪࡶࡨࡃࠥࡡࠠࠨࣨ") + Fore.GREEN + Style.DIM + l11lllll (u"࠭ࡹࡦࡵࣩࠪ") + Fore.RED + Style.DIM + l11lllll (u"ࠧ࠰ࡰࡲࠤࡢࠦ࠺ࠡࠩ࣪") + Style.RESET_ALL + Style.DIM)
			if l1111.lower() == l11lllll (u"ࠨࡻࡨࡷࠬ࣫"):
				print(Fore.RED + Style.DIM + l11lllll (u"ࠩࠣࡂࠥࡕࡶࡦࡴࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡊ࡮ࡲࡥ࠯ࠩ࣬"))
				os.system(l11lllll (u"ࠪࡶࡲ࣭ࠦࠧ") + l1111ll)
				break
			else:
				continue
		except l1l1l11:
			print(Fore.RED + Style.NORMAL + l11lllll (u"ࠫࠥࡄࠠࡊࡰࡹࡥࡱ࡯ࡤࠡࡋࡱࡴࡺࡺ࠮࣮ࠡࠩ") + Style.RESET_ALL)
			continue
	for l111lll in l11l1ll1:
		try:
			for l1ll11l in l1ll1lll:
				if l1ll11l == l11lllll (u"ࠬࡍ࡯ࡰࡩ࡯ࡩ࣯ࠬ"):
					print(Fore.GREEN + Style.DIM + l11lllll (u"࠭ࠠ࠿ࠢ࡞ࡋࡴࡵࡧ࡭ࡧࡠࠤࡘࡩࡲࡢࡲ࡬ࡲ࡬ࠦࡋࡦࡻࡺࡳࡷࡪࠠ࠻ࣰࠢࠪ") + Style.BRIGHT + str(l111lll) + Style.RESET_ALL)
					time.sleep(1)
					l1l11l1l = l1llllll(l11lllll (u"ࠧࡴ࡫ࡷࡩ࠿ࡶࡡࡴࡶࡨࡦ࡮ࡴ࠮ࡤࡱࡰࠤ࡮ࡴࡴࡦࡺࡷ࠾ࣱࠬ") + l111lll)
					l1l1 = threading.Thread(name=l11lllll (u"ࠨࡵࡦࡶࡦࡶࡩ࡯ࡩࡢࡸ࡭ࡸࡥࡢࡦࣲࠪ"), target=(l1l11l1l.l11), args=(l1ll11[l1ll11l]))
					l1l1.start()
					while l1l1.is_alive():
						if not l1l11l1l.l1ll1l11:
							l1l11l1l.l1l1lll()
					print(Fore.GREEN + Style.DIM + l11lllll (u"ࠩ࡟ࡲࠥࡄࠠ࡜ࡉࡲࡳ࡬ࡲࡥ࡞ࠢࡖࡩࡦࡸࡣࡩࠢࡆࡳࡲࡶ࡬ࡦࡶࡨࡨ࠳ࠦࡔࡰࡶࡤࡰ࡛ࠥࡒࡍࡵࠣࡊࡴࡻ࡮ࡥࠢ࠽ࠤࠬࣳ") + Style.NORMAL + str(len(l1ll)))
					print(Fore.GREEN + Style.DIM + l11lllll (u"ࠪࡠࡳࠦ࠾ࠡ࡝ࡇࡹࡨࡱࡄࡶࡥ࡮ࡋࡴࡣࠠࡔࡧࡤࡶࡨ࡮ࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠱ࠤ࡙ࡵࡴࡢ࡮࡙ࠣࡗࡒࡳࠡࡈࡲࡹࡳࡪࠠ࠻ࠢࠪࣴ") + Style.NORMAL + str(len(l1ll)))
		except KeyboardInterrupt:
			print(Fore.GREEN + Style.DIM + l11lllll (u"ࠫࠥࡢ࡮ࠡࡀࠣࡗࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡘࡥࡴࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࡏࡪࡿࡷࡰࡴࡧࡷ࠳࠭ࣵ"))
			break
	print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠬࠦ࠾ࠡࡕࡦࡶࡦࡶࡩ࡯ࡩࠣࡇࡴࡳࡰ࡭ࡧࡷࡩ࠳ࣶࠦࠧ") + Fore.CYAN + Style.BRIGHT + str(len(l1ll)) + Fore.GREEN + Style.NORMAL + l11lllll (u"࠭ࠠࡖࡔࡏࡷࠥࡌ࡯ࡶࡰࡧ࠲ࠬࣷ"))
	l1ll = list(dict.fromkeys(l1ll))
	print(Fore.GREEN + Style.NORMAL + l11lllll (u"ࠧࠡࡀࠣࡇࡱ࡫ࡡ࡯࡫ࡱ࡫࡛ࠥࡒࡍࡵࠣࠪࠥࡘࡥ࡮ࡱࡹ࡭ࡳ࡭ࠠࡅࡷࡳࡰ࡮ࡩࡡࡵࡧࡶ࠲ࠥ࠭ࣸ") + Fore.CYAN + Style.BRIGHT + str(len(l1ll)) + Fore.GREEN + Style.NORMAL + l11lllll (u"ࠨࠢࡘࡖࡑࡹࠠࡓࡧࡰࡥ࡮ࡴ࠮ࠨࣹ"))
	l111ll1 = input(Fore.GREEN + Style.BRIGHT + l11lllll (u"ࠩࠣࡂࠥࡖࡲࡦࡵࡶࠤࡊࡴࡴࡦࡴࠣࡸࡴࠦࡂࡦࡩ࡬ࡲࠥࡒࡥࡦࡥ࡫࡭ࡳ࡭࠮ࠨࣺ") + Style.RESET_ALL)
	l11l1lll = l111lll1(l1111ll)
	l11l1lll.l1l1111l(l1ll)
except KeyboardInterrupt:
	try:
		l1llll11 = 0
		with open(l11l1lll.filename, l11lllll (u"ࠪࡶࠬࣻ")) as l11l111l:
			for line in l11l111l:
				l1llll11 = l1llll11 + 1
		print(Fore.RED + Style.NORMAL + l11lllll (u"ࠫࡡࡴࠠ࠿ࠢࡄࡦࡴࡸࡴࡪࡰࡪࠤࡕࡸ࡯ࡨࡴࡤࡱ࠳࠭ࣼ"))
		print(Fore.RED + Style.DIM + l11lllll (u"ࠬࠦ࠾ࠡࡅࡲࡱࡧࡵࡳࠡࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤ࠿ࠦࠧࣽ") + str(l1llll11))
		os.system(l11lllll (u"࠭࡫ࡪ࡮࡯ࠤࠬࣾ") + str(os.getpid()))
	except:
		print(Fore.RED + Style.DIM + l11lllll (u"ࠧࠡࡀࠣࡇࡴࡳࡢࡰࡵࠣࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦ࠺ࠡ࠲ࠪࣿ"))
		os.system(l11lllll (u"ࠨ࡭࡬ࡰࡱࠦࠧऀ") + str(os.getpid()))
		exit()
