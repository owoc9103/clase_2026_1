/**
 * Angry Birds Académico — NumPy
 * Banco de 18 preguntas NumPy (orden aleatorio). Música: media/*.mp3 en bucle.
 */

const canvas = document.getElementById("game-canvas");
const ctx = canvas.getContext("2d");

const W = canvas.width;
const H = canvas.height;

/**
 * Banco de preguntas NumPy (18 ítems). En cada partida se baraja el orden.
 */
const QUESTIONS_BANK = [
  {
    prompt: "¿Cuál es el objeto principal de NumPy?",
    options: ["tuple", "ndarray", "list", "matrix"],
    correctIndex: 1,
  },
  {
    prompt: "¿Qué función se utiliza para crear un arreglo lleno de ceros?",
    options: ["np.full()", "np.ones()", "np.zeros()", "np.empty()"],
    correctIndex: 2,
  },
  {
    prompt: "¿Cuál es la forma (shape) de una matriz creada con np.zeros((3,4))?",
    options: ["(12,)", "(4,3)", "(2,6)", "(3,4)"],
    correctIndex: 3,
  },
  {
    prompt: "¿Qué representa el atributo ndim en un ndarray?",
    options: [
      "Tipo de dato",
      "Número de dimensiones (ejes)",
      "Número de elementos",
      "Número de filas",
    ],
    correctIndex: 1,
  },
  {
    prompt: "¿Cuál es el tamaño (size) de una matriz con forma (3,4)?",
    options: ["3", "4", "12", "7"],
    correctIndex: 2,
  },
  {
    prompt: "¿Qué función permite crear un arreglo con valores dentro de un rango?",
    options: ["np.arange()", "np.zeros()", "np.full()", "np.linspace()"],
    correctIndex: 0,
  },
  {
    prompt: "¿Cuál es la principal diferencia entre np.arange() y np.linspace()?",
    options: [
      "Son iguales",
      "arange incluye el valor final",
      "linspace define número de puntos y arange usa paso",
      "linspace no usa floats",
    ],
    correctIndex: 2,
  },
  {
    prompt: "¿Qué hace np.random.rand(3,4)?",
    options: [
      "Genera valores entre -1 y 1",
      "Genera ceros aleatorios",
      "Genera valores uniformes entre 0 y 1",
      "Genera enteros aleatorios",
    ],
    correctIndex: 2,
  },
  {
    prompt:
      "¿Qué tipo de dato devuelve NumPy por defecto al usar números enteros?",
    options: ["int64", "complex64", "float32", "int32"],
    correctIndex: 0,
  },
  {
    prompt: "¿Qué sucede al usar reshape() en un array?",
    options: [
      "Elimina elementos",
      "Cambia la forma sin cambiar los datos",
      "Cambia el tipo de dato",
      "Copia los datos",
    ],
    correctIndex: 1,
  },
  {
    prompt: "¿Qué ocurre si modificas un array creado con reshape()?",
    options: [
      "Solo cambia el nuevo array",
      "Se elimina el array",
      "No pasa nada",
      "También cambia el original",
    ],
    correctIndex: 3,
  },
  {
    prompt: "¿Qué operación realiza A * B en NumPy?",
    options: [
      "Multiplicación elemento a elemento",
      "Producto cruzado",
      "Multiplicación matricial",
      "Producto escalar",
    ],
    correctIndex: 0,
  },
  {
    prompt: "¿Qué es el broadcasting en NumPy?",
    options: [
      "Eliminar dimensiones",
      "Copiar arrays",
      "Ajustar dimensiones automáticamente para operar arrays",
      "Ordenar matrices",
    ],
    correctIndex: 2,
  },
  {
    prompt: "¿Qué resultado devuelve A[A < 25]?",
    options: [
      "Un error",
      "Un array con valores que cumplen la condición",
      "Un número",
      "Un booleano",
    ],
    correctIndex: 1,
  },
  {
    prompt: "¿Qué hace np.vstack()?",
    options: [
      "Apila matrices horizontalmente",
      "Cambia el tipo de dato",
      "Divide matrices",
      "Apila matrices verticalmente",
    ],
    correctIndex: 3,
  },
  {
    prompt: "¿Qué es una operación matricial en NumPy?",
    options: [
      "Una operación exclusiva para gráficos",
      "Una operación que sigue reglas del álgebra lineal entre matrices",
      "Una operación sobre listas de Python",
      "Una operación que se aplica solo a números escalares",
    ],
    correctIndex: 1,
  },
  {
    prompt:
      "Dadas A = [[1,2],[3,4]] y B = [[5,6],[7,8]], ¿cuál es el resultado de A + B?",
    options: [
      "[[5, 12], [21, 32]]",
      "[[1,2,5,6], [3,4,7,8]]",
      "Error",
      "[[6, 8], [10, 12]]",
    ],
    correctIndex: 3,
  },
  {
    prompt:
      "¿Cuál de las siguientes opciones realiza una multiplicación matricial en NumPy?",
    options: ["A / B", "A * B", "A.dot(B)", "A + B"],
    correctIndex: 2,
  },
];

