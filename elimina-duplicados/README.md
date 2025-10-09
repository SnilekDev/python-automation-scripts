# Eliminador de archivos duplicados por hash

Detecta archivos duplicados dentro de una carpeta (de forma recursiva) comparando su contenido mediante hash SHA-256.
Permite simular la eliminación antes de aplicar los cambios, garantizando seguridad en el proceso.

### Ejemplo de uso
```bash
python elimina_duplicados.py --carpeta carpeta/ --seco
python elimina_duplicados.py --carpeta carpeta/ --borrar

--seco → modo simulación, muestra los duplicados sin borrarlos.
--borrar → elimina automáticamente los duplicados, conservando una sola copia.
```

### Requisitos
Python 3.8+

No requiere librerías externas

### Entrega
Incluye script + README + demo + soporte 3 días.