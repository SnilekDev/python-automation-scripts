from pathlib import Path 
import argparse, re 
 
HDR = re.compile(r'^(?P<lvl>#{1,6})\s+(?P<txt>.+)$', re.M) 
 
def slug(s: str) -> str: 
    s = s.strip().lower() 
    s = re.sub(r'[^a-z0-9\s\-]', '', s) 
    s = re.sub(r'\s+', '-', s) 
    return s 
 
def build_toc(md: str) -> str: 
    lines = [] 
    for m in HDR.finditer(md): 
        lvl = len(m.group('lvl')) 
        txt = m.group('txt').strip() 
        lines.append("  "*(lvl-1) + f"- [{txt}](#{slug(txt)})") 
    return "\n".join(lines) 
 
def main(): 
    ap = argparse.ArgumentParser(description="Genera/actualiza ToC a partir de encabezados Markdown.") 
    ap.add_argument("--md", required=True, help="Archivo Markdown.") 
    ap.add_argument("--escribir", action="store_true", help="Escribir ToC dentro del archivo.") 
    args = ap.parse_args() 
 
    md_path = Path(args.md) 
    md = md_path.read_text(encoding="utf-8") 
    toc = build_toc(md) 
    if not args.escribir: 
        print(toc); return 
 
    start, end = "<!-- TOC START -->", "<!-- TOC END -->" 
    if start in md and end in md: 
        new = re.sub(r'<!-- TOC START -->.*?<!-- TOC END -->', f"{start}\n{toc}\n{end}", md, flags=re.S) 
    else: 
        new = f"{start}\n{toc}\n{end}\n\n{md}" 
    md_path.write_text(new, encoding="utf-8") 
    print("[OK] ToC insertada/actualizada.") 
 
if __name__ == "__main__": 
    main()