/** Partida actual (orden aleatorio) */
let activeQuestions = [];

/** Gravedad; integración en subpasos para movimiento más suave */
const GRAVITY = 0.34;
const AIR_DRAG = 0.9992;
const PHYS_SUBSTEPS = 5;

const GROUND_Y = H - 70;
const SLING_X = 248;
const SLING_Y = 286;
const MAX_PULL = 260;
const POWER_SCALE = 0.22;
/** Radio de colisión (coherente con el dibujo del pájaro) */
const BIRD_R = 16;

const TARGET_COL_W = 268;
const TARGET_ROW_H = 56;
const TARGET_GAP = 8;
const TARGET_PAD_RIGHT = 28;

const LABELS = ["A", "B", "C", "D"];

let playerName = "";
let sessionId = "";
let connectionFingerprint = "";
/** Último resultado para descarga */
let lastResultPayload = null;

let qIndex = 0;
let totalLaunches = 0;
let t0Game = 0;
let gameEnded = false;
let rafId = 0;

let bird = {
  x: SLING_X,
  y: SLING_Y,
  vx: 0,
  vy: 0,
  flying: false,
};

let drag = { active: false };
let targets = [];

function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function initSessionId() {
  try {
    sessionId =
      sessionStorage.getItem("angry_numpy_session") || crypto.randomUUID();
    sessionStorage.setItem("angry_numpy_session", sessionId);
  } catch {
    sessionId = `sess-${Date.now()}-${Math.random().toString(36).slice(2, 11)}`;
  }
  const ua = navigator.userAgent || "";
  connectionFingerprint = [
    `lang=${navigator.language}`,
    `tz=${Intl.DateTimeFormat().resolvedOptions().timeZone}`,
    `screen=${screen.width}x${screen.height}`,
    `ua=${ua.slice(0, 96)}`,
  ].join(" | ");
}

function buildTargets() {
  const q = activeQuestions[qIndex];
  const n = q.options.length;
  const tw = TARGET_COL_W;
  const th = TARGET_ROW_H;
  const gap = TARGET_GAP;
  const bottomMargin = 12;
  const colX = W - tw - TARGET_PAD_RIGHT;
  targets = [];
  for (let i = 0; i < n; i++) {
    const y = GROUND_Y - bottomMargin - (n - i) * th - (n - 1 - i) * gap;
    targets.push({
      x: colX,
      y,
      w: tw,
      h: th,
      optIndex: i,
      label: LABELS[i],
      hit: false,
    });
  }
}

function showToast(msg, kind) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.className = `show ${kind}`;
  clearTimeout(showToast._t);
  showToast._t = setTimeout(() => {
    el.className = "";
  }, 1800);
}

/**
 * Calificación por rangos (N preguntas → ideal N lanzamientos).
 * Nivel 0 = mejor. Más lanzamientos o más tiempo → niveles más altos → nota más baja.
 */
