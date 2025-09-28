from pathlib import Path 
import argparse, hashlib, itertools, shutil 
 
def sha256sum(p: Path, chunk=1024*1024) -> str: 
    h = hashlib.sha256() 
    with p.open('rb') as f: 
        while True: 
            b = f.read(chunk) 
            if not b: break 
            h.update(b) 
    return h.hexdigest() 
 
def main(): 
    ap = argparse.ArgumentParser(description="Detecta archivos duplicados por hash.") 
    ap.add_argument("--carpeta", required=True, help="Carpeta raíz a analizar (recursivo).") 
    ap.add_argument("--seco", action="store_true", help="Simulación: no borra, solo muestra.") 
    ap.add_argument("--borrar", action="store_true", help="Borrar duplicados dejando 1 copia.") 
    args = ap.parse_args() 
 
    root = Path(args.carpeta) 
    if not root.exists() or not root.is_dir(): 
        print(f"[ERROR] Carpeta inválida: {root}"); return 
 
    # Agrupar por tamaño 
    sizes = {} 
    for p in root.rglob("*"): 
        if p.is_file(): 
            sizes.setdefault(p.stat().st_size, []).append(p) 
    total_files = sum(len(v) for v in sizes.values()) 
    print(f"[INFO] Archivos totales: {total_files}") 
 
    dup_groups = [] 
    for size, files in sizes.items(): 
        if len(files) < 2: continue 
        by_hash = {} 
        for f in files: 
            h = sha256sum(f) 
            by_hash.setdefault(h, []).append(f) 
        for h, group in by_hash.items(): 
            if len(group) > 1: 
                dup_groups.append(group) 
 
    if not dup_groups: 
        print("[OK] No se encontraron duplicados."); return 
 
    print(f"[INFO] Grupos de duplicados: {len(dup_groups)}") 
    borrados = 0 
    for i, group in enumerate(dup_groups, 1): 
        print(f"\n[DUP {i}]") 
        for j, f in enumerate(sorted(group)): 
            mark = " (conservar)" if j == 0 else "" 
            print(" -", f, mark) 
        if args.borrar: 
            for f in group[1:]: 
                if args.seco: 
                    print(f"[SECO] Borraría: {f}") 
                else: 
                    try: 
                        f.unlink() 
                        borrados += 1 
                        print(f"[OK] Borrado: {f}") 
                    except Exception as e: 
                        print(f"[ERROR] No se pudo borrar {f}: {e}") 
    if args.borrar: 
        print(f"\n[RESUMEN] Borrados: {borrados}") 
    else: 
        print("\n[SUGERENCIA] Use --borrar para eliminar duplicados (primero con --seco).") 
 
if __name__ == "__main__": 
    main()