#!/usr/bin/env python3
"""Genera quiz/index.html incrustando preguntas/preguntas.json en quiz/plantilla.html.

Uso: python herramientas/construir_quiz.py
El resultado funciona abriendo el archivo directamente (sin servidor).
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "herramientas"))
import validar  # noqa: E402

MARCA = "/*__PREGUNTAS__*/[]"


def construir():
    preguntas = validar.cargar()
    errores = validar.validar(preguntas)
    if errores:
        print("❌ El banco no es válido; corrige antes de construir:")
        for e in errores:
            print(" -", e)
        return 1
    plantilla = (RAIZ / "quiz" / "plantilla.html").read_text(encoding="utf-8")
    if plantilla.count(MARCA) != 1:
        print("❌ La plantilla debe contener una sola vez la marca", MARCA)
        return 1
    datos = json.dumps(preguntas, ensure_ascii=False, separators=(",", ":"))
    datos = datos.replace("</", "<\\/")  # evita cerrar el <script> antes de tiempo
    (RAIZ / "quiz" / "index.html").write_text(plantilla.replace(MARCA, datos), encoding="utf-8")
    print(f"✅ quiz/index.html generado con {len(preguntas)} preguntas")
    return 0


if __name__ == "__main__":
    sys.exit(construir())