const GRADING_LAUNCH_EXCESS_MAX = [2, 5, 9, 14, 22, 32, 45, 60];
const GRADING_TIME_MAX_SEC = [72, 100, 135, 175, 220, 275, 340, 420, 520];

function launchLevel(totalLaunches, nPreguntas) {
  const exceso = totalLaunches - nPreguntas;
  if (exceso <= 0) return 0;
  for (let i = 0; i < GRADING_LAUNCH_EXCESS_MAX.length; i++) {
    if (exceso <= GRADING_LAUNCH_EXCESS_MAX[i]) return i + 1;
  }
  return 9;
}

function timeLevel(totalSec) {
  if (totalSec <= GRADING_TIME_MAX_SEC[0]) return 0;
  for (let i = 1; i < GRADING_TIME_MAX_SEC.length; i++) {
    if (totalSec <= GRADING_TIME_MAX_SEC[i]) return i;
  }
  return 9;
}

/** Rango de lanzamientos totales para cada nivel (según N preguntas) */
function launchRangeLabel(nivel, n) {
  if (nivel === 0) return `${n} (sin exceso)`;
  if (nivel === 9) return `≥ ${n + GRADING_LAUNCH_EXCESS_MAX[7] + 1}`;
  const lowEx = nivel === 1 ? 1 : GRADING_LAUNCH_EXCESS_MAX[nivel - 2] + 1;
  const highEx = GRADING_LAUNCH_EXCESS_MAX[nivel - 1];
  return `${n + lowEx} – ${n + highEx}`;
}

function timeRangeLabel(nivel) {
  if (nivel === 0) return `0 – ${GRADING_TIME_MAX_SEC[0]} s`;
  if (nivel === 9) return `> ${GRADING_TIME_MAX_SEC[8]} s`;
  const lo = GRADING_TIME_MAX_SEC[nivel - 1] + 1;
  const hi = GRADING_TIME_MAX_SEC[nivel];
  return `${lo} – ${hi} s`;
}

function notaFromNivelPromedio(promedio) {
  let g = 5 - (promedio / 9) * 2;
  g = Math.round(g * 5) / 5;
  return Math.min(5, Math.max(3, g));
}

function computeGrade() {
  const n = activeQuestions.length;
  const totalSec = (performance.now() - t0Game) / 1000;
  const levL = launchLevel(totalLaunches, n);
  const levT = timeLevel(totalSec);
  const promedio = (levL + levT) / 2;
  const nota = notaFromNivelPromedio(promedio);
  return {
    nota,
    totalSec,
    nivelLanzamientos: levL,
    nivelTiempo: levT,
    nivelPromedio: promedio,
    lanzamientos: totalLaunches,
    nPreguntas: n,
  };
}

/** Tablas de rangos en la pantalla de inicio (mismas reglas que computeGrade). */
function buildGradingLegendHTML(n) {
  let bodyL = "";
  for (let nivel = 0; nivel <= 9; nivel++) {
    bodyL += `<tr><td>${nivel}</td><td>${launchRangeLabel(nivel, n)}</td></tr>`;
  }
  let bodyT = "";
  for (let nivel = 0; nivel <= 9; nivel++) {
    bodyT += `<tr><td>${nivel}</td><td>${timeRangeLabel(nivel)}</td></tr>`;
  }
  let bodyP = "";
  for (let k = 0; k <= 18; k++) {
    const p = k / 2;
    const nota = notaFromNivelPromedio(p);
    const pLabel = p % 1 === 0 ? String(p) : p.toFixed(1);
    bodyP += `<tr><td>${pLabel}</td><td>${nota.toFixed(1)}</td></tr>`;
  }
  return (
    `<p>Se calculan dos niveles de <strong>0 (mejor)</strong> a <strong>9 (peor)</strong>: uno por los <strong>lanzamientos totales</strong> frente al ideal (${n} para ${n} preguntas) y otro por el <strong>tiempo total</strong>. La <strong>nota</strong> sale del <em>promedio</em> de esos dos niveles (tabla de abajo; escala 3–5 en pasos de 0,2).</p>` +
    `<div class="grade-tables-wrap">` +
    `<table class="grade-table"><caption>Lanzamientos totales</caption><thead><tr><th>Nivel</th><th>Rango</th></tr></thead><tbody>${bodyL}</tbody></table>` +
    `<table class="grade-table"><caption>Tiempo total</caption><thead><tr><th>Nivel</th><th>Rango</th></tr></thead><tbody>${bodyT}</tbody></table>` +
    `<table class="grade-table grade-table-wide"><caption>Promedio de los dos niveles → nota</caption><thead><tr><th>Promedio</th><th>Nota</th></tr></thead><tbody>${bodyP}</tbody></table>` +
    `</div>`
  );
}

