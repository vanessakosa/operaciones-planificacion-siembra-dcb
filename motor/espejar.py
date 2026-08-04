#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Espeja archivos de Drive al repo SIN transcribir base64 a mano.

El problema que resuelve: al bajar un archivo de Drive, el contenido llega como
base64 dentro del resultado de la herramienta. Copiarlo a mano para escribirlo
en disco es poco confiable — un base64 truncado produce un archivo corrupto, y
un archivo de datos primarios corrupto hace mas daño que no tenerlo.

La solucion: los resultados de herramienta quedan registrados en el transcript
de la sesion (JSONL) y, si son grandes, en tool-results/. Este script los lee
de ahi, decodifica y escribe, y VERIFICA el tamaño contra el que reporta Drive.

Uso:
    python3 motor/espejar.py listar
    python3 motor/espejar.py escribir <titulo> <ruta_destino> [bytes_esperados]
"""

import base64
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROYECTOS = os.path.expanduser("~/.claude/projects")


def _fuentes():
    """Todos los ficheros donde puede haber quedado un resultado de descarga."""
    rutas = []
    rutas += glob.glob(os.path.join(PROYECTOS, "*", "*.jsonl"))
    rutas += glob.glob(os.path.join(PROYECTOS, "*", "*", "tool-results", "*.txt"))
    return rutas


def _payloads(texto):
    """Extrae los objetos {content, id, mimeType, title} que haya en el texto."""
    fuera = []
    for pos in range(len(texto)):
        if not texto.startswith('{"content":', pos):
            continue
        dec = json.JSONDecoder()
        try:
            obj, _ = dec.raw_decode(texto, pos)
        except ValueError:
            continue
        if isinstance(obj, dict) and "content" in obj and "title" in obj:
            fuera.append(obj)
    return fuera


def descargas():
    """titulo -> payload mas reciente encontrado."""
    encontrados = {}
    for ruta in _fuentes():
        try:
            with open(ruta, encoding="utf-8", errors="replace") as fh:
                texto = fh.read()
        except OSError:
            continue
        # Los .jsonl traen el JSON escapado dentro de otro JSON: se desescapa.
        candidatos = _payloads(texto) + _payloads(texto.replace('\\"', '"').replace("\\n", "\n"))
        for obj in candidatos:
            encontrados[obj["title"]] = obj
    return encontrados


def cmd_listar():
    d = descargas()
    if not d:
        print("No encontre descargas registradas.")
        return
    print("DESCARGAS DISPONIBLES PARA ESPEJAR\n")
    print("%-42s %10s  %s" % ("TITULO", "BYTES", "DRIVE ID"))
    print("-" * 78)
    for titulo in sorted(d):
        obj = d[titulo]
        try:
            n = len(base64.b64decode(obj["content"]))
        except Exception:
            n = -1
        print("%-42s %10s  %s" % (titulo[:42], n if n >= 0 else "ILEGIBLE", obj.get("id", "?")))


def cmd_escribir(titulo, destino, esperados=None):
    d = descargas()
    obj = d.get(titulo)
    if obj is None:
        # Coincidencia parcial para no pelear con acentos y mayusculas
        for k in d:
            if titulo.lower() in k.lower():
                obj, titulo = d[k], k
                break
    if obj is None:
        raise SystemExit("No encontre una descarga con titulo '%s'. Corre: listar" % titulo)

    crudo = base64.b64decode(obj["content"])
    ruta = destino if os.path.isabs(destino) else os.path.join(RAIZ, destino)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "wb") as fh:
        fh.write(crudo)

    print("%s -> %s" % (titulo, destino))
    print("  bytes escritos: %d" % len(crudo))
    if esperados is not None:
        esperados = int(esperados)
        if len(crudo) == esperados:
            print("  VERIFICADO: coincide con los %d bytes que reporta Drive" % esperados)
        else:
            print("  *** NO COINCIDE: Drive reporta %d. Archivo sospechoso." % esperados)
            return 1
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    if argv[1] == "listar":
        cmd_listar()
        return 0
    if argv[1] == "escribir":
        if len(argv) < 4:
            raise SystemExit("Uso: espejar.py escribir <titulo> <destino> [bytes]")
        return cmd_escribir(argv[2], argv[3], argv[4] if len(argv) > 4 else None) or 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
