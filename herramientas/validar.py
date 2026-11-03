#!/usr/bin/env python3
"""Valida el banco de preguntas preguntas/preguntas.json.

Uso: python herramientas/validar.py [ruta_json]
Devuelve código 0 si todo es correcto; 1 y la lista de errores si no.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA_POR_DEFECTO = RAIZ / "preguntas" / "preguntas.json"

TOTAL = 200
REPARTO = {1: 24, 2: 44, 3: 36, 4: 56, 5: 40}
OBJETIVOS = {1: 4, 2: 5, 3: 4, 4: 9, 5: 6}  # n.º de objetivos por dominio (1.1–5.6)
MAX_POSICION = 0.35


def _normalizar(texto):
    return re.sub(r"\W+", " ", texto.lower()).strip()


def cargar(ruta=RUTA_POR_DEFECTO):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def validar(preguntas):
    errores = []
    if not isinstance(preguntas, list):
        return ["El JSON debe ser una lista de preguntas"]
    if len(preguntas) != TOTAL:
        errores.append(f"Hay {len(preguntas)} preguntas; se esperaban {TOTAL}")

    ids = Counter(p.get("id") for p in preguntas)
    for i, n in ids.items():
        if n > 1:
            errores.append(f"id duplicado: {i}")

    enunciados = Counter(_normalizar(p.get("enunciado", "")) for p in preguntas)
    for e, n in enunciados.items():
        if n > 1:
            errores.append(f"Enunciado duplicado: {e[:60]}…")

    por_dominio = Counter(p.get("dominio") for p in preguntas)
    for d, esperado in REPARTO.items():
        if por_dominio.get(d, 0) != esperado:
            errores.append(f"Dominio {d}: {por_dominio.get(d, 0)} preguntas; se esperaban {esperado}")

    for p in preguntas:
        pid = p.get("id", "?")
        for campo in ("id", "dominio", "objetivo", "enunciado", "opciones", "correcta", "explicacion"):
            if campo not in p:
                errores.append(f"{pid}: falta el campo '{campo}'")
        ops = p.get("opciones", [])
        if not isinstance(ops, list) or len(ops) != 4:
            errores.append(f"{pid}: debe tener 4 opciones")
        elif len({_normalizar(o) for o in ops}) != 4 or any(not str(o).strip() for o in ops):
            errores.append(f"{pid}: opciones vacías o repetidas")
        c = p.get("correcta")
        if not isinstance(c, int) or isinstance(c, bool) or not 0 <= c < 4:
            errores.append(f"{pid}: índice de respuesta correcta no válido ({c!r})")
        if not str(p.get("explicacion", "")).strip():
            errores.append(f"{pid}: explicación vacía")
        if not str(p.get("enunciado", "")).strip():
            errores.append(f"{pid}: enunciado vacío")
        d, obj = p.get("dominio"), str(p.get("objetivo", ""))
        m = re.fullmatch(r"(\d)\.(\d)", obj)
        if not m or int(m.group(1)) != d or not 1 <= int(m.group(2)) <= OBJETIVOS.get(d, 0):
            errores.append(f"{pid}: objetivo '{obj}' no válido para el dominio {d}")

    if preguntas:
        posiciones = Counter(p.get("correcta") for p in preguntas)
        for pos, n in posiciones.items():
            if n / len(preguntas) > MAX_POSICION:
                errores.append(f"La posición {pos} es la correcta en {n / len(preguntas):.0%} de las preguntas (> 35 %)")
    return errores


def main(argv):
    ruta = Path(argv[1]) if len(argv) > 1 else RUTA_POR_DEFECTO
    errores = validar(cargar(ruta))
    if errores:
        print("❌ Errores en el banco de preguntas:")
        for e in errores:
            print(" -", e)
        return 1
    print(f"✅ Banco válido: {TOTAL} preguntas, reparto {REPARTO}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
