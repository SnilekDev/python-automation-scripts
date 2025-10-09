# Eliminador de párrafos duplicados o similares

Limpia un texto eliminando párrafos idénticos o con alta similitud, según un umbral configurable.
Ideal para depurar documentos largos, reportes o textos generados automáticamente.

### Ejemplo de uso
```bash
python elimina_parrafos_iguales.py --in texto_original.txt --out texto_limpio.txt --umbral 0.9

--in → archivo de entrada con el texto original.
--out → archivo donde se guardará el texto limpio.
--umbral → valor entre 0 y 1 que indica el nivel de similitud (por defecto 0.9).
```

### Requisitos
Python 3.8+

No requiere librerías externas

### Entrega
Incluye script + README + demo + soporte 3 días.