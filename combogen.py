# coding: UTF-8
import sys
l1111l1 = sys.version_info [0] == 2
l11111 = 2048
l1lll1ll = 7
def l1 (l111):
    global l1llll
    l1llll1 = ord (l111 [-1])
    l1l1ll = l111 [:-1]
    l11l11l = l1llll1 % len (l1l1ll)
    l1l1l1 = l1l1ll [:l11l11l] + l1l1ll [l11l11l:]
    if l1111l1:
        l1l1ll1l = unicode () .join ([unichr (ord (char) - l11111 - (l1l11ll1 + l1llll1) % l1lll1ll) for l1l11ll1, char in enumerate (l1l1l1)])
    else:
        l1l1ll1l = str () .join ([chr (ord (char) - l11111 - (l1l11ll1 + l1llll1) % l1lll1ll) for l1l11ll1, char in enumerate (l1l1l1)])
    return eval (l1l1ll1l)
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
		print(l1 (u"ࠫࠥࡄࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡘࡣ࡬ࡸࠥ࡝ࡨࡪ࡮ࡨࠤࡹ࡮ࡥࠡࡒࡵࡳ࡬ࡸࡡ࡮ࠢࡌࡲࡸࡺࡡ࡭࡮ࡶࠤࡹ࡮ࡥࠡࡆࡨࡴࡪࡴࡤࡦࡰࡦ࡭ࡪࡹ࠮ࠡࡖࡋࡍࡘࠦࡍࡊࡉࡋࡘ࡚ࠥࡁࡌࡇࠣࡅࠥࡒࡏࡏࡉࠣࡘࡎࡓࡅ࠯ࠩࠀ"))
		os.system(l1 (u"ࠬࡧࡰࡵࠢࡸࡴࡩࡧࡴࡦࠢࠩࠪࠥࡧࡰࡵࠢࡸࡴ࡬ࡸࡡࡥࡧࠣࠪࠫࠦࡡࡱࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡷࡵ࡯ࡵ࠯ࡵࡩࡵࡵࠠࡶࡰࡶࡸࡦࡨ࡬ࡦ࠯ࡵࡩࡵࡵࠠ࠮ࡻࠪࠁ"))
		os.system(l1 (u"࠭ࡡࡱࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡨࡲࡡ࡯ࡩࠣࡴࡾࡺࡨࡰࡰࠣࡰ࡮ࡨࡸࡴ࡮ࡷࠤࡱ࡯ࡢࡪࡥࡲࡲࡻࠦ࡬ࡪࡤ࡬ࡧࡴࡴࡶࠡ࠯ࡼࠫࠂ"))
		os.system(l1 (u"ࠧࡱ࡫ࡳࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡲࡸ࡮࡮ࠪࠃ"))
		os.system(l1 (u"ࠨࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦ࠭ࡳࠢࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳࠨࠄ"))
		os.system(l1 (u"ࠩࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡴࡧ࡯ࡩࡨࡺ࡭ࡦࡰࡸࠤࠬࠅ"))
		print(l1 (u"ࠪࡠࡳࡢ࡮ࠡࡀࠣࡈࡪࡶࡥ࡯ࡦࡨࡲࡨ࡯ࡥࡴࠢࡌࡲࡸࡺࡡ࡭࡮ࡨࡨ࠳ࠦࡒࡦࡵࡷࡥࡷࡺࡩ࡯ࡩ࠱࠲࠳࠭ࠆ"))
		os.system(l1 (u"ࠫࡨࡲࡥࡢࡴࠪࠇ"))
		continue
colorama.init(autoreset=True)
l = Lock()
l11l1 = []
l11111l = l1 (u"ࠬ࠵ࡤࡢࡶࡤ࠳ࡩࡧࡴࡢ࠱ࡦࡳࡲ࠴ࡴࡦࡴࡰࡹࡽ࠵ࡦࡪ࡮ࡨࡷ࠴࡮࡯࡮ࡧ࠲ࠫࠈ")
l1ll11l1 = l1 (u"࠭࠯ࡥࡣࡷࡥ࠴ࡪࡡࡵࡣ࠲ࡧࡴࡳ࠮ࡵࡧࡵࡱࡺࡾ࠯ࡧ࡫࡯ࡩࡸ࠵ࡨࡰ࡯ࡨ࠳ࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴࠭ࠉ")
class l111ll(Exception):
	pass
class l1ll11l(Exception):
	pass
class l11ll(Exception):
	pass
class l1llllll(Exception):
	pass
class l11l1l1(Exception):
	pass
class l1lll11(Exception):
	pass
