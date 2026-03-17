const STORAGE_KEY = "mision-banco-millonario-history";
const TURN_TIME = 20;
const MIN_PLAYERS = 2;
const MAX_PLAYERS = 4;
const LEVELS = [100, 200, 400, 800, 1600, 3200];
const SAFE_LEVELS = new Set([1, 3, 5]);

const characters = [
  {
    id: "ada",
    emoji: "🧠",
    name: "Ada Analitica",
    role: "Experta en biblioteca estandar",
    perk: "Suma 50 puntos extra al acertar preguntas de biblioteca estandar.",
  },
  {
    id: "bruno",
    emoji: "🐞",
    name: "Bruno BugHunter",
    role: "Cazador de errores",
    perk: "Suma 50 puntos extra al acertar preguntas de errores y excepciones.",
  },
  {
    id: "clara",
    emoji: "🏛️",
    name: "Clara Clase",
    role: "Arquitecta POO",
    perk: "Suma 50 puntos extra al acertar preguntas de clases y objetos.",
  },
  {
    id: "diego",
    emoji: "🛠️",
    name: "Diego Debug",
    role: "Segunda oportunidad",
    perk: "Puede fallar una vez en toda la partida y responder de nuevo.",
  },
  {
    id: "elena",
    emoji: "🛡️",
    name: "Elena Excepcion",
    role: "Controladora de pistas",
    perk: "Usa pistas sin penalizacion de puntos.",
  },
  {
    id: "sofia",
    emoji: "⚡",
    name: "Sofia Speed",
    role: "Velocidad de ejecucion",
    perk: "Suma 75 puntos extra si responde bien en menos de 8 segundos.",
  },
];