function mountGradingLegend() {
  const root = document.getElementById("grading-table-root");
  if (root) {
    root.innerHTML = buildGradingLegendHTML(QUESTIONS_BANK.length);
  }
}

function endGame() {
  gameEnded = true;
  if (rafId) cancelAnimationFrame(rafId);
  const g = computeGrade();
  const lines = [
    `Nombre completo: ${playerName}`,
    `Nota (escala 3–5, pasos 0,2): ${g.nota.toFixed(1)}`,
    `Lanzamientos totales: ${totalLaunches} (ideal: ${activeQuestions.length})`,
    `Tiempo total: ${g.totalSec.toFixed(1)} s`,
    `Nivel lanzamientos: ${g.nivelLanzamientos}/9 | Nivel tiempo: ${g.nivelTiempo}/9 (promedio ${g.nivelPromedio.toFixed(1)})`,
    `Menor nivel = mejor desempeño. Ver tablas al inicio del juego.`,
    ``,
    `ID de sesión / jugador (navegador): ${sessionId}`,
    `Huella de entorno (no es IP): ${connectionFingerprint}`,
    ``,
    `La IP pública no está disponible en HTML puro sin servidor.`,
  ];
  document.getElementById("result-pre").textContent = lines.join("\n");

  lastResultPayload = {
    nombreCompleto: playerName,
    nota: g.nota,
    notaTexto: g.nota.toFixed(1),
    escala: "3 a 5, pasos 0.2",
    lanzamientos: totalLaunches,
    lanzamientosIdeal: activeQuestions.length,
    tiempoSegundos: Number(g.totalSec.toFixed(2)),
    nivelLanzamientos: g.nivelLanzamientos,
    nivelTiempo: g.nivelTiempo,
    nivelPromedio: Number(g.nivelPromedio.toFixed(2)),
    idSesion: sessionId,
    huellaEntorno: connectionFingerprint,
    preguntasEnPartida: activeQuestions.length,
    fechaISO: new Date().toISOString(),
  };

  document.getElementById("screen-game").classList.remove("active");
  document.getElementById("screen-end").classList.add("active");
  console.log("RESULTADO\n" + lines.join("\n"));
}

function updateHud() {
  document.getElementById("hud-q").textContent = `Pregunta ${qIndex + 1} / ${activeQuestions.length}`;
  const elapsed = (performance.now() - t0Game) / 1000;
  document.getElementById("hud-time").textContent = `Tiempo: ${elapsed.toFixed(1)} s`;
  document.getElementById("hud-launches").textContent = `Lanzamientos: ${totalLaunches}`;
}

function nextQuestion() {
  if (qIndex >= activeQuestions.length) {
    endGame();
    return;
  }
  buildTargets();
  resetBird();
  updateHud();
}

function resetBird() {
  bird.x = SLING_X;
  bird.y = SLING_Y;
  bird.vx = 0;
  bird.vy = 0;
  bird.flying = false;
}

function launchBird(dx, dy) {
  const len = Math.hypot(dx, dy) || 1;
  const pull = Math.min(len, MAX_PULL);
  const nx = dx / len;
  const ny = dy / len;
  const pullNorm = pull / MAX_PULL;
  /** Lanzamiento algo más suave + curva legible */
  const speed =
    pull * POWER_SCALE * (1 + 0.38 * pullNorm) * 0.88;
  bird.vx = -nx * speed;
  bird.vy = -ny * speed;
  bird.flying = true;
  totalLaunches += 1;
  updateHud();
}

