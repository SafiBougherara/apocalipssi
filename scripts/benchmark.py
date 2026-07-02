import time, json, statistics, urllib.request
from datetime import datetime

MODELS = ["phi3:mini", "llama3.2", "llama3.1"]
OLLAMA_URL = "http://localhost:11434/api/generate"

# Prompt court : 1 seul QCM, on mesure tokens/sec puis on extrapole
PROMPT = """Generate exactly 1 multiple choice question about photosynthesis.
JSON only: [{"question":"...","options":{"A":"...","B":"...","C":"...","D":"..."},"answer":"A"}]"""

def test_model(model):
    body = json.dumps({"model": model, "prompt": PROMPT, "stream": False}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=body,
                                  headers={"Content-Type": "application/json"}, method="POST")
    print(f"  {model}... ", end="", flush=True)
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.loads(r.read())
        elapsed = time.perf_counter() - t0
        tokens = data.get("eval_count", 1)
        ns = data.get("eval_duration", 1)
        tps = round(tokens / (ns / 1e9), 1)
        # Un quiz 10 QCM = ~400 tokens de sortie (estimation conservative)
        estimated_10qcm = round(400 / tps, 1)
        print(f"{elapsed:.1f}s | {tps} tok/s | ~{estimated_10qcm}s pour 10 QCM")
        return {"model": model, "elapsed_s": round(elapsed,1), "tok_per_s": tps,
                "estimated_10qcm_s": estimated_10qcm, "ok": True}
    except Exception as e:
        elapsed = time.perf_counter() - t0
        print(f"ERREUR apres {elapsed:.1f}s ({type(e).__name__})")
        return {"model": model, "ok": False}

print(f"\n== BENCHMARK EXPRESS -- EduTutor IA -- {datetime.now().strftime('%d/%m/%Y %H:%M')} ==")
print(f"1 run par modele | prompt : 1 QCM | estimation extrapolee pour 10 QCM\n")

results = [test_model(m) for m in MODELS]

print(f"\n{'='*58}")
print(f"  {'Modele':<18} {'tok/s':<10} {'~10 QCM':<14} {'Objectif<=15s'}")
print(f"  {'-'*18} {'-'*10} {'-'*14} {'-'*13}")
for r in results:
    if r["ok"]:
        ok = "OK" if r["estimated_10qcm_s"] <= 15 else "TROP LENT"
        print(f"  {r['model']:<18} {str(r['tok_per_s'])+'t/s':<10} {str(r['estimated_10qcm_s'])+'s':<14} {ok}")
    else:
        print(f"  {r['model']:<18} {'---':<10} {'---':<14} ERREUR")
print(f"{'='*58}")

ok_models = [r for r in results if r["ok"] and r["estimated_10qcm_s"] <= 15]
best = min(ok_models, key=lambda r: r["estimated_10qcm_s"]) if ok_models else \
       min([r for r in results if r["ok"]], key=lambda r: r["estimated_10qcm_s"], default=None)
if best:
    print(f"\n  >> RECOMMANDATION : {best['model']} ({best['tok_per_s']} tok/s, ~{best['estimated_10qcm_s']}s)")

fname = f"benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(fname, "w") as f:
    json.dump({"date": datetime.now().isoformat(), "note": "1 run par modele, latence 10 QCM extrapolee",
               "resultats": results}, f, indent=2)
print(f"  Sauvegarde : {fname}\n")