const questionBank = [
  {
    id: "err-1",
    difficulty: 0,
    category: "errores",
    mission: "Errores y Excepciones",
    topic: "Errores de sintaxis",
    prompt: "En `if x > 3` sin dos puntos al final, que error aparece?",
    options: ["TypeError", "SyntaxError", "KeyError", "ValueError"],
    correctIndex: 1,
    explanation:
      "Es un error de sintaxis porque Python no puede interpretar la estructura del codigo antes de ejecutarlo.",
    clue: "Piensa si el problema ocurre antes o durante la ejecucion.",
  },
  {
    id: "err-2",
    difficulty: 0,
    category: "errores",
    mission: "Errores y Excepciones",
    topic: "ZeroDivisionError",
    prompt: "Que excepcion aparece al ejecutar `10 / 0`?",
    options: ["IndexError", "ValueError", "ZeroDivisionError", "ImportError"],
    correctIndex: 2,
    explanation:
      "Dividir por cero produce `ZeroDivisionError`, una excepcion que ocurre en tiempo de ejecucion.",
    clue: "La pista esta en el nombre de la operacion que falla.",
  },
  {
    id: "err-3",
    difficulty: 1,
    category: "errores",
    mission: "Errores y Excepciones",
    topic: "try/except",
    prompt: "Cual es la mejor practica al usar `except`?",
    options: [
      "Capturar errores especificos",
      "Usar siempre un except vacio",
      "Ocultar el error sin decir nada",
      "Evitar try para que el codigo sea corto",
    ],
    correctIndex: 0,
    explanation:
      "Capturar excepciones especificas mejora la claridad, evita ocultar problemas y permite dar mensajes utiles.",
    clue: "La respuesta correcta no intenta esconder el problema.",
  },
  {
    id: "err-4",
    difficulty: 1,
    category: "errores",
    mission: "Errores y Excepciones",
    topic: "finally",
    prompt: "Que describe mejor el bloque `finally`?",
    options: [
      "Solo se ejecuta si no hay error",
      "Solo se ejecuta si hay error",
      "Siempre se ejecuta",
      "Sirve solo para imprimir mensajes",
    ],
    correctIndex: 2,
    explanation:
      "`finally` siempre se ejecuta y por eso es muy util para cerrar archivos o liberar recursos.",
    clue: "Piensa en tareas que deben pasar pase lo que pase.",
  },
  {
    id: "err-5",
    difficulty: 2,
    category: "errores",
    mission: "Errores y Excepciones",
    topic: "raise",
    prompt: "Que haces al escribir `raise ValueError('edad invalida')`?",
    options: [
      "Ignoras un error",
      "Lanzas una excepcion manualmente",
      "Creas una variable",
      "Conviertes texto en entero",
    ],
    correctIndex: 1,
    explanation:
      "`raise` permite detener el flujo cuando tu propia logica detecta un dato invalido.",
    clue: "Tu codigo decide actuar aunque Python aun no haya explotado.",
  },
  {
    id: "err-6",
    difficulty: 2,
    category: "errores",
    mission: "Errores y Excepciones",
    topic: "Excepciones personalizadas",
    prompt: "Por que seria util crear `SaldoInsuficienteError`?",
    options: [
      "Porque cualquier error sirve",
      "Porque comunica mejor un problema del dominio",
      "Porque evita usar clases",
      "Porque reemplaza a `Exception`",
    ],
    correctIndex: 1,
    explanation:
      "Las excepciones personalizadas hacen que el programa exprese mejor el problema real del contexto.",
    clue: "Piensa en una app bancaria de verdad.",
  },
  {
    id: "poo-1",
    difficulty: 0,
    category: "poo",
    mission: "Programacion Orientada a Objetos",
    topic: "Clases",
    prompt: "Una clase en Python se parece mas a:",
    options: [
      "Un molde para crear objetos",
      "Una variable global",
      "Una excepcion",
      "Un archivo de texto",
    ],
    correctIndex: 0,
    explanation:
      "Una clase define estructura y comportamiento; luego se crean objetos concretos a partir de ella.",
    clue: "Piensa en un plano y luego en la construccion real.",
  },
  {
    id: "poo-2",
    difficulty: 0,
    category: "poo",
    mission: "Programacion Orientada a Objetos",
    topic: "self",
    prompt: "Que representa `self` dentro de un metodo de instancia?",
    options: [
      "El archivo donde esta la clase",
      "La clase completa",
      "El objeto actual",
      "Una palabra reservada para listas",
    ],
    correctIndex: 2,
    explanation:
      "`self` referencia a la instancia actual y por eso puede acceder a sus atributos y metodos.",
    clue: "Es la forma de hablar del objeto que recibio la llamada.",
  },
  {
    id: "poo-3",
    difficulty: 1,
    category: "poo",
    mission: "Programacion Orientada a Objetos",
    topic: "Herencia",
    prompt: "Si `CuentaAhorros` hereda de `CuentaBancaria`, cual es una ventaja clara?",
    options: [
      "Reutilizar codigo comun",
      "Eliminar atributos del padre",
      "Evitar constructores",
      "No usar metodos",
    ],
    correctIndex: 0,
    explanation:
      "La herencia permite reutilizar comportamiento compartido y especializar solo lo que cambia.",
    clue: "La palabra clave es reutilizacion.",
  },
  {
    id: "poo-4",
    difficulty: 1,
    category: "poo",
    mission: "Programacion Orientada a Objetos",
    topic: "__str__",
    prompt: "Que metodo especial define en general la salida de `print(objeto)`?",
    options: ["__len__", "__str__", "__eq__", "__lt__"],
    correctIndex: 1,
    explanation:
      "`__str__` ofrece una representacion amigable para el usuario cuando se imprime un objeto.",
    clue: "Es la salida en texto mas legible.",
  },
  {
    id: "poo-5",
    difficulty: 2,
    category: "poo",
    mission: "Programacion Orientada a Objetos",
    topic: "Metodos estaticos",
    prompt: "Que tipo de metodo usarias para validar un saldo sin depender de una cuenta concreta?",
    options: ["Metodo estatico", "Metodo de instancia", "Metodo magico", "Herencia"],
    correctIndex: 0,
    explanation:
      "Un metodo estatico sirve cuando la logica esta relacionada con la clase, pero no necesita ni `self` ni `cls`.",
    clue: "No depende del objeto actual.",
  },
  {
    id: "poo-6",
    difficulty: 2,
    category: "poo",
    mission: "Programacion Orientada a Objetos",
    topic: "Polimorfismo",
    prompt: "Dos clases responden a `retirar()` de formas distintas. Eso es:",
    options: ["Encapsulacion", "Polimorfismo", "Indexacion", "Casting"],
    correctIndex: 1,
    explanation:
      "El polimorfismo permite que el mismo mensaje produzca comportamientos distintos segun el objeto.",
    clue: "Mismo metodo, distinta respuesta.",
  },
  {
    id: "bib-1",
    difficulty: 0,
    category: "biblioteca",
    mission: "Biblioteca Estandar",
    topic: "math",
    prompt: "Que modulo te ayuda a calcular una raiz cuadrada?",
    options: ["math", "time", "pathlib", "json"],
    correctIndex: 0,
    explanation:
      "`math` incluye funciones matematicas como `sqrt`, `factorial`, `log` y otras.",
    clue: "Es el modulo mas directo para calculos puros.",
  },
  {
    id: "bib-2",
    difficulty: 0,
    category: "biblioteca",
    mission: "Biblioteca Estandar",
    topic: "datetime",
    prompt: "Que modulo usarias para poner la fecha actual en un reporte?",
    options: ["statistics", "datetime", "random", "os"],
    correctIndex: 1,
    explanation:
      "`datetime` sirve para fechas, horas y formateos de tiempo.",
    clue: "Piensa en calendarios y relojes.",
  },
  {
    id: "bib-3",
    difficulty: 1,
    category: "biblioteca",
    mission: "Biblioteca Estandar",
    topic: "statistics",
    prompt: "Cual modulo ayuda a calcular promedio, mediana y desviacion estandar?",
    options: ["statistics", "json", "pathlib", "math"],
    correctIndex: 0,
    explanation:
      "`statistics` resume conjuntos de datos numericos con funciones ya preparadas.",
    clue: "Piensa en analisis descriptivo.",
  },
  {
    id: "bib-4",
    difficulty: 1,
    category: "biblioteca",
    mission: "Biblioteca Estandar",
    topic: "pathlib",
    prompt: "Que modulo moderno facilita trabajar con rutas y archivos?",
    options: ["time", "collections", "pathlib", "statistics"],
    correctIndex: 2,
    explanation:
      "`pathlib` hace mas claro el trabajo con rutas, nombres de archivo y verificaciones.",
    clue: "Su nombre ya sugiere trabajar con paths.",
  },
  {
    id: "bib-5",
    difficulty: 2,
    category: "biblioteca",
    mission: "Biblioteca Estandar",
    topic: "time",
    prompt: "Si quieres medir cuanto tarda una operacion en ejecutarse, que modulo usaras?",
    options: ["time", "datetime", "json", "math"],
    correctIndex: 0,
    explanation:
      "`time` es muy util para cronometros simples y pausas de ejecucion.",
    clue: "Piensa en un cronometro.",
  },
  {
    id: "bib-6",
    difficulty: 2,
    category: "biblioteca",
    mission: "Biblioteca Estandar",
    topic: "json",
    prompt: "Si quieres guardar un ranking estructurado, que formato es muy practico?",
    options: ["PNG", "JSON", "GIF", "MP3"],
    correctIndex: 1,
    explanation:
      "JSON es ideal para guardar objetos y listas de forma estructurada y ligera.",
    clue: "Formato de texto para intercambio de datos.",
  },
];

