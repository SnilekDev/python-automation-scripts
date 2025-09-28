from pathlib import Path 
import argparse, hashlib, shutil 
 
def sha256sum(p: Path, chunk=1024*1024) -> str: 
    h = hashlib.sha256() 
    with p.open('rb') as f: 
        while True: 
            b = f.read(chunk) 
            if not b: break 
            h.update(b) 
    return h.hexdigest() 
 
def main(): 
    ap = argparse.ArgumentParser(description="Copia incremental basada en hash.") 
    ap.add_argument("--origen", required=True, help="Carpeta de origen (recursivo).") 
    ap.add_argument("--destino", required=True, help="Carpeta de destino.") 
    ap.add_argument("--seco", action="store_true", help="Simulación: no copia, solo muestra.") 
    args = ap.parse_args() 
 
    src, dst = Path(args.origen), Path(args.destino) 
    if not src.is_dir(): 
        print(f"[ERROR] Origen inválido: {src}"); return 
    dst.mkdir(parents=True, exist_ok=True) 
 
    copiados, actualizados = 0, 0 
    for p in src.rglob("*"): 
        if not p.is_file(): continue 
        rel = p.relative_to(src) 
        q = dst / rel 
        if not q.exists(): 
            q.parent.mkdir(parents=True, exist_ok=True) 
            if args.seco: 
                print(f"[SECO] Copiaría NUEVO: {rel}") 
            else: 
                shutil.copy2(p, q) 
                print(f"[OK] Copiado NUEVO: {rel}") 
            copiados += 1 
        else: 
            if sha256sum(p) != sha256sum(q): 
                if args.seco: 
                    print(f"[SECO] Actualizaría: {rel}") 
                else: 
                    shutil.copy2(p, q) 
                    print(f"[OK] Actualizado: {rel}") 
                actualizados += 1 
    print(f"[RESUMEN] Nuevos: {copiados}, Actualizados: {actualizados}")


if __name__ == "__main__": 
    main() 