function circleRect(cx, cy, r, rx, ry, rw, rh) {
  const nx = Math.max(rx, Math.min(cx, rx + rw));
  const ny = Math.max(ry, Math.min(cy, ry + rh));
  return (cx - nx) ** 2 + (cy - ny) ** 2 < r * r;
}

/**
 * Pájaro estilo caricatura (inspirado en juegos de lanzamiento tipo pájaro rojo).
 * Sin usar sprites externos.
 */
function drawAngryBirdSprite(x, y, angleRad) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angleRad);

  // Cuerpo
  ctx.beginPath();
  ctx.ellipse(0, 2, 17, 15, 0, 0, Math.PI * 2);
  ctx.fillStyle = "#d32f2f";
  ctx.fill();
  ctx.strokeStyle = "#7f0000";
  ctx.lineWidth = 2;
  ctx.stroke();

  // Vientre claro
  ctx.beginPath();
  ctx.ellipse(-1, 6, 11, 9, 0, 0, Math.PI * 2);
  ctx.fillStyle = "#ffccbc";
  ctx.fill();

  // Ojos (blanco)
  ctx.fillStyle = "#fff";
  ctx.beginPath();
  ctx.arc(-5, -4, 6, 0, Math.PI * 2);
  ctx.fill();
  ctx.beginPath();
  ctx.arc(5, -4, 6, 0, Math.PI * 2);
  ctx.fill();

  // Pupilas
  ctx.fillStyle = "#1a1a1a";
  ctx.beginPath();
  ctx.arc(-4, -3, 2.5, 0, Math.PI * 2);
  ctx.arc(6, -3, 2.5, 0, Math.PI * 2);
  ctx.fill();

  // Cejas
  ctx.strokeStyle = "#212121";
  ctx.lineWidth = 3;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(-10, -12);
  ctx.lineTo(-2, -10);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(2, -10);
  ctx.lineTo(10, -12);
  ctx.stroke();

  // Pico
  ctx.fillStyle = "#fbc02d";
  ctx.beginPath();
  ctx.moveTo(-2, 2);
  ctx.lineTo(0, 12);
  ctx.lineTo(4, 2);
  ctx.closePath();
  ctx.fill();
  ctx.strokeStyle = "#f57f17";
  ctx.lineWidth = 1;
  ctx.stroke();

  ctx.restore();
}

function drawBird() {
  let ang = 0;
  if (bird.flying) {
    const sp = Math.hypot(bird.vx, bird.vy);
    if (sp > 0.5) ang = Math.atan2(bird.vy, bird.vx);
  }
  drawAngryBirdSprite(bird.x, bird.y, ang);
}

function updatePhysics() {
  if (gameEnded) return;

  if (bird.flying) {
    for (let s = 0; s < PHYS_SUBSTEPS; s++) {
      bird.vy += GRAVITY / PHYS_SUBSTEPS;
      bird.vx *= Math.pow(AIR_DRAG, 1 / PHYS_SUBSTEPS);
      bird.vy *= Math.pow(AIR_DRAG, 1 / PHYS_SUBSTEPS);
      bird.x += bird.vx / PHYS_SUBSTEPS;
      bird.y += bird.vy / PHYS_SUBSTEPS;
    }

    if (bird.y + BIRD_R > GROUND_Y) {
      bird.y = GROUND_Y - BIRD_R;
      bird.vx *= 0.72;
      bird.vy *= -0.35;
      if (Math.abs(bird.vx) < 0.45 && Math.abs(bird.vy) < 0.45) {
        bird.flying = false;
        showToast("Prueba otra vez — ajusta ángulo y potencia.", "err");
        resetBird();
      }
    }
    if (bird.x > W + 40 || bird.x < -40) {
      bird.flying = false;
      showToast("Fuera de pantalla.", "err");
      resetBird();
    }

    for (const t of targets) {
      if (circleRect(bird.x, bird.y, BIRD_R, t.x, t.y, t.w, t.h)) {
        bird.flying = false;
        const correct =
          t.optIndex === activeQuestions[qIndex].correctIndex;
        if (correct) {
          showToast("¡Correcto!", "ok");
          qIndex += 1;
          if (qIndex >= activeQuestions.length) {
            endGame();
            return;
          }
          nextQuestion();
        } else {
          showToast("Incorrecto — otro disparo.", "err");
          resetBird();
        }
        break;
      }
    }
  }
}

