# coding: UTF-8
import sys
l111lll = sys.version_info [0] == 2
l1l1l = 2048
l11ll = 7
def l111lll1 (l1):
    global l1ll11l
    l1ll111 = ord (l1 [-1])
    l11ll11l = l1 [:-1]
    l11111l = l1ll111 % len (l11ll11l)
    l11l1ll1 = l11ll11l [:l11111l] + l11ll11l [l11111l:]
    if l111lll:
        l11l1l1 = unicode () .join ([unichr (ord (char) - l1l1l - (l1ll1l + l1ll111) % l11ll) for l1ll1l, char in enumerate (l11l1ll1)])
    else:
        l11l1l1 = str () .join ([chr (ord (char) - l1l1l - (l1ll1l + l1ll111) % l11ll) for l1ll1l, char in enumerate (l11l1ll1)])
    return eval (l11l1l1)
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
		print(l111lll1 (u"ࠫࠥࡄࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡘࡣ࡬ࡸࠥ࡝ࡨࡪ࡮ࡨࠤࡹ࡮ࡥࠡࡒࡵࡳ࡬ࡸࡡ࡮ࠢࡌࡲࡸࡺࡡ࡭࡮ࡶࠤࡹ࡮ࡥࠡࡆࡨࡴࡪࡴࡤࡦࡰࡦ࡭ࡪࡹ࠮ࠡࡖࡋࡍࡘࠦࡍࡊࡉࡋࡘ࡚ࠥࡁࡌࡇࠣࡅࠥࡒࡏࡏࡉࠣࡘࡎࡓࡅ࠯ࠩࠀ"))
		os.system(l111lll1 (u"ࠬࡧࡰࡵࠢࡸࡴࡩࡧࡴࡦࠢࠩࠪࠥࡧࡰࡵࠢࡸࡴ࡬ࡸࡡࡥࡧࠣࠪࠫࠦࡡࡱࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡷࡵ࡯ࡵ࠯ࡵࡩࡵࡵࠠࡶࡰࡶࡸࡦࡨ࡬ࡦ࠯ࡵࡩࡵࡵࠠ࠮ࡻࠪࠁ"))
		os.system(l111lll1 (u"࠭ࡡࡱࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡨࡲࡡ࡯ࡩࠣࡴࡾࡺࡨࡰࡰࠣࡰ࡮ࡨࡸࡴ࡮ࡷࠤࡱ࡯ࡢࡪࡥࡲࡲࡻࠦ࡬ࡪࡤ࡬ࡧࡴࡴࡶࠡ࠯ࡼࠫࠂ"))
		os.system(l111lll1 (u"ࠧࡱ࡫ࡳࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡲࡸ࡮࡮ࠪࠃ"))
		os.system(l111lll1 (u"ࠨࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦ࠭ࡳࠢࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳࠨࠄ"))
		os.system(l111lll1 (u"ࠩࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡴࡧ࡯ࡩࡨࡺ࡭ࡦࡰࡸࠤࠬࠅ"))
		print(l111lll1 (u"ࠪࡠࡳࡢ࡮ࠡࡀࠣࡈࡪࡶࡥ࡯ࡦࡨࡲࡨ࡯ࡥࡴࠢࡌࡲࡸࡺࡡ࡭࡮ࡨࡨ࠳ࠦࡒࡦࡵࡷࡥࡷࡺࡩ࡯ࡩ࠱࠲࠳࠭ࠆ"))
		os.system(l111lll1 (u"ࠫࡨࡲࡥࡢࡴࠪࠇ"))
		continue
colorama.init(autoreset=True)
l = Lock()
l1l1llll = []
l1l1ll = l111lll1 (u"ࠬ࠵ࡤࡢࡶࡤ࠳ࡩࡧࡴࡢ࠱ࡦࡳࡲ࠴ࡴࡦࡴࡰࡹࡽ࠵ࡦࡪ࡮ࡨࡷ࠴࡮࡯࡮ࡧ࠲ࠫࠈ")
l1l111l1 = l111lll1 (u"࠭࠯ࡥࡣࡷࡥ࠴ࡪࡡࡵࡣ࠲ࡧࡴࡳ࠮ࡵࡧࡵࡱࡺࡾ࠯ࡧ࡫࡯ࡩࡸ࠵ࡨࡰ࡯ࡨ࠳ࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴࠭ࠉ")
class l11lll11(Exception):
	pass
class l111l(Exception):
	pass
class l11l1ll(Exception):
	pass
class l111ll1(Exception):
	pass
class l1l1l1ll(Exception):
	pass
class l111111(Exception):
	pass
