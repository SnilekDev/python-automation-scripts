from pathlib import Path
import argparse
from datetime import datetime
import shutil

def renombrar(carpeta: Path, prefijo: str, separador: str, mover_por_fecha: bool, seco: bool):
    if not carpeta.exists() or not carpeta.is_dir():
        print(f"Carpeta no válida: {carpeta}")
        return

    archivos = [p for p in carpeta.iterdir() if p.is_file()]
    if not archivos:
        print("No hay archivos para procesar.")
        return

    contador = 1
    for p in sorted(archivos):
        fecha = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y%m%d")
        nuevo_nombre = f"{prefijo}{separador}{fecha}{separador}{contador:03d}{p.suffix.lower()}"
        destino = p.with_name(nuevo_nombre)

        if mover_por_fecha:
            sub = carpeta / fecha
            sub.mkdir(exist_ok=True)
            destino = sub / nuevo_nombre

        print(f"{p.name}  →  {destino.relative_to(carpeta)}")
        if not seco:
            shutil.move(str(p), str(destino))
        contador += 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Renombra y (opcional) ordena archivos por fecha.")
    ap.add_argument("--carpeta", required=True, help="Ruta de la carpeta a procesar")
    ap.add_argument("--prefijo", default="archivo", help="Prefijo del nuevo nombre")
    ap.add_argument("--separador", default="_", help="Separador del nombre")
    ap.add_argument("--mover_por_fecha", action="store_true", help="Mover a subcarpetas por fecha (YYYYMMDD)")
    ap.add_argument("--seco", action="store_true", help="Modo simulación (no mueve nada)")
    args = ap.parse_args()

    renombrar(Path(args.carpeta), args.prefijo.strip(), args.separador, args.mover_por_fecha, args.seco)