function drawGround() {
  ctx.fillStyle = "#5d4037";
  ctx.fillRect(0, GROUND_Y, W, H - GROUND_Y);
  ctx.fillStyle = "#7cb342";
  ctx.fillRect(0, GROUND_Y, W, 8);
}

function drawSling() {
  ctx.strokeStyle = "#3e2723";
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.moveTo(SLING_X - 38, GROUND_Y);
  ctx.lineTo(SLING_X, SLING_Y);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(SLING_X + 38, GROUND_Y);
  ctx.lineTo(SLING_X, SLING_Y);
  ctx.stroke();
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.moveTo(SLING_X, SLING_Y + 8);
  ctx.lineTo(SLING_X, SLING_Y + 22);
  ctx.stroke();
}

function wrapText(text, maxWidth) {
  ctx.font = "bold 14px Segoe UI, sans-serif";
  const words = text.split(" ");
  const lines = [];
  let line = "";
  for (const w of words) {
    const t = line + w + " ";
    if (ctx.measureText(t).width > maxWidth && line) {
      lines.push(line.trim());
      line = w + " ";
    } else line = t;
  }
  lines.push(line.trim());
  return lines;
}

function drawQuestion() {
  const q = activeQuestions[qIndex];
  const wrap = wrapText(q.prompt, W - 40);
  const boxH = 20 + wrap.length * 18;
  ctx.fillStyle = "rgba(0,0,0,0.55)";
  ctx.fillRect(0, 0, W, boxH);
  ctx.fillStyle = "#fff";
  ctx.textAlign = "left";
  let y = 18;
  for (const line of wrap) {
    ctx.fillText(line, 20, y);
    y += 18;
  }
}

function drawTargets() {
  const q = activeQuestions[qIndex];
  ctx.textAlign = "center";
  for (const t of targets) {
    ctx.fillStyle = t.hit ? "#9e9e9e" : "#ff9800";
    ctx.strokeStyle = "#e65100";
    ctx.lineWidth = 2;
    ctx.fillRect(t.x, t.y, t.w, t.h);
    ctx.strokeRect(t.x, t.y, t.w, t.h);
    ctx.fillStyle = "#fff";
    ctx.font = "bold 16px Segoe UI, sans-serif";
    ctx.fillText(t.label, t.x + t.w / 2, t.y + 22);
    ctx.font = "11px Segoe UI, sans-serif";
    const words = q.options[t.optIndex].split(" ");
    let line = "";
    let yy = t.y + 38;
    const textMax = t.w - 16;
    for (const w of words) {
      const test = line + w + " ";
      if (ctx.measureText(test).width > textMax && line) {
        ctx.fillStyle = "#fffde7";
        ctx.fillText(line, t.x + t.w / 2, yy);
        line = w + " ";
        yy += 13;
      } else line = test;
    }
    ctx.fillStyle = "#fffde7";
    ctx.fillText(line, t.x + t.w / 2, yy);
  }
}

function drawDrag() {
  if (!drag.active || bird.flying) return;
  ctx.strokeStyle = "rgba(0,0,0,0.35)";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(SLING_X, SLING_Y);
  ctx.lineTo(bird.x, bird.y);
  ctx.stroke();
}

