// ASCII variants (keep short and fixed-width friendly)
const ASCII_VARIANTS = [
`  .-"      "-.
.'              '.
/   O        O     \\
:                \`    :
|                  \\\\  |
:    .------.      ;  :
 \\\\  '        '    /  /
  '.          _.'  .'
    '-......-'   -'`,
`  _     _
/ \\~~~/ \\
(    o o   )
 \\__\\_/__/
   /   \\
  (_/ \\_)`,
`      ____  
    /   o\\__
   /    \`--'
  |     |
  |  (o)|
  \\_____/
    |||
   / | \\`
];

const STORAGE_KEY = "ascii_companion_variant_v1";

// Reroll only when visiting '/' (homepage). One reroll per tab session.
const isHome = location.pathname === "/" || location.pathname === "/index.html";
if (isHome && !sessionStorage.getItem("homeRerolled")) {
  localStorage.removeItem(STORAGE_KEY);
  sessionStorage.setItem("homeRerolled", "1");
}

// Pick or reuse variant index
let pick = localStorage.getItem(STORAGE_KEY);
if (pick === null) {
  pick = String(Math.floor(Math.random() * ASCII_VARIANTS.length));
  localStorage.setItem(STORAGE_KEY, pick);
}
const ART = ASCII_VARIANTS[Number(pick)] ?? ASCII_VARIANTS[0];

// Create element after DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  const el = document.createElement("pre");
  el.id = "ascii-companion";
  el.title = "your ascii companion";
  el.setAttribute("role", "img");
  el.setAttribute("aria-label", "your ascii companion");
  el.textContent = ART;
  document.body.appendChild(el);
  enableDrag(el);
});

// Minimal drag (mouse + touch)
function enableDrag(node) {
  let dragging = false;
  let offsetX = 0, offsetY = 0;

  const start = (x, y) => {
    dragging = true;
    const r = node.getBoundingClientRect();
    offsetX = x - r.left;
    offsetY = y - r.top;
    node.style.right = "auto";
    node.style.bottom = "auto";
  };
  const move = (x, y) => {
    if (!dragging) return;
    node.style.left = `${x - offsetX}px`;
    node.style.top  = `${y - offsetY}px`;
  };
  const end = () => { dragging = false; };

  node.addEventListener("mousedown", e => { e.preventDefault(); start(e.clientX, e.clientY); });
  document.addEventListener("mousemove", e => move(e.clientX, e.clientY));
  document.addEventListener("mouseup", end);

  node.addEventListener("touchstart", e => { const t = e.touches[0]; start(t.clientX, t.clientY); }, { passive: true });
  document.addEventListener("touchmove", e => { const t = e.touches[0]; move(t.clientX, t.clientY); }, { passive: true });
  document.addEventListener("touchend", end);
}