const state = {
  setupPlayers: [],
  rounds: 4,
  players: [],
  turnIndex: 0,
  currentQuestion: null,
  currentQuestionStart: 0,
  currentHintUsed: false,
  currentRetryUsedOnQuestion: false,
  currentValue: LEVELS[0],
  timeLeft: TURN_TIME,
  timerInterval: null,
  audioEnabled: false,
  audioContext: null,
  lastUrgencySecond: null,
  history: loadHistory(),
};

const dom = {};

document.addEventListener("DOMContentLoaded", () => {
  cacheDom();
  bootstrapSetup();
  bindEvents();
  renderCharacterGallery();
  renderSetupPlayers();
  setSetupMessage("Puedes iniciar de una vez o cambiar nombres, personajes y niveles.");
  renderHistory();
});

function cacheDom() {
  dom.setupScreen = document.getElementById("setup-screen");
  dom.gameScreen = document.getElementById("game-screen");
  dom.resultsScreen = document.getElementById("results-screen");
  dom.playersForm = document.getElementById("players-form");
  dom.characterGallery = document.getElementById("character-gallery");
  dom.setupMessage = document.getElementById("setup-message");
  dom.roundsInput = document.getElementById("rounds-input");
  dom.addPlayerBtn = document.getElementById("add-player-btn");
  dom.startGameBtn = document.getElementById("start-game-btn");
  dom.audioToggleBtn = document.getElementById("audio-toggle-btn");
  dom.scoreboard = document.getElementById("scoreboard");
  dom.turnLabel = document.getElementById("turn-label");
  dom.turnSubtitle = document.getElementById("turn-subtitle");
  dom.timerBar = document.getElementById("timer-bar");
  dom.timerText = document.getElementById("timer-text");
  dom.missionBadge = document.getElementById("mission-badge");
  dom.topicBadge = document.getElementById("topic-badge");
  dom.questionValueBadge = document.getElementById("question-value-badge");
  dom.questionTitle = document.getElementById("question-title");
  dom.questionText = document.getElementById("question-text");
  dom.optionsContainer = document.getElementById("options-container");
  dom.clueBtn = document.getElementById("clue-btn");
  dom.skipBtn = document.getElementById("skip-btn");
  dom.feedbackBox = document.getElementById("feedback-box");
  dom.ladderBoard = document.getElementById("ladder-board");
  dom.winnerCard = document.getElementById("winner-card");
  dom.resultsTable = document.getElementById("results-table");
  dom.historyTable = document.getElementById("history-table");
  dom.playAgainBtn = document.getElementById("play-again-btn");
  dom.backSetupBtn = document.getElementById("back-setup-btn");
}

function bootstrapSetup() {
  state.setupPlayers = [createSetupPlayer(), createSetupPlayer()];
  state.setupPlayers[0].name = "Jugador 1";
  state.setupPlayers[1].name = "Jugador 2";
  setShowState("setup");
}