function loop() {
  if (!document.getElementById("screen-game").classList.contains("active")) {
    return;
  }
  ctx.clearRect(0, 0, W, H);
  drawGround();
  drawSling();
  if (!gameEnded) {
    drawQuestion();
    drawTargets();
    drawDrag();
    drawBird();
    updatePhysics();
    const elapsed = (performance.now() - t0Game) / 1000;
    document.getElementById("hud-time").textContent = `Tiempo: ${elapsed.toFixed(1)} s`;
  }
  rafId = requestAnimationFrame(loop);
}

function getPointer(e) {
  const r = canvas.getBoundingClientRect();
  const scaleX = canvas.width / r.width;
  const scaleY = canvas.height / r.height;
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  return {
    x: (clientX - r.left) * scaleX,
    y: (clientY - r.top) * scaleY,
  };
}

function onDown(e) {
  if (gameEnded || bird.flying) return;
  const p = getPointer(e);
  if (Math.hypot(p.x - SLING_X, p.y - SLING_Y) < 78) {
    drag.active = true;
    bird.x = SLING_X;
    bird.y = SLING_Y;
  }
  e.preventDefault();
}

function onMove(e) {
  if (!drag.active || bird.flying) return;
  const p = getPointer(e);
  let dx = p.x - SLING_X;
  let dy = p.y - SLING_Y;
  const len = Math.hypot(dx, dy) || 1;
  if (len > MAX_PULL) {
    dx = (dx / len) * MAX_PULL;
    dy = (dy / len) * MAX_PULL;
  }
  bird.x = SLING_X + dx;
  bird.y = SLING_Y + dy;
  const maxY = GROUND_Y - BIRD_R - 6;
  if (bird.y > maxY) bird.y = maxY;
  e.preventDefault();
}

function onUp(e) {
  if (!drag.active || bird.flying) return;
  drag.active = false;
  const dx = bird.x - SLING_X;
  const dy = bird.y - SLING_Y;
  const len = Math.hypot(dx, dy);
  if (len > 14) {
    launchBird(dx, dy);
  } else {
    resetBird();
  }
  e.preventDefault();
}

/** Hora legible en Colombia (America/Bogota, sin horario de verano) */
function formatFechaHoraColombia(date = new Date()) {
  return new Intl.DateTimeFormat("es-CO", {
    timeZone: "America/Bogota",
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  }).format(date);
}

/** Sello para nombre de archivo: YYYYMMDDHHmmss en hora Colombia */
function timestampArchivoColombia(date = new Date()) {
  const s = new Intl.DateTimeFormat("sv-SE", {
    timeZone: "America/Bogota",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  }).format(date);
  return s.replace(/\D/g, "");
}

