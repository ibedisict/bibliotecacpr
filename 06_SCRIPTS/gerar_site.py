#!/usr/bin/env python3
from pathlib import Path
import json, re, hashlib, datetime

ROOT = Path(__file__).resolve().parents[1]

def frontmatter(text):
    meta={}
    if text.startswith("---"):
        parts=text.split("---",2)
        if len(parts)==3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k,v=line.split(":",1); meta[k.strip()]=v.strip().strip('"').strip("'")
    return meta

docs=[]
for p in sorted(ROOT.rglob("*.md")):
    text=p.read_text(encoding="utf-8",errors="replace")
    meta=frontmatter(text)
    title=meta.get("titulo")
    if not title:
        m=re.search(r"^#\s+(.+)$",text,re.M); title=m.group(1).strip() if m else p.stem
    docs.append({
        "path":p.relative_to(ROOT).as_posix(),
        "title":title,
        "date":meta.get("data_publicacao") or meta.get("data_verificacao") or "",
        "status":meta.get("status_juridico",""),
        "type":meta.get("tipo",""),
        "authority":meta.get("autoridade","")
    })

idx=ROOT/"00_INDICES"; idx.mkdir(exist_ok=True)
(idx/"catalogo_documentos_index.json").write_text(json.dumps(docs,ensure_ascii=False,indent=2),encoding="utf-8")

ordered=sorted(docs,key=lambda d:(d["date"] or "0000-00-00",d["title"]),reverse=True)
lines=["# Índice cronológico consolidado","",f"**Atualizado em:** {datetime.date.today().isoformat()}  ",f"**Total:** {len(docs)} documentos","",
"| Data | Documento | Status | Tipo | Caminho |","|---|---|---|---|---|"]
for d in ordered:
    lines.append(f'| {d["date"] or "sem data"} | {d["title"].replace("|","/")} | {d["status"] or "não informado"} | {d["type"] or "não informado"} | `{d["path"]}` |')
(ROOT/"INDEX_CRONOLOGICO.md").write_text("\n".join(lines),encoding="utf-8")

manifest=[]
for p in sorted(ROOT.rglob("*")):
    if p.is_file() and p.name!="MANIFEST_SHA256_ATUALIZADO.json":
        b=p.read_bytes()
        manifest.append({"file":p.relative_to(ROOT).as_posix(),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()})
(ROOT/"MANIFEST_SHA256_ATUALIZADO.json").write_text(json.dumps({"generated_at":datetime.date.today().isoformat(),"files":manifest},ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Catálogo e manifesto atualizados: {len(docs)} Markdown.")
print("Observação: para incorporar o conteúdo integral no HTML offline, execute o gerador mestre distribuído na versão do projeto.")