class l11l1lll:
	def __init__(self, l1l111l):
		self.ll = l1l111l
		self.l11l111 = {l111lll1 (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫࠊ"):l111lll1 (u"ࠨࡏࡲࡾ࡮ࡲ࡬ࡢ࠱࠸࠲࠵ࠦࠨࡂࡰࡧࡶࡴ࡯ࡤࠡ࠻࠾ࠤࡒࡵࡢࡪ࡮ࡨ࠿ࠥࡸࡶ࠻࠸࠺࠲࠵࠯ࠠࡈࡧࡦ࡯ࡴ࠵࠶࠸࠰࠳ࠤࡋ࡯ࡲࡦࡨࡲࡼ࠴࠼࠷࠯࠲ࠪࠋ"),
		 l111lll1 (u"ࠩࡄࡧࡨ࡫ࡰࡵࠩࠌ"):l111lll1 (u"ࠪࡸࡪࡾࡴ࠰ࡺࡰࡰ࠱ࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼࡲࡲࠬࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾࡨࡵ࡯࡯࠯ࡽࡳ࡬࠭ࡶࡨࡼࡹ࠵ࡨࡵ࡯࡯࠿ࡶࡃ࠰࠯࠻࠯ࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴ࠻ࡲ࠿࠳࠲࠽࠲ࡩ࡮ࡣࡪࡩ࠴ࡶ࡮ࡨ࠮࠭࠳࠯ࡁࡱ࠾࠲࠱࠹ࠬࠍ"),
		 l111lll1 (u"ࠫࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨࠎ"):l111lll1 (u"ࠬࡱࡥࡦࡲ࠰ࡥࡱ࡯ࡶࡦࠩࠏ"),
		 l111lll1 (u"࠭ࡋࡦࡧࡳ࠱ࡆࡲࡩࡷࡧࠪࠐ"):l111lll1 (u"ࠧ࠲࠳࠸ࠫࠑ"),
		 l111lll1 (u"ࠨࡃࡦࡧࡪࡶࡴ࠮ࡅ࡫ࡥࡷࡹࡥࡵࠩࠒ"):l111lll1 (u"ࠩࡌࡗࡔ࠳࠸࠹࠷࠼࠱࠶࠲ࡵࡵࡨ࠰࠼ࡀࡷ࠽࠱࠰࠺࠰࠯ࡁࡱ࠾࠲࠱࠻ࠬࠓ"),
		 l111lll1 (u"ࠪࡅࡨࡩࡥࡱࡶ࠰ࡐࡦࡴࡧࡶࡣࡪࡩࠬࠔ"):l111lll1 (u"ࠫࡪࡴ࠭ࡶࡵ࠯ࡩࡳࡁࡱ࠾࠲࠱࠹ࠬࠕ")}
		self.l1lll1ll = []
		self.l1lll1l = 4
		self.l11l = 6
		self.cookie = l111lll1 (u"ࠬ࠭ࠖ")
		self.l11l111 = l111lll1 (u"࠭ࠧࠗ")
		self.ei = l111lll1 (u"ࠧࠨ࠘")
		self.s = Session()
		self.s.headers.update(self.l11l111)
		self.l1l11ll = None
		self.l1ll1ll = False
		self.l11l1l = False
	def l1ll11(self, l1l11lll):
		l1l1111l = requests.cookies.create_cookie(name=l111lll1 (u"ࠨࡉࡒࡓࡌࡒࡅࡠࡃࡅ࡙ࡘࡋ࡟ࡆ࡚ࡈࡑࡕ࡚ࡉࡐࡐࠪ࠙"), value=l1l11lll)
		self.s.cookies.set_cookie(l1l1111l)
		self.l1ll1ll = False
		self.l11l1l = False
	def l1lll(self, url):
		req = Request(l111lll1 (u"ࠩࡊࡉ࡙࠭ࠚ"), url)
		prep = req.prepare()
		l1l1l111 = self.s.send(prep, timeout=30)
		return l1l1l111
	def l111ll1l(self):
		time.sleep(random.choice([self.l1lll1l, self.l11l]))
	def l11l11l(self):
		l1l11ll1 = self.l1lll(l111lll1 (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰࠫࠛ"))
		self.l111ll1l()
		self.l1lll(l111lll1 (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯ࡩࡲࡳ࡬ࡲࡥ࠯ࡥࡲࡱ࠴ࡴࡣࡳࠩࠜ"))
	def l1l1l11(self):
		l1l11ll1 = self.l1lll(l111lll1 (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡪࡳࡴ࡭࡬ࡦ࠰ࡦࡳࡲ࠵ࡰࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࡃ࡭ࡲ࠽ࡦࡰࠪࠝ"))
		soup = BeautifulSoup(l1l11ll1.content, l111lll1 (u"࠭ࡨࡵ࡯࡯࠲ࡵࡧࡲࡴࡧࡵࠫࠞ"))
		l11l11 = soup.find(l111lll1 (u"ࠧࡪࡰࡳࡹࡹ࠭ࠟ"), {l111lll1 (u"ࠨࡰࡤࡱࡪ࠭ࠠ"): l111lll1 (u"ࠩࡶ࡭࡬࠭ࠡ")})
		self.l111ll1l()
		self.l1lll(l111lll1 (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰ࠳ࡸ࡫ࡴࡱࡴࡨࡪࡸࡅࡳࡪࡩࡀࠫࠢ") + quote(l11l11[l111lll1 (u"ࠫࡻࡧ࡬ࡶࡧࠪࠣ")]) + l111lll1 (u"ࠬࠬࡨ࡭࠿ࡨࡲࠫࡲࡲ࠾࡮ࡤࡲ࡬ࡥࡥ࡯ࠨࡶࡥ࡫࡫ࡵࡪ࠿࡬ࡱࡦ࡭ࡥࡴࠨࡶࡹ࡬࡭࡯࡯࠿࠵ࠪࡳ࡫ࡷࡸ࡫ࡱࡨࡴࡽ࠽࠱ࠨࡱࡹࡲࡃ࠱࠱࠲ࠩࡵࡂࠬࡰࡳࡧࡹࡁ࡭ࡺࡴࡱࠧ࠶ࡅࠪ࠸ࡆࠦ࠴ࡉࡻࡼࡽ࠮ࡨࡱࡲ࡫ࡱ࡫࠮ࡤࡱࡰࠩ࠷ࡌࠦࡴࡷࡥࡱ࡮ࡺ࠲࠾ࡕࡤࡺࡪ࠱ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶ࠯ࠬࠤ"))
	def l111l11(self, l111ll=None):
		while 1:
			try:
				l1ll1ll1 = l111lll1 (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡷࡸࡹ࠱࡫ࡴࡵࡧ࡭ࡧ࠱ࡧࡴࡳ࠯ࡴࡧࡤࡶࡨ࡮࠿ࡲ࠿ࠪࠥ") + str(quote(self.ll)) + l111lll1 (u"ࠧࠧࡶࡥࡷࡂࡷࡤࡳ࠼ࠪࠦ") + l111ll + l111lll1 (u"ࠨࠨࡱࡹࡲࡃ࠱࠱࠲ࠩ࡬ࡱࡃࡥ࡯ࠨࡥ࡭ࡼࡃ࠱࠳࠺࠳ࠪࡧ࡯ࡨ࠾࠸࠴࠶ࠫࡶࡲ࡮ࡦࡀ࡭ࡻࡴࡳࠧࡧ࡬ࡁࠬࠧ") + str(quote(self.ei)) + l111lll1 (u"ࠩࠩࡷࡦࡃࡎࠨࠨ")
				l1l11ll1 = self.l1lll(l1ll1ll1)
				soup = BeautifulSoup(l1l11ll1.text, l111lll1 (u"ࠪ࡬ࡹࡳ࡬࠯ࡲࡤࡶࡸ࡫ࡲࠨࠩ"))
				l1l1l1l = soup.findAll(l111lll1 (u"ࠫ࡫ࡵࡲ࡮ࠩࠪ"))
				if not l1l1l1l is not None:
					if l1l1l1l != []:
						if l1l1l1l[0][l111lll1 (u"ࠬ࡯ࡤࠨࠫ")] == l111lll1 (u"࠭ࡣࡢࡲࡷࡧ࡭ࡧ࠭ࡧࡱࡵࡱࠬࠬ"):
							raise l11lll11
				links = soup.findAll(l111lll1 (u"ࠧࡢࠩ࠭"))
				for link in links:
					l1lll111 = link[l111lll1 (u"ࠨࡪࡵࡩ࡫࠭࠮")]
					if l111lll1 (u"ࠩ࠲ࡹࡷࡲ࠿ࡲ࠿࡫ࡸࡹࡶࡳ࠻࠱࠲ࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮ࠩ࠯") in l1lll111:
						self.l1lll1ll.append(l1lll111[7:])
				break
			except l11lll11:
				print(Fore.RED + Style.DIM + l111lll1 (u"ࠪࡠࡳࠦ࠾࡛ࠡࡲࡹࠥ࡮ࡡࡷࡧࠣࡆࡪ࡫࡮ࠡࡄ࡯ࡥࡨࡱ࡬ࡪࡵࡷࡩࡩࠦࡦࡳࡱࡰࠤࡌࡵ࡯ࡨ࡮ࡨ࠲ࠥࡕࡰࡦࡰࠣࠫ࠰") + Style.BRIGHT + l1ll1ll1 + Style.DIM + l111lll1 (u"ࠫࠥ࡯࡮ࠡࡈ࡬ࡶࡪ࡬࡯ࡹࠢࡤࡲࡩࠦࡅ࡯ࡶࡨࡶࠥࡺࡨࡦࠢࡆࡳࡳࡺࡥ࡯ࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࡋࡔࡕࡇࡍࡇࡢࡅࡇ࡛ࡓࡆࡡࡈ࡜ࡊࡓࡐࡕࡋࡒࡒࠥࡉ࡯ࡰ࡭࡬ࡩ࠳ࠦࡃࡐࡑࡎࡍࡊ࡙ࠠࡏࡑࡗࠤ࡜ࡕࡒࡌࡋࡑࡋ࠳࠭࠱") + Style.RESET_ALL)
				break
	def l1l1ll1l(self):
		chars = l111lll1 (u"ࠬ࠵࠭࡝࡞ࡿࠫ࠲")
		for char in chars:
			sys.stdout.write(l111lll1 (u"࠭࡜ࡳࠩ࠳") + Fore.GREEN + Style.DIM + l111lll1 (u"ࠧࠡࡀࠣࡗࡨࡸࡡࡱ࡫ࡱ࡫࠳࠴࠮ࠨ࠴") + str(char))
			time.sleep(0.2)
			sys.stdout.flush()
	def l11l11ll(self):
		global l1l1llll
		for link in self.l1lll1ll:
			l1ll1lll = link.index(l111lll1 (u"ࠨࠨࠪ࠵"))
			l1111l1 = link[0:l1ll1lll]
			if l111lll1 (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮࠱ࡸ࠳ࠬ࠶") not in l1111l1:
				l1l1llll.append(link[0:l1ll1lll])
	def l1ll11l1(self, l111ll):
		self.l11l11l()
		self.l111ll1l()
		self.l1l1l11()
		self.l111ll1l()
		self.l111l11(l111ll)
		self.l11l11ll()
l111lll1 (u"ࠥࠦࠧࠐࡣ࡭ࡣࡶࡷࠥࡊࡵࡤ࡭ࡇࡹࡨࡱࡇࡰࡕࡦࡶࡦࡶࡥࡳ࠼ࠍࠎࠎࡪࡥࡧࠢࡢࡣ࡮ࡴࡩࡵࡡࡢࠬࡸ࡫࡬ࡧࠫ࠽ࠎࠎࠏࡳࡦ࡮ࡩ࠲ࡺࡸ࡬ࠡ࠿ࠣࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡪࡵࡤ࡭ࡧࡹࡨࡱࡧࡰ࠰ࡦࡳࡲ࠵ࡨࡵ࡯࡯࠳ࠬࠐࠉࠊࡵࡨࡰ࡫࠴ࡰࡢࡴࡤࡱࡸࠦ࠽ࠡࡽࠪࡵࠬࡀࡎࡰࡰࡨ࠰ࠥࠦࠧࡴࠩ࠽ࠫ࠵࠭ࡽࠋࠋࠌࡷࡪࡲࡦ࠯ࡪࡨࡥࡩ࡫ࡲࡴࠢࡀࠤࢀ࠭ࡕࡴࡧࡵ࠱ࡆ࡭ࡥ࡯ࡶࠪ࠾ࠬࡩࡵࡳ࡮࠲࠻࠳࠼࠵࠯࠵ࠪ࠰ࠏࠏࠉࠡࠩࡄࡧࡨ࡫ࡰࡵࠩ࠽ࠫ࠯࠵ࠪࠨࡿࠍࠎࠎࡪࡥࡧࠢࡶࡩࡹࡑࡥࡺࡹࡲࡶࡩ࠮ࡳࡦ࡮ࡩ࠰ࠥࡱࡥࡺࡹࡲࡶࡩ࠯࠺ࠋࠋࠌࡷࡪࡲࡦ࠯ࡲࡤࡶࡦࡳࡳ࡜ࠩࡴࠫࡢࠦ࠽ࠡ࡭ࡨࡽࡼࡵࡲࡥࠢ࠮ࠤࠬࠦࡳࡪࡶࡨ࠾ࡵࡧࡳࡵࡧࡥ࡭ࡳ࠴ࡣࡰ࡯ࠪࠎࠏࠏࡤࡦࡨࠣࡷࡨࡸࡡࡱࡧࠫࡷࡪࡲࡦ࠭ࠢࡩࡶࡪࡹࡨ࡯ࡧࡶࡷࡂࡔ࡯࡯ࡧࠬ࠾ࠏࠏࠉࡱࡣࡵࡥࡲࡹࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡱࡣࡵࡥࡲࡹࠊࠊࠋ࡫ࡩࡦࡪࡥࡳࡵࠣࡁࠥࡹࡥ࡭ࡨ࠱࡬ࡪࡧࡤࡦࡴࡶࠎࠎࠏࡵࡳ࡮ࠣࡁࠥࡹࡥ࡭ࡨ࠱ࡹࡷࡲࠊࠊࠋࡰࡥࡽࡥࡲࡦࡵࡸࡰࡹࡹࠠ࠾ࠢ࠴࠴࠵࠶ࠊࠊࠋࡼ࡭ࡪࡲࡤࡦࡦࠣࡁࠥ࠶ࠊࠊࠋ࡬ࡪࠥ࡬ࡲࡦࡵ࡫ࡲࡪࡹࡳ࠻ࠌࠌࠍࠎࡶࡡࡳࡣࡰࡷࡠ࠭ࡴࠨ࡟ࠣࡁࠥ࠭ࡨࡱࠩࠍࠍࠎࠏࡰࡢࡴࡤࡱࡸࡡࠧࡥࡨࠪࡡࠥࡃࠠࡧࡴࡨࡷ࡭ࡴࡥࡴࡵࠍࠍࠎࡽࡨࡪ࡮ࡨࠤ࡙ࡸࡵࡦ࠼ࠍࠍࠎࠏࡲࡦࡵࡳࡳࡳࡹࡥࡠࡦࡧ࡫ࠥࡃࠠࡳࡧࡴࡹࡪࡹࡴࡴ࠰ࡳࡳࡸࡺࠨࡶࡴ࡯࠰ࠥࡪࡡࡵࡣࡀࡴࡦࡸࡡ࡮ࡵ࠯ࠤ࡭࡫ࡡࡥࡧࡵࡷࡂ࡮ࡥࡢࡦࡨࡶࡸ࠯ࠊࠊࠋࠌࡰࡽࡳ࡬ࡠࡲࡤࡶࡸ࡫ࡤࠡ࠿ࠣ࡬ࡹࡳ࡬࠯ࡨࡵࡳࡲࡹࡴࡳ࡫ࡱ࡫࠭ࡸࡥࡴࡲࡲࡲࡸ࡫࡟ࡥࡦࡪ࠲ࡹ࡫ࡸࡵࠫࠍࠍࠎࠏࡩࡧࠢࠪࡍ࡫ࠦࡴࡩ࡫ࡶࠤࡪࡸࡲࡰࡴࠣࡴࡪࡸࡳࡪࡵࡷࡷ࠱࠭ࠠࡪࡰࠣࡶࡪࡹࡰࡰࡰࡶࡩࡤࡪࡤࡨ࠰ࡷࡩࡽࡺ࠺ࠋࠋࠌࠍࠎࡶࡲࡪࡰࡷࠬࡋࡵࡲࡦ࠰ࡕࡉࡉࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡃࡔࡌࡋࡍ࡚ࠠࠬࠢࠥࠤࡃࠦࡗࡦ࡮࡯ࠤࡾࡵࡵࠨࡴࡨࠤࡋࡻࡣ࡬ࡧࡧ࠲ࠥࡋࡶࡦࡰࠣࡈࡺࡩ࡫ࡅࡷࡦ࡯ࡌࡵࠠࡃࡣࡱࡲࡪࡪ࡚ࠠࡱࡸ࠰࡚ࠥࡡ࡬ࡧࠣࡥࠥࡉࡨࡪ࡮࡯ࠤࡉࡻࡤࡦ࠰ࠥ࠭ࠏࠏࠉࠊࠋࡥࡶࡪࡧ࡫ࠋࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࡳࡧࡶࡹࡱࡺࡳࠡ࠿ࠣ࡟ࡦ࠴ࡧࡦࡶࠫࠫ࡭ࡸࡥࡧࠩࠬࠤ࡫ࡵࡲࠡࡣࠣ࡭ࡳࠦ࡬ࡹ࡯࡯ࡣࡵࡧࡲࡴࡧࡧ࠲ࡨࡹࡳࡴࡧ࡯ࡩࡨࡺࠨࠨࠥ࡯࡭ࡳࡱࡳࠡ࠰࡯࡭ࡳࡱࡳࡠ࡯ࡤ࡭ࡳࠦࡡࠨࠫࡠࠎࠎࠏࠉࠊࡨࡲࡶࠥࡸࡥࡴࡷ࡯ࡸࠥ࡯࡮ࠡࡴࡨࡷࡺࡲࡴࡴ࠼ࠍࠍࠎࠏࠉࠊࡷࡵࡰࡱ࡯ࡳࡵ࠰ࡤࡴࡵ࡫࡮ࡥࠪࡵࡩࡸࡻ࡬ࡵࠫࠍࠍࠎࠏࠉࠊࡻ࡬ࡩࡱࡪࡥࡥࠢ࠮ࡁࠥ࠷ࠊࠊࠋࠌࠍࠎ࡯ࡦࠡ࡯ࡤࡼࡤࡸࡥࡴࡷ࡯ࡸࡸࡀࠊࠊࠋࠌࠍࠎࠏࡩࡧࠢࡼ࡭ࡪࡲࡤࡦࡦࠣࡂࡂࠦ࡭ࡢࡺࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠏࠏࠉࠊࠋࠌࠍࠎࡨࡲࡦࡣ࡮ࠎࠏࠏࠉࠊࠋࡷࡶࡾࡀࠊࠊࠋࠌࠍࠎ࡬࡯ࡳ࡯ࠣࡁࠥࡲࡸ࡮࡮ࡢࡴࡦࡸࡳࡦࡦ࠱ࡧࡸࡹࡳࡦ࡮ࡨࡧࡹ࠮ࠧ࠯ࡴࡨࡷࡺࡲࡴࡴࡡ࡯࡭ࡳࡱࡳࡠ࡯ࡲࡶࡪࠦࡦࡰࡴࡰࠫ࠮ࡡࠨ࠮࠳ࠬࡡࠏࠏࠉࠊࠋࡨࡼࡨ࡫ࡰࡵࠢࡌࡲࡩ࡫ࡸࡆࡴࡵࡳࡷࡀࠊࠊࠋࠌࠍࠎࡨࡲࡦࡣ࡮ࠎࠏࠏࠉࠊࠋࡳࡥࡷࡧ࡭ࡴࠢࡀࠤࡩ࡯ࡣࡵࠪࡩࡳࡷࡳ࠮ࡧ࡫ࡨࡰࡩࡹࠩࠋࠌࠌࡨࡪ࡬ࠠࡤ࡮ࡨࡥࡳࡒࡩࡴࡶࠫࡷࡪࡲࡦ࠭ࠢࡸࡶࡱࡲࡩࡴࡶࠬ࠾ࠏࠏࠉࡱࡷࡵࡩࡤࡲࡩࡴࡶࠣࡁࠥࡲࡩࡴࡶࠫࡨ࡮ࡩࡴ࠯ࡨࡵࡳࡲࡱࡥࡺࡵࠫࡹࡷࡲ࡬ࡪࡵࡷ࠭࠮ࠐࠉࠊࡴࡨࡸࡺࡸ࡮ࠡࡲࡸࡶࡪࡥ࡬ࡪࡵࡷࠎࠏࠏࡤࡦࡨࠣࡥࡳ࡯࡭ࡢࡶࡨࡨࡤࡲ࡯ࡢࡦ࡬ࡲ࡬࠮ࡳࡦ࡮ࡩ࠭࠿ࠐࠉࠊ࡮࠱ࡥࡨࡷࡵࡪࡴࡨࠬ࠮ࠐࠉࠊࡥ࡫ࡥࡷࡹࠠ࠾ࠢࠪ࠳࠲ࡢ࡜ࡽࠩࠍࠍࠎ࡬࡯ࡳࠢࡦ࡬ࡦࡸࠠࡪࡰࠣࡧ࡭ࡧࡲࡴ࠼ࠍࠍࠎࠏࡳࡺࡵ࠱ࡷࡹࡪ࡯ࡶࡶ࠱ࡻࡷ࡯ࡴࡦࠪࠪࡠࡷ࠭ࠠࠬࠢࡉࡳࡷ࡫࠮ࡈࡔࡈࡉࡓࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡅࡋࡐࠤ࠰ࠦࠧࠡࡀࠣࡗࡨࡸࡡࡱ࡫ࡱ࡫࠳࠴࠮ࠨࠢ࠮ࠤࡸࡺࡲࠩࡥ࡫ࡥࡷ࠯ࠩࠋࠋࠌࠍࡹ࡯࡭ࡦ࠰ࡶࡰࡪ࡫ࡰࠩ࠲࠱࠶࠮ࠐࠉࠊࠋࡶࡽࡸ࠴ࡳࡵࡦࡲࡹࡹ࠴ࡦ࡭ࡷࡶ࡬࠭࠯ࠊࠋࠋࠌࡰ࠳ࡸࡥ࡭ࡧࡤࡷࡪ࠮ࠩࠋࠤࠥࠦ࠷")
class l1lll1:
	def __init__(self, filename):
		self.l11ll1 = l111lll1 (u"ࠫࡵࡧࡳࡵࡧࡥ࡭ࡳ࠴ࡣࡰ࡯࠲ࡶࡦࡽࠧ࠸")
		self.s = Session()
		self.l11l111 = {l111lll1 (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩ࠹"):l111lll1 (u"࠭ࡍࡰࡼ࡬ࡰࡱࡧ࠯࠶࠰࠳ࠤ࠭ࡇ࡮ࡥࡴࡲ࡭ࡩࠦ࠹࠼ࠢࡐࡳࡧ࡯࡬ࡦ࠽ࠣࡶࡻࡀ࠶࠸࠰࠳࠭ࠥࡍࡥࡤ࡭ࡲ࠳࠻࠽࠮࠱ࠢࡉ࡭ࡷ࡫ࡦࡰࡺ࠲࠺࠼࠴࠰ࠨ࠺"),
		 l111lll1 (u"ࠧࡂࡥࡦࡩࡵࡺࠧ࠻"):l111lll1 (u"ࠨࡶࡨࡼࡹ࠵ࡸ࡮࡮࠯ࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺࡰࡰ࠱ࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࡭ࡺ࡭࡭࠭ࡻࡱࡱ࠲ࡴࡦࡺࡷ࠳࡭ࡺ࡭࡭࠽ࡴࡁ࠵࠴࠹࠭ࡶࡨࡼࡹ࠵ࡰ࡭ࡣ࡬ࡲࡀࡷ࠽࠱࠰࠻࠰࡮ࡳࡡࡨࡧ࠲ࡴࡳ࡭ࠬࠫ࠱࠭࠿ࡶࡃ࠰࠯࠷ࠪ࠼"),
		 l111lll1 (u"ࠩࡆࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭࠽"):l111lll1 (u"ࠪ࡯ࡪ࡫ࡰ࠮ࡣ࡯࡭ࡻ࡫ࠧ࠾"),
		 l111lll1 (u"ࠫࡐ࡫ࡥࡱ࠯ࡄࡰ࡮ࡼࡥࠨ࠿"):l111lll1 (u"ࠬ࠷࠱࠶ࠩࡀ"),
		 l111lll1 (u"࠭ࡁࡤࡥࡨࡴࡹ࠳ࡃࡩࡣࡵࡷࡪࡺࠧࡁ"):l111lll1 (u"ࠧࡊࡕࡒ࠱࠽࠾࠵࠺࠯࠴࠰ࡺࡺࡦ࠮࠺࠾ࡵࡂ࠶࠮࠸࠮࠭࠿ࡶࡃ࠰࠯࠹ࠪࡂ"),
		 l111lll1 (u"ࠨࡃࡦࡧࡪࡶࡴ࠮ࡎࡤࡲ࡬ࡻࡡࡨࡧࠪࡃ"):l111lll1 (u"ࠩࡨࡲ࠲ࡻࡳ࠭ࡧࡱ࠿ࡶࡃ࠰࠯࠷ࠪࡄ")}
		self.s.headers.update(self.l11l111)
		self.l11l111l = re.compile(l111lll1 (u"ࠪࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࠯ࡡ࠰ࡡ࠰ࡆ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࠰ࡡ࠰ࡢ࡜࠯࡝ࡤ࠱ࡿࡇ࡛࠭࠰ࡠࡿ࠷࠲࠹ࡾࠦࠪࡅ"), re.IGNORECASE)
		self.l1l1ll1 = re.compile(l111lll1 (u"ࠫࡣࡡ࠰࠮࠻ࡄ࠱࡟ࡧ࠭ࡻࠣࡃࠧࠩࡅࠥ࠯ࡡ࠰ࡡࢀ࠸ࠬ࠴࠴ࢀࠨࠬࡆ"), re.IGNORECASE)
		self.l1l1l1 = re.compile(l111lll1 (u"ࠬࡤࠨࡩࡶࡷࡴࢁ࡮ࡴࡵࡲࡶ࠭࠿࠵࠯ࡱࡣࡶࡸࡪࡨࡩ࡯࠰ࡦࡳࡲ࠵࡜ࡸ࠭ࠧࠫࡇ"), re.IGNORECASE)
		self.filename = filename
		self.n = 0
	def l1ll(self, links):
		self.n = 0
		l11lll1l = []
		for link in links:
			if link != l111lll1 (u"࠭ࠧࡈ") and link is not None: # and self.l1l1l1.match(link):
				l11lll1l.append(link)
		with open(self.filename, l111lll1 (u"ࠧࡢࠩࡉ")) as l11lll1:
			for link in l11lll1l:
				print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠨࠢࡁࠤࡑ࡫ࡥࡤࡪ࡬ࡲ࡬ࠦࠧࡊ") + link + l111lll1 (u"ࠩ࠱࠲࠳࠭ࡋ"))
				l1111ll = link.replace(l111lll1 (u"ࠪࡴࡦࡹࡴࡦࡤ࡬ࡲ࠳ࡩ࡯࡮ࠩࡌ"), self.l11ll1, 1)
				req = Request(l111lll1 (u"ࠫࡌࡋࡔࠨࡍ"), l1111ll)
				prep = req.prepare()
				l1l1l111 = self.s.send(prep, timeout=30)
				soup = BeautifulSoup(l1l1l111.content, l111lll1 (u"ࠬ࡮ࡴ࡮࡮࠱ࡴࡦࡸࡳࡦࡴࠪࡎ"))
				l1l11l1 = l111lll1 (u"࠭ࠧࡏ").join(soup.findAll(text=True))
				l1lll11l = l1l11l1.split(l111lll1 (u"ࠧ࡝ࡰࠪࡐ"))
				i = 0
				for line in l1lll11l:
					if l111lll1 (u"ࠨࡾࠪࡑ") in line:
						line = line.split(l111lll1 (u"ࠩࡿࠫࡒ"))[0]
					if l111lll1 (u"ࠪ࠾ࠬࡓ") in line:
						if l111lll1 (u"ࠫࡅ࠭ࡔ") in line:
							try:
								l1lllll1, l11lll = line.split(l111lll1 (u"ࠬࡀࠧࡕ"))
							except ValueError:
								l11ll111 = line.split(l111lll1 (u"࠭࠺ࠨࡖ"))
								l1lllll1 = l11ll111[0]
								l11lll = l11ll111[1]
							l1lllll1 = l1lllll1.strip()
							l11lll = l11lll.strip()
							if self.l11l111l.match(l1lllll1):
								if self.l1l1ll1.match(l11lll):
									l1ll11ll = l1lllll1 + l111lll1 (u"ࠧ࠻ࠩࡗ") + l11lll
									print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠨࠢ࡟ࡸࡃࠦࡃࡰ࡯ࡥࡳࠥࡌ࡯ࡶࡰࡧࠤ࠿ࠦࠧࡘ") + l1ll11ll)
									l11lll1.write(l1ll11ll + l111lll1 (u"ࠩ࡟ࡲ࡙ࠬ"))
									i = i + 1
									self.n = self.n + 1
				print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠪࠤࡃࠦࡆࡰࡷࡱࡨ࡚ࠥ࠭") + str(i) + l111lll1 (u"ࠫࠥࡉ࡯࡮ࡤࡲࡷࠥ࡯࡮ࠡࡖ࡫࡭ࡸࠦࡌࡪࡰ࡮࠲࡛ࠬ"))
				#print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠬࠦ࠾ࠡࡖࡲࡸࡦࡲࠠࡄࡱࡰࡦࡴࡹࠠ࠻ࠢࠪ࡜") + Style.BRIGHT + str(self.n))
				print(Fore.YELLOW + Style.DIM + l111lll1 (u"࠭ࠠ࠿ࠢࡓࡶࡪࡹࡳࠡࡅࡗࡖࡑࠦࠫࠡࡅࠣࡥࡹࠦࡁ࡯ࡻࠣࡔࡴ࡯࡮ࡵࠢࡷࡳࠥࡉࡡ࡯ࡥࡨࡰࠥࡧ࡮ࡥࠢࡖࡥࡻ࡫ࠠࡄࡱࡰࡦࡴࡹ࠮ࠡ࡞ࡱࠫ࡝"))
		l111llll = 0
		with open(self.filename, l111lll1 (u"ࠧࡳࠩ࡞")) as l1llllll:
			for line in l1llllll:
				l111llll = l111llll + 1
		print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠨ࡞ࡱࠤࡃࠦࡆࡰࡷࡱࡨࠥ࠭࡟") + Style.BRIGHT + str(l111llll) + Style.NORMAL + l111lll1 (u"ࠩࠣࡇࡴࡳࡢࡰࡵ࠱ࠫࡠ"))
		print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠪࠤࡃࠦࡓࡢࡸࡨࡨ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼ࠲ࠬࡡ"))
		print(Fore.CYAN + Style.BRIGHT + l111lll1 (u"ࠫࠥࡄࠠࡄࡱࡰࡦࡴࡍࡥ࡯ࠢࡥࡽࠥࡆࡨࡦࡹ࡫ࡳࡲࡻࡳࡵࡰ࠳ࡸࡧ࡫࡮ࡢ࡯ࡨࡨ࠳ࠦࡐࡦࡣࡦࡩࠦ࠭ࡢ"))
def l11lllll():
	if os.path.isfile(l111lll1 (u"ࠬ࠴ࡦࡪࡴࡶࡸࠬࡣ")):
		l1l11l1l = strtobool(open(l111lll1 (u"࠭࠮ࡧ࡫ࡵࡷࡹ࠭ࡤ"), l111lll1 (u"ࠧࡳࠩࡥ")).read().strip())
	else:
		l1l11l1l = True
	return l1l11l1l
def l1l1ll11():
	print(Fore.CYAN + l111lll1 (u"ࠨࠢࡁࠤࡕࡲࡥࡢࡵࡨࠤࡆࡲ࡬ࡰࡹࠣࡗࡹࡵࡲࡢࡩࡨࠤࡕ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠢࡌࡪࠥࡇࡳ࡬ࡧࡧࠤࡹࡵࠠࡥࡱࠣࡗࡴ࠴ࠧࡦ"))
	time.sleep(2)
	if not os.path.isdir(l1l1ll + l111lll1 (u"ࠩࡶࡸࡴࡸࡡࡨࡧࠪࡧ")):
		os.system(l111lll1 (u"ࠪࡸࡪࡸ࡭ࡶࡺ࠰ࡷࡪࡺࡵࡱ࠯ࡶࡸࡴࡸࡡࡨࡧࠪࡨ"))
	if os.path.isdir(l1l1ll + l111lll1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩࠬࡩ")):
		print(Fore.GREEN + l111lll1 (u"ࠬࠦ࠾ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡆࡵࡷࡥࡧࡲࡩࡴࡪࡨࡨ࡙ࠥࡴࡰࡴࡤ࡫ࡪ࠴ࠧࡪ"))
		if not os.path.isdir(l1l1ll + l111lll1 (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴࠧ࡫")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠨ࡬"))
		if not os.path.isdir(l1l1ll + l111lll1 (u"ࠨࡵࡷࡳࡷࡧࡧࡦ࠱ࡶ࡬ࡦࡸࡥࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯࠱ࡎࡩࡾࡽ࡯ࡳࡦࡶࠫ࡭")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠩࡶࡸࡴࡸࡡࡨࡧ࠲ࡷ࡭ࡧࡲࡦࡦ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬ࡮"))
		if not os.path.isdir(l1l1ll + l111lll1 (u"ࠪࡷࡹࡵࡲࡢࡩࡨ࠳ࡸ࡮ࡡࡳࡧࡧ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡈࡵ࡭ࡣࡱࡏ࡭ࡸࡺࡳࠨ࡯")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡉ࡯࡮ࡤࡲࡐ࡮ࡹࡴࡴࠩࡰ"))
		print(Fore.GREEN + l111lll1 (u"ࠬࠦ࠾ࠡࡋࡱࡸࡪࡸ࡮ࡢ࡮ࠣࡗࡹࡵࡲࡢࡩࡨ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺࠢࡆࡶࡪࡧࡴࡦࡦࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠪࡱ"))
		print(Fore.GREEN + l111lll1 (u"࠭ࠠ࠿ࠢࡕࡩࡸࡺࡡࡳࡶ࡬ࡲ࡬࠴ࠧࡲ"))
		time.sleep(1.5)
		os.system(l111lll1 (u"ࠧࡤ࡮ࡨࡥࡷ࠭ࡳ"))
		open(l111lll1 (u"ࠨ࠰ࡩ࡭ࡷࡹࡴࠨࡴ"), l111lll1 (u"ࠩࡺࠫࡵ")).write(l111lll1 (u"ࠪࡊࡦࡲࡳࡦࠩࡶ"))
def l11l1(l1l111ll):
	if l1l111ll != l111lll1 (u"ࠫࡦ࡜ࡡࡅࡃࠣ࡯ࡊࡊࡡࡗࡴࡄࠫࡷ"):
		l1l111ll = float(l1l111ll)
		l1lll1l1 = float(requests.get(l111lll1 (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡲࡢࡹ࠱࡫࡮ࡺࡨࡶࡤࡸࡷࡪࡸࡣࡰࡰࡷࡩࡳࡺ࠮ࡤࡱࡰ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡲࡧࡳࡵࡧࡵ࠳࠳ࡼࡥࡳࡵ࡬ࡳࡳ࠭ࡸ")).text.strip())
		if l1lll1l1 > l1l111ll:
			l1l1l11l = str(requests.get(l111lll1 (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡳࡣࡺ࠲࡬࡯ࡴࡩࡷࡥࡹࡸ࡫ࡲࡤࡱࡱࡸࡪࡴࡴ࠯ࡥࡲࡱ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡳࡡࡴࡶࡨࡶ࠴࠴ࡣࡩࡣࡱ࡫ࡪࡲ࡯ࡨࠩࡹ")).text.strip())
			print(Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠧࠡࡀ࡙ࠣࡵࡪࡡࡵࡧࠣࡅࡻࡧࡩ࡭ࡣࡥࡰࡪ࠴࡜࡯ࠩࡺ"))
			time.sleep(0.7)
			l1l11111 = input(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠨࠢࡁࠤࡈ࡮ࡡ࡯ࡩࡨࡰࡴ࡭࠺ࠡ࡞ࡱࡠࡳ࠭ࡻ") + Style.DIM + l1l1l11l + Fore.YELLOW + Style.BRIGHT + l111lll1 (u"ࠩ࡟ࡲࡡࡴࠠ࠿ࠢࡇࡳࠥ࡟࡯ࡶ࡚ࠢࡥࡳࡺࠠࡵࡱ࡙ࠣࡵࡪࡡࡵࡧࠣࡒࡴࡽ࠿ࠡ࡝ࠪࡼ") + Fore.GREEN + l111lll1 (u"ࠪ࡝ࠬࡽ") + Fore.YELLOW + l111lll1 (u"ࠫ࠴࠭ࡾ") + Fore.RED + l111lll1 (u"ࠬࡔࠧࡿ") + Fore.YELLOW + l111lll1 (u"࠭࡝ࠡࠩࢀ") + Style.RESET_ALL)
			if l1l11111.lower() == l111lll1 (u"ࠧࡺࠩࢁ"):
				print(Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠨࠢࡁࠤࡎࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡗࡳࡨࡦࡺࡥ࠯ࠩࢂ"))
				os.system(l111lll1 (u"ࠩࡪ࡭ࡹࠦࡲࡦࡵࡨࡸࠥ࠳࠭ࡩࡣࡵࡨࠬࢃ"))
				os.system(l111lll1 (u"ࠪ࡫࡮ࡺࠠࡱࡷ࡯ࡰࠥࡵࡲࡪࡩ࡬ࡲࠥࡳࡡࡴࡶࡨࡶࠬࢄ"))
				time.sleep(5)
				print(Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠫࠥࡄࠠࡖࡲࡧࡥࡹ࡫ࠠࡄࡱࡰࡴࡱ࡫ࡴࡦ࠰ࠪࢅ"))
				print(Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠬࠦ࠾ࠡࡒ࡯ࡩࡦࡹࡥࠡࡔࡨࡷࡹࡧࡲࡵࠢࡷ࡬ࡪࠦࡐࡳࡱࡪࡶࡦࡳࠠࡵࡱࠣࡍࡳࡩ࡯ࡳࡲࡲࡶࡦࡺࡥࠡࡶ࡫ࡩ࡛ࠥࡰࡥࡣࡷࡩ࠳࠭ࢆ"))
		elif l1lll1l1 == l1l111ll:
			print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠨࠠ࠿ࠢ࡜ࡳࡺ࠭ࡲࡦࠢࡄࡰࡷ࡫ࡡࡥࡻࠣࡳࡳࠦࡴࡩࡧࠣࡐࡦࡺࡥࡴࡶ࡚ࠣࡪࡸࡳࡪࡱࡱ࠲ࠥࡉࡨࡦࡧࡵࡷࠦࠨࢇ"))
		elif l1lll1l1 < l1l111ll:
			l111l1l = os.getcwd()
			os.system(l111lll1 (u"ࠧࡳ࡯ࠣ࠱ࡷ࡬ࠠࠨ࢈") + l111l1l)
			os.system(l111lll1 (u"ࠨࡴࡰࠤ࠲ࡸࡦࠡ࠱ࡶࡨࡨࡧࡲࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯ࠩࢉ"))
			print(Fore.RED + Style.BRIGHT + l111lll1 (u"ࠩࠣࡂࠥࡓ࡯ࡥ࡫ࡩ࡭ࡨࡧࡴࡪࡱࡱࡷࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡌࡩ࡭ࡧࡶࡽࡸࡺࡥ࡮ࠢࡋࡥࡻ࡫ࠠࡃࡧࡨࡲࠥࡊࡥࡵࡧࡦࡸࡪࡪ࠮ࠡࡃ࡯ࡰࠥࡊࡡࡵࡣࠣ࡬ࡦࡹࠠࡃࡧࡨࡲࠥࡋࡲࡢࡵࡨࡨࠥࡧࡳࠡࡣࡱࠤࡆࡴࡴࡪࠢࡓ࡭ࡷࡧࡣࡺࠢࡐࡩࡦࡹࡵࡳࡧ࠱ࠫࢊ"))
			exit()
	else:
		print(l111lll1 (u"ࠪࠤࡃࠦࡄࡦࡸࡨࡰࡴࡶࡥࡳࠢࡈࡼࡪࡳࡰࡵ࡫ࡲࡲ࠳࠭ࢋ"))
def l1llll1():
	if not os.path.isdir(l1l1ll + l111lll1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩࠬࢌ")):
		os.system(l111lll1 (u"ࠬࡺࡥࡳ࡯ࡸࡼ࠲ࡹࡥࡵࡷࡳ࠱ࡸࡺ࡯ࡳࡣࡪࡩࠬࢍ"))
	if os.path.isdir(l1l1ll + l111lll1 (u"࠭ࡳࡵࡱࡵࡥ࡬࡫ࠧࢎ")):
		if not os.path.isdir(l1l1ll + l111lll1 (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮ࠨ࢏")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠨࡵࡷࡳࡷࡧࡧࡦ࠱ࡶ࡬ࡦࡸࡥࡥ࠱࡙ࡳࡱࡪࡥ࡮ࡱࡵࡸࡈࡵ࡭࡮ࡷࡱ࡭ࡹࡿ࠯ࡄࡱࡰࡦࡴࡍࡥ࡯ࠩ࢐"))
		if not os.path.isdir(l1l1ll + l111lll1 (u"ࠩࡶࡸࡴࡸࡡࡨࡧ࠲ࡷ࡭ࡧࡲࡦࡦ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬ࢑")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠪࡷࡹࡵࡲࡢࡩࡨ࠳ࡸ࡮ࡡࡳࡧࡧ࠳࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡃࡰ࡯ࡰࡹࡳ࡯ࡴࡺ࠱ࡆࡳࡲࡨ࡯ࡈࡧࡱ࠳ࡐ࡫ࡹࡸࡱࡵࡨࡸ࠭࢒"))
		if not os.path.isdir(l1l1ll + l111lll1 (u"ࠫࡸࡺ࡯ࡳࡣࡪࡩ࠴ࡹࡨࡢࡴࡨࡨ࠴࡜࡯࡭ࡦࡨࡱࡴࡸࡴࡄࡱࡰࡱࡺࡴࡩࡵࡻ࠲ࡇࡴࡳࡢࡰࡉࡨࡲ࠴ࡉ࡯࡮ࡤࡲࡐ࡮ࡹࡴࡴࠩ࢓")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠬࡹࡴࡰࡴࡤ࡫ࡪ࠵ࡳࡩࡣࡵࡩࡩ࠵ࡖࡰ࡮ࡧࡩࡲࡵࡲࡵࡅࡲࡱࡲࡻ࡮ࡪࡶࡼ࠳ࡈࡵ࡭ࡣࡱࡊࡩࡳ࠵ࡃࡰ࡯ࡥࡳࡑ࡯ࡳࡵࡵࠪ࢔"))
		if not os.path.isdir(l1l1ll + l111lll1 (u"࠭ࡳࡵࡱࡵࡥ࡬࡫࠯ࡴࡪࡤࡶࡪࡪ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴ࠯ࡑࡴࡲࡼࡾࡒࡩࡴࡶࡶࠫ࢕")):
			os.makedirs(l1l1ll + l111lll1 (u"ࠧࡴࡶࡲࡶࡦ࡭ࡥ࠰ࡵ࡫ࡥࡷ࡫ࡤ࠰ࡘࡲࡰࡩ࡫࡭ࡰࡴࡷࡇࡴࡳ࡭ࡶࡰ࡬ࡸࡾ࠵ࡃࡰ࡯ࡥࡳࡌ࡫࡮࠰ࡒࡵࡳࡽࡿࡌࡪࡵࡷࡷࠬ࢖"))
def l1l11l11():
	l1lllll = l1l1111 (u"ࠨࡣࡋࡖ࠵ࡩࡈࡎ࠸ࡏࡽ࠾ࡽ࡙࡙ࡐ࠳࡞࡜ࡐࡰࡣ࡫࠸࡮ࡧ࠸࠰ࡷࡥࡰࡊ࠸ࡒ࠲ࡓࡇࡐ࡜ࡓࡗࡔࡆࡌ࠷ࡇ࡬ࡃ࠽ࠨࢗ") #l1l1lll://l1lllll.l1llll.l1l111/l1lll11/9feb808d806d23622be56559c4bc8334/raw/l11ll1ll
	print(Fore.RED + Style.BRIGHT + l111lll1 (u"ࠩࠣࡂࠥࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠥࡘࡥࡲࡷ࡬ࡶࡪࡪ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡘࡨࡶ࡮࡬ࡹ࡛ࠡࡲࡹࡷࠦࡃࡳࡧࡧࡩࡳࡺࡩࡢ࡮ࡶ࠲ࠬ࢘"))
	uname = input(Fore.GREEN + Style.DIM + l111lll1 (u"ࠪࠤࡃࠦࡕࡴࡧࡵࡲࡦࡳࡥࠡ࠼࢙ࠣࠫ") + Fore.RESET + Style.DIM)
	pwd = hashlib.sha256(getpass.getpass(Fore.GREEN + Style.DIM + l111lll1 (u"ࠫࠥࡄࠠࡑࡣࡶࡷࡼࡵࡲࡥࠢ࠽ࠤ࢚ࠬ") + Fore.RESET + Style.DIM).encode(l111lll1 (u"ࠬࡧࡳࡤ࡫࡬࢛ࠫ"))).hexdigest()
	l11l11l1 = requests.get(base64.b64decode(l1lllll).decode(l111lll1 (u"࠭ࡡࡴࡥ࡬࡭ࠬ࢜"))).text
	for x in l11l11l1.split(l111lll1 (u"ࠧ࡝ࡰࠪ࢝")):
		if uname in x:
			if pwd == x.split(l111lll1 (u"ࠣ࠼ࠥ࢞"))[1]:
				print(Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠩࠣࡂࠥࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࠰ࠪ࢟"))
				return
	print(Fore.RED + Style.BRIGHT + l111lll1 (u"ࠪࠤࡃࠦࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳࠦࡕ࡯ࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰ࠳ࠦࡐࡳࡱࡪࡶࡦࡳࠠࡕࡧࡵࡱ࡮ࡴࡡࡵࡧࡧ࠲ࠬࢠ"))
	print(Fore.RED + Style.DIM + l111lll1 (u"ࠫࠥࡄࠠࡄࡱࡰࡦࡴࡹࠠࡄࡱ࡯ࡰࡪࡩࡴࡦࡦࠣ࠾ࠥ࠶ࠧࢡ"))
	os.system(l111lll1 (u"ࠬࡱࡩ࡭࡮ࠣࠫࢢ") + str(os.getpid()))
	exit()
try:
	l1l11l11()
	l1l111ll = open(l111lll1 (u"࠭࠮ࡷࡧࡵࡷ࡮ࡵ࡮ࠨࢣ"), l111lll1 (u"ࠧࡳࠩࢤ")).read().strip()
	l1llll1()
	if l11lllll():
		l1l1ll11()
	print(Fore.CYAN + Style.NORMAL + l111lll1 (u"ࠨ࡞ࡱࡠࡹࡢࡴࠡࡡࡢࡣࡤࡥ࡟ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡤࠦࠠࠡࠢࠣࠤࠥࠦ࡟ࡠࡡࡢࡣࡤࡢ࡮࡝ࡶ࡟ࡸࢁࠦࠠࠡࠢࠣࠤࢁࡥ࡟ࡠࠢࡢࡣࡤࡥ࡟ࡽࠢࡿࡣࡤࠦ࡟ࡠࡡࡿࠤࠥࠦ࡟ࡠࡡࡿࡣࡤࡥࠠࡠࡡࡢࡠࡳࡢࡴ࡝ࡶࡿࠤࠥࠦ࠭࠮࠯ࡿࠤ࠳ࠦࡼ࡝ࡶࠣࢀࠥ࠴ࠠࠡࡾࠣ࠲ࠥࢂࠠࠡࡾࠣࠤࠥࢂࠠ࠮ࡡࡿࠤࠥࠦࡼ࡝ࡰ࡟ࡸࡡࡺࡼࡠࡡࡢࡣࡤࡥࡼࡠࡡࡢࢀࡤࢂ࡟ࡽࡡࡿࡣࡤࡥ࡟ࡽࡡࡢࡣࢁࡥ࡟ࡠࡡࡢࡣࢁࡥ࡟ࡠࡾࡢࢀࡤࢂ࡜࡯࡞ࡱࡠࡹࡢࡴ࡝ࡶ࡟ࡸࡡࡺ࡜ࡵ࡞ࡷࠫࢥ") + Style.DIM + l111lll1 (u"ࠩ࡟ࡸࠥࡼࠧࢦ") + l1l111ll + l111lll1 (u"ࠪࠤࡧࡿࠠࡁࡪࡨࡻ࡭ࡵ࡭ࡶࡵࡷࡲ࠵ࡺࡢࡦࡰࡤࡱࡪࡪ࡜࡯࡞ࡱࡠࡳࠦ࠾ࠡࡉ࡬ࡸ࡭ࡻࡢ࠻ࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲࡫࡮ࡺࡨࡶࡤ࠱ࡧࡴࡳ࠯ࡗࡱ࡯ࡨࡪࡳ࡯ࡳࡶࡆࡳࡲࡳࡵ࡯࡫ࡷࡽ࠴ࡉ࡯࡮ࡤࡲࡋࡪࡴ࡜࡯࡞ࡷࠫࢧ"))
	time.sleep(2)
	print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠫࠥࡄࠠࡷࠩࢨ") + l1l111ll + l111lll1 (u"ࠬࠦࡄࡦࡸࡨࡰࡴࡶࡥࡥࠢࡥࡽࠥ࠭ࢩ") + Fore.GREEN + Style.BRIGHT + l111lll1 (u"࠭ࡀࡩࡧࡺ࡬ࡴࡳࡵࡴࡶࡱ࠴ࡹࡨࡥ࡯ࡣࡰࡩࡩ࠭ࢪ") + Style.RESET_ALL + Fore.GREEN + Style.DIM + l111lll1 (u"ࠧࠡࠪࡗࡩࡱ࡫ࡧࡳࡣࡰ࠭࠳࠭ࢫ"))
	time.sleep(1)
	print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠨࠢࡁࠤࡋࡵࡲࠡࡗࡳࡨࡦࡺࡥࡴࠢࠩࠤࡒࡵࡲࡦ࠮ࠣࡇ࡭࡫ࡣ࡬ࠢࡲࡹࡹ࠭ࢬ") + Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠩࠣࡄ࡛ࡵ࡬ࡥࡧࡰࡳࡷࡺࡎࡦࡹࡶࡰࡪࡺࡴࡦࡴࠪࢭ") + Style.RESET_ALL + Fore.GREEN + Style.DIM + l111lll1 (u"ࠪࠤ࡚࠭ࡥ࡭ࡧࡪࡶࡦࡳࠩ࠯ࠩࢮ"))
	time.sleep(2)
	l11l1(l1l111ll)
	l11llll1 = input(Fore.GREEN + Style.DIM + l111lll1 (u"ࠫࠥࡄࠠࡑࡴࡨࡷࡸࠦࡅ࡯ࡶࡨࡶࠥࡺ࡯ࠡࡅࡲࡲࡹ࡯࡮ࡶࡧ࠱ࠫࢯ") + Style.RESET_ALL)
	print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠬࡢ࡮ࠡࡀࠣࡐࡴࡧࡤࡪࡰࡪࠤࡐ࡫ࡹࡸࡱࡵࡨࡸ࠴࡜࡯ࠢࡁࠤࡕࡲࡥࡢࡵࡨࠤࡒࡵࡶࡦࠢࡷ࡬ࡪࠦࡋࡦࡻࡺࡳࡷࡪࡳࠡࡈ࡬ࡰࡪࠦࡴࡰࠩࢰ") + Style.BRIGHT + l111lll1 (u"࠭ࠠࡊࡰࡷࡩࡷࡴࡡ࡭ࠢࡖࡸࡴࡸࡡࡨࡧ࠲࡚ࡴࡲࡤࡦ࡯ࡲࡶࡹࡉ࡯࡮࡯ࡸࡲ࡮ࡺࡹ࠰ࡅࡲࡱࡧࡵࡇࡦࡰ࠲ࡏࡪࡿࡷࡰࡴࡧࡷࠬࢱ"))
	time.sleep(4)
	l11llll = l111lll1 (u"ࠧࠨࢲ")
	l11ll1l1 = []
	while 1:
		try:
			l1l = SelectMenu()
			l1ll1l1 = os.listdir(l1l111l1 + l111lll1 (u"ࠨࡍࡨࡽࡼࡵࡲࡥࡵࠪࢳ"))
			l11l1l1l = {}
			l11ll1l = []
			for file in l1ll1l1:
				if os.path.isfile(l1l111l1 + l111lll1 (u"ࠩࡎࡩࡾࡽ࡯ࡳࡦࡶ࠳ࠬࢴ") + file):
					l1l11l = {l111lll1 (u"ࠪࡲࡦࡳࡥࠨࢵ"):file,
					 l111lll1 (u"ࠫࡵࡧࡴࡩࠩࢶ"):l1l111l1 + l111lll1 (u"ࠬࡑࡥࡺࡹࡲࡶࡩࡹ࠯ࠨࢷ") + file}
					l11l1l1l[file] = l1l11l
					l11ll1l.append(l1l11l[l111lll1 (u"࠭࡮ࡢ࡯ࡨࠫࢸ")])
			l11ll1l.append(l111lll1 (u"ࠧࡓࡧࡩࡶࡪࡹࡨࠡࡈ࡬ࡰࡪࠦࡌࡪࡵࡷࠫࢹ"))
			l11ll1l.append(l111lll1 (u"ࠨࡇࡱࡸࡪࡸࠠࡌࡧࡼࡻࡴࡸࡤࡴࠢࡐࡥࡳࡻࡡ࡭࡮ࡼࠫࢺ"))
			l1l.add_choices(l11ll1l)
			l11llll = l1l.select(l111lll1 (u"ࠩࠣࡂࠥࡖ࡬ࡦࡣࡶࡩ࡙ࠥࡥ࡭ࡧࡦࡸࠥࡺࡨࡦࠢࡇࡩࡸ࡯ࡲࡦࡦࠣࡊ࡮ࡲࡥ࠯ࠩࢻ"))
			if l11llll == l111lll1 (u"ࠪࡖࡪ࡬ࡲࡦࡵ࡫ࠤࡋ࡯࡬ࡦࠢࡏ࡭ࡸࡺࠧࢼ"):
				raise l11l1ll
			else:
				if l11llll == l111lll1 (u"ࠫࡊࡴࡴࡦࡴࠣࡏࡪࡿࡷࡰࡴࡧࡷࠥࡓࡡ࡯ࡷࡤࡰࡱࡿࠧࢽ"):
					raise l111ll1
				print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠬࠦ࠾ࠡࡎࡲࡥࡩ࡯࡮ࡨࠢࡎࡩࡾࡽ࡯ࡳࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡉ࡭ࡱ࡫ࠠ࠻ࠢࠪࢾ") + Style.NORMAL + l11llll)
				time.sleep(1)
				try:
					with open(l11l1l1l[l11llll][l111lll1 (u"࠭ࡰࡢࡶ࡫ࠫࢿ")], l111lll1 (u"ࠧࡳࠩࣀ")) as key_file:
						l1l1 = key_file.readlines()
						for x in l1l1:
							l11ll1l1.append(x.strip())
						if l11ll1l1 == []:
							raise l1l1l1ll
				except l1l1l1ll:
					print(Fore.RED + Style.NORMAL + l111lll1 (u"ࠨࠢࡁࠤࡋ࡯࡬ࡦࠢ࡬ࡷࠥࡋ࡭ࡱࡶࡼ࠲ࠥ࠭ࣁ") + Style.RESET_ALL)
					continue
			break
		except l11l1ll:
			print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠩࠣࡂࠥࡘࡥࡧࡴࡨࡷ࡭࡯࡮ࡨࠢࡉ࡭ࡱ࡫ࠠࡍ࡫ࡶࡸ࠳࠭ࣂ"))
			time.sleep(1)
			continue
		except l111ll1:
			try:
				l11ll11 = input(Fore.GREEN + Style.DIM + l111lll1 (u"ࠪࠤࡃࠦࡅ࡯ࡶࡨࡶࠥࡑࡥࡺࡹࡲࡶࡩࡹࠠࡔࡧࡳࡩࡷࡧࡴࡦࡦࠣࡦࡾࠦࡃࡰ࡯ࡰࡥࡸࠦࠨ࠭ࠫࠣ࠾ࠥ࠭ࣃ") + Fore.RESET + Style.DIM)
				l11ll11 = l11ll11.strip()
				l11ll11 = l11ll11.strip(l111lll1 (u"ࠫ࠱࠭ࣄ"))
				if l11ll11 == l111lll1 (u"ࠬ࠭ࣅ") or l11ll11 == None:
					raise l1l1l1ll
				else:
					l1l1 = l11ll11.split(l111lll1 (u"࠭ࠬࠨࣆ"))
					print(Style.RESET_ALL)
					for x in l1l1:
						l11ll1l1.append(x.strip())
				break
			except l1l1l1ll:
				print(Fore.RED + Style.NORMAL + l111lll1 (u"ࠧࠡࡀࠣࡍࡳࡼࡡ࡭࡫ࡧࠤࡎࡴࡰࡶࡶ࠱ࠤࠬࣇ") + Style.RESET_ALL)
				continue
	#l11l1111 = l11l1l11()
	l1ll1111 = 0
	l1l11 = [l111lll1 (u"ࠣࡉࡲࡳ࡬ࡲࡥࠣࣈ")]
	l111lll1 (u"ࠤࠥࠦࠏࠏࡥ࡯ࡩ࡬ࡲࡪࡥࡣࡩࡱ࡬ࡧࡪࡹࠠ࠾ࠢ࡞ࠫࡠࠦ࡝ࠡࡉࡲࡳ࡬ࡲࡥࠨ࠮ࠣࠫࡠࠦ࡝ࠡࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬ࠲ࠠࠨࡆࡲࡲࡪ࠭࡝ࠋࠋࡺ࡬࡮ࡲࡥࠡ࠳࠽ࠎࠎࠏࡴࡳࡻ࠽ࠎࠎࠏࠉࡦࡰࡪ࡭ࡳ࡫࡟࡮ࡧࡱࡹࠥࡃࠠࡔࡧ࡯ࡩࡨࡺࡍࡦࡰࡸࠬ࠮ࠐࠉࠊࠋࡨࡲ࡬࡯࡮ࡦࡡࡰࡩࡳࡻ࠮ࡢࡦࡧࡣࡨ࡮࡯ࡪࡥࡨࡷ࠭࡫࡮ࡨ࡫ࡱࡩࡤࡩࡨࡰ࡫ࡦࡩࡸ࠯ࠊࠊࠋࠌࡩࡳ࡭ࡩ࡯ࡧࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࠽ࠡࡧࡱ࡫࡮ࡴࡥࡠ࡯ࡨࡲࡺ࠴ࡳࡦ࡮ࡨࡧࡹ࠮ࠧࠡࡀࠣࡗࡪࡲࡥࡤࡶࠣࡗࡪࡧࡲࡤࡪࠣࡉࡳ࡭ࡩ࡯ࡧࡶࠤࡹࡵࠠࡖࡶ࡬ࡰ࡮ࡹࡥࠡࠪࡐࡹࡱࡺࡩࡱ࡮ࡨࠤࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡳࠡࡣࡵࡩࠥࡇ࡬࡭ࡱࡺࡩࡩ࠯ࠠ࠻ࠢࠪ࠭ࠏࠏࠉࠊ࡫ࡩࠤࡪࡴࡧࡪࡰࡨࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࠾࠿ࠣࠫࡠࠦ࡝ࠡࡉࡲࡳ࡬ࡲࡥࠨ࠼ࠍࠍࠎࠏࠉࡦࡰࡪ࡭ࡳ࡫࡟ࡤࡪࡲ࡭ࡨ࡫ࡳ࡜࠲ࡠࠤࡂࠦࠧ࡜ࠥࡠࠤࡌࡵ࡯ࡨ࡮ࡨࠫࠏࠏࠉࠊࠋࡶࡩࡱ࡫ࡣࡵࡧࡧࡣࡪࡴࡧࡪࡰࡨࡷ࠳ࡧࡰࡱࡧࡱࡨ࠭࠭ࡇࡰࡱࡪࡰࡪ࠭ࠩࠋࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࡪࡨࠣࡩࡳ࡭ࡩ࡯ࡧࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࠽࠾ࠢࠪ࡟ࠥࡣࠠࡅࡷࡦ࡯ࡉࡻࡣ࡬ࡉࡲࠫ࠿ࠐࠉࠊࠋࠌࠍࡪࡴࡧࡪࡰࡨࡣࡨ࡮࡯ࡪࡥࡨࡷࡠ࠷࡝ࠡ࠿ࠣࠫࡠࠩ࡝ࠡࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬࠐࠉࠊࠋࠌࠍࡸ࡫࡬ࡦࡥࡷࡩࡩࡥࡥ࡯ࡩ࡬ࡲࡪࡹ࠮ࡢࡲࡳࡩࡳࡪࠨࠨࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬ࠯ࠊࠊࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࠊ࡫ࡩࠤࡪࡴࡧࡪࡰࡨࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࠾࠿ࠣࠫࡠࠩ࡝ࠡࡉࡲࡳ࡬ࡲࡥࠨ࠼ࠍࠍࠎࠏࠉࠊࠋࡨࡲ࡬࡯࡮ࡦࡡࡦ࡬ࡴ࡯ࡣࡦࡵ࡞࠴ࡢࠦ࠽ࠡࠩ࡞ࠤࡢࠦࡇࡰࡱࡪࡰࡪ࠭ࠊࠊࠋࠌࠍࠎࠏࡳࡦ࡮ࡨࡧࡹ࡫ࡤࡠࡧࡱ࡫࡮ࡴࡥࡴ࠰ࡵࡩࡲࡵࡶࡦࠪࠪࡋࡴࡵࡧ࡭ࡧࠪ࠭ࠏࠏࠉࠊࠋࠌࡩࡱࡹࡥ࠻ࠌࠌࠍࠎࠏࠉࠊ࡫ࡩࠤࡪࡴࡧࡪࡰࡨࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࠾࠿ࠣࠫࡠࠩ࡝ࠡࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࠬࡀࠊࠊࠋࠌࠍࠎࠏࠉࡦࡰࡪ࡭ࡳ࡫࡟ࡤࡪࡲ࡭ࡨ࡫ࡳ࡜࠳ࡠࠤࡂࠦࠧ࡜ࠢࡠࠤࡉࡻࡣ࡬ࡆࡸࡧࡰࡍ࡯ࠨࠌࠌࠍࠎࠏࠉࠊࠋࡶࡩࡱ࡫ࡣࡵࡧࡧࡣࡪࡴࡧࡪࡰࡨࡷ࠳ࡸࡥ࡮ࡱࡹࡩ࠭࠭ࡄࡶࡥ࡮ࡈࡺࡩ࡫ࡈࡱࠪ࠭ࠏࠏࠉࠊࠋࠌࠍࡪࡲࡳࡦ࠼ࠍࠍࠎࠏࠉࠊࠋࠌ࡭࡫ࠦࡥ࡯ࡩ࡬ࡲࡪࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡀࡁࠥ࠭ࡄࡰࡰࡨࠫ࠿ࠐࠉࠊࠋࠌࠍࠎࠏࠉࡪࡨࠣࡷࡪࡲࡥࡤࡶࡨࡨࡤ࡫࡮ࡨ࡫ࡱࡩࡸࠦࠡ࠾ࠢ࡞ࡡ࠿ࠐࠉࠊࠋࠌࠍࠎࠏࠉࠊࡤࡵࡩࡦࡱࠊࠊࠋࠌࠍࠎࠏࠉࠊࡧ࡯ࡷࡪࡀࠊࠊࠋࠌࠍࠎࠏࠉࠊࠋࡵࡥ࡮ࡹࡥࠡࡇࡰࡴࡹࡿࡌࡪࡵࡷࡉࡷࡸ࡯ࡳࠌࠌࠍࡪࡾࡣࡦࡲࡷࠤࡊࡳࡰࡵࡻࡏ࡭ࡸࡺࡅࡳࡴࡲࡶ࠿ࠐࠉࠊࠋࡳࡶ࡮ࡴࡴࠩࡈࡲࡶࡪ࠴ࡒࡆࡆࠣ࠯࡙ࠥࡴࡺ࡮ࡨ࠲ࡓࡕࡒࡎࡃࡏࠤ࠰ࠦࠧࠡࡀࠣࡍࡳࡼࡡ࡭࡫ࡧࠤࡎࡴࡰࡶࡶ࠱ࠤࠬࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡓࡇࡖࡉ࡙ࡥࡁࡍࡎࠬࠎࠎࠏࠉࡤࡱࡱࡸ࡮ࡴࡵࡦࠌࠥࠦࠧࣉ")
	l1ll1l1l = {}
	l1l1lll1 = {l111lll1 (u"ࠪࡋࡴࡵࡧ࡭ࡧࠪ࣊"):[
	  l111lll1 (u"ࠫࡆࡴࡹࠡࡖ࡬ࡱࡪ࠭࣋"), l111lll1 (u"ࠬࡖࡡࡴࡶࠣࡌࡴࡻࡲࠨ࣌"), l111lll1 (u"࠭ࡐࡢࡵࡷࠤ࠷࠺ࠠࡉࡱࡸࡶࡸ࠭࣍"), l111lll1 (u"ࠧࡑࡣࡶࡸࠥ࡝ࡥࡦ࡭ࠪ࣎"), l111lll1 (u"ࠨࡒࡤࡷࡹࠦࡍࡰࡰࡷ࡬࣏ࠬ"), l111lll1 (u"ࠩࡓࡥࡸࡺ࡚ࠠࡧࡤࡶ࣐ࠬ")],
	 l111lll1 (u"ࠪࡈࡺࡩ࡫ࡅࡷࡦ࡯ࡌࡵ࣑ࠧ"):[l111lll1 (u"ࠫࡆࡴࡹࠡࡖ࡬ࡱࡪ࣒࠭")]}
	for l111l1 in l1l11:
		l1111l = SelectMenu()
		l1111l.add_choices(l1l1lll1[l111l1])
		l1l1l1l1 = l1111l.select(l111lll1 (u"ࠬࠦ࠾ࠡ࡝࣓ࠪ") + l111l1 + l111lll1 (u"࠭࡝ࠡࡈ࡬ࡲࡩࠦࡒࡦࡵࡸࡰࡹࡹࠠࡰࡨࠣ࠾ࠥ࠭ࣔ"))
		if l1l1l1l1 == l111lll1 (u"ࠧࡂࡰࡼࠤ࡙࡯࡭ࡦࠩࣕ"):
			l1ll1l1l[l111l1] = l111lll1 (u"ࠨࡼࠪࣖ")
		elif l1l1l1l1 == l111lll1 (u"ࠩࡓࡥࡸࡺࠠࡉࡱࡸࡶࠬࣗ"):
			l1ll1l1l[l111l1] = l111lll1 (u"ࠪ࡬ࠬࣘ")
		elif l1l1l1l1 == l111lll1 (u"ࠫࡕࡧࡳࡵࠢ࠵࠸ࠥࡎ࡯ࡶࡴࡶࠫࣙ"):
			l1ll1l1l[l111l1] = l111lll1 (u"ࠬࡪࠧࣚ")
		elif l1l1l1l1 == l111lll1 (u"࠭ࡐࡢࡵࡷࠤ࡜࡫ࡥ࡬ࠩࣛ"):
			l1ll1l1l[l111l1] = l111lll1 (u"ࠧࡸࠩࣜ")
		elif l1l1l1l1 == l111lll1 (u"ࠨࡒࡤࡷࡹࠦࡍࡰࡰࡷ࡬ࠬࣝ"):
			l1ll1l1l[l111l1] = l111lll1 (u"ࠩࡰࠫࣞ")
		elif l1l1l1l1 == l111lll1 (u"ࠪࡔࡦࡹࡴ࡛ࠡࡨࡥࡷ࠭ࣟ"):
			l1ll1l1l[l111l1] = l111lll1 (u"ࠫࡾ࠭࣠")
		else:
			l1ll1l1l[l111l1] = l111lll1 (u"ࠬࢀࠧ࣡")
		print(Fore.GREEN + Style.DIM + l111lll1 (u"࠭ࠠ࠿ࠢࡉ࡭ࡳࡪࡩ࡯ࡩࠣࡖࡪࡹࡵ࡭ࡶࡶࠤࡴ࡬ࠠࠨ࣢") + Style.NORMAL + l1l1l1l1 + Style.DIM + l111lll1 (u"ࠧࠡࡨࡲࡶࣣࠥ࠭") + Fore.GREEN + Style.NORMAL + l111l1 + Fore.GREEN + Style.DIM + l111lll1 (u"ࠨ࠰ࠪࣤ"))
	while True:
		try:
			l1llll11 = input(Fore.GREEN + Style.DIM + l111lll1 (u"ࠩࠣࡂࠥࡋ࡮ࡵࡧࡵࠤࡋ࡯࡬ࡦࠢࡑࡥࡲ࡫ࠠࡵࡱࠣࡗࡹࡵࡲࡦࠢࡆࡳࡲࡨ࡯ࠡࡎ࡬ࡷࡹࠦ࠺ࠡࠩࣥ") + Style.RESET_ALL + Style.DIM)
			if l1llll11 == l111lll1 (u"ࣦࠪࠫ") or l1llll11 == None:
				raise l1l1l1ll
			else:
				if l111lll1 (u"ࠫ࠳ࡺࡸࡵࠩࣧ") not in l1llll11:
					l1llll11 = l1llll11.strip() + l111lll1 (u"ࠬ࠴ࡴࡹࡶࠪࣨ")
				l1ll1l11 = l1l111l1 + l111lll1 (u"࠭ࡃࡰ࡯ࡥࡳࡑ࡯ࡳࡵࡵ࠲ࣩࠫ") + l1llll11
				if os.path.isfile(l1ll1l11):
					raise l111111
			break
		except l111111:
			l111 = input(Fore.RED + Style.DIM + l111lll1 (u"ࠧࠡࡀࠣࡊ࡮ࡲࡥࠡࡃ࡯ࡶࡪࡧࡤࡺࠢࡈࡼ࡮ࡹࡴࡴ࠰ࠣࡓࡻ࡫ࡲࡸࡴ࡬ࡸࡪࡅࠠ࡜ࠢࠪ࣪") + Fore.GREEN + Style.DIM + l111lll1 (u"ࠨࡻࡨࡷࠬ࣫") + Fore.RED + Style.DIM + l111lll1 (u"ࠩ࠲ࡲࡴࠦ࡝ࠡ࠼ࠣࠫ࣬") + Style.RESET_ALL + Style.DIM)
			if l111.lower() == l111lll1 (u"ࠪࡽࡪࡹ࣭ࠧ"):
				print(Fore.RED + Style.DIM + l111lll1 (u"ࠫࠥࡄࠠࡐࡸࡨࡶࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡌࡩ࡭ࡧ࠱࣮ࠫ"))
				os.system(l111lll1 (u"ࠬࡸ࡭࣯ࠡࠩ") + l1ll1l11)
				break
			else:
				continue
		except l1l1l1ll:
			print(Fore.RED + Style.NORMAL + l111lll1 (u"࠭ࠠ࠿ࠢࡌࡲࡻࡧ࡬ࡪࡦࠣࡍࡳࡶࡵࡵ࠰ࣰࠣࠫ") + Style.RESET_ALL)
			continue
	for ll in l11ll1l1:
		try:
			for l111l1 in l1l11:
				if l111l1 == l111lll1 (u"ࠧࡈࡱࡲ࡫ࡱ࡫ࣱࠧ"):
					print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠨࠢࡁࠤࡠࡍ࡯ࡰࡩ࡯ࡩࡢࠦࡓࡤࡴࡤࡴ࡮ࡴࡧࠡࡍࡨࡽࡼࡵࡲࡥࠢ࠽ࠤࣲࠬ") + Style.BRIGHT + str(ll) + Style.RESET_ALL)
					time.sleep(1)
					l11 = l11l1lll(l111lll1 (u"ࠩࡶ࡭ࡹ࡫࠺ࡱࡣࡶࡸࡪࡨࡩ࡯࠰ࡦࡳࡲࠦࡩ࡯ࡶࡨࡼࡹࡀࠧࣳ") + ll)
					l1ll1 = threading.Thread(name=l111lll1 (u"ࠪࡷࡨࡸࡡࡱ࡫ࡱ࡫ࡤࡺࡨࡳࡧࡤࡨࠬࣴ"), target=(l11.l1ll11l1), args=(l1ll1l1l[l111l1]))
					l1ll1.start()
					while l1ll1.is_alive():
						if not l11.l1ll1ll:
							l11.l1l1ll1l()
					print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠫࡡࡴࠠ࠿ࠢ࡞ࡋࡴࡵࡧ࡭ࡧࡠࠤࡘ࡫ࡡࡳࡥ࡫ࠤࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠮ࠡࡖࡲࡸࡦࡲࠠࡖࡔࡏࡷࠥࡌ࡯ࡶࡰࡧࠤ࠿ࠦࠧࣵ") + Style.NORMAL + str(len(l1l1llll)))
					l111lll1 (u"ࠧࠨࠢࠋࠋࠌࠍࠎࠏࡩࡧࠢࡨࡲ࡬࡯࡮ࡦࠢࡀࡁࠥ࠭ࡄࡶࡥ࡮ࡈࡺࡩ࡫ࡈࡱࠪ࠾ࠏࠏࠉࠊࠋࠌࡴࡷ࡯࡮ࡵࠪࡉࡳࡷ࡫࠮ࡈࡔࡈࡉࡓࠦࠫࠡࡕࡷࡽࡱ࡫࠮ࡅࡋࡐࠤ࠰ࠦࠧࠡࡀࠣ࡟ࡉࡻࡣ࡬ࡆࡸࡧࡰࡍ࡯࡞ࠢࡖࡧࡷࡧࡰࡪࡰࡪࠤࡐ࡫ࡹࡸࡱࡵࡨࠥࡀࠠࠨࠢ࠮ࠤࡘࡺࡹ࡭ࡧ࠱ࡆࡗࡏࡇࡉࡖࠣ࠯ࠥࡹࡴࡳࠪ࡮ࡩࡾࡽ࡯ࡳࡦࠬࠤ࠰ࠦࡓࡵࡻ࡯ࡩ࠳ࡘࡅࡔࡇࡗࡣࡆࡒࡌࠪࠌࠌࠍࠎࠏࠉࡵ࡫ࡰࡩ࠳ࡹ࡬ࡦࡧࡳࠬ࠶࠯ࠊࠊࠋࠌࠍࠎࡊࡵࡤ࡭ࡇࡹࡨࡱࡇࡰࡕࡦࡶࡦࡶࡥࡳࡑࡥ࡮ࡪࡩࡴ࠯ࡵࡨࡸࡐ࡫ࡹࡸࡱࡵࡨ࠭ࡱࡥࡺࡹࡲࡶࡩ࠯ࠊࠊࠋࠌࠍࠎࡹࡣࡳࡣࡳࡩࡤࡶࡲࡰࡥࡨࡷࡸࠦ࠽ࠡࡶ࡫ࡶࡪࡧࡤࡪࡰࡪ࠲࡙࡮ࡲࡦࡣࡧࠬࡳࡧ࡭ࡦ࠿ࠪࡷࡨࡸࡡࡱ࡫ࡱ࡫ࡤࡺࡨࡳࡧࡤࡨࠬ࠲ࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠩࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࡘࡩࡲࡢࡲࡨࡶࡔࡨࡪࡦࡥࡷ࠲ࡸࡩࡲࡢࡲࡨ࠭࠮ࠐࠉࠊࠋࠌࠍࡸࡩࡲࡢࡲࡨࡣࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡹࡴࡢࡴࡷࠬ࠮ࠐࠉࠊࠋࠌࠍࡼ࡮ࡩ࡭ࡧࠣࡷࡨࡸࡡࡱࡧࡢࡴࡷࡵࡣࡦࡵࡶ࠲࡮ࡹ࡟ࡢ࡮࡬ࡺࡪ࠮ࠩ࠻ࠌࠌࠍࠎࠏࠉࠊࡆࡸࡧࡰࡊࡵࡤ࡭ࡊࡳࡘࡩࡲࡢࡲࡨࡶࡔࡨࡪࡦࡥࡷ࠲ࡦࡴࡩ࡮ࡣࡷࡩࡩࡥ࡬ࡰࡣࡧ࡭ࡳ࡭ࠨࠪࠌࠌࠍࠎࠏࠉࠣࠤࣶࠥ")
					print(Fore.GREEN + Style.DIM + l111lll1 (u"࠭࡜࡯ࠢࡁࠤࡠࡊࡵࡤ࡭ࡇࡹࡨࡱࡇࡰ࡟ࠣࡗࡪࡧࡲࡤࡪࠣࡇࡴࡳࡰ࡭ࡧࡷࡩࡩ࠴ࠠࡕࡱࡷࡥࡱࠦࡕࡓࡎࡶࠤࡋࡵࡵ࡯ࡦࠣ࠾ࠥ࠭ࣷ") + Style.NORMAL + str(len(l1l1llll)))
		except KeyboardInterrupt:
			print(Fore.GREEN + Style.DIM + l111lll1 (u"ࠧࠡ࡞ࡱࠤࡃࠦࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡔࡨࡷࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡋࡦࡻࡺࡳࡷࡪࡳ࠯ࠩࣸ"))
			break
	print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠨࠢࡁࠤࡘࡩࡲࡢࡲ࡬ࡲ࡬ࠦࡃࡰ࡯ࡳࡰࡪࡺࡥ࠯ࣹࠢࠪ") + Fore.CYAN + Style.BRIGHT + str(len(l1l1llll)) + Fore.GREEN + Style.NORMAL + l111lll1 (u"࡙ࠩࠣࡗࡒࡳࠡࡈࡲࡹࡳࡪ࠮ࠨࣺ"))
	l1l1llll = l11l1111.l1111(l1l1llll)
	print(Fore.GREEN + Style.NORMAL + l111lll1 (u"ࠪࠤࡃࠦࡃ࡭ࡧࡤࡲ࡮ࡴࡧࠡࡗࡕࡐࡸࠦࠦࠡࡔࡨࡱࡴࡼࡩ࡯ࡩࠣࡈࡺࡶ࡬ࡪࡥࡤࡸࡪࡹ࠮ࠡࠩࣻ") + Fore.CYAN + Style.BRIGHT + str(len(l1l1llll)) + Fore.GREEN + Style.NORMAL + l111lll1 (u"࡛ࠫࠥࡒࡍࡵࠣࡖࡪࡳࡡࡪࡰ࠱ࠫࣼ"))
	l1llll1l = input(Fore.GREEN + Style.BRIGHT + l111lll1 (u"ࠬࠦ࠾ࠡࡒࡵࡩࡸࡹࠠࡆࡰࡷࡩࡷࠦࡴࡰࠢࡅࡩ࡬࡯࡮ࠡࡎࡨࡩࡨ࡮ࡩ࡯ࡩ࠱ࠫࣽ") + Style.RESET_ALL)
	l11111 = l1lll1(l1ll1l11)
	l11111.l1ll(l1l1llll)
except KeyboardInterrupt:
	try:
		l111llll = 0
		with open(l11111.filename, l111lll1 (u"࠭ࡲࠨࣾ")) as l1llllll:
			for line in l1llllll:
				l111llll = l111llll + 1
		print(Fore.RED + Style.NORMAL + l111lll1 (u"ࠧ࡝ࡰࠣࡂࠥࡇࡢࡰࡴࡷ࡭ࡳ࡭ࠠࡑࡴࡲ࡫ࡷࡧ࡭࠯ࠩࣿ"))
		print(Fore.RED + Style.DIM + l111lll1 (u"ࠨࠢࡁࠤࡈࡵ࡭ࡣࡱࡶࠤࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠ࠻ࠢࠪऀ") + str(l111llll))
		os.system(l111lll1 (u"ࠩ࡮࡭ࡱࡲࠠࠨँ") + str(os.getpid()))
	except:
		print(Fore.RED + Style.DIM + l111lll1 (u"ࠪࠤࡃࠦࡃࡰ࡯ࡥࡳࡸࠦࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢ࠽ࠤ࠵࠭ं"))
		os.system(l111lll1 (u"ࠫࡰ࡯࡬࡭ࠢࠪः") + str(os.getpid()))
		exit()