function saveResultsFile() {
  if (!lastResultPayload) return;
  const exportTime = new Date();
  const fechaColTexto = formatFechaHoraColombia(exportTime);
  const tsFile = timestampArchivoColombia(exportTime);
  const safe = playerName.replace(/[^\w\u00f1\u00d1\- ]/g, "_").slice(0, 40);

  const jspdf = typeof window !== "undefined" && window.jspdf;
  if (jspdf && typeof jspdf.jsPDF === "function") {
    const { jsPDF } = jspdf;
    const doc = new jsPDF({ unit: "mm", format: "a4" });
    const margin = 16;
    let y = 18;
    doc.setFont("helvetica", "bold");
    doc.setFontSize(15);
    doc.text("Angry Birds Académico — NumPy", margin, y);
    y += 9;
    doc.setFont("helvetica", "normal");
    doc.setFontSize(10);
    doc.text(
      "Resultado de partida (zona horaria: Colombia — America/Bogota)",
      margin,
      y
    );
    y += 7;
    const bloque = [
      `Fecha y hora de exportación: ${fechaColTexto}`,
      "",
      `Nombre completo: ${lastResultPayload.nombreCompleto}`,
      `Nota (${lastResultPayload.escala}): ${lastResultPayload.notaTexto}`,
      `Lanzamientos: ${lastResultPayload.lanzamientos} (ideal mínimo: ${lastResultPayload.lanzamientosIdeal})`,
      `Tiempo total: ${lastResultPayload.tiempoSegundos} s`,
      `Niveles (0=mejor): lanzamientos ${lastResultPayload.nivelLanzamientos}/9, tiempo ${lastResultPayload.nivelTiempo}/9, promedio ${lastResultPayload.nivelPromedio}`,
      "",
      `ID de sesión: ${lastResultPayload.idSesion}`,
      `Huella de entorno: ${lastResultPayload.huellaEntorno}`,
      "",
      `Preguntas en la partida: ${lastResultPayload.preguntasEnPartida}`,
    ];
    const texto = bloque.join("\n");
    const lineas = doc.splitTextToSize(texto, 180);
    doc.text(lineas, margin, y);
    doc.save(`angry_numpy_${safe}_${tsFile}.pdf`);
    return;
  }

  const blob = new Blob([JSON.stringify({ ...lastResultPayload, fechaExportacionColombia: fechaColTexto }, null, 2)], {
    type: "application/json;charset=utf-8",
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `angry_numpy_${safe}_${tsFile}.json`;
  a.click();
  URL.revokeObjectURL(url);
  alert(
    "No se cargó jsPDF (¿sin internet?). Se descargó un JSON de respaldo con la hora de Colombia."
  );
}

function getBgMusic() {
  return document.getElementById("bg-music");
}

function musicPlay() {
  const el = getBgMusic();
  if (!el) return;
  el.volume = 0.42;
  el.muted = false;
  el.play().catch(() => {});
}

function musicPauseReset() {
  const el = getBgMusic();
  if (!el) return;
  el.pause();
  el.currentTime = 0;
}

function musicToggleMute() {
  const el = getBgMusic();
  if (!el) return true;
  el.muted = !el.muted;
  return !el.muted;
}

function musicIsMuted() {
  const el = getBgMusic();
  return !el || el.muted;
}

function updateAudioButton() {
  const btn = document.getElementById("btn-audio");
  if (!btn || !getBgMusic()) return;
  const on = !musicIsMuted();
  btn.setAttribute("aria-pressed", on ? "true" : "false");
  btn.textContent = on ? "🔊 Música" : "🔇 Activar música";
}

function startGame() {
  playerName =
    document.getElementById("player-name").value.trim() || "Estudiante";
  initSessionId();
  activeQuestions = shuffleArray(QUESTIONS_BANK);
  qIndex = 0;
  totalLaunches = 0;
  gameEnded = false;
  t0Game = performance.now();
  lastResultPayload = null;

  document.getElementById("screen-intro").classList.remove("active");
  document.getElementById("screen-game").classList.add("active");
  document.getElementById("hud-name").textContent = `Jugador: ${playerName}`;

  const audioBtn = document.getElementById("btn-audio");
  if (audioBtn) {
    audioBtn.hidden = false;
  }
  if (getBgMusic()) {
    musicPlay();
    updateAudioButton();
  } else if (audioBtn) {
    audioBtn.hidden = true;
  }

  nextQuestion();
  if (rafId) cancelAnimationFrame(rafId);
  rafId = requestAnimationFrame(loop);
}

mountGradingLegend();

document.getElementById("btn-start").addEventListener("click", startGame);
document.getElementById("btn-replay").addEventListener("click", () => {
  document.getElementById("screen-end").classList.remove("active");
  document.getElementById("screen-intro").classList.add("active");
  document.getElementById("player-name").value = playerName;
  const audioBtn = document.getElementById("btn-audio");
  if (audioBtn) audioBtn.hidden = true;
  musicPauseReset();
});
document.getElementById("btn-save").addEventListener("click", saveResultsFile);

document.getElementById("btn-audio")?.addEventListener("click", () => {
  musicToggleMute();
  updateAudioButton();
});

canvas.addEventListener("mousedown", onDown);
canvas.addEventListener("mousemove", onMove);
window.addEventListener("mouseup", onUp);
canvas.addEventListener("touchstart", onDown, { passive: false });
canvas.addEventListener("touchmove", onMove, { passive: false });
window.addEventListener("touchend", onUp);
