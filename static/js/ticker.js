import { tickerMessages } from './ticker_messages.js';

window.onload = function() {
  // CRT Scanlines
  function drawScanlines() {
    const canvas = document.getElementById('scanlines');
    const ctx = canvas.getContext('2d');
    const h = canvas.height = window.innerHeight;
    const w = canvas.width = window.innerWidth;
    ctx.clearRect(0,0,w,h);
    ctx.globalAlpha = 0.18;
    for(let y=0; y<h; y+=3) {
      ctx.fillStyle = '#39ff1420';
      ctx.fillRect(0, y, w, 1);
    }
  }
  window.addEventListener('resize', drawScanlines);
  drawScanlines();
  // CRT Noise
  function drawNoise() {
    const canvas = document.getElementById('noise');
    const ctx = canvas.getContext('2d');
    const h = canvas.height = window.innerHeight;
    const w = canvas.width = window.innerWidth;
    const imgData = ctx.createImageData(w, h);
    for(let i=0; i<imgData.data.length; i+=4) {
      const shade = Math.random() > 0.5 ? 60 : 0;
      imgData.data[i] = shade;
      imgData.data[i+1] = shade;
      imgData.data[i+2] = shade;
      imgData.data[i+3] = Math.random() > 0.7 ? 30 : 0;
    }
    ctx.putImageData(imgData, 0, 0);
  }
  setInterval(drawNoise, 60);
  // --- Ticker ---
  const ticker = document.getElementById('ticker-text');
  if (!ticker) {
    console.error('Ticker-Element nicht gefunden!');
    return;
  }
  if (!tickerMessages || tickerMessages.length === 0) {
    ticker.textContent = 'No ticker messages found!';
    return;
  }
  // Setze initialen Tickertext
  function shuffle(arr) {
    let a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }
  const tickerCount = 10;
  function setTickerText() {
    let tickerLineArr = shuffle(tickerMessages).slice(0, tickerCount);
    let tickerLine = tickerLineArr.join('  |  ');
    ticker.textContent = tickerLine + '  |  ' + tickerLine;
  }
  setTickerText();
  // Nach jedem Durchlauf neuen Text setzen
  ticker.addEventListener('animationiteration', setTickerText);
}

// Dynamische Feiertagsnachrichten
function getDynamicTickerMessage() {
  const now = new Date();
  // Christmas
  const christmas = new Date(now.getFullYear(), 11, 25);
  if (now > christmas) christmas.setFullYear(now.getFullYear() + 1);
  const daysToChristmas = Math.ceil((christmas - now) / (1000 * 60 * 60 * 24));
  // New Year
  const newYear = new Date(now.getFullYear() + 1, 0, 1);
  const daysToNewYear = Math.ceil((newYear - now) / (1000 * 60 * 60 * 24));
  const specials = [
    `Christmas is in ${daysToChristmas} days!`,
    `New Year is in ${daysToNewYear} days!`
  ];
  // 1 von 25 mal eine Spezialnachricht
  if (Math.random() < 0.04) {
    return specials[Math.floor(Math.random() * specials.length)];
  }
  return null;
}

function getRandomTickerMessage() {
  const dynamic = getDynamicTickerMessage();
  if (dynamic) return dynamic;
  return tickerMessages[Math.floor(Math.random() * tickerMessages.length)];
}

// Beispiel für die Nutzung:
// const message = getRandomTickerMessage(); 