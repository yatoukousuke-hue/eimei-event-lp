import json
p = "vercel.json"
v = json.load(open(p, encoding="utf-8"))
r = v.setdefault("redirects", [])
if not any(x.get("source") == "/" for x in r):
    r.insert(0, {"source": "/", "destination": "/christmas-2026", "permanent": False})
    json.dump(v, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a").write("\n")
    print("switched")
