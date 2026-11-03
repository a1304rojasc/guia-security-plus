import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "herramientas"))
import validar  # noqa: E402

PREGUNTAS = validar.cargar()


def test_banco_sin_errores():
    assert validar.validar(PREGUNTAS) == []


def test_total_y_reparto():
    assert len(PREGUNTAS) == 200
    assert Counter(p["dominio"] for p in PREGUNTAS) == Counter(validar.REPARTO)


def test_ids_unicos():
    assert len({p["id"] for p in PREGUNTAS}) == len(PREGUNTAS)


def test_estructura_de_cada_pregunta():
    for p in PREGUNTAS:
        assert len(p["opciones"]) == 4, p["id"]
        assert 0 <= p["correcta"] < 4, p["id"]
        assert p["explicacion"].strip(), p["id"]


def test_sin_enunciados_duplicados():
    enunciados = [validar._normalizar(p["enunciado"]) for p in PREGUNTAS]
    assert len(set(enunciados)) == len(enunciados)


def test_posicion_correcta_repartida():
    for pos, n in Counter(p["correcta"] for p in PREGUNTAS).items():
        assert n / len(PREGUNTAS) <= 0.35, f"posición {pos}: {n}"


def test_validador_detecta_errores():
    malo = [dict(p) for p in PREGUNTAS]
    malo[0]["correcta"] = 7
    malo[1]["explicacion"] = ""
    malo.append(dict(malo[2]))
    errores = validar.validar(malo)
    assert any("índice" in e for e in errores)
    assert any("explicación vacía" in e for e in errores)
    assert any("duplicado" in e for e in errores)
    assert any("Hay 201" in e for e in errores)
