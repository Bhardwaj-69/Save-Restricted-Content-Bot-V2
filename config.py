# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27392387"))
API_HASH = getenv("API_HASH", "37ee47c18c8be62716a27335a771e7da")
BOT_TOKEN = getenv("BOT_TOKEN", "🖕🏿FuckYou.🖕🏿")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5787359348").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Bhardwaj:7vVHr6zrvpsMsU3@cluster0.p2smf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002406770624")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002197825290"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "Modijiurl.com")
AD_API = getenv("AD_API", "f2bb4074d89772fb1db2ed878a7b417d06c3e121")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", "# Netscape HTTP Cookie File
# This is a generated file! Do not edit.

# domain  include_subdomains  path  secure  expiration_date  name  value
.youtube.com	TRUE	/	TRUE	1770205221	__Secure-1PSIDCC	AKEyXzVKZqq7XjBLkQgf5bssy6G9f8vb0tfoqlXYvSeY39uD3iKwHoEriizOv_6iscXdTH61
.youtube.com	TRUE	/	TRUE	1738669721	CONSISTENCY	AKreu9vaorvq2Aul_bgs0_Cweut6tKHuexa_W3QJFEABi9m9bKM1q1LSwO_c_JbwJa_xT2WfPMusLzVnvxRoueXzQTidgEYYCcP7xLdE7ZNmeH3Lm3cxVqaytwQ
.youtube.com	TRUE	/	FALSE	1773229015	SID	g.a000tAi_eYFXaNjnRZH4eBOZrmIdCeU_6_cfmk67BKbTUjxm1BwsY7t7Mdgeo_F0V_XJCWOl5AACgYKAagSARMSFQHGX2MinceJZy3Y50WyKfCg0lSeNxoVAUF8yKob4IT0gHXD5-L4CLFgket80076
.youtube.com	TRUE	/	TRUE	1773229015	__Secure-1PAPISID	IX-B5LiPQuvfD9GV/A3cNKo89uZ2FtZN_H
.youtube.com	TRUE	/	TRUE	1773229015	SAPISID	IX-B5LiPQuvfD9GV/A3cNKo89uZ2FtZN_H
.youtube.com	TRUE	/	FALSE	1770205221	SIDCC	AKEyXzVGKMTfSw_8fsYL4lQz571Yq-rGssDXFd_6Me0_AaHXWGxcPLPtecvPFPS-PgdUQkEqdw
.youtube.com	TRUE	/	TRUE	1773229015	__Secure-3PSID	g.a000tAi_eYFXaNjnRZH4eBOZrmIdCeU_6_cfmk67BKbTUjxm1Bws0jk9hDTVQvczFhUCQiNgZQACgYKAYISARMSFQHGX2MiU0wbIM8TwH3YqLxlAYdGBxoVAUF8yKrDoArCYTM0lOU1oPnHUbJk0076
.youtube.com	TRUE	/	FALSE	1773229015	HSID	A2sZLemw1qedqP-so
.youtube.com	TRUE	/	TRUE	1770204986	__Secure-1PSIDTS	sidts-CjIBmiPuTSfHWuw8MUl0bRRMueTJVLlDxjIXrRHrghcUXvyzigo8aZ02_mQP3KimivXU9BAA
.youtube.com	TRUE	/	FALSE	1773229015	APISID	n6cg48_g3i0xmkon/AbcnTcR7Qf_XhwcMP
.youtube.com	TRUE	/	TRUE	1770204986	__Secure-3PSIDTS	sidts-CjIBmiPuTSfHWuw8MUl0bRRMueTJVLlDxjIXrRHrghcUXvyzigo8aZ02_mQP3KimivXU9BAA
.youtube.com	TRUE	/	TRUE	1754221101	VISITOR_INFO1_LIVE	ie9Ms_LoNc4
.youtube.com	TRUE	/	TRUE	1773229015	SSID	AuhBkWgC0vz5Lm0Vp
.youtube.com	TRUE	/	TRUE	1754221101	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgJA%3D%3D
.youtube.com	TRUE	/	TRUE	1773229101	PREF	tz=Asia.Calcutta
.youtube.com	TRUE	/	TRUE	1773229015	__Secure-1PSID	g.a000tAi_eYFXaNjnRZH4eBOZrmIdCeU_6_cfmk67BKbTUjxm1BwsuGuPAK9MgEQrrHcpn3D1UAACgYKAV4SARMSFQHGX2MiDIWmxcTc3eiuPYN_uFDt3xoVAUF8yKpn8ysMkG0l1evlRQTxIGlW0076
.youtube.com	TRUE	/	TRUE	1773229015	__Secure-3PAPISID	IX-B5LiPQuvfD9GV/A3cNKo89uZ2FtZN_H
.youtube.com	TRUE	/	TRUE	1754220677	__Secure-ROLLOUT_TOKEN	CJab1vyvgaXdFBD4gcDH9amLAxj4gcDH9amLAw%3D%3D
.youtube.com	TRUE	/	TRUE	1770205221	__Secure-3PSIDCC	AKEyXzVJuwzXzMk7CNuuaSlST28als2m2rBjydeEZ76TPYoJjbibwgHcc5dTg8T4XBZdFs-t
.youtube.com	TRUE	/	TRUE	1773228991	LOGIN_INFO	AFmmF2swRQIgPO0RQNmR1LYj7Ip08SDFROtDjPygbLbvouImOI7ayOACIQD-lnhAegUbu_XW71vD6nQT9XgSrX6Y14x090SNLccScw:QUQ3MjNmeGxoVGJDUllQTlE3TDVVR1cwb3lhV1JISzVaWjBIUER6U2dzcjdmc0R0WkNpb243MEZBM0dQT3VrMl81MkppUGl1WWQwd0pwQ0V3TEczTW40eWVoM0NlU2RxWUgxV05YVDBVQUhjNUF4VDFJSUNRc1NhV1B0SlRsQzJHUnJIN3hXLTVndHJUMENET2lsMXFxZlg0Q3FBMUFiWVdR
.youtube.com	TRUE	/	TRUE	0	YSC	NaHxy0i33lM
.youtube.com	TRUE	/	TRUE	1738670477	GPS	1
")
INSTA_COOKIES = getenv("INSTA_COOKIES", "# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.instagram.com	TRUE	/	TRUE	1769863755	csrftoken	QJ28ZuyDOV9cVNG7ka_6Lx
.instagram.com	TRUE	/	TRUE	1772974155	datr	ShieZx6zZeiiyBSZYUkzwGNn
.instagram.com	TRUE	/	TRUE	1769950155	ig_did	F723BB93-7DA6-4B9D-B284-BDDCA1631C63
.instagram.com	TRUE	/	TRUE	1739018958	wd	384x726
.instagram.com	TRUE	/	TRUE	1739018958	dpr	1.875
.instagram.com	TRUE	/	TRUE	1772974160	mid	Z54YSgABAAFpeC1G9bUsW1av0qZo
")
