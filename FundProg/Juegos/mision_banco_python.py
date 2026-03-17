from __future__ import annotations

import json
import random
import statistics
import textwrap
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RANKING_FILE = BASE_DIR / "ranking_mision_banco_python.json"


class InvalidChoiceError(Exception):
    """Raised when the player chooses an invalid option."""


@dataclass
class Question:
    topic: str
    prompt: str
    options: dict[str, str]
    correct_option: str
    explanation: str
    points: int = 10
    clue: str = ""

    def ask(self) -> bool:
        print()
        print("=" * 72)
        print(f"Tema: {self.topic}")
        print("-" * 72)
        print(wrap(self.prompt))
        print()

        for key, value in self.options.items():
            print(f"  {key}) {value}")

        if self.clue:
            print("\nEscribe 'P' si quieres una pista.")

        while True:
            raw_answer = input("\nTu respuesta: ").strip().upper()

            try:
                if self.clue and raw_answer == "P":
                    print(f"\nPista: {wrap(self.clue)}")
                    continue

                if raw_answer not in self.options:
                    raise InvalidChoiceError(
                        "Opcion invalida. Elige una letra mostrada en pantalla."
                    )
                break
            except InvalidChoiceError as error:
                print(error)

        if raw_answer == self.correct_option:
            print("\nCorrecto.")
            print(wrap(self.explanation))
            return True

        print("\nNo fue la mejor opcion.")
        print(f"Respuesta correcta: {self.correct_option}) {self.options[self.correct_option]}")
        print(wrap(self.explanation))
        return False


@dataclass
class Player:
    name: str
    score: int = 0
    streak: int = 0
    max_streak: int = 0
    correct_answers: int = 0
    answered_questions: int = 0
    badges: list[str] = field(default_factory=list)
    start_time: float = field(default_factory=time.time)

    def register_result(self, was_correct: bool, base_points: int) -> None:
        self.answered_questions += 1

        if was_correct:
            self.correct_answers += 1
            self.streak += 1
            self.max_streak = max(self.max_streak, self.streak)
            earned_points = base_points

            if self.streak > 0 and self.streak % 3 == 0:
                earned_points += 5
                print("Bonus de racha: +5 puntos por tres respuestas seguidas.")

            self.score += earned_points
        else:
            self.streak = 0

    @property
    def accuracy(self) -> float:
        if self.answered_questions == 0:
            return 0.0
        return (self.correct_answers / self.answered_questions) * 100

    @property
    def elapsed_seconds(self) -> float:
        return time.time() - self.start_time


