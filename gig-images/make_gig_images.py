from playwright.sync_api import sync_playwright
import pathlib

HERE = pathlib.Path("C:/Users/Matth/web-demos/gig-images")

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{width:1280px;height:769px;overflow:hidden;font-family:'Segoe UI',-apple-system,Roboto,sans-serif;position:relative;}
.frame{background:#fff;border-radius:12px;box-shadow:0 24px 60px rgba(10,15,30,.45);overflow:hidden;}
.chrome{height:30px;background:#e9ecf2;display:flex;align-items:center;gap:6px;padding:0 12px;}
.chrome i{width:10px;height:10px;border-radius:50%;display:block;}
.chrome i:nth-child(1){background:#ff5f57}.chrome i:nth-child(2){background:#febc2e}.chrome i:nth-child(3){background:#28c840}
.chrome .url{flex:1;margin-left:8px;background:#fff;border-radius:6px;font-size:11px;color:#7a8194;padding:3px 10px;}
.frame img{width:100%;display:block;}
"""

img1 = f"""<!DOCTYPE html><html><head><style>{BASE_CSS}
body{{background:linear-gradient(135deg,#141a2e 0%,#1f2c54 55%,#2b3f7d 100%);}}
h1{{position:absolute;top:52px;left:0;right:0;text-align:center;color:#fff;font-size:58px;font-weight:800;letter-spacing:-.01em;}}
h1 span{{color:#8fb4ff;}}
.sub{{position:absolute;top:132px;left:0;right:0;text-align:center;color:#b9c6e8;font-size:24px;font-weight:600;}}
.frame{{position:absolute;width:560px;}}
.f1{{left:64px;top:208px;transform:rotate(-2.5deg);}}
.f2{{right:64px;top:238px;transform:rotate(2deg);}}
.ribbon{{position:absolute;bottom:36px;left:0;right:0;text-align:center;color:#fff;font-size:22px;font-weight:700;}}
.ribbon b{{color:#8fb4ff;}}
</style></head><body>
<h1>Modern websites for <span>small businesses</span></h1>
<div class="sub">Designed around YOUR brand — no two look alike</div>
<div class="frame f1"><div class="chrome"><i></i><i></i><i></i><div class="url">greencrestlawns.com</div></div><img src="shot_lawn.png"></div>
<div class="frame f2"><div class="chrome"><i></i><i></i><i></i><div class="url">ironandoak.com</div></div><img src="shot_barber.png"></div>
<div class="ribbon">Fast &nbsp;·&nbsp; Mobile-friendly &nbsp;·&nbsp; <b>Delivered in 3 days</b></div>
</body></html>"""

img2 = f"""<!DOCTYPE html><html><head><style>{BASE_CSS}
body{{background:linear-gradient(135deg,#0f3d22 0%,#1d6b3c 60%,#2f8a50 100%);}}
.left{{position:absolute;left:70px;top:0;bottom:0;width:470px;display:flex;flex-direction:column;justify-content:center;gap:22px;}}
h1{{color:#fff;font-size:56px;font-weight:800;line-height:1.08;}}
.check{{color:#d7f2df;font-size:25px;font-weight:600;display:flex;gap:12px;align-items:center;}}
.check b{{color:#9fe8b6;}}
.price{{margin-top:8px;display:inline-block;background:#fff;color:#14522c;font-size:30px;font-weight:800;border-radius:12px;padding:14px 26px;width:fit-content;}}
.frame{{position:absolute;width:610px;right:180px;top:96px;transform:rotate(1.5deg);}}
.phone{{position:absolute;right:70px;top:200px;width:210px;border-radius:26px;border:9px solid #101418;overflow:hidden;box-shadow:0 24px 60px rgba(5,20,10,.55);transform:rotate(-3deg);background:#fff;}}
.phone img{{width:100%;display:block;}}
</style></head><body>
<div class="left">
  <h1>Look professional online</h1>
  <div class="check">✅ <span><b>Mobile-first</b> design</span></div>
  <div class="check">✅ <span>Loads <b>fast</b></span></div>
  <div class="check">✅ <span><b>Free hosting</b> setup</span></div>
  <div class="price">Starting at $60</div>
</div>
<div class="frame"><div class="chrome"><i></i><i></i><i></i><div class="url">yourbusiness.com</div></div><img src="shot_lawn.png"></div>
<div class="phone"><img src="shot_lawn_mobile.png"></div>
</body></html>"""

img3 = f"""<!DOCTYPE html><html><head><style>{BASE_CSS}
body{{background:linear-gradient(135deg,#3b0d18 0%,#7c1d35 55%,#b3324e 100%);}}
h1{{position:absolute;top:56px;left:70px;width:520px;color:#fff;font-size:52px;font-weight:800;line-height:1.1;}}
h1 span{{color:#ffc46b;}}
.pt{{position:absolute;left:70px;top:250px;width:470px;color:#ffd9e0;font-size:24px;line-height:1.55;font-weight:600;}}
.badge{{position:absolute;left:70px;bottom:60px;background:#fff;border-radius:12px;padding:16px 24px;font-size:22px;font-weight:800;color:#7c1d35;}}
.frame{{position:absolute;right:56px;top:110px;width:620px;transform:rotate(2deg);}}
.live{{position:absolute;right:70px;top:74px;background:#16a34a;color:#fff;font-weight:800;font-size:18px;border-radius:999px;padding:8px 20px;z-index:2;letter-spacing:.04em;}}
</style></head><body>
<h1>Built by a <span>real store owner</span></h1>
<div class="pt">This is my own live e-commerce store — I build your website with the same owner's eye: made to win customers, not just look nice.</div>
<div class="badge">See it live in my portfolio ↗</div>
<div class="live">● LIVE STORE</div>
<div class="frame"><div class="chrome"><i></i><i></i><i></i><div class="url">hotstufffinds.com</div></div><img src="shot_hotstuff.png"></div>
</body></html>"""

for name, html in [("comp1.html", img1), ("comp2.html", img2), ("comp3.html", img3)]:
    (HERE / name).write_text(html, encoding="utf-8")

with sync_playwright() as p:
    b = p.chromium.launch()
    for i in (1, 2, 3):
        pg = b.new_page(viewport={"width": 1280, "height": 769}, device_scale_factor=2)
        pg.goto((HERE / f"comp{i}.html").as_uri()); pg.wait_for_timeout(500)
        pg.screenshot(path=str(HERE / f"gig-image-{i}.png"))
        print(f"rendered gig-image-{i}.png")
        pg.close()
    b.close()
