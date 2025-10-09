# Copia incremental basada en hash

Realiza copias de seguridad inteligentes comparando archivos por su huella SHA-256.
Solo copia los archivos nuevos o modificados, evitando duplicados innecesarios. Ideal para mantener sincronizadas carpetas de respaldo o proyectos grandes.

### Ejemplo de uso
```bash
python copia_incremental.py --origen carpeta_origen --destino carpeta_respaldo --seco
```

### Requisitos
Python 3.8+

No requiere librerías externas

### Entrega
Incluye script + README + demo + soporte 3 días.