class MissionBankGame:
    def __init__(self) -> None:
        self.questions_by_mission = self._build_questions()

    def run(self) -> None:
        self._show_intro()

        while True:
            print("\nMENU PRINCIPAL")
            print("1. Jugar")
            print("2. Ver ranking")
            print("3. Salir")

            option = input("\nElige una opcion: ").strip()

            if option == "1":
                self._play()
            elif option == "2":
                self._show_ranking()
            elif option == "3":
                print("\nHasta la proxima mision.")
                return
            else:
                print("Opcion invalida. Intenta otra vez.")

    def _play(self) -> None:
        name = input("\nNombre del jugador o equipo: ").strip()
        if not name:
            name = "Equipo Python"

        player = Player(name=name)

        print("\nBienvenido a la Mision Banco Python.")
        print(
            wrap(
                "Tu reto es rescatar el sistema del banco resolviendo misiones sobre "
                "errores, programacion orientada a objetos y biblioteca estandar."
            )
        )
        print("Cada respuesta correcta suma puntos. Las rachas tambien premian.")

        for mission_name, questions in self.questions_by_mission.items():
            self._play_mission(mission_name, questions, player)

        self._assign_badges(player)
        self._show_final_report(player)
        self._save_result(player)

    def _play_mission(
        self, mission_name: str, questions: list[Question], player: Player
    ) -> None:
        print("\n" + "#" * 72)
        print(f"MISION: {mission_name}")
        print("#" * 72)

        selected_questions = random.sample(questions, k=min(4, len(questions)))
        mission_start_score = player.score

        for question in selected_questions:
            was_correct = question.ask()
            player.register_result(was_correct, question.points)
            print(f"Puntaje actual: {player.score}")

        earned = player.score - mission_start_score
        print(f"\nFin de la mision '{mission_name}'. Puntos ganados: {earned}")

    def _show_intro(self) -> None:
        print("=" * 72)
        print("MISION BANCO PYTHON")
        print("=" * 72)
        print(
            wrap(
                "Un fallo misterioso esta afectando al Banco Python. Para recuperar el "
                "control del sistema debes superar tres misiones: errores y excepciones, "
                "POO y biblioteca estandar."
            )
        )
        print()
        print("Este juego esta pensado para reforzar los temas del notebook:")
        print("- errores y excepciones")
        print("- clases, objetos, herencia y metodos")
        print("- modulos utiles de la biblioteca estandar")

    def _show_final_report(self, player: Player) -> None:
        elapsed = player.elapsed_seconds
        elapsed_text = f"{elapsed:.1f} segundos"

        print("\n" + "=" * 72)
        print("REPORTE FINAL DE LA MISION")
        print("=" * 72)
        print(f"Jugador o equipo: {player.name}")
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Puntaje final: {player.score}")
        print(f"Precision: {player.accuracy:.1f}%")
        print(f"Mayor racha: {player.max_streak}")
        print(f"Tiempo total: {elapsed_text}")

        if player.badges:
            print("Insignias:", ", ".join(player.badges))

        print("\nLectura pedagogica del resultado:")
        if player.accuracy >= 85:
            print(
                wrap(
                    "Excelente dominio. El grupo ya reconoce bien cuando usar excepciones, "
                    "como modelar objetos y para que sirven varios modulos estandar."
                )
            )
        elif player.accuracy >= 60:
            print(
                wrap(
                    "Buen avance. Conviene repasar la diferencia entre conceptos parecidos, "
                    "por ejemplo instancia vs clase, o except vs finally."
                )
            )
        else:
            print(
                wrap(
                    "El juego ya mostro por donde seguir. Repite la mision y conversa cada "
                    "respuesta antes de marcarla: la discusion tambien hace parte del aprendizaje."
                )
            )

    def _assign_badges(self, player: Player) -> None:
        if player.correct_answers >= 8:
            player.badges.append("Cazaerrores")
        if player.max_streak >= 3:
            player.badges.append("Racha de Codigo")
        if player.accuracy >= 85:
            player.badges.append("Arquitecto del Banco")
        if player.elapsed_seconds < 120:
            player.badges.append("Respuesta Rapida")

    def _save_result(self, player: Player) -> None:
        ranking = self._load_ranking()
        record = {
            "name": player.name,
            "score": player.score,
            "accuracy": round(player.accuracy, 1),
            "max_streak": player.max_streak,
            "badges": player.badges,
            "played_at": datetime.now().isoformat(timespec="seconds"),
        }
        ranking.append(record)
        ranking.sort(key=lambda item: (-item["score"], -item["accuracy"], item["name"]))
        ranking = ranking[:10]
        RANKING_FILE.write_text(json.dumps(ranking, indent=2, ensure_ascii=True), encoding="utf-8")

        print(f"\nRanking actualizado en: {RANKING_FILE.name}")
        if ranking:
            scores = [item["score"] for item in ranking]
            print(f"Puntaje promedio historico del ranking: {statistics.mean(scores):.2f}")

    def _load_ranking(self) -> list[dict[str, object]]:
        if not RANKING_FILE.exists():
            return []

        try:
            return json.loads(RANKING_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(
                wrap(
                    "No se pudo leer el ranking existente. Se iniciara uno nuevo para evitar errores."
                )
            )
            return []

    def _show_ranking(self) -> None:
        ranking = self._load_ranking()

        print("\n" + "=" * 72)
        print("RANKING DE MISION BANCO PYTHON")
        print("=" * 72)

        if not ranking:
            print("Aun no hay partidas registradas.")
            return

        for index, item in enumerate(ranking, start=1):
            badges = ", ".join(item.get("badges", [])) or "Sin insignias"
            print(
                f"{index:>2}. {item['name']} | "
                f"Puntaje: {item['score']} | "
                f"Precision: {item['accuracy']}% | "
                f"Racha: {item['max_streak']} | "
                f"{badges}"
            )

        scores = [entry["score"] for entry in ranking]
        print(f"\nPromedio del top {len(scores)}: {statistics.mean(scores):.2f}")
        print(f"Puntaje maximo registrado: {max(scores)}")

    def _build_questions(self) -> dict[str, list[Question]]:
        return {
            "Centro de Errores y Excepciones": [
                Question(
                    topic="Errores",
                    prompt=(
                        "En el codigo `if x > 3` sin dos puntos al final, "
                        "que tipo de problema aparece?"
                    ),
                    options={
                        "A": "TypeError",
                        "B": "SyntaxError",
                        "C": "KeyError",
                        "D": "FileNotFoundError",
                    },
                    correct_option="B",
                    explanation=(
                        "La sintaxis esta incompleta. Python ni siquiera puede empezar a "
                        "ejecutar el programa."
                    ),
                    clue="Piensa si el problema aparece antes o durante la ejecucion.",
                ),
                Question(
                    topic="Excepciones",
                    prompt="Que excepcion aparece al ejecutar `10 / 0`?",
                    options={
                        "A": "ZeroDivisionError",
                        "B": "ValueError",
                        "C": "IndexError",
                        "D": "ImportError",
                    },
                    correct_option="A",
                    explanation=(
                        "Dividir por cero produce una excepcion de ejecucion llamada "
                        "ZeroDivisionError."
                    ),
                    clue="La pista esta en el propio nombre del operador fallido.",
                ),
                Question(
                    topic="try/except",
                    prompt=(
                        "Cual es la mejor practica cuando manejas errores con `except`?"
                    ),
                    options={
                        "A": "Capturar todo con un except vacio y seguir",
                        "B": "Capturar excepciones especificas y mostrar mensajes utiles",
                        "C": "Evitar usar try para no complicar el codigo",
                        "D": "Ocultar los errores para que el usuario no los vea",
                    },
                    correct_option="B",
                    explanation=(
                        "Capturar errores especificos ayuda a depurar, comunicar mejor el "
                        "problema y evitar comportamientos inesperados."
                    ),
                    clue="La mejor respuesta combina control y claridad.",
                ),
                Question(
                    topic="finally",
                    prompt=(
                        "Para que sirve un bloque `finally` dentro de una estructura de manejo "
                        "de excepciones?"
                    ),
                    options={
                        "A": "Solo corre cuando hay error",
                        "B": "Solo corre si no hay error",
                        "C": "Siempre corre, haya o no excepcion",
                        "D": "Sirve unicamente para imprimir mensajes",
                    },
                    correct_option="C",
                    explanation=(
                        "finally se ejecuta siempre y es ideal para cerrar archivos, liberar "
                        "recursos o dejar el programa en un estado ordenado."
                    ),
                    clue="Piensa en tareas de cierre que deben pasar sin falta.",
                ),
                Question(
                    topic="raise",
                    prompt=(
                        "Cuando usas `raise ValueError('edad invalida')`, que estas haciendo?"
                    ),
                    options={
                        "A": "Ignorando un error",
                        "B": "Convirtiendo el dato en entero",
                        "C": "Lanzando una excepcion manualmente",
                        "D": "Creando una lista vacia",
                    },
                    correct_option="C",
                    explanation=(
                        "raise permite detener el flujo cuando detectas un dato invalido "
                        "y quieres reportarlo con claridad."
                    ),
                    clue="No esperas a que Python falle solo; actuas tu.",
                ),
                Question(
                    topic="Excepciones personalizadas",
                    prompt=(
                        "Por que seria util crear una excepcion como `SaldoInsuficienteError`?"
                    ),
                    options={
                        "A": "Porque cualquier error sirve igual",
                        "B": "Porque comunica mejor un problema del dominio del programa",
                        "C": "Porque evita usar clases",
                        "D": "Porque reemplaza al modulo math",
                    },
                    correct_option="B",
                    explanation=(
                        "Las excepciones personalizadas hacen que el programa hable el lenguaje "
                        "del problema real y no solo el del interprete."
                    ),
                    clue="Piensa en mensajes mas cercanos a una app bancaria real.",
                ),
            ],
            "Academia de POO": [
                Question(
                    topic="Clases y objetos",
                    prompt="Una clase en Python se parece mas a:",
                    options={
                        "A": "Una instancia unica e irrepetible",
                        "B": "Un plano o molde para crear objetos",
                        "C": "Un error del sistema",
                        "D": "Un archivo JSON",
                    },
                    correct_option="B",
                    explanation=(
                        "La clase define estructura y comportamiento; los objetos son las "
                        "instancias concretas creadas a partir de ella."
                    ),
                    clue="Piensa en el plano de una casa frente a una casa construida.",
                ),
                Question(
                    topic="self",
                    prompt="Que representa `self` dentro de un metodo de instancia?",
                    options={
                        "A": "El archivo donde vive la clase",
                        "B": "La clase completa",
                        "C": "El objeto actual sobre el que actua el metodo",
                        "D": "Una variable global obligatoria",
                    },
                    correct_option="C",
                    explanation=(
                        "self es la referencia a la instancia actual, por eso permite acceder "
                        "a sus atributos y metodos."
                    ),
                    clue="Sirve para hablar del objeto que recibio la llamada.",
                ),
                Question(
                    topic="Herencia",
                    prompt=(
                        "Si `CuentaAhorros` hereda de `CuentaBancaria`, cual es una ventaja clara?"
                    ),
                    options={
                        "A": "No volver a escribir metodos que ya sirven para todas las cuentas",
                        "B": "Eliminar todos los atributos del padre",
                        "C": "Evitar usar constructores",
                        "D": "Hacer que Python ejecute mas rapido siempre",
                    },
                    correct_option="A",
                    explanation=(
                        "La herencia permite reutilizar codigo comun y sobrescribir solo la "
                        "parte que necesita un comportamiento distinto."
                    ),
                    clue="La palabra clave es reutilizacion.",
                ),
                Question(
                    topic="Metodos especiales",
                    prompt=(
                        "Que metodo especial se usa para definir una representacion legible "
                        "cuando hacemos `print(objeto)`?"
                    ),
                    options={
                        "A": "__len__",
                        "B": "__repr__",
                        "C": "__str__",
                        "D": "__eq__",
                    },
                    correct_option="C",
                    explanation=(
                        "__str__ se usa para una salida mas amigable para usuarios, mientras que "
                        "__repr__ suele pensarse mas para desarrolladores."
                    ),
                    clue="Piensa en la salida bonita y directa al imprimir.",
                ),
                Question(
                    topic="Tipos de metodos",
                    prompt=(
                        "Que tipo de metodo conviene usar para validar si un saldo es negativo "
                        "sin depender de una cuenta concreta?"
                    ),
                    options={
                        "A": "Metodo estatico",
                        "B": "Metodo de instancia",
                        "C": "Constructor",
                        "D": "Metodo magico __lt__",
                    },
                    correct_option="A",
                    explanation=(
                        "Si la logica no depende ni del objeto actual ni de la clase como tal, "
                        "un metodo estatico es una buena opcion."
                    ),
                    clue="La validacion funciona como utilidad aislada.",
                ),
                Question(
                    topic="Polimorfismo",
                    prompt=(
                        "Dos clases distintas responden al metodo `retirar()` de formas "
                        "diferentes. Que concepto describe eso?"
                    ),
                    options={
                        "A": "Indexacion",
                        "B": "Polimorfismo",
                        "C": "Sintaxis",
                        "D": "Importacion circular",
                    },
                    correct_option="B",
                    explanation=(
                        "El polimorfismo permite que un mismo mensaje o metodo tenga "
                        "comportamientos distintos segun el objeto."
                    ),
                    clue="Mismo nombre, distinta respuesta.",
                ),
            ],
            "Laboratorio de Biblioteca Estandar": [
                Question(
                    topic="math",
                    prompt=(
                        "Si necesitas calcular una raiz cuadrada rapidamente, que modulo te ayuda?"
                    ),
                    options={
                        "A": "datetime",
                        "B": "statistics",
                        "C": "math",
                        "D": "pathlib",
                    },
                    correct_option="C",
                    explanation=(
                        "El modulo math trae funciones matematicas como sqrt, log, ceil y factorial."
                    ),
                    clue="Es el mas natural para operaciones matematicas puras.",
                ),
                Question(
                    topic="datetime",
                    prompt=(
                        "Que modulo conviene usar para poner la fecha de generacion de un reporte?"
                    ),
                    options={
                        "A": "datetime",
                        "B": "random",
                        "C": "statistics",
                        "D": "os",
                    },
                    correct_option="A",
                    explanation=(
                        "datetime permite obtener la fecha actual, formatearla y hacer operaciones "
                        "con fechas y horas."
                    ),
                    clue="Piensa en fechas, horas y formatos legibles.",
                ),
                Question(
                    topic="statistics",
                    prompt=(
                        "Si quieres sacar el promedio de varios puntajes, cual modulo ayuda mas?"
                    ),
                    options={
                        "A": "pathlib",
                        "B": "statistics",
                        "C": "math",
                        "D": "json",
                    },
                    correct_option="B",
                    explanation=(
                        "statistics incluye funciones como mean, median, mode y stdev para "
                        "resumir datos numericos."
                    ),
                    clue="Piensa en promedios, mediana y dispersion.",
                ),
                Question(
                    topic="pathlib",
                    prompt=(
                        "Que modulo moderno facilita trabajar con rutas y archivos de forma clara?"
                    ),
                    options={
                        "A": "pathlib",
                        "B": "time",
                        "C": "statistics",
                        "D": "math",
                    },
                    correct_option="A",
                    explanation=(
                        "pathlib hace mas legible el trabajo con rutas, nombres de archivo y "
                        "verificaciones de existencia."
                    ),
                    clue="Se centra en paths o rutas.",
                ),
                Question(
                    topic="time",
                    prompt=(
                        "Si quieres medir cuanto tarda una operacion en ejecutarse, cual modulo "
                        "te sirve mejor?"
                    ),
                    options={
                        "A": "time",
                        "B": "json",
                        "C": "math",
                        "D": "collections",
                    },
                    correct_option="A",
                    explanation=(
                        "El modulo time permite medir tiempos de ejecucion y pausar el programa "
                        "cuando hace falta."
                    ),
                    clue="Se usa mucho para cronometros simples.",
                ),
                Question(
                    topic="json",
                    prompt=(
                        "Si quieres guardar el ranking del juego para reutilizarlo luego, que "
                        "formato es una opcion practica?"
                    ),
                    options={
                        "A": "PNG",
                        "B": "JSON",
                        "C": "MP3",
                        "D": "ZIP",
                    },
                    correct_option="B",
                    explanation=(
                        "JSON es un formato de texto muy comodo para almacenar datos estructurados "
                        "como listas, puntajes y configuraciones."
                    ),
                    clue="Se usa mucho para intercambio y persistencia ligera de datos.",
                ),
            ],
        }


def wrap(text: str) -> str:
    return textwrap.fill(text, width=72)


def main() -> None:
    random.seed()
    game = MissionBankGame()
    game.run()


if __name__ == "__main__":
    main()
