from pathlib import Path 
import argparse, difflib 
 
def main(): 
    ap = argparse.ArgumentParser(description="Elimina párrafos duplicados/similares.") 
    ap.add_argument("--in", dest="entrada", required=True, help="Archivo de entrada.") 
    ap.add_argument("--out", dest="salida", required=True, help="Archivo de salida.") 
    ap.add_argument("--umbral", type=float, default=0.9, help="Similitud mínima para considerar duplicado (0-1).") 
    args = ap.parse_args() 
 
    text = Path(args.entrada).read_text(encoding="utf-8") 
    paras = [p.strip() for p in text.split("\n\n") if p.strip()] 
 
    kept = [] 
    for p in paras: 
        if any(difflib.SequenceMatcher(a=p, b=q).ratio() >= args.umbral for q in kept): 
            continue 
        kept.append(p) 
 
    Path(args.salida).write_text("\n\n".join(kept), encoding="utf-8") 
    print(f"[OK] Párrafos: {len(paras)} → {len(kept)} (umbral={args.umbral})") 
 
if __name__ == "__main__": 
    main()