# Analizador de movimientos CSV con categorización automática

Analiza archivos CSV de movimientos (fecha, descripción, monto) y los clasifica automáticamente por categorías definidas en un archivo JSON.
Genera un resumen mensual por categoría, ideal para análisis financieros, control de gastos o reportes contables.

### Ejemplo de uso
```bash
python analizador_csv.py --csv movimientos.csv --reglas categorias.json --salida resumen.csv
```
Ejemplo de categorias.json:

{
  "Alimentación": ["supermercado", "restaurante", "mercado"],
  "Transporte": ["bus", "taxi", "gasolina"],
  "Servicios": ["luz", "agua", "internet"]
}

### Requisitos
Python 3.8+

No requiere librerías externas

### Entrega
Incluye script + README + demo + soporte 3 días.