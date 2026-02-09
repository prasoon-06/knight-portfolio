// ===============================
// STAGE 6: Scroll storytelling engine
// ===============================

const chapters = document.querySelectorAll(".chapter");

// MUST match your HTML id="story-bg"
const bgLayer = document.getElementById("story-bg");

const bgConfig = {
  newborn: { img: "/static/portfolio/images/bg_ch1.jpeg", pos: "left center" },
  boy:     { img: "/static/portfolio/images/bg_ch2.jpeg", pos: "left center" },
  teen:    { img: "/static/portfolio/images/bg_ch3.jpeg", pos: "left center" },
  adult:   { img: "/static/portfolio/images/bg_ch4.jpeg", pos: "center center" },
  middle:  { img: "/static/portfolio/images/bg_ch5.jpeg", pos: "center center" },
  old:     { img: "/static/portfolio/images/bg_ch6.jpeg", pos: "left center" },
  sunset:  { img: "/static/portfolio/images/bg_ch6.jpeg", pos: "left center" }
};

function setBackgroundForStage(stage) {
  if (!bgLayer) return;

  const cfg = bgConfig[stage];
  if (!cfg) return;

  bgLayer.style.backgroundImage = `url("${cfg.img}")`;
  bgLayer.style.backgroundPosition = cfg.pos;
}

const observerOptions = {
  root: null,
  threshold: 0.55,
};

function setActiveChapter(entry) {
  const chapter = entry.target;

  if (entry.isIntersecting) {
    chapters.forEach(c => c.classList.remove("is-active"));
    chapter.classList.add("is-active");

    const stage = chapter.dataset.stage;

    updateKnightStage(stage);
    setBackgroundForStage(stage);
  }
}

const chapterObserver = new IntersectionObserver((entries) => {
  entries.forEach(setActiveChapter);
}, observerOptions);

chapters.forEach(ch => chapterObserver.observe(ch));

// ===============================
// Knight stage logic (placeholder)
// ===============================
function updateKnightStage(stage) {
  const active = document.querySelector(".chapter.is-active");
  if (!active) return;

  const knight = active.querySelector(".knight");
  if (!knight) return;

  knight.className = "knight";
  knight.classList.add(`knight--${stage}`);
}

// ===============================
// On load: activate first chapter + set initial background
// ===============================
window.addEventListener("load", () => {
  const first = document.querySelector(".chapter");
  if (first) {
    first.classList.add("is-active");
    updateKnightStage(first.dataset.stage);
    setBackgroundForStage(first.dataset.stage);
  }
});
