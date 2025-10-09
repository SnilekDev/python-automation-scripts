# Generador automático de Tabla de Contenidos (ToC) para Markdown

Crea o actualiza automáticamente una tabla de contenidos basada en los encabezados (#, ##, etc.) de un archivo Markdown.
Ideal para documentaciones técnicas, repositorios de GitHub o blogs con muchos apartados.

### Ejemplo de uso
```bash
python genera_markdown.py --md README.md


Para insertar la tabla dentro del mismo archivo (entre etiquetas <!-- TOC START --> y <!-- TOC END -->):

python genera_markdown.py --md README.md --escribir
```

### Requisitos
Python 3.8+

No requiere librerías externas

### Entrega
Incluye script + README + demo + soporte 3 días.