function bindEvents() {
  dom.addPlayerBtn.addEventListener("click", addSetupPlayer);
  dom.startGameBtn.addEventListener("click", startGame);
  dom.audioToggleBtn.addEventListener("click", toggleAudio);
  dom.roundsInput.addEventListener("change", () => {
    const value = clamp(Number(dom.roundsInput.value), 3, 6);
    state.rounds = value;
    dom.roundsInput.value = value;
  });
  dom.clueBtn.addEventListener("click", showClue);
  dom.skipBtn.addEventListener("click", skipTurn);
  dom.playAgainBtn.addEventListener("click", startGame);
  dom.backSetupBtn.addEventListener("click", () => {
    stopTimer();
    setShowState("setup");
    showScreen("setup");
  });
}

function createSetupPlayer() {
  const defaultCharacter = characters[state.setupPlayers.length % characters.length];
  return {
    id: createId(),
    name: `Jugador ${state.setupPlayers.length + 1}`,
    characterId: defaultCharacter.id,
  };
}

function createId() {
  if (window.crypto && typeof window.crypto.randomUUID === "function") {
    return window.crypto.randomUUID();
  }
  return `id-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function addSetupPlayer() {
  if (state.setupPlayers.length >= MAX_PLAYERS) {
    setSetupMessage("Solo se permiten hasta 4 jugadores.", true);
    return;
  }
  state.setupPlayers.push(createSetupPlayer());
  renderSetupPlayers();
  setSetupMessage("");
}

function removeSetupPlayer(playerId) {
  if (state.setupPlayers.length <= MIN_PLAYERS) {
    setSetupMessage("La partida necesita al menos 2 jugadores.", true);
    return;
  }
  state.setupPlayers = state.setupPlayers.filter((player) => player.id !== playerId);
  renderSetupPlayers();
  setSetupMessage("");
}

function renderSetupPlayers() {
  dom.playersForm.innerHTML = "";

  state.setupPlayers.forEach((player, index) => {
    const card = document.createElement("div");
    card.className = "player-card";

    const meta = document.createElement("div");
    meta.className = "player-meta";

    const nameField = document.createElement("label");
    nameField.className = "field";
    nameField.innerHTML = `
      <span>Jugador ${index + 1}</span>
      <input type="text" value="${escapeHtml(player.name)}" placeholder="Nombre del jugador" />
    `;
    nameField.querySelector("input").addEventListener("input", (event) => {
      player.name = event.target.value;
    });

    const selectField = document.createElement("label");
    selectField.className = "field";
    selectField.innerHTML = `
      <span>Personaje</span>
      <select></select>
    `;
    const select = selectField.querySelector("select");
    characters.forEach((character) => {
      const option = document.createElement("option");
      option.value = character.id;
      option.textContent = `${character.emoji} ${character.name}`;
      option.selected = player.characterId === character.id;
      select.appendChild(option);
    });
    select.addEventListener("change", (event) => {
      player.characterId = event.target.value;
    });

    meta.appendChild(nameField);
    meta.appendChild(selectField);
    card.appendChild(meta);

    if (state.setupPlayers.length > MIN_PLAYERS) {
      const removeButton = document.createElement("button");
      removeButton.type = "button";
      removeButton.className = "remove-btn";
      removeButton.textContent = "Eliminar";
      removeButton.addEventListener("click", () => removeSetupPlayer(player.id));
      card.appendChild(removeButton);
    }

    dom.playersForm.appendChild(card);
  });
}

function renderCharacterGallery() {
  dom.characterGallery.innerHTML = "";
  characters.forEach((character) => {
    const card = document.createElement("article");
    card.className = "character-card";
    card.innerHTML = `
      <h3>${character.emoji} ${character.name}</h3>
      <p class="character-role">${character.role}</p>
      <p class="character-perk">${character.perk}</p>
    `;
    dom.characterGallery.appendChild(card);
  });
}

function setSetupMessage(message, isError = false) {
  dom.setupMessage.textContent = message;
  dom.setupMessage.style.color = isError ? "#fda4af" : "#93c5fd";
}

function validateSetup() {
  const roundsValue = Number(dom.roundsInput.value);
  if (!Number.isInteger(roundsValue) || roundsValue < 3 || roundsValue > 6) {
    return { ok: false, message: "Los niveles por jugador deben estar entre 3 y 6." };
  }

  state.setupPlayers.forEach((player, index) => {
    if (!player.name.trim()) {
      player.name = `Jugador ${index + 1}`;
    }
  });

  const names = state.setupPlayers.map((player) => player.name.trim());

  const lowerNames = names.map((name) => name.toLowerCase());
  if (new Set(lowerNames).size !== lowerNames.length) {
    return { ok: false, message: "Los nombres deben ser unicos." };
  }

  const selectedCharacters = state.setupPlayers.map((player) => player.characterId);
  if (new Set(selectedCharacters).size !== selectedCharacters.length) {
    return { ok: false, message: "Cada jugador debe tener un personaje distinto." };
  }

  return { ok: true };
}

function startGame() {
  const validation = validateSetup();
  if (!validation.ok) {
    setSetupMessage(validation.message, true);
    showScreen("setup");
    return;
  }

  stopTimer();
  setSetupMessage("");
  playSound("start");
  setShowState("thinking");
  state.rounds = clamp(Number(dom.roundsInput.value), 3, 6);
  state.turnIndex = 0;
  state.currentQuestion = null;
  state.currentHintUsed = false;
  state.currentRetryUsedOnQuestion = false;
  state.players = state.setupPlayers.map((draft) => {
    const character = characters.find((item) => item.id === draft.characterId);
    return {
      id: draft.id,
      name: draft.name.trim(),
      character,
      score: 0,
      answered: 0,
      correct: 0,
      streak: 0,
      maxStreak: 0,
      usedQuestionIds: [],
      retryAvailable: character.id === "diego",
      guaranteedScore: 0,
    };
  });

  showScreen("game");
  renderScoreboard();
  loadTurn();
}

function loadTurn() {
  const totalTurns = state.rounds * state.players.length;
  if (state.turnIndex >= totalTurns) {
    endGame();
    return;
  }

  const player = getCurrentPlayer();
  const questionLevel = player.answered;
  state.currentValue = LEVELS[questionLevel];
  state.currentQuestion = getQuestionForPlayer(player, questionLevel);
  state.currentHintUsed = false;
  state.currentRetryUsedOnQuestion = false;
  state.currentQuestionStart = performance.now();
  state.timeLeft = TURN_TIME;
  state.lastUrgencySecond = null;

  renderScoreboard();
  renderLadder(player, questionLevel);
  renderQuestion(player, state.currentQuestion, questionLevel);
  setShowState("thinking");
  playSound("question");
  startTimer();
}

function renderScoreboard() {
  dom.scoreboard.innerHTML = "";
  const currentPlayer = getCurrentPlayer();

  state.players.forEach((player) => {
    const card = document.createElement("div");
    card.className = "score-card";
    if (currentPlayer && player.id === currentPlayer.id) {
      card.classList.add("active-turn");
    }

    card.innerHTML = `
      <div class="score-top">
        <div class="score-meta">
          <span class="score-name">${player.character.emoji} ${escapeHtml(player.name)}</span>
          <span class="score-character">${player.character.name}</span>
        </div>
        <span class="score-points">${formatMoney(player.score)}</span>
      </div>
      <div class="score-bottom">
        <span>Aciertos: ${player.correct}/${player.answered}</span>
        <span>Seguro: ${formatMoney(player.guaranteedScore)}</span>
      </div>
    `;
    dom.scoreboard.appendChild(card);
  });
}

function renderLadder(player, questionLevel) {
  dom.ladderBoard.innerHTML = "";

  for (let index = LEVELS.length - 1; index >= 0; index -= 1) {
    const step = document.createElement("div");
    step.className = "ladder-step";

    if (index < player.answered) {
      step.classList.add("earned");
    }
    if (index === questionLevel) {
      step.classList.add("current");
    }
    if (SAFE_LEVELS.has(index)) {
      step.classList.add("safe");
    }

    step.innerHTML = `
      <span class="ladder-level">Nivel ${index + 1}</span>
      <span class="ladder-value">${formatMoney(LEVELS[index])}</span>
    `;
    dom.ladderBoard.appendChild(step);
  }
}

function renderQuestion(player, question, questionLevel) {
  dom.missionBadge.textContent = question.mission;
  dom.topicBadge.textContent = `${capitalize(question.category)} · ${question.topic}`;
  dom.questionValueBadge.textContent = `Valor en juego: ${formatMoney(LEVELS[questionLevel])}`;
  dom.questionTitle.textContent = `${player.character.emoji} Turno de ${player.name}`;
  dom.questionText.textContent = question.prompt;
  dom.feedbackBox.className = "feedback-box hidden";
  dom.feedbackBox.textContent = "";
  dom.clueBtn.disabled = false;
  dom.skipBtn.disabled = false;
  dom.optionsContainer.innerHTML = "";

  question.options.forEach((option, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "option-btn";
    button.innerHTML = `
      <span class="option-label">${String.fromCharCode(65 + index)}</span>
      <span>${escapeHtml(option)}</span>
    `;
    button.addEventListener("click", () => submitAnswer(index, button));
    dom.optionsContainer.appendChild(button);
  });
}

function submitAnswer(selectedIndex, buttonElement) {
  if (!state.currentQuestion || buttonElement.disabled) {
    return;
  }

  const player = getCurrentPlayer();
  const isCorrect = selectedIndex === state.currentQuestion.correctIndex;

  if (
    !isCorrect &&
    player.character.id === "diego" &&
    player.retryAvailable &&
    !state.currentRetryUsedOnQuestion
  ) {
    state.currentRetryUsedOnQuestion = true;
    player.retryAvailable = false;
    buttonElement.disabled = true;
    buttonElement.classList.add("wrong");
    playSound("retry");
    setShowState("warning");
    showFeedback(
      "info",
      `${player.character.name} activa su segunda oportunidad. Vuelve a intentarlo, pero ahora con mas cuidado.`
    );
    return;
  }

  finishTurn({ selectedIndex, isCorrect, timedOut: false, skipped: false });
}

function showClue() {
  if (!state.currentQuestion || state.currentHintUsed) {
    return;
  }

  state.currentHintUsed = true;
  const player = getCurrentPlayer();
  const extra =
    player.character.id === "elena"
      ? `${player.character.name} usa esta pista sin penalizacion.`
      : "Usar pista reducira 50 puntos si respondes correctamente.";

  playSound("clue");
  setShowState("warning");
  showFeedback("info", `Pista: ${state.currentQuestion.clue} ${extra}`);
}

function skipTurn() {
  finishTurn({ selectedIndex: -1, isCorrect: false, timedOut: false, skipped: true });
}

function finishTurn({ selectedIndex, isCorrect, timedOut, skipped }) {
  stopTimer();

  const player = getCurrentPlayer();
  const question = state.currentQuestion;
  const responseMs = performance.now() - state.currentQuestionStart;
  const optionButtons = [...dom.optionsContainer.querySelectorAll(".option-btn")];

  optionButtons.forEach((button, index) => {
    button.disabled = true;
    if (index === question.correctIndex) {
      button.classList.add("correct");
    }
    if (index === selectedIndex && index !== question.correctIndex) {
      button.classList.add("wrong");
    }
  });

  player.answered += 1;

  let pointsEarned = 0;
  let feedbackType = "error";
  let summary = "";
  const notes = [];

  if (isCorrect) {
    feedbackType = "success";
    player.correct += 1;
    player.streak += 1;
    player.maxStreak = Math.max(player.maxStreak, player.streak);

    pointsEarned = state.currentValue;

    if (state.currentHintUsed && player.character.id !== "elena") {
      pointsEarned = Math.max(pointsEarned - 50, 50);
      notes.push("Se descontaron 50 puntos por usar pista.");
    }

    const bonus = getCharacterBonus(player, question, responseMs);
    if (bonus.points > 0) {
      pointsEarned += bonus.points;
      notes.push(bonus.reason);
    }

    if (player.streak > 0 && player.streak % 3 === 0) {
      pointsEarned += 100;
      notes.push("Bonus de 100 puntos por racha de 3 aciertos.");
    }

    player.score += pointsEarned;
    updateGuaranteedScore(player);
    summary = `Respuesta correcta. Ganas ${formatMoney(pointsEarned)}.`;
    playSound("correct");
    setShowState("success");
  } else {
    player.streak = 0;
    if (timedOut) {
      summary = "Tiempo agotado. No sumas puntos en este turno.";
      playSound("timeout");
      setShowState("error");
    } else if (skipped) {
      summary = "Pregunta pasada. No sumas puntos en este turno.";
      playSound("skip");
      setShowState("warning");
    } else {
      summary = `Respuesta incorrecta. La opcion correcta era ${letterFromIndex(question.correctIndex)}.`;
      playSound("wrong");
      setShowState("error");
    }
  }

  const extraNotes = notes.length ? ` ${notes.join(" ")}` : "";
  const feedbackText = `${summary} Retroalimentacion: ${question.explanation}${extraNotes}`;
  showFeedback(feedbackType, feedbackText);
  renderScoreboard();
  renderLadder(player, player.answered);

  state.turnIndex += 1;
  window.setTimeout(loadTurn, 3200);
}

function getCharacterBonus(player, question, responseMs) {
  const elapsedSeconds = responseMs / 1000;

  if (player.character.id === "ada" && question.category === "biblioteca") {
    return { points: 50, reason: "Ada recibe 50 puntos extra por dominar biblioteca estandar." };
  }

  if (player.character.id === "bruno" && question.category === "errores") {
    return { points: 50, reason: "Bruno recibe 50 puntos extra por detectar errores." };
  }

  if (player.character.id === "clara" && question.category === "poo") {
    return { points: 50, reason: "Clara recibe 50 puntos extra por preguntas de POO." };
  }

  if (player.character.id === "sofia" && elapsedSeconds <= 8) {
    return { points: 75, reason: "Sofia recibe 75 puntos extra por responder rapido." };
  }

  return { points: 0, reason: "" };
}

function updateGuaranteedScore(player) {
  const lastClearedLevel = player.answered - 1;
  if (SAFE_LEVELS.has(lastClearedLevel)) {
    player.guaranteedScore = Math.max(player.guaranteedScore, LEVELS[lastClearedLevel]);
  }
}

function startTimer() {
  stopTimer();
  state.timeLeft = TURN_TIME;
  updateTimerUi();

  state.timerInterval = window.setInterval(() => {
    state.timeLeft -= 0.1;
    if (state.timeLeft <= 0) {
      state.timeLeft = 0;
      updateTimerUi();
      finishTurn({ selectedIndex: -1, isCorrect: false, timedOut: true, skipped: false });
      return;
    }
    updateTimerUi();
  }, 100);
}

function stopTimer() {
  if (state.timerInterval) {
    window.clearInterval(state.timerInterval);
    state.timerInterval = null;
  }
}

function updateTimerUi() {
  const player = getCurrentPlayer();
  const progress = Math.max(state.timeLeft / TURN_TIME, 0);
  dom.timerBar.style.transform = `scaleX(${progress})`;
  dom.timerText.textContent = `${state.timeLeft.toFixed(1)} segundos restantes`;

  if (state.timeLeft <= 5 && state.timeLeft > 0) {
    const currentSecond = Math.ceil(state.timeLeft);
    if (state.lastUrgencySecond !== currentSecond) {
      state.lastUrgencySecond = currentSecond;
      playSound("tick");
      setShowState("warning");
    }
  }

  if (player) {
    dom.turnLabel.textContent = `${player.character.emoji} ${player.name} esta en la silla caliente`;
    dom.turnSubtitle.textContent = `Seguridad actual: ${formatMoney(player.guaranteedScore)} · Puntaje total: ${formatMoney(player.score)}`;
  }
}

function showFeedback(type, text) {
  dom.feedbackBox.className = `feedback-box ${type}`;
  dom.feedbackBox.textContent = text;
}

function endGame() {
  stopTimer();
  playSound("victory");
  setShowState("results");
  showScreen("results");

  const ranking = [...state.players].sort((a, b) => {
    if (b.score !== a.score) {
      return b.score - a.score;
    }
    return b.correct - a.correct;
  });

  const winner = ranking[0];
  dom.winnerCard.innerHTML = `
    <h3>${winner.character.emoji} Ganador: ${escapeHtml(winner.name)}</h3>
    <p>${winner.character.name} domina la escalera y termina con ${formatMoney(winner.score)}.</p>
    <p>Precision: ${formatPercent(winner.correct, winner.answered)} · Seguro alcanzado: ${formatMoney(winner.guaranteedScore)}</p>
  `;

  dom.resultsTable.innerHTML = "";
  ranking.forEach((player, index) => {
    const row = document.createElement("div");
    row.className = "result-row";
    row.innerHTML = `
      <div class="result-rank">#${index + 1}</div>
      <div class="result-main">
        <div class="result-name">${player.character.emoji} ${escapeHtml(player.name)}</div>
        <div class="result-subtitle">${player.character.name} · Aciertos ${player.correct}/${player.answered} · Seguro ${formatMoney(player.guaranteedScore)}</div>
      </div>
      <div class="result-value">${formatMoney(player.score)}</div>
    `;
    dom.resultsTable.appendChild(row);
  });

  saveMatch(ranking);
  renderHistory();
}

function saveMatch(ranking) {
  const winner = ranking[0];
  const record = {
    id: createId(),
    playedAt: new Date().toISOString(),
    winnerName: winner.name,
    winnerEmoji: winner.character.emoji,
    winnerCharacter: winner.character.name,
    winnerScore: winner.score,
  };

  state.history.unshift(record);
  state.history = state.history.slice(0, 12);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.history));
}

function renderHistory() {
  dom.historyTable.innerHTML = "";

  if (!state.history.length) {
    const row = document.createElement("div");
    row.className = "result-row";
    row.innerHTML = `
      <div class="result-main">
        <div class="result-name">Todavia no hay partidas guardadas.</div>
        <div class="result-subtitle">Al terminar una partida aparecera aqui el ganador.</div>
      </div>
    `;
    dom.historyTable.appendChild(row);
    return;
  }

  state.history.forEach((match, index) => {
    const row = document.createElement("div");
    row.className = "result-row";
    const dateText = new Date(match.playedAt).toLocaleString("es-CO");
    row.innerHTML = `
      <div class="result-rank">#${index + 1}</div>
      <div class="result-main">
        <div class="result-name">${match.winnerEmoji} ${escapeHtml(match.winnerName)}</div>
        <div class="result-subtitle">${match.winnerCharacter} · ${dateText}</div>
      </div>
      <div class="result-value">${formatMoney(match.winnerScore)}</div>
    `;
    dom.historyTable.appendChild(row);
  });
}

function getCurrentPlayer() {
  if (!state.players.length) {
    return null;
  }
  return state.players[state.turnIndex % state.players.length];
}

function getQuestionForPlayer(player, questionLevel) {
  const pool = questionBank.filter(
    (question) =>
      question.difficulty === Math.min(questionLevel, 2) &&
      !player.usedQuestionIds.includes(question.id)
  );

  const fallbackPool = questionBank.filter(
    (question) => !player.usedQuestionIds.includes(question.id)
  );

  const usablePool = pool.length ? pool : fallbackPool.length ? fallbackPool : questionBank;
  const question = usablePool[Math.floor(Math.random() * usablePool.length)];
  player.usedQuestionIds.push(question.id);
  return question;
}

function showScreen(screenName) {
  dom.setupScreen.classList.toggle("active", screenName === "setup");
  dom.gameScreen.classList.toggle("active", screenName === "game");
  dom.resultsScreen.classList.toggle("active", screenName === "results");

  if (screenName === "setup") {
    setShowState("setup");
  }
}

function toggleAudio() {
  state.audioEnabled = !state.audioEnabled;

  if (state.audioEnabled) {
    ensureAudioContext();
    dom.audioToggleBtn.textContent = "Audio: encendido";
    dom.audioToggleBtn.classList.add("active");
    playSound("toggleOn");
  } else {
    dom.audioToggleBtn.textContent = "Audio: apagado";
    dom.audioToggleBtn.classList.remove("active");
  }
}

function ensureAudioContext() {
  if (!state.audioContext) {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) {
      return null;
    }
    state.audioContext = new AudioContextClass();
  }

  if (state.audioContext.state === "suspended") {
    state.audioContext.resume();
  }

  return state.audioContext;
}

function playSound(type) {
  if (!state.audioEnabled) {
    return;
  }

  const context = ensureAudioContext();
  if (!context) {
    return;
  }

  switch (type) {
    case "toggleOn":
      playToneSequence(context, [
        [523.25, 0.08, "sine", 0.03],
        [659.25, 0.1, "sine", 0.03],
      ]);
      break;
    case "start":
      playToneSequence(context, [
        [392, 0.08, "triangle", 0.04],
        [523.25, 0.1, "triangle", 0.04],
        [659.25, 0.14, "triangle", 0.05],
      ]);
      break;
    case "question":
      playToneSequence(context, [
        [330, 0.06, "sine", 0.02],
        [392, 0.08, "sine", 0.02],
      ]);
      break;
    case "correct":
      playToneSequence(context, [
        [523.25, 0.1, "triangle", 0.05],
        [659.25, 0.12, "triangle", 0.05],
        [783.99, 0.16, "triangle", 0.06],
      ]);
      break;
    case "wrong":
      playToneSequence(context, [
        [220, 0.12, "sawtooth", 0.045],
        [164.81, 0.16, "sawtooth", 0.04],
      ]);
      break;
    case "timeout":
      playToneSequence(context, [
        [180, 0.08, "square", 0.04],
        [180, 0.08, "square", 0.04],
        [120, 0.18, "square", 0.04],
      ]);
      break;
    case "tick":
      playToneSequence(context, [[900, 0.04, "square", 0.018]]);
      break;
    case "clue":
      playToneSequence(context, [[440, 0.08, "sine", 0.03]]);
      break;
    case "retry":
      playToneSequence(context, [
        [392, 0.06, "triangle", 0.03],
        [349.23, 0.06, "triangle", 0.03],
        [392, 0.1, "triangle", 0.03],
      ]);
      break;
    case "skip":
      playToneSequence(context, [[260, 0.06, "sine", 0.02]]);
      break;
    case "victory":
      playToneSequence(context, [
        [523.25, 0.08, "triangle", 0.04],
        [659.25, 0.08, "triangle", 0.04],
        [783.99, 0.12, "triangle", 0.05],
        [1046.5, 0.18, "triangle", 0.06],
      ]);
      break;
    default:
      break;
  }
}

function playToneSequence(context, sequence) {
  let start = context.currentTime;

  sequence.forEach(([frequency, duration, type, gainValue]) => {
    const oscillator = context.createOscillator();
    const gain = context.createGain();

    oscillator.type = type;
    oscillator.frequency.setValueAtTime(frequency, start);
    gain.gain.setValueAtTime(0.0001, start);
    gain.gain.exponentialRampToValueAtTime(gainValue, start + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, start + duration);

    oscillator.connect(gain);
    gain.connect(context.destination);

    oscillator.start(start);
    oscillator.stop(start + duration + 0.02);
    start += duration + 0.03;
  });
}

function setShowState(mode) {
  document.body.dataset.showState = mode;
}

function loadHistory() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch (_error) {
    return [];
  }
}

function formatMoney(value) {
  return new Intl.NumberFormat("es-CO", {
    style: "currency",
    currency: "COP",
    maximumFractionDigits: 0,
  }).format(value);
}

function formatPercent(correct, answered) {
  if (!answered) {
    return "0%";
  }
  return `${Math.round((correct / answered) * 100)}%`;
}

function capitalize(text) {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

function letterFromIndex(index) {
  return String.fromCharCode(65 + index);
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function escapeHtml(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}