class l11lllll:
	def __init__(self, l11lll1):
		self.l1l11111 = l11lll1
		self.l1l1l = {l1 (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫࠊ"):l1 (u"ࠨࡏࡲࡾ࡮ࡲ࡬ࡢ࠱࠸࠲࠵ࠦࠨࡂࡰࡧࡶࡴ࡯ࡤࠡ࠻࠾ࠤࡒࡵࡢࡪ࡮ࡨ࠿ࠥࡸࡶ࠻࠸࠺࠲࠵࠯ࠠࡈࡧࡦ࡯ࡴ࠵࠶࠸࠰࠳ࠤࡋ࡯ࡲࡦࡨࡲࡼ࠴࠼࠷࠯࠲ࠪࠋ"),
		 l1 (u"ࠩࡄࡧࡨ࡫ࡰࡵࠩࠌ"):l1 (u"ࠪࡸࡪࡾࡴ࠰ࡺࡰࡰ࠱ࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼࡲࡲࠬࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾࡨࡵ࡯࡯࠯ࡽࡳ࡬࠭ࡶࡨࡼࡹ࠵ࡨࡵ࡯࡯࠿ࡶࡃ࠰࠯࠻࠯ࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴ࠻ࡲ࠿࠳࠲࠽࠲ࡩ࡮ࡣࡪࡩ࠴ࡶ࡮ࡨ࠮࠭࠳࠯ࡁࡱ࠾࠲࠱࠹ࠬࠍ"),
		 l1 (u"ࠫࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨࠎ"):l1 (u"ࠬࡱࡥࡦࡲ࠰ࡥࡱ࡯ࡶࡦࠩࠏ"),
		 l1 (u"࠭ࡋࡦࡧࡳ࠱ࡆࡲࡩࡷࡧࠪࠐ"):l1 (u"ࠧ࠲࠳࠸ࠫࠑ"),
		 l1 (u"ࠨࡃࡦࡧࡪࡶࡴ࠮ࡅ࡫ࡥࡷࡹࡥࡵࠩࠒ"):l1 (u"ࠩࡌࡗࡔ࠳࠸࠹࠷࠼࠱࠶࠲ࡵࡵࡨ࠰࠼ࡀࡷ࠽࠱࠰࠺࠰࠯ࡁࡱ࠾࠲࠱࠻ࠬࠓ"),
		 l1 (u"ࠪࡅࡨࡩࡥࡱࡶ࠰ࡐࡦࡴࡧࡶࡣࡪࡩࠬࠔ"):l1 (u"ࠫࡪࡴ࠭ࡶࡵ࠯ࡩࡳࡁࡱ࠾࠲࠱࠹ࠬࠕ")}
		self.l1l1l1l = []
		self.l1lll1 = 4
		self.l1ll1l = 6
		self.cookie = l1 (u"ࠬ࠭ࠖ")
		self.l1l1l = l1 (u"࠭ࠧࠗ")
		self.ei = l1 (u"ࠧࠨ࠘")
		self.s = Session()
		self.s.headers.update(self.l1l1l)
		self.l1l1l1l1 = None
		self.l1ll = False
		self.l1ll1ll = False
	def l1l1111(self, l1ll11ll):
		l1111l = requests.cookies.create_cookie(name=l1 (u"ࠨࡉࡒࡓࡌࡒࡅࡠࡃࡅ࡙ࡘࡋ࡟ࡆ࡚ࡈࡑࡕ࡚ࡉࡐࡐࠪ࠙"), value=l1ll11ll)
		self.s.cookies.set_cookie(l1111l)
		self.l1ll = False
		self.l1ll1ll = False
	def l11l11ll(self, url):
		req = Request(l1 (u"ࠩࡊࡉ࡙࠭ࠚ"), url)
		prep = req.prepare()
		l1lll1l = self.s.send(prep, timeout=30)
		return l1lll1l
	def ll(self):
		time.sleep(random.choice([self.l1lll1, self.l1ll1l]))
	def l1ll1lll(self):
		l1lllll1 = self.l11l11ll(l1 (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰࠫࠛ"))
		self.ll()
		self.l11l11ll(l1 (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯ࡩࡲࡳ࡬ࡲࡥ࠯ࡥࡲࡱ࠴ࡴࡣࡳࠩࠜ"))
	def l111l11(self):
		l1lllll1 = self.l11l11ll(l1 (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡪࡳࡴ࡭࡬ࡦ࠰ࡦࡳࡲ࠵ࡰࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࡃ࡭ࡲ࠽ࡦࡰࠪࠝ"))
		soup = BeautifulSoup(l1lllll1.content, l1 (u"࠭ࡨࡵ࡯࡯࠲ࡵࡧࡲࡴࡧࡵࠫࠞ"))
		l1l1111l = soup.find(l1 (u"ࠧࡪࡰࡳࡹࡹ࠭ࠟ"), {l1 (u"ࠨࡰࡤࡱࡪ࠭ࠠ"): l1 (u"ࠩࡶ࡭࡬࠭ࠡ")})
		self.ll()
		self.l11l11ll(l1 (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰ࠳ࡸ࡫ࡴࡱࡴࡨࡪࡸࡅࡳࡪࡩࡀࠫࠢ") + quote(l1l1111l[l1 (u"ࠫࡻࡧ࡬ࡶࡧࠪࠣ")]) + l1 (u"ࠬࠬࡨ࡭࠿ࡨࡲࠫࡲࡲ࠾࡮ࡤࡲ࡬ࡥࡥ࡯ࠨࡶࡥ࡫࡫ࡵࡪ࠿࡬ࡱࡦ࡭ࡥࡴࠨࡶࡹ࡬࡭࡯࡯࠿࠵ࠪࡳ࡫ࡷࡸ࡫ࡱࡨࡴࡽ࠽࠱ࠨࡱࡹࡲࡃ࠱࠱࠲ࠩࡵࡂࠬࡰࡳࡧࡹࡁ࡭ࡺࡴࡱࠧ࠶ࡅࠪ࠸ࡆࠦ࠴ࡉࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰࠩ࠷ࡌࠦࡴࡷࡥࡱ࡮ࡺ࠲࠾ࡕࡤࡺࡪ࠱ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶ࠯ࠬࠤ"))
	def l11l1ll(self, l1l1lll=None):
		while 1:
			try:
				l11 = l1 (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡷࡸࡹ࠱࡫ࡴࡵࡧ࡭ࡧ࠱ࡧࡴࡳ࠯ࡴࡧࡤࡶࡨ࡮࠿ࡲ࠿ࠪࠥ") + str(quote(self.l1l11111)) + l1 (u"ࠧࠧࡶࡥࡷࡂࡷࡤࡳ࠼ࠪࠦ") + l1l1lll + l1 (u"ࠨࠨࡱࡹࡲࡃ࠱࠱࠲ࠩ࡬ࡱࡃࡥ࡯ࠨࡥ࡭ࡼࡃ࠱࠳࠺࠳ࠪࡧ࡯ࡨ࠾࠸࠴࠶ࠫࡶࡲ࡮ࡦࡀ࡭ࡻࡴࡳࠧࡧ࡬ࡁࠬࠧ") + str(quote(self.ei)) + l1 (u"ࠩࠩࡷࡦࡃࡎࠨࠨ")
				l1lllll1 = self.l11l11ll(l11)
				soup = BeautifulSoup(l1lllll1.text, l1 (u"ࠪ࡬ࡹࡳ࡬࠯ࡲࡤࡶࡸ࡫ࡲࠨࠩ"))
				l1ll1l1 = soup.findAll(l1 (u"ࠫ࡫ࡵࡲ࡮ࠩࠪ"))
				if not l1ll1l1 is not None:
					if l1ll1l1 != []:
						if l1ll1l1[0][l1 (u"ࠬ࡯ࡤࠨࠫ")] == l1 (u"࠭ࡣࡢࡲࡷࡧ࡭ࡧ࠭ࡧࡱࡵࡱࠬࠬ"):
							raise l111ll
				links = soup.findAll(l1 (u"ࠧࡢࠩ࠭"))
				for link in links:
					l1ll111 = link[l1 (u"ࠨࡪࡵࡩ࡫࠭࠮")]
					if l1 (u"ࠩ࠲ࡹࡷࡲ࠿ࡲ࠿࡫ࡸࡹࡶࡳ࠻࠱࠲ࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮ࠩ࠯") in l1ll111:
						self.l1l1l1l.append(l1ll111[7:])
				break
			except l111ll:
				print(Fore.RED + Style.DIM + l1 (u"ࠪࡠࡳࠦ࠾࡛ࠡࡲࡹࠥ࡮ࡡࡷࡧࠣࡆࡪ࡫࡮ࠡࡄ࡯ࡥࡨࡱ࡬ࡪࡵࡷࡩࡩࠦࡦࡳࡱࡰࠤࡌࡵ࡯ࡨ࡮ࡨ࠲ࠥࡕࡰࡦࡰࠣࠫ࠰") + Style.BRIGHT + l11 + Style.DIM + l1 (u"ࠫࠥ࡯࡮ࠡࡈ࡬ࡶࡪ࡬࡯ࡹࠢࡤࡲࡩࠦࡅ࡯ࡶࡨࡶࠥࡺࡨࡦࠢࡆࡳࡳࡺࡥ࡯ࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࡋࡔࡕࡇࡍࡇࡢࡅࡇ࡛ࡓࡆࡡࡈ࡜ࡊࡓࡐࡕࡋࡒࡒࠥࡉ࡯ࡰ࡭࡬ࡩ࠳ࠦࡃࡐࡑࡎࡍࡊ࡙ࠠࡏࡑࡗࠤ࡜ࡕࡒࡌࡋࡑࡋ࠳࠭࠱") + Style.RESET_ALL)
				break
	def l1l1(self):
		chars = l1 (u"ࠬ࠵࠭࡝࡞ࡿࠫ࠲")
		for char in chars:
			sys.stdout.write(l1 (u"࠭࡜ࡳࠩ࠳") + Fore.GREEN + Style.DIM + l1 (u"ࠧࠡࡀࠣࡗࡨࡸࡡࡱ࡫ࡱ࡫࠳࠴࠮ࠨ࠴") + str(char))
			time.sleep(0.2)
			sys.stdout.flush()
	def l1l1l1ll(self):
		global l11l1
		for link in self.l1l1l1l:
			l11llll1 = link.index(l1 (u"ࠨࠨࠪ࠵"))
			l111111 = link[0:l11llll1]
			if l1 (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮࠱ࡸ࠳ࠬ࠶") not in l111111:
				l11l1.append(link[0:l11llll1])
	def l1l11l(self, l1l1lll):
		self.l1ll1lll()
		self.ll()
		self.l111l11()
		self.ll()
		self.l11l1ll(l1l1lll)
		self.l1l1l1ll()
l1 (u"ࠥࠦࠧࠐࡣ࡭ࡣࡶࡷࠥࡊࡵࡤ࡭ࡇࡹࡨࡱࡇࡰࡕࡦࡶࡦࡶࡥࡳ࠼ࠍࠎࠎࡪࡥࡧࠢࡢࡣ࡮ࡴࡩࡵࡡࡢࠬࡸ࡫࡬ࡧࠫ࠽ࠎࠎࠏࡳࡦ࡮ࡩ࠲ࡺࡸ࡬ࠡ࠿ࠣࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡪࡵࡤ࡭ࡧࡹࡨࡱࡧࡰ࠰ࡦࡳࡲ࠵ࡨࡵ࡯࡯࠳ࠬࠐࠉࠊࡵࡨࡰ࡫࠴ࡰࡢࡴࡤࡱࡸࠦ࠽ࠡࡽࠪࡵࠬࡀࡎࡰࡰࡨ࠰ࠥࠦࠧࡴࠩ࠽ࠫ࠵࠭ࡽࠋࠋࠌࡷࡪࡲࡦ࠯ࡪࡨࡥࡩ࡫ࡲࡴࠢࡀࠤࢀ࠭ࡕࡴࡧࡵ࠱ࡆ࡭ࡥ࡯ࡶࠪ࠾ࠬࡩࡵࡳ࡮࠲࠻࠳࠼࠵࠯࠵ࠪ࠰ࠏࠏࠉࠡࠩࡄࡧࡨ࡫ࡰࡵࠩ࠽ࠫ࠯࠵ࠪࠨࡿࠍࠎࠎࡪࡥࡧࠢࡶࡩࡹࡑࡥࡺࡹࡲࡶࡩ࠮ࡳࡦ࡮ࡩ࠰ࠥࡱࡥࡺࡹࡲࡶࡩ࠯࠺ࠋࠋࠌࡷࡪࡲࡦ࠯ࡲࡤࡶࡦࡳࡳ࡜ࠩࡴࠫࡢࠦ࠽ࠡ࡭ࡨࡽࡼࡵࡲࡥࠢ࠮ࠤࠬࠦࡳࡪࡶࡨ࠾ࡵࡧࡳࡵࡧࡥ࡭ࡳ࠴ࡣࡰ࡯ࠪࠎࠏࠏࡤࡦࡨࠣࡷࡨࡸࡡࡱࡧࠫࡷࡪࡲࡦ࠭ࠢࡩࡶࡪࡹࡨ࡯ࡧࡶࡷࡂࡔ࡯࡯ࡧࠬ࠾ࠏࠏࠉࡱࡣࡵࡥࡲࡹࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡱࡣࡵࡥࡲࡹࠊࠊࠋ࡫ࡩࡦࡪࡥࡳࡵࠣࡁࠥࡹࡥ࡭ࡨ࠱࡬ࡪࡧࡤࡦࡴࡶࠎࠎࠏࡵࡳ࡮ࠣࡁࠥࡹࡥ࡭ࡨ࠱ࡹࡷࡲࠊࠊࠋࡰࡥࡽࡥࡲࡦࡵࡸࡰࡹࡹࠠ࠾ࠢ࠴࠴࠵࠶ࠊࠊࠋࡼ࡭ࡪࡲࡤࡦࡦࠣࡁࠥ࠶ࠊࠊࠋ࡬ࡪࠥ࡬ࡲࡦࡵ࡫ࡲࡪࡹࡳ࠻ࠌࠌࠍࠎࡶࡡࡳࡣࡰࡷࡠ࠭ࡴࠨ࡟ࠣࡁࠥ࠭ࡨࡱࠩࠍࠍࠎࠏࡰࡢࡴࡤࡱࡸࡡࠧࡥࡨࠪࡡࠥࡃࠠࡧࡴࡨࡷ࡭ࡴࡥࡴࡵࠍࠍࠎࡽࡨࡪ࡮ࡨࠤ࡙ࡸࡵࡦ࠼ࠍࠍࠎࠏࡲࡦࡵࡳࡳࡳࡹࡥࡠࡦࡧ࡫ࠥࡃࠠࡳࡧࡴࡹࡪࡹࡴࡴ࠰ࡳࡳࡸࡺࠨࡶࡴ࡯࠰ࠥࡪࡡࡵࡣࡀࡴࡦࡸࡡ࡮ࡵ࠯ࠤ࡭࡫ࡡࡥࡧࡵࡷࡂ࡮ࡥࡢࡦࡨࡶࡸ࠯ࠊࠊࠋࠌࡰࡽࡳ࡬ࡠࡲࡤࡶࡸ࡫ࡤࠡ࠿ࠣ࡬ࡹࡳ࡬࠯ࡨࡵࡳࡲࡹࡴࡳ࡫ࡱ࡫࠭ࡸࡥࡴࡲࡲࡲࡸ࡫࡟ࡥࡦࡪ࠲ࡹ࡫ࡸࡵࠫࠍࠍࠎࠏࡩࡧࠢࠪࡍ࡫ࠦࡴࡩ࡫ࡶࠤࡪࡸࡲࡰࡴࠣࡴࡪࡸࡳࡪࡵࡷࡷ࠱࠭ࠠࡪࡰࠣࡶࡪࡹࡰࡰࡰࡶࡩࡤࡪࡤࡨ࠰ࡷࡩࡽࡺ࠺ࠋࠋࠌࠍࠎࡶࡲࡪࡰࡷࠬࡋࡵࡲࡦ࠰ࡕࡉࡉࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡃࡔࡌࡋࡍ࡚ࠠࠬࠢࠥࠤࡃࠦࡗࡦ࡮࡯ࠤࡾࡵࡵࠨࡴࡨࠤࡋࡻࡣ࡬ࡧࡧ࠲ࠥࡋࡶࡦࡰࠣࡈࡺࡩ࡫ࡅࡷࡦ࡯ࡌࡵࠠࡃࡣࡱࡲࡪࡪ࡚ࠠࡱࡸ࠰࡚ࠥࡡ࡬ࡧࠣࡥࠥࡉࡨࡪ࡮࡯ࠤࡉࡻࡤࡦ࠰ࠥ࠭ࠏࠏࠉࠊࠋࡥࡶࡪࡧ࡫ࠋࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࡳࡧࡶࡹࡱࡺࡳࠡ࠿ࠣ࡟ࡦ࠴ࡧࡦࡶࠫࠫ࡭ࡸࡥࡧࠩࠬࠤ࡫ࡵࡲࠡࡣࠣ࡭ࡳࠦ࡬ࡹ࡯࡯ࡣࡵࡧࡲࡴࡧࡧ࠲ࡨࡹࡳࡴࡧ࡯ࡩࡨࡺࠨࠨࠥ࡯࡭ࡳࡱࡳࠡ࠰࡯࡭ࡳࡱࡳࡠ࡯ࡤ࡭ࡳࠦࡡࠨࠫࡠࠎࠎࠏࠉࠊࡨࡲࡶࠥࡸࡥࡴࡷ࡯ࡸࠥ࡯࡮ࠡࡴࡨࡷࡺࡲࡴࡴ࠼ࠍࠍࠎࠏࠉࠊࡷࡵࡰࡱ࡯ࡳࡵ࠰ࡤࡴࡵ࡫࡮ࡥࠪࡵࡩࡸࡻ࡬ࡵࠫࠍࠍࠎࠏࠉࠊࡻ࡬ࡩࡱࡪࡥࡥࠢ࠮ࡁࠥ࠷ࠊࠊࠋࠌࠍࠎ࡯ࡦࠡ࡯ࡤࡼࡤࡸࡥࡴࡷ࡯ࡸࡸࡀࠊࠊࠋࠌࠍࠎࠏࡩࡧࠢࡼ࡭ࡪࡲࡤࡦࡦࠣࡂࡂࠦ࡭ࡢࡺࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠏࠏࠉࠊࠋࠌࠍࠎࡨࡲࡦࡣ࡮ࠎࠏࠏࠉࠊࠋࡷࡶࡾࡀࠊࠊࠋࠌࠍࠎ࡬࡯ࡳ࡯ࠣࡁࠥࡲࡸ࡮࡮ࡢࡴࡦࡸࡳࡦࡦ࠱ࡧࡸࡹࡳࡦ࡮ࡨࡧࡹ࠮ࠧ࠯ࡴࡨࡷࡺࡲࡴࡴࡡ࡯࡭ࡳࡱࡳࡠ࡯ࡲࡶࡪࠦࡦࡰࡴࡰࠫ࠮ࡡࠨ࠮࠳ࠬࡡࠏࠏࠉࠊࠋࡨࡼࡨ࡫ࡰࡵࠢࡌࡲࡩ࡫ࡸࡆࡴࡵࡳࡷࡀࠊࠊࠋࠌࠍࠎࡨࡲࡦࡣ࡮ࠎࠏࠏࠉࠊࠋࡳࡥࡷࡧ࡭ࡴࠢࡀࠤࡩ࡯ࡣࡵࠪࡩࡳࡷࡳ࠮ࡧ࡫ࡨࡰࡩࡹࠩࠋࠌࠌࡨࡪ࡬ࠠࡤ࡮ࡨࡥࡳࡒࡩࡴࡶࠫࡷࡪࡲࡦ࠭ࠢࡸࡶࡱࡲࡩࡴࡶࠬ࠾ࠏࠏࠉࡱࡷࡵࡩࡤࡲࡩࡴࡶࠣࡁࠥࡲࡩࡴࡶࠫࡨ࡮ࡩࡴ࠯ࡨࡵࡳࡲࡱࡥࡺࡵࠫࡹࡷࡲ࡬ࡪࡵࡷ࠭࠮ࠐࠉࠊࡴࡨࡸࡺࡸ࡮ࠡࡲࡸࡶࡪࡥ࡬ࡪࡵࡷࠎࠏࠏࡤࡦࡨࠣࡥࡳ࡯࡭ࡢࡶࡨࡨࡤࡲ࡯ࡢࡦ࡬ࡲ࡬࠮ࡳࡦ࡮ࡩ࠭࠿ࠐࠉࠊ࡮࠱ࡥࡨࡷࡵࡪࡴࡨࠬ࠮ࠐࠉࠊࡥ࡫ࡥࡷࡹࠠ࠾ࠢࠪ࠳࠲ࡢ࡜ࡽࠩࠍࠍࠎ࡬࡯ࡳࠢࡦ࡬ࡦࡸࠠࡪࡰࠣࡧ࡭ࡧࡲࡴ࠼ࠍࠍࠎࠏࡳࡺࡵ࠱ࡷࡹࡪ࡯ࡶࡶ࠱ࡻࡷ࡯ࡴࡦࠪࠪࡠࡷ࠭ࠠࠬࠢࡉࡳࡷ࡫࠮ࡈࡔࡈࡉࡓࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡅࡋࡐࠤ࠰ࠦࠧࠡࡀࠣࡗࡨࡸࡡࡱ࡫ࡱ࡫࠳࠴࠮ࠨࠢ࠮ࠤࡸࡺࡲࠩࡥ࡫ࡥࡷ࠯ࠩࠋࠋࠌࠍࡹ࡯࡭ࡦ࠰ࡶࡰࡪ࡫ࡰࠩ࠲࠱࠶࠮ࠐࠉࠊࠋࡶࡽࡸ࠴ࡳࡵࡦࡲࡹࡹ࠴ࡦ࡭ࡷࡶ࡬࠭࠯ࠊࠋࠋࠌࡰ࠳ࡸࡥ࡭ࡧࡤࡷࡪ࠮ࠩࠋࠤࠥࠦ࠷")
class l11l1ll1:
	def __init__(self, filename):
		self.l111l1l = l1 (u"ࠫࡵࡧࡳࡵࡧࡥ࡭ࡳ࠴ࡣࡰ࡯࠲ࡶࡦࡽࠧ࠸")
		self.s = Session()
		self.l1l1l = {l1 (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩ࠹"):l1 (u"࠭ࡍࡰࡼ࡬ࡰࡱࡧ࠯࠶࠰࠳ࠤ࠭ࡇ࡮ࡥࡴࡲ࡭ࡩࠦ࠹࠼ࠢࡐࡳࡧ࡯࡬ࡦ࠽ࠣࡶࡻࡀ࠶࠸࠰࠳࠭ࠥࡍࡥࡤ࡭ࡲ࠳࠻࠽࠮࠱ࠢࡉ࡭ࡷ࡫ࡦࡰࡺ࠲࠺࠼࠴࠰ࠨ࠺"),
		 l1 (u"ࠧࡂࡥࡦࡩࡵࡺࠧ࠻"):l1 (u"ࠨࡶࡨࡼࡹ࠵ࡸ࡮࡮࠯ࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺࡰࡰ࠱ࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࡭ࡺ࡭࡭࠭ࡻࡱࡱ࠲ࡴࡦࡺࡷ࠳࡭ࡺ࡭࡭࠽ࡴࡁ࠵࠴࠹࠭ࡶࡨࡼࡹ࠵ࡰ࡭ࡣ࡬ࡲࡀࡷ࠽࠱࠰࠻࠰࡮ࡳࡡࡨࡧ࠲ࡴࡳ࡭ࠬࠫ࠱࠭࠿ࡶࡃ࠰࠯࠷ࠪ࠼"),
		 l1 (u"ࠩࡆࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭࠽"):l1 (u"ࠪ࡯ࡪ࡫ࡰ࠮ࡣ࡯࡭ࡻ࡫ࠧ࠾"),
		 l1 (u"ࠫࡐ࡫ࡥࡱ࠯ࡄࡰ࡮ࡼࡥࠨ࠿"):l1 (u"ࠬ࠷࠱࠶ࠩࡀ"),
		 l1 (u"࠭ࡁࡤࡥࡨࡴࡹ࠳ࡃࡩࡣࡵࡷࡪࡺࠧࡁ"):l1 (u"ࠧࡊࡕࡒ࠱࠽࠾࠵࠺࠯࠴࠰ࡺࡺࡦ࠮࠺࠾ࡵࡂ࠶࠮࠸࠮࠭࠿ࡶࡃ࠰࠯࠹ࠪࡂ"),
		 l1 (u"ࠨࡃࡦࡧࡪࡶࡴ࠮ࡎࡤࡲ࡬ࡻࡡࡨࡧࠪࡃ"):l1 (u"ࠩࡨࡲ࠲ࡻࡳ࠭ࡧࡱ࠿ࡶࡃ࠰࠯࠷ࠪࡄ")}
		self.s.headers.update(self.l1l1l)
		self.l1l111l = re.compile(l1 (u"ࠪࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࠯ࡡ࠰ࡡ࠰ࡆ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࠰ࡡ࠰ࡢ࡜࠯࡝ࡤ࠱ࡿࡇ࡛࠭࠰ࡠࡿ࠷࠲࠹ࡾࠦࠪࡅ"), re.IGNORECASE)
		self.l11ll111 = re.compile(l1 (u"ࠫࡣࡡ࠰࠮࠻ࡄ࠱࡟ࡧ࠭ࡻࠣࡃࠧࠩࡅࠥ࠯ࡡ࠰ࡡࢀ࠸ࠬ࠴࠴ࢀࠨࠬࡆ"), re.IGNORECASE)
		self.l1l1ll11 = re.compile(l1 (u"ࠬࡤࠨࡩࡶࡷࡴࢁ࡮ࡴࡵࡲࡶ࠭࠿࠵࠯ࡱࡣࡶࡸࡪࡨࡩ࡯࠰ࡦࡳࡲ࠵࡜ࡸ࠭ࠧࠫࡇ"), re.IGNORECASE)
		self.filename = filename
		self.n = 0
	def l1lll111(self, links):
		self.n = 0
		l1lll1l1 = []
		for link in links:
			if link != l1 (u"࠭ࠧࡈ") and link is not None: # and self.l1l1ll11.match(link):
				l1lll1l1.append(link)
		with open(self.filename, l1 (u"ࠧࡢࠩࡉ")) as l11ll1:
			for link in l1lll1l1:
				print(Fore.GREEN + Style.NORMAL + l1 (u"ࠨࠢࡁࠤࡑ࡫ࡥࡤࡪ࡬ࡲ࡬ࠦࠧࡊ") + link + l1 (u"ࠩ࠱࠲࠳࠭ࡋ"))
				l1ll1l1l = link.replace(l1 (u"ࠪࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮ࠩࡌ"), self.l111l1l, 1)
				req = Request(l1 (u"ࠫࡌࡋࡔࠨࡍ"), l1ll1l1l)
				prep = req.prepare()
				l1lll1l = self.s.send(prep, timeout=30)
				soup = BeautifulSoup(l1lll1l.content, l1 (u"ࠬ࡮ࡴ࡮࡮࠱ࡴࡦࡸࡳࡦࡴࠪࡎ"))
				l1l = l1 (u"࠭ࠧࡏ").join(soup.findAll(text=True))
				l111ll1 = l1l.split(l1 (u"ࠧ࡝ࡰࠪࡐ"))
				i = 0
				for line in l111ll1:
					if l1 (u"ࠨࡾࠪࡑ") in line:
						line = line.split(l1 (u"ࠩࡿࠫࡒ"))[0]
					if l1 (u"ࠪ࠾ࠬࡓ") in line:
						if l1 (u"ࠫࡅ࠭ࡔ") in line:
							try:
								l1l1ll1, l11ll1ll = line.split(l1 (u"ࠬࡀࠧࡕ"))
							except ValueError:
								l1ll1111 = line.split(l1 (u"࠭࠺ࠨࡖ"))
								l1l1ll1 = l1ll1111[0]
								l11ll1ll = l1ll1111[1]
							l1l1ll1 = l1l1ll1.strip()
							l11ll1ll = l11ll1ll.strip()
							if self.l1l111l.match(l1l1ll1):
								if self.l11ll111.match(l11ll1ll):
									l11l1lll = l1l1ll1 + l1 (u"ࠧ࠻ࠩࡗ") + l11ll1ll
									print(Fore.GREEN + Style.DIM + l1 (u"ࠨࠢ࡟ࡸࡃࠦࡃࡰ࡯ࡥࡳࠥࡌ࡯ࡶࡰࡧࠤ࠿ࠦࠧࡘ") + l11l1lll)
									l11ll1.write(l11l1lll + l1 (u"ࠩ࡟ࡲ࡙ࠬ"))
									i = i + 1
									self.n = self.n + 1
				print(Fore.GREEN + Style.NORMAL + l1 (u"ࠪࠤࡃࠦࡆࡰࡷࡱࡨ࡚ࠥ࠭") + str(i) + l1 (u"ࠫࠥࡉ࡯࡮ࡤࡲࡷࠥ࡯࡮ࠡࡖ࡫࡭ࡸࠦࡌࡪࡰ࡮࠲࡛ࠬ"))
				#print(Fore.GREEN + Style.NORMAL + l1 (u"ࠬࠦ࠾ࠡࡖࡲࡸࡦࡲࠠࡄࡱࡰࡦࡴࡹࠠ࠻ࠢࠪ࡜") + Style.BRIGHT + str(self.n))
				print(Fore.YELLOW + Style.DIM + l1 (u"࠭ࠠ࠿ࠢࡓࡶࡪࡹࡳࠡࡅࡗࡖࡑࠦࠫࠡࡅࠣࡥࡹࠦࡁ࡯ࡻࠣࡔࡴ࡯࡮ࡵࠢࡷࡳࠥࡉࡡ࡯ࡥࡨࡰࠥࡧ࡮ࡥࠢࡖࡥࡻ࡫ࠠࡄࡱࡰࡦࡴࡹ࠮ࠡ࡞ࡱࠫ࡝"))
		l11llll = 0
		with open(self.filename, l1 (u"ࠧࡳࠩ࡞")) as l11l1l:
			for line in l11l1l:
				l11llll = l11llll + 1
		print(Fore.GREEN + Style.NORMAL + l1 (u"ࠨ࡞ࡱࠤࡃࠦࡆࡰࡷࡱࡨࠥ࠭࡟") + Style.BRIGHT + str(l11llll) + Style.NORMAL + l1 (u"ࠩࠣࡇࡴࡳࡢࡰࡵ࠱ࠫࡠ"))
		print(Fore.GREEN + Style.NORMAL + l1 (u"ࠪࠤࡃࠦࡓࡢࡸࡨࡨ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼ࠲ࠬࡡ"))
		print(Fore.CYAN + Style.BRIGHT + l1 (u"ࠫࠥࡄࠠࡄࡱࡰࡦࡴࡍࡥ࡯ࠢࡥࡽࠥࡆࡨࡦࡹ࡫ࡳࡲࡻࡳࡵࡰ࠳ࡸࡧ࡫࡮ࡢ࡯ࡨࡨ࠳ࠦࡐࡦࡣࡦࡩࠦ࠭ࡢ"))
def l1111ll():
	if os.path.isfile(l1 (u"ࠬ࠴ࡦࡪࡴࡶࡸࠬࡣ")):
		l1ll1 = strtobool(open(l1 (u"࠭࠮ࡧ࡫ࡵࡷࡹ࠭ࡤ"), l1 (u"ࠧࡳࠩࡥ")).read().strip())
	else:
		l1ll1 = True
	return l1ll1
def l1llll11():
	print(Fore.CYAN + l1 (u"ࠨࠢࡁࠤࡕࡲࡥࡢࡵࡨࠤࡆࡲ࡬ࡰࡹࠣࡗࡹࡵࡲࡢࡩࡨࠤࡕ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠢࡌࡪࠥࡇࡳ࡬ࡧࡧࠤࡹࡵࠠࡥࡱࠣࡗࡴ࠴ࠧࡦ"))
	time.sleep(2)
	if not os.path.isdir(l11111l + l1 (u"ࠩࡶࡸࡴࡸࡡࡨࡧࠪࡧ")):
		os.system(l1 (u"ࠪࡸࡪࡸ࡭ࡶࡺ࠰ࡷࡪࡺࡵࡱ࠯ࡶࡸࡴࡸࡡࡨࡧࠪࡨ"))
	if os.path.isdir(l11111l + l1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩࠬࡩ")):
		print(Fore.GREEN + l1 (u"ࠬࠦ࠾ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡆࡵࡷࡥࡧࡲࡩࡴࡪࡨࡨ࡙ࠥࡴࡰࡴࡤ࡫ࡪ࠴ࠧࡪ"))
		if not os.path.isdir(l11111l + l1 (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴࠧ࡫")):
			os.makedirs(l11111l + l1 (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠨ࡬"))
		if not os.path.isdir(l11111l + l1 (u"ࠨࡵࡷࡳࡷࡧࡧࡦ࠱ࡶ࡬ࡦࡸࡥࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯࠱ࡎࡩࡾࡽ࡯ࡳࡦࡶࠫ࡭")):
			os.makedirs(l11111l + l1 (u"ࠩࡶࡸࡴࡸࡡࡨࡧ࠲ࡷ࡭ࡧࡲࡦࡦ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬ࡮"))
		if not os.path.isdir(l11111l + l1 (u"ࠪࡷࡹࡵࡲࡢࡩࡨ࠳ࡸ࡮ࡡࡳࡧࡧ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡈࡵ࡭ࡣࡱࡏ࡭ࡸࡺࡳࠨ࡯")):
			os.makedirs(l11111l + l1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡉ࡯࡮ࡤࡲࡐ࡮ࡹࡴࡴࠩࡰ"))
		print(Fore.GREEN + l1 (u"ࠬࠦ࠾ࠡࡋࡱࡸࡪࡸ࡮ࡢ࡮ࠣࡗࡹࡵࡲࡢࡩࡨ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺࠢࡆࡶࡪࡧࡴࡦࡦࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠪࡱ"))
		print(Fore.GREEN + l1 (u"࠭ࠠ࠿ࠢࡕࡩࡸࡺࡡࡳࡶ࡬ࡲ࡬࠴ࠧࡲ"))
		time.sleep(1.5)
		os.system(l1 (u"ࠧࡤ࡮ࡨࡥࡷ࠭ࡳ"))
		open(l1 (u"ࠨ࠰ࡩ࡭ࡷࡹࡴࠨࡴ"), l1 (u"ࠩࡺࠫࡵ")).write(l1 (u"ࠪࡊࡦࡲࡳࡦࠩࡶ"))
def l11ll1l(l11lll1l):
	if l11lll1l != l1 (u"ࠫࡦ࡜ࡡࡅࡃࠣ࡯ࡊࡊࡡࡗࡴࡄࠫࡷ"):
		l11lll1l = float(l11lll1l)
		l1l11 = float(requests.get(l1 (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡲࡢࡹ࠱࡫࡮ࡺࡨࡶࡤࡸࡷࡪࡸࡣࡰࡰࡷࡩࡳࡺ࠮ࡤࡱࡰ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡲࡧࡳࡵࡧࡵ࠳࠳ࡼࡥࡳࡵ࡬ࡳࡳ࠭ࡸ")).text.strip())
		if l1l11 > l11lll1l:
			l1l1lll1 = str(requests.get(l1 (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡳࡣࡺ࠲࡬࡯ࡴࡩࡷࡥࡹࡸ࡫ࡲࡤࡱࡱࡸࡪࡴࡴ࠯ࡥࡲࡱ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡳࡡࡴࡶࡨࡶ࠴࠴ࡣࡩࡣࡱ࡫ࡪࡲ࡯ࡨࠩࡹ")).text.strip())
			print(Fore.GREEN + Style.BRIGHT + l1 (u"ࠧࠡࡀ࡙ࠣࡵࡪࡡࡵࡧࠣࡅࡻࡧࡩ࡭ࡣࡥࡰࡪ࠴࡜࡯ࠩࡺ"))
			time.sleep(0.7)
			l1l11l1 = input(Fore.GREEN + Style.NORMAL + l1 (u"ࠨࠢࡁࠤࡈ࡮ࡡ࡯ࡩࡨࡰࡴ࡭࠺ࠡ࡞ࡱࡠࡳ࠭ࡻ") + Style.DIM + l1l1lll1 + Fore.YELLOW + Style.BRIGHT + l1 (u"ࠩ࡟ࡲࡡࡴࠠ࠿ࠢࡇࡳࠥ࡟࡯ࡶ࡚ࠢࡥࡳࡺࠠࡵࡱ࡙ࠣࡵࡪࡡࡵࡧࠣࡒࡴࡽ࠿ࠡ࡝ࠪࡼ") + Fore.GREEN + l1 (u"ࠪ࡝ࠬࡽ") + Fore.YELLOW + l1 (u"ࠫ࠴࠭ࡾ") + Fore.RED + l1 (u"ࠬࡔࠧࡿ") + Fore.YELLOW + l1 (u"࠭࡝ࠡࠩࢀ") + Style.RESET_ALL)
			if l1l11l1.lower() == l1 (u"ࠧࡺࠩࢁ"):
				print(Fore.GREEN + Style.BRIGHT + l1 (u"ࠨࠢࡁࠤࡎࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡗࡳࡨࡦࡺࡥ࠯ࠩࢂ"))
				os.system(l1 (u"ࠩࡪ࡭ࡹࠦࡲࡦࡵࡨࡸࠥ࠳࠭ࡩࡣࡵࡨࠬࢃ"))
				os.system(l1 (u"ࠪ࡫࡮ࡺࠠࡱࡷ࡯ࡰࠥࡵࡲࡪࡩ࡬ࡲࠥࡳࡡࡴࡶࡨࡶࠬࢄ"))
				time.sleep(5)
				print(Fore.GREEN + Style.BRIGHT + l1 (u"ࠫࠥࡄࠠࡖࡲࡧࡥࡹ࡫ࠠࡄࡱࡰࡴࡱ࡫ࡴࡦ࠰ࠪࢅ"))
				print(Fore.GREEN + Style.BRIGHT + l1 (u"ࠬࠦ࠾ࠡࡒ࡯ࡩࡦࡹࡥࠡࡔࡨࡷࡹࡧࡲࡵࠢࡷ࡬ࡪࠦࡐࡳࡱࡪࡶࡦࡳࠠࡵࡱࠣࡍࡳࡩ࡯ࡳࡲࡲࡶࡦࡺࡥࠡࡶ࡫ࡩ࡛ࠥࡰࡥࡣࡷࡩ࠳࠭ࢆ"))
		elif l1l11 == l11lll1l:
			print(Fore.GREEN + Style.DIM + l1 (u"ࠨࠠ࠿ࠢ࡜ࡳࡺ࠭ࡲࡦࠢࡄࡰࡷ࡫ࡡࡥࡻࠣࡳࡳࠦࡴࡩࡧࠣࡐࡦࡺࡥࡴࡶ࡚ࠣࡪࡸࡳࡪࡱࡱ࠲ࠥࡉࡨࡦࡧࡵࡷࠦࠨࢇ"))
		elif l1l11 < l11lll1l:
			l1llll1l = os.getcwd()
			os.system(l1 (u"ࠧࡳ࡯ࠣ࠱ࡷ࡬ࠠࠨ࢈") + l1llll1l)
			os.system(l1 (u"ࠨࡴࡰࠤ࠲ࡸࡦࠡ࠱ࡶࡨࡨࡧࡲࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯ࠩࢉ"))
			print(Fore.RED + Style.BRIGHT + l1 (u"ࠩࠣࡂࠥࡓ࡯ࡥ࡫ࡩ࡭ࡨࡧࡴࡪࡱࡱࡷࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡌࡩ࡭ࡧࡶࡽࡸࡺࡥ࡮ࠢࡋࡥࡻ࡫ࠠࡃࡧࡨࡲࠥࡊࡥࡵࡧࡦࡸࡪࡪ࠮ࠡࡃ࡯ࡰࠥࡊࡡࡵࡣࠣ࡬ࡦࡹࠠࡃࡧࡨࡲࠥࡋࡲࡢࡵࡨࡨࠥࡧࡳࠡࡣࡱࠤࡆࡴࡴࡪࠢࡓ࡭ࡷࡧࡣࡺࠢࡐࡩࡦࡹࡵࡳࡧ࠱ࠫࢊ"))
			exit()
	else:
		print(l1 (u"ࠪࠤࡃࠦࡄࡦࡸࡨࡰࡴࡶࡥࡳࠢࡈࡼࡪࡳࡰࡵ࡫ࡲࡲ࠳࠭ࢋ"))
def l1l1l11l():
	if not os.path.isdir(l11111l + l1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩࠬࢌ")):
		os.system(l1 (u"ࠬࡺࡥࡳ࡯ࡸࡼ࠲ࡹࡥࡵࡷࡳ࠱ࡸࡺ࡯ࡳࡣࡪࡩࠬࢍ"))
	if os.path.isdir(l11111l + l1 (u"࠭ࡳࡵࡱࡵࡥ࡬࡫ࠧࢎ")):
		if not os.path.isdir(l11111l + l1 (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠨ࢏")):
			os.makedirs(l11111l + l1 (u"ࠨࡵࡷࡳࡷࡧࡧࡦ࠱ࡶ࡬ࡦࡸࡥࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯ࠩ࢐"))
		if not os.path.isdir(l11111l + l1 (u"ࠩࡶࡸࡴࡸࡡࡨࡧ࠲ࡷ࡭ࡧࡲࡦࡦ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬ࢑")):
			os.makedirs(l11111l + l1 (u"ࠪࡷࡹࡵࡲࡢࡩࡨ࠳ࡸ࡮ࡡࡳࡧࡧ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡐ࡫ࡹࡸࡱࡵࡨࡸ࠭࢒"))
		if not os.path.isdir(l11111l + l1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡉ࡯࡮ࡤࡲࡐ࡮ࡹࡴࡴࠩ࢓")):
			os.makedirs(l11111l + l1 (u"ࠬࡹࡴࡰࡴࡤ࡫ࡪ࠵ࡳࡩࡣࡵࡩࡩ࠵ࡖࡰ࡮ࡧࡩࡲࡵࡲࡵࡅࡲࡱࡲࡻ࡮ࡪࡶࡼ࠳ࡈࡵ࡭ࡣࡱࡊࡩࡳ࠵ࡃࡰ࡯ࡥࡳࡑ࡯ࡳࡵࡵࠪ࢔"))
		if not os.path.isdir(l11111l + l1 (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴ࠯ࡑࡴࡲࡼࡾࡒࡩࡴࡶࡶࠫ࢕")):
			os.makedirs(l11111l + l1 (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮࠰ࡒࡵࡳࡽࡿࡌࡪࡵࡷࡷࠬ࢖"))
def l11ll11l():
	l11l11 = b'aHR0cHM6Ly9naXN0LmdpdGh1YnVzZXJjb250ZW50LmNvbS9qYXluYW1tb2RpLzlmZWI4MDhkODA2ZDIzNjIyYmU1NjU1OWM0YmM4MzM0L3Jhdy9mMDAzZmM4MDg0YmU5Zjk1MzA0NjVjZmU1MjY2N2E4Y2JiYjg1ZjYwL3VzZXJz'
	print(Fore.RED + Style.BRIGHT + l1 (u"ࠩࠣࡂࠥࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠥࡘࡥࡲࡷ࡬ࡶࡪࡪ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡘࡨࡶ࡮࡬ࡹ࡛ࠡࡲࡹࡷࠦࡃࡳࡧࡧࡩࡳࡺࡩࡢ࡮ࡶ࠲ࠬ࢘"))
	uname = input(Fore.GREEN + Style.DIM + l1 (u"ࠪࠤࡃࠦࡕࡴࡧࡵࡲࡦࡳࡥࠡ࠼࢙ࠣࠫ") + Fore.RESET + Style.DIM)
	pwd = hashlib.sha256(getpass.getpass(Fore.GREEN + Style.DIM + l1 (u"ࠫࠥࡄࠠࡑࡣࡶࡷࡼࡵࡲࡥࠢ࠽ࠤ࢚ࠬ") + Fore.RESET + Style.DIM).encode(l1 (u"ࠬࡧࡳࡤ࡫࡬࢛ࠫ"))).hexdigest()
	l1l111l1 = requests.get(base64.b64decode(l11l11).decode(l1 (u"࠭ࡡࡴࡥ࡬࡭ࠬ࢜"))).text
	for x in l1l111l1.split(l1 (u"ࠧ࡝ࡰࠪ࢝")):
		if uname in x:
			if pwd == x.split(l1 (u"ࠣ࠼ࠥ࢞"))[1]:
				print(Fore.GREEN + Style.BRIGHT + l1 (u"ࠩࠣࡂࠥࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࠰ࠪ࢟"))
				return
	print(Fore.RED + Style.BRIGHT + l1 (u"ࠪࠤࡃࠦࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳࠦࡕ࡯ࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰ࠳ࠦࡐࡳࡱࡪࡶࡦࡳࠠࡕࡧࡵࡱ࡮ࡴࡡࡵࡧࡧ࠲ࠬࢠ"))
	print(Fore.RED + Style.DIM + l1 (u"ࠫࠥࡄࠠࡄࡱࡰࡦࡴࡹࠠࡄࡱ࡯ࡰࡪࡩࡴࡦࡦࠣ࠾ࠥ࠶ࠧࢡ"))
	os.system(l1 (u"ࠬࡱࡩ࡭࡮ࠣࠫࢢ") + str(os.getpid()))
	exit()
try:
	l11ll11l()
	l11lll1l = open(l1 (u"࠭࠮ࡷࡧࡵࡷ࡮ࡵ࡮ࠨࢣ"), l1 (u"ࠧࡳࠩࢤ")).read().strip()
	l1l1l11l()
	if l1111ll():
		l1llll11()
	print(Fore.CYAN + Style.NORMAL + l1 (u"ࠨ࡞ࡱࡠࡹࡢࡴࠡࡡࡢࡣࡤࡥ࡟ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡤࠦࠠࠡࠢࠣࠤࠥࠦ࡟ࡠࡡࡢࡣࡤࡢ࡮࡝ࡶ࡟ࡸࢁࠦࠠࠡࠢࠣࠤࢁࡥ࡟ࡠࠢࡢࡣࡤࡥ࡟ࡽࠢࡿࡣࡤࠦ࡟ࡠࡡࡿࠤࠥࠦ࡟ࡠࡡࡿࡣࡤࡥࠠࡠࡡࡢࡠࡳࡢࡴ࡝ࡶࡿࠤࠥࠦ࠭࠮࠯ࡿࠤ࠳ࠦࡼ࡝ࡶࠣࢀࠥ࠴ࠠࠡࡾࠣ࠲ࠥࢂࠠࠡࡾࠣࠤࠥࢂࠠ࠮ࡡࡿࠤࠥࠦࡼ࡝ࡰ࡟ࡸࡡࡺࡼࡠࡡࡢࡣࡤࡥࡼࡠࡡࡢࢀࡤࢂ࡟ࡽࡡࡿࡣࡤࡥ࡟ࡽࡡࡢࡣࢁࡥ࡟ࡠࡡࡢࡣࢁࡥ࡟ࡠࡾࡢࢀࡤࢂ࡜࡯࡞ࡱࡠࡹࡢࡴ࡝ࡶ࡟ࡸࡡࡺ࡜ࡵ࡞ࡷࠫࢥ") + Style.DIM + l1 (u"ࠩ࡟ࡸࠥࡼࠧࢦ") + l11lll1l + l1 (u"ࠪࠤࡧࡿࠠࡁࡪࡨࡻ࡭ࡵ࡭ࡶࡵࡷࡲ࠵ࡺࡢࡦࡰࡤࡱࡪࡪ࡜࡯࡞ࡱࡠࡳࠦ࠾ࠡࡉ࡬ࡸ࡭ࡻࡢ࠻ࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲࡫࡮ࡺࡨࡶࡤ࠱ࡧࡴࡳ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴ࡜࡯࡞ࡷࠫࢧ"))
	time.sleep(2)
	print(Fore.GREEN + Style.DIM + l1 (u"ࠫࠥࡄࠠࡷࠩࢨ") + l11lll1l + l1 (u"ࠬࠦࡄࡦࡸࡨࡰࡴࡶࡥࡥࠢࡥࡽࠥ࠭ࢩ") + Fore.GREEN + Style.BRIGHT + l1 (u"࠭ࡀࡩࡧࡺ࡬ࡴࡳࡵࡴࡶࡱ࠴ࡹࡨࡥ࡯ࡣࡰࡩࡩ࠭ࢪ") + Style.RESET_ALL + Fore.GREEN + Style.DIM + l1 (u"ࠧࠡࠪࡗࡩࡱ࡫ࡧࡳࡣࡰ࠭࠳࠭ࢫ"))
	time.sleep(1)
	print(Fore.GREEN + Style.DIM + l1 (u"ࠨࠢࡁࠤࡋࡵࡲࠡࡗࡳࡨࡦࡺࡥࡴࠢࠩࠤࡒࡵࡲࡦ࠮ࠣࡇ࡭࡫ࡣ࡬ࠢࡲࡹࡹ࠭ࢬ") + Fore.GREEN + Style.BRIGHT + l1 (u"ࠩࠣࡄ࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡎࡦࡹࡶࡰࡪࡺࡴࡦࡴࠪࢭ") + Style.RESET_ALL + Fore.GREEN + Style.DIM + l1 (u"ࠪࠤ࡚࠭ࡥ࡭ࡧࡪࡶࡦࡳࠩ࠯ࠩࢮ"))
	time.sleep(2)
	l11ll1l(l11lll1l)
	l1lllll = input(Fore.GREEN + Style.DIM + l1 (u"ࠫࠥࡄࠠࡑࡴࡨࡷࡸࠦࡅ࡯ࡶࡨࡶࠥࡺ࡯ࠡࡅࡲࡲࡹ࡯࡮ࡶࡧ࠱ࠫࢯ") + Style.RESET_ALL)
	print(Fore.GREEN + Style.DIM + l1 (u"ࠬࡢ࡮ࠡࡀࠣࡐࡴࡧࡤࡪࡰࡪࠤࡐ࡫ࡹࡸࡱࡵࡨࡸ࠴࡜࡯ࠢࡁࠤࡕࡲࡥࡢࡵࡨࠤࡒࡵࡶࡦࠢࡷ࡬ࡪࠦࡋࡦࡻࡺࡳࡷࡪࡳࠡࡈ࡬ࡰࡪࠦࡴࡰࠩࢰ") + Style.BRIGHT + l1 (u"࠭ࠠࡊࡰࡷࡩࡷࡴࡡ࡭ࠢࡖࡸࡴࡸࡡࡨࡧ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬࢱ"))
	time.sleep(4)
	l11l11l1 = l1 (u"ࠧࠨࢲ")
	l1ll111l = []
	while 1:
		try:
			l1ll1ll1 = SelectMenu()
			l1l111 = os.listdir(l1ll11l1 + l1 (u"ࠨࡍࡨࡽࡼࡵࡲࡥࡵࠪࢳ"))
			l1l11l1l = {}
			l1l11l11 = []
			for file in l1l111:
				if os.path.isfile(l1ll11l1 + l1 (u"ࠩࡎࡩࡾࡽ࡯ࡳࡦࡶ࠳ࠬࢴ") + file):
					l1l11ll = {l1 (u"ࠪࡲࡦࡳࡥࠨࢵ"):file,
					 l1 (u"ࠫࡵࡧࡴࡩࠩࢶ"):l1ll11l1 + l1 (u"ࠬࡑࡥࡺࡹࡲࡶࡩࡹ࠯ࠨࢷ") + file}
					l1l11l1l[file] = l1l11ll
					l1l11l11.append(l1l11ll[l1 (u"࠭࡮ࡢ࡯ࡨࠫࢸ")])
			l1l11l11.append(l1 (u"ࠧࡓࡧࡩࡶࡪࡹࡨࠡࡈ࡬ࡰࡪࠦࡌࡪࡵࡷࠫࢹ"))
			l1l11l11.append(l1 (u"ࠨࡇࡱࡸࡪࡸࠠࡌࡧࡼࡻࡴࡸࡤࡴࠢࡐࡥࡳࡻࡡ࡭࡮ࡼࠫࢺ"))
			l1ll1ll1.add_choices(l1l11l11)
			l11l11l1 = l1ll1ll1.select(l1 (u"ࠩࠣࡂࠥࡖ࡬ࡦࡣࡶࡩ࡙ࠥࡥ࡭ࡧࡦࡸࠥࡺࡨࡦࠢࡇࡩࡸ࡯ࡲࡦࡦࠣࡊ࡮ࡲࡥ࠯ࠩࢻ"))
			if l11l11l1 == l1 (u"ࠪࡖࡪ࡬ࡲࡦࡵ࡫ࠤࡋ࡯࡬ࡦࠢࡏ࡭ࡸࡺࠧࢼ"):
				raise l11ll
			else:
				if l11l11l1 == l1 (u"ࠫࡊࡴࡴࡦࡴࠣࡏࡪࡿࡷࡰࡴࡧࡷࠥࡓࡡ࡯ࡷࡤࡰࡱࡿࠧࢽ"):
					raise l1llllll
				print(Fore.GREEN + Style.DIM + l1 (u"ࠬࠦ࠾ࠡࡎࡲࡥࡩ࡯࡮ࡨࠢࡎࡩࡾࡽ࡯ࡳࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡉ࡭ࡱ࡫ࠠ࠻ࠢࠪࢾ") + Style.NORMAL + l11l11l1)
				time.sleep(1)
				try:
					with open(l1l11l1l[l11l11l1][l1 (u"࠭ࡰࡢࡶ࡫ࠫࢿ")], l1 (u"ࠧࡳࠩࣀ")) as key_file:
						l1lll = key_file.readlines()
						for x in l1lll:
							l1ll111l.append(x.strip())
						if l1ll111l == []:
							raise l11l1l1
				except l11l1l1:
					print(Fore.RED + Style.NORMAL + l1 (u"ࠨࠢࡁࠤࡋ࡯࡬ࡦࠢ࡬ࡷࠥࡋ࡭ࡱࡶࡼ࠲ࠥ࠭ࣁ") + Style.RESET_ALL)
					continue
			break
		except l11ll:
			print(Fore.GREEN + Style.DIM + l1 (u"ࠩࠣࡂࠥࡘࡥࡧࡴࡨࡷ࡭࡯࡮ࡨࠢࡉ࡭ࡱ࡫ࠠࡍ࡫ࡶࡸ࠳࠭ࣂ"))
			time.sleep(1)
			continue
		except l1llllll:
			try:
				l111l1 = input(Fore.GREEN + Style.DIM + l1 (u"ࠪࠤࡃࠦࡅ࡯ࡶࡨࡶࠥࡑࡥࡺࡹࡲࡶࡩࡹࠠࡔࡧࡳࡩࡷࡧࡴࡦࡦࠣࡦࡾࠦࡃࡰ࡯ࡰࡥࡸࠦࠨ࠭ࠫࠣ࠾ࠥ࠭ࣃ") + Fore.RESET + Style.DIM)
				l111l1 = l111l1.strip()
				l111l1 = l111l1.strip(l1 (u"ࠫ࠱࠭ࣄ"))
				if l111l1 == l1 (u"ࠬ࠭ࣅ") or l111l1 == None:
					raise l11l1l1
				else:
					l1lll = l111l1.split(l1 (u"࠭ࠬࠨࣆ"))
					print(Style.RESET_ALL)
					for x in l1lll:
						l1ll111l.append(x.strip())
				break
			except l11l1l1:
				print(Fore.RED + Style.NORMAL + l1 (u"ࠧࠡࡀࠣࡍࡳࡼࡡ࡭࡫ࡧࠤࡎࡴࡰࡶࡶ࠱ࠤࠬࣇ") + Style.RESET_ALL)
				continue
	#l1l111ll = l1l11lll()
	l1111 = 0
	l11l1l11 = [l1 (u"ࠣࡉࡲࡳ࡬ࡲࡥࠣࣈ")]
	l1 (u"ࠤࠥࠦࠏࠏࡥ࡯ࡩ࡬ࡲࡪࡥࡣࡩࡱ࡬ࡧࡪࡹࠠ࠾ࠢ࡞ࠫࡠࠦ࡝ࠡࡉࡲࡳ࡬ࡲࡥࠨ࠮ࠣࠫࡠࠦ࡝ࠡࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬ࠲ࠠࠨࡆࡲࡲࡪ࠭࡝ࠋࠋࡺ࡬࡮ࡲࡥࠡ࠳࠽ࠎࠎࠏࡴࡳࡻ࠽ࠎࠎࠏࠉࡦࡰࡪ࡭ࡳ࡫࡟࡮ࡧࡱࡹࠥࡃࠠࡔࡧ࡯ࡩࡨࡺࡍࡦࡰࡸࠬ࠮ࠐࠉࠊࠋࡨࡲ࡬࡯࡮ࡦࡡࡰࡩࡳࡻ࠮ࡢࡦࡧࡣࡨ࡮࡯ࡪࡥࡨࡷ࠭࡫࡮ࡨ࡫ࡱࡩࡤࡩࡨࡰ࡫ࡦࡩࡸ࠯ࠊࠊࠋࠌࡩࡳ࡭ࡩ࡯ࡧࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࠽ࠡࡧࡱ࡫࡮ࡴࡥࡠ࡯ࡨࡲࡺ࠴ࡳࡦ࡮ࡨࡧࡹ࠮ࠧࠡࡀࠣࡗࡪࡲࡥࡤࡶࠣࡗࡪࡧࡲࡤࡪࠣࡉࡳ࡭ࡩ࡯ࡧࡶࠤࡹࡵࠠࡖࡶ࡬ࡰ࡮ࡹࡥࠡࠪࡐࡹࡱࡺࡩࡱ࡮ࡨࠤࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡳࠡࡣࡵࡩࠥࡇ࡬࡭ࡱࡺࡩࡩ࠯ࠠ࠻ࠢࠪ࠭ࠏࠏࠉࠊ࡫ࡩࠤࡪࡴࡧࡪࡰࡨࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࠾࠿ࠣࠫࡠࠦ࡝ࠡࡉࡲࡳ࡬ࡲࡥࠨ࠼ࠍࠍࠎࠏࠉࡦࡰࡪ࡭ࡳ࡫࡟ࡤࡪࡲ࡭ࡨ࡫ࡳ࡜࠲ࡠࠤࡂࠦࠧ࡜ࠥࡠࠤࡌࡵ࡯ࡨ࡮ࡨࠫࠏࠏࠉࠊࠋࡶࡩࡱ࡫ࡣࡵࡧࡧࡣࡪࡴࡧࡪࡰࡨࡷ࠳ࡧࡰࡱࡧࡱࡨ࠭࠭ࡇࡰࡱࡪࡰࡪ࠭ࠩࠋࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࡪࡨࠣࡩࡳ࡭ࡩ࡯ࡧࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࠽࠾ࠢࠪ࡟ࠥࡣࠠࡅࡷࡦ࡯ࡉࡻࡣ࡬ࡉࡲࠫ࠿ࠐࠉࠊࠋࠌࠍࡪࡴࡧࡪࡰࡨࡣࡨ࡮࡯ࡪࡥࡨࡷࡠ࠷࡝ࠡ࠿ࠣࠫࡠࠩ࡝ࠡࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬࠐࠉࠊࠋࠌࠍࡸ࡫࡬ࡦࡥࡷࡩࡩࡥࡥ࡯ࡩ࡬ࡲࡪࡹ࠮ࡢࡲࡳࡩࡳࡪࠨࠨࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬ࠯ࠊࠊࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࠊ࡫ࡩࠤࡪࡴࡧࡪࡰࡨࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࠾࠿ࠣࠫࡠࠩ࡝ࠡࡉࡲࡳ࡬ࡲࡥࠨ࠼ࠍࠍࠎࠏࠉࠊࠋࡨࡲ࡬࡯࡮ࡦࡡࡦ࡬ࡴ࡯ࡣࡦࡵ࡞࠴ࡢࠦ࠽ࠡࠩ࡞ࠤࡢࠦࡇࡰࡱࡪࡰࡪ࠭ࠊࠊࠋࠌࠍࠎࠏࡳࡦ࡮ࡨࡧࡹ࡫ࡤࡠࡧࡱ࡫࡮ࡴࡥࡴ࠰ࡵࡩࡲࡵࡶࡦࠪࠪࡋࡴࡵࡧ࡭ࡧࠪ࠭ࠏࠏࠉࠊࠋࠌࡩࡱࡹࡥ࠻ࠌࠌࠍࠎࠏࠉࠊ࡫ࡩࠤࡪࡴࡧࡪࡰࡨࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࠾࠿ࠣࠫࡠࠩ࡝ࠡࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬࡀࠊࠊࠋࠌࠍࠎࠏࠉࡦࡰࡪ࡭ࡳ࡫࡟ࡤࡪࡲ࡭ࡨ࡫ࡳ࡜࠳ࡠࠤࡂࠦࠧ࡜ࠢࡠࠤࡉࡻࡣ࡬ࡆࡸࡧࡰࡍ࡯ࠨࠌࠌࠍࠎࠏࠉࠊࠋࡶࡩࡱ࡫ࡣࡵࡧࡧࡣࡪࡴࡧࡪࡰࡨࡷ࠳ࡸࡥ࡮ࡱࡹࡩ࠭࠭ࡄࡶࡥ࡮ࡈࡺࡩ࡫ࡈࡱࠪ࠭ࠏࠏࠉࠊࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࠊࠋࠌ࡭࡫ࠦࡥ࡯ࡩ࡬ࡲࡪࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡀࡁࠥ࠭ࡄࡰࡰࡨࠫ࠿ࠐࠉࠊࠋࠌࠍࠎࠏࠉࡪࡨࠣࡷࡪࡲࡥࡤࡶࡨࡨࡤ࡫࡮ࡨ࡫ࡱࡩࡸࠦࠡ࠾ࠢ࡞ࡡ࠿ࠐࠉࠊࠋࠌࠍࠎࠏࠉࠊࡤࡵࡩࡦࡱࠊࠊࠋࠌࠍࠎࠏࠉࠊࡧ࡯ࡷࡪࡀࠊࠊࠋࠌࠍࠎࠏࠉࠊࠋࡵࡥ࡮ࡹࡥࠡࡇࡰࡴࡹࡿࡌࡪࡵࡷࡉࡷࡸ࡯ࡳࠌࠌࠍࡪࡾࡣࡦࡲࡷࠤࡊࡳࡰࡵࡻࡏ࡭ࡸࡺࡅࡳࡴࡲࡶ࠿ࠐࠉࠊࠋࡳࡶ࡮ࡴࡴࠩࡈࡲࡶࡪ࠴ࡒࡆࡆࠣ࠯࡙ࠥࡴࡺ࡮ࡨ࠲ࡓࡕࡒࡎࡃࡏࠤ࠰ࠦࠧࠡࡀࠣࡍࡳࡼࡡ࡭࡫ࡧࠤࡎࡴࡰࡶࡶ࠱ࠤࠬࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡓࡇࡖࡉ࡙ࡥࡁࡍࡎࠬࠎࠎࠏࠉࡤࡱࡱࡸ࡮ࡴࡵࡦࠌࠥࠦࠧࣉ")
	l11ll1l1 = {}
	l1ll11 = {l1 (u"ࠪࡋࡴࡵࡧ࡭ࡧࠪ࣊"):[
	  l1 (u"ࠫࡆࡴࡹࠡࡖ࡬ࡱࡪ࠭࣋"), l1 (u"ࠬࡖࡡࡴࡶࠣࡌࡴࡻࡲࠨ࣌"), l1 (u"࠭ࡐࡢࡵࡷࠤ࠷࠺ࠠࡉࡱࡸࡶࡸ࠭࣍"), l1 (u"ࠧࡑࡣࡶࡸࠥ࡝ࡥࡦ࡭ࠪ࣎"), l1 (u"ࠨࡒࡤࡷࡹࠦࡍࡰࡰࡷ࡬࣏ࠬ"), l1 (u"ࠩࡓࡥࡸࡺ࡚ࠠࡧࡤࡶ࣐ࠬ")],
	 l1 (u"ࠪࡈࡺࡩ࡫ࡅࡷࡦ࡯ࡌࡵ࣑ࠧ"):[l1 (u"ࠫࡆࡴࡹࠡࡖ࡬ࡱࡪ࣒࠭")]}
	for l11l in l11l1l11:
		l11l1l1l = SelectMenu()
		l11l1l1l.add_choices(l1ll11[l11l])
		l1l1llll = l11l1l1l.select(l1 (u"ࠬࠦ࠾ࠡ࡝࣓ࠪ") + l11l + l1 (u"࠭࡝ࠡࡈ࡬ࡲࡩࠦࡒࡦࡵࡸࡰࡹࡹࠠࡰࡨࠣ࠾ࠥ࠭ࣔ"))
		if l1l1llll == l1 (u"ࠧࡂࡰࡼࠤ࡙࡯࡭ࡦࠩࣕ"):
			l11ll1l1[l11l] = l1 (u"ࠨࡼࠪࣖ")
		elif l1l1llll == l1 (u"ࠩࡓࡥࡸࡺࠠࡉࡱࡸࡶࠬࣗ"):
			l11ll1l1[l11l] = l1 (u"ࠪ࡬ࠬࣘ")
		elif l1l1llll == l1 (u"ࠫࡕࡧࡳࡵࠢ࠵࠸ࠥࡎ࡯ࡶࡴࡶࠫࣙ"):
			l11ll1l1[l11l] = l1 (u"ࠬࡪࠧࣚ")
		elif l1l1llll == l1 (u"࠭ࡐࡢࡵࡷࠤ࡜࡫ࡥ࡬ࠩࣛ"):
			l11ll1l1[l11l] = l1 (u"ࠧࡸࠩࣜ")
		elif l1l1llll == l1 (u"ࠨࡒࡤࡷࡹࠦࡍࡰࡰࡷ࡬ࠬࣝ"):
			l11ll1l1[l11l] = l1 (u"ࠩࡰࠫࣞ")
		elif l1l1llll == l1 (u"ࠪࡔࡦࡹࡴ࡛ࠡࡨࡥࡷ࠭ࣟ"):
			l11ll1l1[l11l] = l1 (u"ࠫࡾ࠭࣠")
		else:
			l11ll1l1[l11l] = l1 (u"ࠬࢀࠧ࣡")
		print(Fore.GREEN + Style.DIM + l1 (u"࠭ࠠ࠿ࠢࡉ࡭ࡳࡪࡩ࡯ࡩࠣࡖࡪࡹࡵ࡭ࡶࡶࠤࡴ࡬ࠠࠨ࣢") + Style.NORMAL + l1l1llll + Style.DIM + l1 (u"ࠧࠡࡨࡲࡶࣣࠥ࠭") + Fore.GREEN + Style.NORMAL + l11l + Fore.GREEN + Style.DIM + l1 (u"ࠨ࠰ࠪࣤ"))
	while True:
		try:
			l1l1l11 = input(Fore.GREEN + Style.DIM + l1 (u"ࠩࠣࡂࠥࡋ࡮ࡵࡧࡵࠤࡋ࡯࡬ࡦࠢࡑࡥࡲ࡫ࠠࡵࡱࠣࡗࡹࡵࡲࡦࠢࡆࡳࡲࡨ࡯ࠡࡎ࡬ࡷࡹࠦ࠺ࠡࠩࣥ") + Style.RESET_ALL + Style.DIM)
			if l1l1l11 == l1 (u"ࣦࠪࠫ") or l1l1l11 == None:
				raise l11l1l1
			else:
				if l1 (u"ࠫ࠳ࡺࡸࡵࠩࣧ") not in l1l1l11:
					l1l1l11 = l1l1l11.strip() + l1 (u"ࠬ࠴ࡴࡹࡶࠪࣨ")
				l11ll11 = l1ll11l1 + l1 (u"࠭ࡃࡰ࡯ࡥࡳࡑ࡯ࡳࡵࡵ࠲ࣩࠫ") + l1l1l11
				if os.path.isfile(l11ll11):
					raise l1lll11
			break
		except l1lll11:
			l11l111 = input(Fore.RED + Style.DIM + l1 (u"ࠧࠡࡀࠣࡊ࡮ࡲࡥࠡࡃ࡯ࡶࡪࡧࡤࡺࠢࡈࡼ࡮ࡹࡴࡴ࠰ࠣࡓࡻ࡫ࡲࡸࡴ࡬ࡸࡪࡅࠠ࡜ࠢࠪ࣪") + Fore.GREEN + Style.DIM + l1 (u"ࠨࡻࡨࡷࠬ࣫") + Fore.RED + Style.DIM + l1 (u"ࠩ࠲ࡲࡴࠦ࡝ࠡ࠼ࠣࠫ࣬") + Style.RESET_ALL + Style.DIM)
			if l11l111.lower() == l1 (u"ࠪࡽࡪࡹ࣭ࠧ"):
				print(Fore.RED + Style.DIM + l1 (u"ࠫࠥࡄࠠࡐࡸࡨࡶࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡌࡩ࡭ࡧ࠱࣮ࠫ"))
				os.system(l1 (u"ࠬࡸ࡭࣯ࠡࠩ") + l11ll11)
				break
			else:
				continue
		except l11l1l1:
			print(Fore.RED + Style.NORMAL + l1 (u"࠭ࠠ࠿ࠢࡌࡲࡻࡧ࡬ࡪࡦࠣࡍࡳࡶࡵࡵ࠰ࣰࠣࠫ") + Style.RESET_ALL)
			continue
	for l1l11111 in l1ll111l:
		try:
			for l11l in l11l1l11:
				if l11l == l1 (u"ࠧࡈࡱࡲ࡫ࡱ࡫ࣱࠧ"):
					print(Fore.GREEN + Style.DIM + l1 (u"ࠨࠢࡁࠤࡠࡍ࡯ࡰࡩ࡯ࡩࡢࠦࡓࡤࡴࡤࡴ࡮ࡴࡧࠡࡍࡨࡽࡼࡵࡲࡥࠢ࠽ࠤࣲࠬ") + Style.BRIGHT + str(l1l11111) + Style.RESET_ALL)
					time.sleep(1)
					l1ll1l11 = l11lllll(l1 (u"ࠩࡶ࡭ࡹ࡫࠺ࡱࡣࡶࡸࡪࡨࡩ࡯࠰ࡦࡳࡲࠦࡩ࡯ࡶࡨࡼࡹࡀࠧࣳ") + l1l11111)
					l1lll11l = threading.Thread(name=l1 (u"ࠪࡷࡨࡸࡡࡱ࡫ࡱ࡫ࡤࡺࡨࡳࡧࡤࡨࠬࣴ"), target=(l1ll1l11.l1l11l), args=(l11ll1l1[l11l]))
					l1lll11l.start()
					while l1lll11l.is_alive():
						if not l1ll1l11.l1ll:
							l1ll1l11.l1l1()
					print(Fore.GREEN + Style.DIM + l1 (u"ࠫࡡࡴࠠ࠿ࠢ࡞ࡋࡴࡵࡧ࡭ࡧࡠࠤࡘ࡫ࡡࡳࡥ࡫ࠤࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠮ࠡࡖࡲࡸࡦࡲࠠࡖࡔࡏࡷࠥࡌ࡯ࡶࡰࡧࠤ࠿ࠦࠧࣵ") + Style.NORMAL + str(len(l11l1)))
					l1 (u"ࠧࠨࠢࠋࠋࠌࠍࠎࠏࡩࡧࠢࡨࡲ࡬࡯࡮ࡦࠢࡀࡁࠥ࠭ࡄࡶࡥ࡮ࡈࡺࡩ࡫ࡈࡱࠪ࠾ࠏࠏࠉࠊࠋࠌࡴࡷ࡯࡮ࡵࠪࡉࡳࡷ࡫࠮ࡈࡔࡈࡉࡓࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡅࡋࡐࠤ࠰ࠦࠧࠡࡀࠣ࡟ࡉࡻࡣ࡬ࡆࡸࡧࡰࡍ࡯࡞ࠢࡖࡧࡷࡧࡰࡪࡰࡪࠤࡐ࡫ࡹࡸࡱࡵࡨࠥࡀࠠࠨࠢ࠮ࠤࡘࡺࡹ࡭ࡧ࠱ࡆࡗࡏࡇࡉࡖࠣ࠯ࠥࡹࡴࡳࠪ࡮ࡩࡾࡽ࡯ࡳࡦࠬࠤ࠰ࠦࡓࡵࡻ࡯ࡩ࠳ࡘࡅࡔࡇࡗࡣࡆࡒࡌࠪࠌࠌࠍࠎࠏࠉࡵ࡫ࡰࡩ࠳ࡹ࡬ࡦࡧࡳࠬ࠶࠯ࠊࠊࠋࠌࠍࠎࡊࡵࡤ࡭ࡇࡹࡨࡱࡇࡰࡕࡦࡶࡦࡶࡥࡳࡑࡥ࡮ࡪࡩࡴ࠯ࡵࡨࡸࡐ࡫ࡹࡸࡱࡵࡨ࠭ࡱࡥࡺࡹࡲࡶࡩ࠯ࠊࠊࠋࠌࠍࠎࡹࡣࡳࡣࡳࡩࡤࡶࡲࡰࡥࡨࡷࡸࠦ࠽ࠡࡶ࡫ࡶࡪࡧࡤࡪࡰࡪ࠲࡙࡮ࡲࡦࡣࡧࠬࡳࡧ࡭ࡦ࠿ࠪࡷࡨࡸࡡࡱ࡫ࡱ࡫ࡤࡺࡨࡳࡧࡤࡨࠬ࠲ࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠩࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࡘࡩࡲࡢࡲࡨࡶࡔࡨࡪࡦࡥࡷ࠲ࡸࡩࡲࡢࡲࡨ࠭࠮ࠐࠉࠊࠋࠌࠍࡸࡩࡲࡢࡲࡨࡣࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡹࡴࡢࡴࡷࠬ࠮ࠐࠉࠊࠋࠌࠍࡼ࡮ࡩ࡭ࡧࠣࡷࡨࡸࡡࡱࡧࡢࡴࡷࡵࡣࡦࡵࡶ࠲࡮ࡹ࡟ࡢ࡮࡬ࡺࡪ࠮ࠩ࠻ࠌࠌࠍࠎࠏࠉࠊࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࡘࡩࡲࡢࡲࡨࡶࡔࡨࡪࡦࡥࡷ࠲ࡦࡴࡩ࡮ࡣࡷࡩࡩࡥ࡬ࡰࡣࡧ࡭ࡳ࡭ࠨࠪࠌࠌࠍࠎࠏࠉࠣࠤࣶࠥ")
					print(Fore.GREEN + Style.DIM + l1 (u"࠭࡜࡯ࠢࡁࠤࡠࡊࡵࡤ࡭ࡇࡹࡨࡱࡇࡰ࡟ࠣࡗࡪࡧࡲࡤࡪࠣࡇࡴࡳࡰ࡭ࡧࡷࡩࡩ࠴ࠠࡕࡱࡷࡥࡱࠦࡕࡓࡎࡶࠤࡋࡵࡵ࡯ࡦࠣ࠾ࠥ࠭ࣷ") + Style.NORMAL + str(len(l11l1)))
		except KeyboardInterrupt:
			print(Fore.GREEN + Style.DIM + l1 (u"ࠧࠡ࡞ࡱࠤࡃࠦࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡔࡨࡷࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡋࡦࡻࡺࡳࡷࡪࡳ࠯ࠩࣸ"))
			break
	print(Fore.GREEN + Style.NORMAL + l1 (u"ࠨࠢࡁࠤࡘࡩࡲࡢࡲ࡬ࡲ࡬ࠦࡃࡰ࡯ࡳࡰࡪࡺࡥ࠯ࣹࠢࠪ") + Fore.CYAN + Style.BRIGHT + str(len(l11l1)) + Fore.GREEN + Style.NORMAL + l1 (u"࡙ࠩࠣࡗࡒࡳࠡࡈࡲࡹࡳࡪ࠮ࠨࣺ"))
	l11l1 = l1l111ll.l1l1l111(l11l1)
	print(Fore.GREEN + Style.NORMAL + l1 (u"ࠪࠤࡃࠦࡃ࡭ࡧࡤࡲ࡮ࡴࡧࠡࡗࡕࡐࡸࠦࠦࠡࡔࡨࡱࡴࡼࡩ࡯ࡩࠣࡈࡺࡶ࡬ࡪࡥࡤࡸࡪࡹ࠮ࠡࠩࣻ") + Fore.CYAN + Style.BRIGHT + str(len(l11l1)) + Fore.GREEN + Style.NORMAL + l1 (u"࡛ࠫࠥࡒࡍࡵࠣࡖࡪࡳࡡࡪࡰ࠱ࠫࣼ"))
	l111lll = input(Fore.GREEN + Style.BRIGHT + l1 (u"ࠬࠦ࠾ࠡࡒࡵࡩࡸࡹࠠࡆࡰࡷࡩࡷࠦࡴࡰࠢࡅࡩ࡬࡯࡮ࠡࡎࡨࡩࡨ࡮ࡩ࡯ࡩ࠱ࠫࣽ") + Style.RESET_ALL)
	l11lll = l11l1ll1(l11ll11)
	l11lll.l1lll111(l11l1)
except KeyboardInterrupt:
	try:
		l11llll = 0
		with open(l11lll.filename, l1 (u"࠭ࡲࠨࣾ")) as l11l1l:
			for line in l11l1l:
				l11llll = l11llll + 1
		print(Fore.RED + Style.NORMAL + l1 (u"ࠧ࡝ࡰࠣࡂࠥࡇࡢࡰࡴࡷ࡭ࡳ࡭ࠠࡑࡴࡲ࡫ࡷࡧ࡭࠯ࠩࣿ"))
		print(Fore.RED + Style.DIM + l1 (u"ࠨࠢࡁࠤࡈࡵ࡭ࡣࡱࡶࠤࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠ࠻ࠢࠪऀ") + str(l11llll))
		os.system(l1 (u"ࠩ࡮࡭ࡱࡲࠠࠨँ") + str(os.getpid()))
	except:
		print(Fore.RED + Style.DIM + l1 (u"ࠪࠤࡃࠦࡃࡰ࡯ࡥࡳࡸࠦࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢ࠽ࠤ࠵࠭ं"))
		os.system(l1 (u"ࠫࡰ࡯࡬࡭ࠢࠪः") + str(os.getpid()))
		exit()
