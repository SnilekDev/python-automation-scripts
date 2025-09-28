from pathlib import Path 
import argparse, csv, json 
from collections import defaultdict 
from datetime import datetime 
 
def categ(desc: str, rules: dict) -> str: 
    d = desc.lower() 
    for cat, keys in rules.items(): 
        for k in keys: 
            if k.lower() in d: 
                return cat 
    return "Sin categoría" 
 
def main(): 
    ap = argparse.ArgumentParser(description="Analiza CSV de movimientos y categoriza por reglas.") 
    ap.add_argument("--csv", required=True, help="Archivo CSV: fecha, descripcion, monto") 
    ap.add_argument("--reglas", required=True, help="JSON con reglas de categorías.") 
    ap.add_argument("--salida", default="resumen.csv", help="CSV de salida con totales por categoría y mes.") 
    args = ap.parse_args() 
 
    rules = json.loads(Path(args.reglas).read_text(encoding="utf-8")) 
    by_cat = defaultdict(float) 
    by_month_cat = defaultdict(float) 
 
    with open(args.csv, newline="", encoding="utf-8") as f: 
        rdr = csv.DictReader(f) 
        for row in rdr: 
            fecha = datetime.fromisoformat(row["fecha"]) 
            desc = row["descripcion"] 
            monto = float(row["monto"]) 
            cat = categ(desc, rules) 
            by_cat[cat] += monto 
            key = (fecha.strftime("%Y-%m"), cat) 
            by_month_cat[key] += monto 
 
    # Escribir resumen 
    with open(args.salida, "w", newline="", encoding="utf-8") as f: 
        wr = csv.writer(f) 
        wr.writerow(["mes","categoria","total"]) 
        for (mes, cat), total in sorted(by_month_cat.items()): 
            wr.writerow([mes, cat, f"{total:.2f}"]) 
 
    print("[RESUMEN POR CATEGORÍA]") 
    for cat, total in sorted(by_cat.items(), key=lambda x: x[0]): 
        print(f" - {cat}: {total:.2f}") 
    print(f"[OK] Resumen mensual guardado en {args.salida}") 
 
if __name__ == "__main__": 
    main()