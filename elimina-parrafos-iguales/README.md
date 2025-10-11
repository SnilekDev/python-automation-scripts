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

## Evidencia visual (demo)

**Archivo de prueba**  
`/demo/input_example/texto_prueba.txt` contiene párrafos duplicados y únicos.

**Ejecuciones**

- `captura_parrafo_eliminado.jpg` → simulación, muestra qué párrafos serían eliminados  `/demo/`
- `captura_resultado.jpg` → modo real, archivo limpio generado en `/demo/`

**Resultados**

El script elimina correctamente párrafos duplicados o muy similares según el umbral especificado, conservando solo los únicos.