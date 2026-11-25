(function(){
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const isTouch = window.matchMedia("(pointer:coarse)").matches;
  const page = document.body.dataset.page || "home";
  const plugins = [ScrollTrigger];
  if (typeof SplitText !== "undefined") plugins.push(SplitText);
  gsap.registerPlugin.apply(gsap, plugins);
  let bootReady = () => {};
  const whenBooted = new Promise((resolve) => { bootReady = resolve; });

  /* Route-clearance boot loader — keep GSAP off SVG transforms */
  (function bootLoader(){
    const loader = document.getElementById("imexLoader");
    if (!loader) {
      document.body.classList.remove("is-loading");
      bootReady();
      return;
    }
    let finished = false;
    const finish = () => {
      if (finished) return;
      finished = true;
      document.body.classList.remove("is-loading");
      loader.setAttribute("aria-busy", "false");
      loader.classList.add("is-done");
      const reveal = [".site-nav", "#main", ".site-foot"].map((s) => document.querySelector(s)).filter(Boolean);
      if (reveal.length) {
        gsap.fromTo(reveal, { opacity: 0 }, {
          opacity: 1, duration: 0.5, stagger: 0.04, ease: "power2.out", clearProps: "opacity"
        });
      }
      bootReady();
      setTimeout(() => { try { loader.remove(); } catch (_) {} }, 650);
    };
    const failSafe = setTimeout(() => {
      try { loader.style.transform = "translateY(-110%)"; } catch (_) {}
      finish();
    }, 6000);

    if (reduce) {
      clearTimeout(failSafe);
      loader.style.display = "none";
      finish();
      return;
    }

    const path = loader.querySelector(".imex-loader-lane-draw");
    const box = loader.querySelector(".imex-loader-box");
    const pct = loader.querySelector(".imex-loader-pct");
    const bar = loader.querySelector(".imex-loader-bar i");
    const tag = loader.querySelector(".imex-loader-tag");
    const nodes = Array.prototype.slice.call(loader.querySelectorAll(".imex-loader-node"));
    const letters = Array.prototype.slice.call(loader.querySelectorAll(".imex-loader-letter"));
    const tags = ["Clearing the route", "Sea · Air · Customs", "Kanpur to the world"];
    const duration = 1.9;

    const placeBox = (dist, len, alpha) => {
      if (!path || !box || !len) return;
      const d = Math.max(0, Math.min(len, dist));
      const pt = path.getPointAtLength(d);
      const pt2 = path.getPointAtLength(Math.min(len, d + 2));
      const ang = Math.atan2(pt2.y - pt.y, pt2.x - pt.x) * 180 / Math.PI;
      /* SVG transform attr for position; style.opacity only (never style.transform) */
      box.setAttribute("transform", "translate(" + pt.x + " " + pt.y + ") rotate(" + ang + ")");
      box.style.opacity = String(alpha);
    };

    const setProgress = (t, len) => {
      const p = Math.max(0, Math.min(1, t));
      const v = Math.round(p * 100);
      if (pct) pct.textContent = String(v);
      if (bar) bar.style.width = v + "%";
      if (path && len) {
        path.style.strokeDasharray = String(len);
        path.style.strokeDashoffset = String(len * (1 - p));
      }
      const boxAlpha = p < 0.04 ? p / 0.04 : 1;
      placeBox(p * len, len, boxAlpha);
      nodes.forEach((n, i) => {
        const gate = (i + 0.35) / nodes.length;
        n.style.opacity = p >= gate ? "1" : "0";
      });
      if (tag) {
        if (p < 0.32) tag.textContent = tags[0];
        else if (p < 0.62) tag.textContent = tags[1];
        else tag.textContent = tags[2];
        tag.style.color = p > 0.7 ? "rgba(255,255,255,.88)" : "rgba(255,255,255,.55)";
      }
    };

    const exitLoader = () => {
      sessionStorage.setItem("imexBooted", "1");
      gsap.to(loader, {
        yPercent: -110,
        duration: 0.75,
        ease: "power4.inOut",
        onComplete: () => {
          clearTimeout(failSafe);
          finish();
        }
      });
    };

    const run = () => {
      const len = (path && path.getTotalLength && path.getTotalLength()) || 0;
      if (path && len) {
        path.style.strokeDasharray = String(len);
        path.style.strokeDashoffset = String(len);
      }
      if (box) box.style.transform = "";
      placeBox(0, len, 0);
      setProgress(0, len);

      const state = { p: 0 };
      const tl = gsap.timeline({ onComplete: exitLoader });

      if (letters.length) {
        tl.fromTo(letters, {
          yPercent: 110,
          opacity: 0
        }, {
          yPercent: 0,
          opacity: 1,
          duration: 0.55,
          stagger: 0.075,
          ease: "power3.out"
        }, 0);
      }

      tl.to(state, {
        p: 1,
        duration: duration,
        ease: "power2.inOut",
        onUpdate: () => setProgress(state.p, len)
      }, 0.12);
    };
    requestAnimationFrame(() => requestAnimationFrame(run));
  })();

  /* Lenis */
  let lenis;
  if (!reduce) {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    ScrollTrigger.scrollerProxy(document.body, {
      scrollTop(v){ if (arguments.length) lenis.scrollTo(v, { immediate: true }); return lenis.scroll; },
      getBoundingClientRect(){ return { top:0, left:0, width: innerWidth, height: innerHeight }; }
    });
  }

  /* Cursor */
  const cur = document.querySelector(".cursor");
  const dot = document.querySelector(".cursor-dot");
  if (cur && dot && !isTouch && !reduce) {
    const xC = gsap.quickTo(cur, "left", { duration: 0.45, ease: "power3" });
    const yC = gsap.quickTo(cur, "top", { duration: 0.45, ease: "power3" });
    const xD = gsap.quickTo(dot, "left", { duration: 0.18, ease: "power3" });
    const yD = gsap.quickTo(dot, "top", { duration: 0.18, ease: "power3" });
    window.addEventListener("pointermove", (e) => { xC(e.clientX); yC(e.clientY); xD(e.clientX); yD(e.clientY); });
    document.querySelectorAll("a,button,.magnetic").forEach((el) => {
      el.addEventListener("pointerenter", () => cur.classList.add("is-hover"));
      el.addEventListener("pointerleave", () => cur.classList.remove("is-hover"));
    });
  }

  /* Magnetic */
  if (!isTouch && !reduce) {
    document.querySelectorAll(".magnetic").forEach((btn) => {
      btn.addEventListener("pointermove", (e) => {
        const r = btn.getBoundingClientRect();
        gsap.to(btn, { x: (e.clientX - r.left - r.width/2) * 0.28, y: (e.clientY - r.top - r.height/2) * 0.28, duration: 0.35 });
      });
      btn.addEventListener("pointerleave", () => gsap.to(btn, { x:0, y:0, duration: 0.5, ease: "elastic.out(1,0.4)" }));
    });
  }

  /* Nav */
  const nav = document.getElementById("siteNav");
  const toggle = document.querySelector(".nav-toggle");
  const drops = document.querySelectorAll(".drop");
  window.addEventListener("scroll", () => {
    if (!nav) return;
    nav.classList.toggle("scrolled", window.scrollY > 40);
  }, { passive: true });
  if (toggle) toggle.addEventListener("click", () => {
    const open = document.body.classList.toggle("nav-open");
    toggle.setAttribute("aria-expanded", open);
  });
  drops.forEach((d) => {
    const btn = d.querySelector("button");
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      drops.forEach((x) => { if (x !== d) x.classList.remove("open"); });
      d.classList.toggle("open");
      btn.setAttribute("aria-expanded", d.classList.contains("open"));
    });
    btn.addEventListener("keydown", (e) => {
      if (e.key === "Escape") { d.classList.remove("open"); btn.focus(); }
    });
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".drop")) drops.forEach((d) => {
      d.classList.remove("open");
      d.querySelector("button")?.setAttribute("aria-expanded", "false");
    });
  });
  document.querySelector(".to-top")?.addEventListener("click", () => {
    if (lenis) lenis.scrollTo(0); else window.scrollTo({ top:0, behavior:"smooth" });
  });
  window.addEventListener("scroll", () => {
    document.querySelector(".to-top")?.classList.toggle("show", window.scrollY > 600);
  }, { passive: true });

  /* Page transitions */
  const overlay = document.querySelector(".vt-overlay");
  function playExit(type){
    return new Promise((resolve) => {
      if (overlay) {
        overlay.classList.remove("is-idle");
        overlay.style.opacity = "1";
        overlay.style.visibility = "visible";
        overlay.dataset.type = type || "wipe";
      }
      const tl = gsap.timeline({ onComplete: resolve, defaults:{ duration: reduce ? 0 : 0.55, ease:"power3.inOut" }});
      if (type === "route") tl.fromTo(".vt-route", { scaleX:0 }, { scaleX:1 });
      else if (type === "zoom") tl.fromTo(".vt-zoom", { scale:0.2, opacity:0 }, { scale:8, opacity:1 });
      else if (type === "frag") tl.to(".vt-frag span", { y:0, stagger:0.04 });
      else tl.fromTo(".vt-wipe", { clipPath:"inset(0 100% 0 0)" }, { clipPath:"inset(0 0 0 0)" });
      setTimeout(resolve, reduce ? 0 : 900);
    });
  }
  if (overlay) {
    overlay.classList.add("is-idle");
    overlay.style.opacity = "0";
    overlay.style.visibility = "hidden";
  }
  document.querySelectorAll('a[href$=".html"]').forEach((a) => {
    if (a.target === "_blank") return;
    a.addEventListener("click", (e) => {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      if (!document.startViewTransition) {
        playExit(a.dataset.vt || "wipe");
      }
    });
  });

  /* Split / reveal */
  const mm = gsap.matchMedia();
  mm.add("(prefers-reduced-motion: no-preference)", () => {
    document.querySelectorAll("[data-split]").forEach((el) => {
      try {
        if (typeof SplitText === "undefined") return;
        const split = SplitText.create(el, { type:"chars,words", aria:"auto" });
        gsap.from(split.chars, { yPercent:120, opacity:0, stagger:0.018, duration:1, ease:"power4.out", delay: el.dataset.delay || 0 });
      } catch (err) {
        gsap.from(el, { y: 24, opacity: 0, duration: 0.8 });
      }
    });
    gsap.utils.toArray("[data-reveal]").forEach((el) => {
      gsap.from(el, {
        y: 48, opacity: 0, duration: 1, ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 84%" }
      });
    });
    gsap.utils.toArray("[data-parallax]").forEach((el) => {
      gsap.to(el, {
        yPercent: Number(el.dataset.parallax) || -12, ease:"none",
        scrollTrigger: { trigger: el.parentElement || el, scrub: true }
      });
    });
  });

  /* Homepage frame-by-frame hero — register before later pins */
  (function heroFilm(){
    const film = document.getElementById("heroFrames");
    if (!film || page !== "home") return;
    const ctx = film.getContext("2d", { alpha: false });
    const count = Number(film.dataset.frames) || 192;
    const prefix = film.dataset.src || "assets/images/hero-frames/frame-";
    const frames = new Array(count);
    let progress = 0;
    let drawn = -1;

    function coverDraw(img){
      const cw = film.width, ch = film.height;
      const ir = img.width / img.height, cr = cw / ch;
      let dw, dh, dx, dy;
      if (ir > cr) { dh = ch; dw = ch * ir; dx = (cw - dw) / 2; dy = 0; }
      else { dw = cw; dh = cw / ir; dx = 0; dy = (ch - dh) / 2; }
      ctx.drawImage(img, dx, dy, dw, dh);
    }

    function render(p){
      progress = p;
      const i = Math.min(count - 1, Math.max(0, Math.round(p * (count - 1))));
      if (i === drawn && frames[i]) return;
      const img = frames[i] || frames.find(Boolean);
      if (!img) return;
      coverDraw(img);
      drawn = frames[i] ? i : drawn;
      const bar = document.querySelector(".hero-film-progress");
      if (bar) bar.style.width = (p * 100) + "%";
    }

    function size(){
      const r = film.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      film.width = Math.max(2, Math.round(r.width * dpr));
      film.height = Math.max(2, Math.round(r.height * dpr));
      drawn = -1;
      render(progress);
    }

    function loadFrame(i){
      return new Promise((resolve) => {
        const img = new Image();
        img.decoding = "async";
        img.onload = () => { frames[i] = img; resolve(img); };
        img.onerror = () => resolve(null);
        img.src = prefix + String(i + 1).padStart(3, "0") + ".jpg";
      });
    }

    loadFrame(0).then((first) => {
      size();
      if (first) render(0);
      ScrollTrigger.refresh();
    });

    let next = 1;
    let inflight = 0;
    let loaded = 1;
    const workers = 6;
    function pump(){
      while (inflight < workers && next < count) {
        const i = next++;
        inflight++;
        loadFrame(i).then(() => {
          inflight--;
          loaded++;
          if (Math.abs(Math.round(progress * (count - 1)) - i) <= 2) render(progress);
          if (loaded === count) ScrollTrigger.refresh();
          pump();
        });
      }
    }
    pump();

    window.addEventListener("resize", size);

    const copy = document.querySelector(".hero-film .hero-copy");
    const canvas = document.getElementById("heroFrames");
    const track = document.querySelector(".hero-film-track");
    const mmFilm = gsap.matchMedia();
    mmFilm.add("(prefers-reduced-motion: no-preference)", () => {
      ScrollTrigger.create({
        trigger: ".hero-film",
        start: "top top",
        endTrigger: track || ".hero-film-track",
        end: "bottom top",
        invalidateOnRefresh: true,
        scrub: 0.35,
        onUpdate: (self) => {
          render(self.progress);
          if (copy) {
            const fade = Math.min(1, self.progress / 0.28);
            copy.style.opacity = String(1 - fade);
            copy.style.transform = "translateY(" + (-56 * fade) + "px)";
            copy.style.pointerEvents = fade > 0.85 ? "none" : "auto";
          }
        }
      });
      if (canvas) {
        gsap.fromTo(canvas, { scale: 1 }, {
          scale: 1.08,
          ease: "none",
          transformOrigin: "center center",
          scrollTrigger: {
            trigger: "[data-story-band]",
            start: "top bottom",
            end: "top top",
            scrub: 0.55
          }
        });
      }
      ScrollTrigger.sort();
      ScrollTrigger.refresh();
      return () => {
        render(0);
        if (copy) {
          copy.style.opacity = "";
          copy.style.transform = "";
          copy.style.pointerEvents = "";
        }
      };
    });
    mmFilm.add("(prefers-reduced-motion: reduce)", () => { render(0); });
  })();

  /* Horizontal rail */
  const rail = document.querySelector(".rail");
  if (rail && !reduce) {
    const panels = gsap.utils.toArray(".rail-panel");
    const railTween = gsap.to(rail, {
      x: () => -(rail.scrollWidth - innerWidth),
      ease: "none",
      scrollTrigger: {
        trigger: ".rail-pin",
        pin: true,
        scrub: 1,
        invalidateOnRefresh: true,
        anticipatePin: 1,
        end: () => "+=" + Math.max(rail.scrollWidth - innerWidth, innerWidth)
      }
    });
    panels.forEach((p) => {
      const bits = p.querySelectorAll(".rail-copy > *");
      if (!bits.length) return;
      gsap.from(bits, {
        y: 36, opacity: 0, stagger: 0.07, duration: 0.7, ease: "power3.out",
        immediateRender: false,
        scrollTrigger: {
          trigger: p,
          containerAnimation: railTween,
          start: "left 78%",
          toggleActions: "play none none reverse"
        }
      });
      const photo = p.querySelector(".rail-visual img");
      if (photo) {
        gsap.fromTo(photo, { scale: 1.12 }, {
          scale: 1.04, ease: "none",
          scrollTrigger: {
            trigger: p,
            containerAnimation: railTween,
            start: "left 100%",
            end: "left -20%",
            scrub: true
          }
        });
      }
    });
  }

  /* Process line */
  if (document.querySelector(".process-line i") && !reduce) {
    gsap.to(".process-line i", {
      width: "100%", ease:"none",
      scrollTrigger: { trigger: ".process", start:"top 70%", end:"bottom 50%", scrub:true }
    });
  }

  /* How it works — dispatch lane */
  (function howBand(){
    const band = document.querySelector("[data-how-band]");
    if (!band) return;
    const words = band.querySelectorAll(".how-title span");
    const logs = band.querySelectorAll(".how-log li");
    const posts = band.querySelectorAll(".how-post");
    const van = band.querySelector(".how-van-wrap");
    const fill = band.querySelector(".how-fill");
    const setStep = (i) => {
      words.forEach((el, n) => el.classList.toggle("is-on", n <= i));
      logs.forEach((el, n) => {
        const on = n === i;
        el.classList.toggle("is-on", on);
        if (on) el.setAttribute("aria-current", "step");
        else el.removeAttribute("aria-current");
      });
      posts.forEach((el, n) => el.classList.toggle("is-on", n <= i));
    };
    setStep(0);

    const mmH = gsap.matchMedia();
    mmH.add("(prefers-reduced-motion: no-preference)", () => {
      const enter = gsap.timeline({
        defaults: { ease: "power3.out" },
        scrollTrigger: { trigger: band, start: "top 78%", once: true }
      });
      enter.from(band.querySelector(".how-kicker"), { y: 16, opacity: 0, duration: 0.45 })
        .from(words, { y: 28, opacity: 0, stagger: 0.08, duration: 0.7 }, "-=0.22")
        .from(logs, { y: 14, stagger: 0.07, duration: 0.45 }, "-=0.4")
        .from(band.querySelector(".how-copy .btn"), { y: 12, opacity: 0, duration: 0.4 }, "-=0.28")
        .from(band.querySelector(".how-slab"), { y: 36, opacity: 0, duration: 0.8 }, 0.08)
        .from(van, { opacity: 0, duration: 0.7 }, 0.22)
        .from(band.querySelector(".how-flag"), { y: 10, opacity: 0, duration: 0.4 }, 0.45);

      const travel = gsap.timeline({
        defaults: { ease: "none" },
        scrollTrigger: {
          trigger: band,
          start: "top 68%",
          end: "bottom 42%",
          scrub: 1.15,
          onUpdate: (self) => setStep(self.progress < 0.34 ? 0 : self.progress < 0.67 ? 1 : 2)
        }
      });
      travel.fromTo(van, { x: 0 }, { x: () => Math.max(0, (band.querySelector(".how-slab")?.offsetWidth || 600) * 0.28) }, 0)
        .fromTo(fill, { scaleX: 0 }, { scaleX: 1 }, 0);
    });
    mmH.add("(prefers-reduced-motion: reduce)", () => {
      setStep(2);
      gsap.set(fill, { scaleX: 1 });
      gsap.set(van, { x: () => Math.max(0, (band.querySelector(".how-slab")?.offsetWidth || 600) * 0.28) });
    });
  })();

  /* 3D */
  const canvas = document.getElementById("scene");
  const scenes = [];
  function hex(n){ return new THREE.Color(n); }
  function lights(scene){
    scene.add(new THREE.AmbientLight(0x9bb7e8, 0.55));
    const a = new THREE.DirectionalLight(0x00adef, 1.15); a.position.set(4,6,8); scene.add(a);
    const b = new THREE.DirectionalLight(0x2e3192, 0.9); b.position.set(-6,2,-4); scene.add(b);
    const p = new THREE.PointLight(0x00adef, 1.4, 18); p.position.set(0, 2.2, 3); scene.add(p);
  }
  function makeRenderer(el){
    const renderer = new THREE.WebGLRenderer({ canvas: el, antialias: !isTouch, alpha: true, powerPreference:"high-performance" });
    renderer.setPixelRatio(Math.min(devicePixelRatio, isTouch ? 1.25 : 1.75));
    renderer.setSize(el.clientWidth, el.clientHeight, false);
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    return renderer;
  }
  function corrugate(w,h,d){
    const g = new THREE.Group();
    const body = new THREE.Mesh(
      new THREE.BoxGeometry(w,h,d),
      new THREE.MeshStandardMaterial({ color: 0x00adef, metalness: 0.72, roughness: 0.28 })
    );
    g.add(body);
    const ribMat = new THREE.MeshStandardMaterial({ color: 0x0099cc, metalness: 0.8, roughness: 0.22 });
    for (let i=0;i<10;i++){
      const rib = new THREE.Mesh(new THREE.BoxGeometry(w*1.02, h*0.06, d*0.98), ribMat);
      rib.position.y = -h/2 + (i+0.6)*(h/10);
      g.add(rib);
    }
    const door = new THREE.Mesh(
      new THREE.BoxGeometry(w*0.96, h*0.96, 0.04),
      new THREE.MeshStandardMaterial({ color: 0x2e3192, metalness: 0.6, roughness: 0.35 })
    );
    door.position.z = d/2 + 0.02;
    g.add(door);
    const frame = new THREE.Mesh(
      new THREE.BoxGeometry(0.08, h, d),
      new THREE.MeshStandardMaterial({ color: 0x222222, metalness: 0.4, roughness: 0.5 })
    );
    frame.position.x = w/2;
    g.add(frame);
    return g;
  }
  function crate(s, color){
    return new THREE.Mesh(
      new THREE.BoxGeometry(s, s*0.7, s*1.1),
      new THREE.MeshStandardMaterial({ color: color || 0xc8a165, metalness: 0.1, roughness: 0.7 })
    );
  }
  function disposeScene(obj){
    obj.traverse((c) => {
      if (c.geometry) c.geometry.dispose();
      if (c.material) {
        if (Array.isArray(c.material)) c.material.forEach((m)=>m.dispose());
        else c.material.dispose();
      }
    });
  }

  function bootScene(el, kind){
    if (!window.THREE || !el) return;
    try {
      const parent = el.parentElement;
      if (parent && (el.clientWidth < 32 || el.clientHeight < 32)) {
        el.style.width = parent.clientWidth + "px";
        el.style.height = Math.max(parent.clientHeight, 320) + "px";
      }
      const renderer = makeRenderer(el);
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(38, el.clientWidth/Math.max(el.clientHeight,1), 0.1, 80);
      camera.position.set(4.6, 2.4, 7.2);
      camera.lookAt(0, 0, 0);
      lights(scene);
      const root = new THREE.Group();
      scene.add(root);
      const pointer = { x:0, y:0 };
      const onMove = (e) => { pointer.x = (e.clientX / innerWidth) * 2 - 1; pointer.y = (e.clientY / innerHeight) * 2 - 1; };
      window.addEventListener("pointermove", onMove);

      if (kind === "container" || kind === "fcl") {
        const c = corrugate(2.2, 2.2, 4.4);
        c.rotation.y = 0.55;
        root.add(c);
        const floor = new THREE.Mesh(
          new THREE.CircleGeometry(7, 48),
          new THREE.MeshStandardMaterial({ color: 0x0a1024, metalness: 0.2, roughness: 0.9 })
        );
        floor.rotation.x = -Math.PI/2; floor.position.y = -1.25; root.add(floor);
        for (let i=0;i<4;i++){
          const p = crate(0.45, i%2?0x2e3192:0x00adef);
          p.position.set((i-1.5)*1.1, -1.6, 2.2);
          root.add(p);
        }
      }
      if (kind === "globe") {
        const R = 2.12;
        const spin = new THREE.Group();
        root.add(spin);
        root.userData.globeSpin = spin;

        const ocean = new THREE.Mesh(
          new THREE.SphereGeometry(R, isTouch ? 48 : 72, isTouch ? 48 : 72),
          new THREE.MeshStandardMaterial({
            color: 0x10224a, emissive: 0x0b2a58, emissiveIntensity: 0.85,
            metalness: 0.35, roughness: 0.55
          })
        );
        spin.add(ocean);

        const wire = new THREE.Mesh(
          new THREE.IcosahedronGeometry(R * 1.01, 2),
          new THREE.MeshBasicMaterial({
            color: 0x4aa8d8, transparent: true, opacity: 0.18, wireframe: true
          })
        );
        spin.add(wire);

        const atmos = new THREE.Mesh(
          new THREE.SphereGeometry(R * 1.09, 48, 48),
          new THREE.MeshBasicMaterial({
            color: 0x00adef, transparent: true, opacity: 0.14, side: THREE.BackSide, depthWrite: false
          })
        );
        spin.add(atmos);

        const halo = new THREE.Mesh(
          new THREE.SphereGeometry(R * 1.2, 48, 48),
          new THREE.MeshBasicMaterial({
            color: 0x33c3f3, transparent: true, opacity: 0.07, side: THREE.BackSide, depthWrite: false
          })
        );
        spin.add(halo);

        const latMat = new THREE.LineBasicMaterial({ color: 0x00adef, transparent: true, opacity: 0.16 });
        [-0.65, -0.3, 0, 0.3, 0.65].forEach((yN) => {
          const pts = [];
          const ry = Math.sqrt(Math.max(0.0001, 1 - yN * yN)) * R * 1.004;
          for (let i = 0; i <= 64; i++) {
            const a = (i / 64) * Math.PI * 2;
            pts.push(new THREE.Vector3(Math.cos(a) * ry, yN * R, Math.sin(a) * ry));
          }
          spin.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), latMat));
        });

        const toVec = (lat, lon, r) => {
          const phi = (90 - lat) * (Math.PI / 180);
          const theta = (lon + 180) * (Math.PI / 180);
          return new THREE.Vector3(
            -r * Math.sin(phi) * Math.cos(theta),
            r * Math.cos(phi),
            r * Math.sin(phi) * Math.sin(theta)
          );
        };

        // Destinations published on IMEX LCL / network copy
        const hubs = [
          { lat: 26.45, lon: 80.33, home: true },   // Kanpur
          { lat: 25.2, lon: 55.27 },                // Dubai / Jebel Ali
          { lat: 1.35, lon: 103.82 },               // Singapore
          { lat: 6.93, lon: 79.85 },                // Colombo
          { lat: 51.96, lon: 1.35 },                // Felixstowe
          { lat: 51.22, lon: 4.4 },                 // Antwerp
          { lat: 51.92, lon: 4.48 },                // Rotterdam
          { lat: 53.55, lon: 9.99 },                // Hamburg
          { lat: 43.3, lon: 5.37 },                 // Marseilles
          { lat: 41.39, lon: 2.17 },                // Barcelona
          { lat: -29.86, lon: 31.02 },              // Durban
          { lat: 40.71, lon: -74.01 },              // New York
          { lat: 33.94, lon: -118.41 }              // Los Angeles
        ].map((h) => ({ ...h, pos: toVec(h.lat, h.lon, R * 1.01) }));

        const hubGroup = new THREE.Group();
        spin.add(hubGroup);
        const hubMat = new THREE.MeshBasicMaterial({ color: 0x00adef });
        const homeMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        hubs.forEach((h) => {
          const d = new THREE.Mesh(
            new THREE.SphereGeometry(h.home ? 0.055 : 0.032, 10, 10),
            h.home ? homeMat : hubMat
          );
          d.position.copy(h.pos);
          hubGroup.add(d);
          if (h.home) {
            const ring = new THREE.Mesh(
              new THREE.RingGeometry(0.08, 0.11, 24),
              new THREE.MeshBasicMaterial({ color: 0x00adef, transparent: true, opacity: 0.85, side: THREE.DoubleSide })
            );
            ring.position.copy(h.pos);
            ring.lookAt(0, 0, 0);
            ring.userData.pulse = true;
            hubGroup.add(ring);
          }
        });

        const makeArc = (a, b) => {
          const mid = a.clone().add(b).multiplyScalar(0.5).normalize().multiplyScalar(R * (1.28 + a.distanceTo(b) * 0.06));
          return new THREE.QuadraticBezierCurve3(a.clone(), mid, b.clone());
        };
        const home = hubs[0].pos;
        const routes = hubs.slice(1).map((h) => makeArc(home, h.pos));
        const arcGroup = new THREE.Group();
        spin.add(arcGroup);
        routes.forEach((curve, i) => {
          const tube = new THREE.Mesh(
            new THREE.TubeGeometry(curve, isTouch ? 28 : 48, i % 2 === 0 ? 0.016 : 0.009, 8, false),
            new THREE.MeshBasicMaterial({
              color: 0x00adef, transparent: true, opacity: i % 2 === 0 ? 0.85 : 0.4
            })
          );
          arcGroup.add(tube);
          const bead = new THREE.Mesh(
            new THREE.SphereGeometry(0.038, 10, 10),
            new THREE.MeshBasicMaterial({ color: 0xffffff })
          );
          bead.userData.route = { curve, speed: 0.1 + (i % 5) * 0.025, t: Math.random() };
          arcGroup.add(bead);
        });

        const starCount = isTouch ? 80 : 160;
        const starPos = new Float32Array(starCount * 3);
        for (let i = 0; i < starCount; i++) {
          const v = new THREE.Vector3().randomDirection().multiplyScalar(5.5 + Math.random() * 3.5);
          starPos[i * 3] = v.x; starPos[i * 3 + 1] = v.y; starPos[i * 3 + 2] = v.z;
        }
        const stars = new THREE.Points(
          new THREE.BufferGeometry().setAttribute("position", new THREE.BufferAttribute(starPos, 3)),
          new THREE.PointsMaterial({ color: 0x9fdfff, size: 0.02, sizeAttenuation: true, transparent: true, opacity: 0.65 })
        );
        root.add(stars);

        // Face Kanpur / India toward the camera, then axial spin uses local Y
        const homeDir = hubs[0].pos.clone().normalize();
        spin.quaternion.setFromUnitVectors(homeDir, new THREE.Vector3(0.18, 0.08, 1).normalize());
        spin.rotateX(-0.14);
        spin.userData.useLocalSpin = true;

        camera.position.set(0.1, 0.2, 6.55);
        camera.lookAt(0, 0, 0);

        /* Homepage: scrub globe as scroll transition into the partners band */
        if (el.dataset.globeScroll === "1" && !reduce) {
          const band = el.closest("[data-globe-band]") || el.closest(".globe-band");
          const frame = el.closest(".globe-frame");
          const copy = band && band.querySelector(".globe-copy");
          const camStart = 9.35;
          const camEnd = 6.55;
          const scaleStart = 0.42;
          root.scale.setScalar(scaleStart);
          camera.position.z = camStart;
          hubGroup.scale.setScalar(0.15);
          hubGroup.traverse((o) => { if (o.material && o.material.opacity != null) { o.userData._op = o.material.opacity; o.material.opacity = 0; } });
          arcGroup.traverse((o) => {
            if (o.material && o.material.opacity != null) {
              o.userData._op = o.material.opacity;
              o.material.opacity = 0;
            }
            if (o.userData.route) o.visible = false;
          });
          if (stars.material) stars.material.opacity = 0.15;
          root.userData.scrollSpin = 0;

          const state = { p: 0 };
          const apply = () => {
            const p = state.p;
            const e = p * p * (3 - 2 * p); // smoothstep
            root.scale.setScalar(scaleStart + (1 - scaleStart) * e);
            camera.position.z = camStart + (camEnd - camStart) * e;
            camera.position.y = 0.55 - 0.35 * e;
            camera.lookAt(0, 0, 0);
            root.rotation.x = (1 - e) * 0.38;
            root.rotation.y = (1 - e) * -0.55;
            hubGroup.scale.setScalar(0.15 + 0.85 * e);
            hubGroup.traverse((o) => {
              if (o.material && o.userData._op != null) o.material.opacity = o.userData._op * Math.min(1, e * 1.35);
            });
            arcGroup.traverse((o) => {
              if (o.material && o.userData._op != null) o.material.opacity = o.userData._op * Math.max(0, (e - 0.28) / 0.72);
              if (o.userData.route) o.visible = e > 0.42;
            });
            if (stars.material) stars.material.opacity = 0.15 + 0.5 * e;
            root.userData.scrollSpin = (1 - e) * 0.012;
            if (frame) {
              frame.style.opacity = String(0.35 + 0.65 * e);
              frame.style.transform = "translate3d(0," + ((1 - e) * 72) + "px,0) rotateY(" + ((1 - e) * -16) + "deg) scale(" + (0.82 + 0.18 * e) + ")";
            }
          };
          apply();

          gsap.to(state, {
            p: 1,
            ease: "none",
            scrollTrigger: {
              trigger: band || frame || el,
              start: "top 92%",
              end: "center 48%",
              scrub: 0.7,
              invalidateOnRefresh: true
            },
            onUpdate: apply
          });

          if (copy) {
            gsap.fromTo(copy.children, { y: 48, opacity: 0 }, {
              y: 0,
              opacity: 1,
              stagger: 0.1,
              ease: "none",
              scrollTrigger: {
                trigger: band || copy,
                start: "top 88%",
                end: "top 42%",
                scrub: 0.55
              }
            });
          }
        }
      }
      if (kind === "ocean") {
        const waterG = new THREE.PlaneGeometry(28, 28, isTouch?18:48, isTouch?18:48);
        const water = new THREE.Mesh(waterG, new THREE.MeshStandardMaterial({ color: 0x123a6b, metalness: 0.7, roughness: 0.25, transparent:true, opacity:0.92 }));
        water.rotation.x = -Math.PI/2; water.position.y = -1.15; root.add(water);
        water.userData.wave = true;
        const ship = new THREE.Group();
        const hull = new THREE.Mesh(new THREE.BoxGeometry(5.2, 0.7, 1.4), new THREE.MeshStandardMaterial({ color: 0x1a1a1a, metalness:0.5, roughness:0.4 }));
        hull.position.y = -0.4; ship.add(hull);
        const stripe = new THREE.Mesh(new THREE.BoxGeometry(5.2, 0.18, 1.42), new THREE.MeshStandardMaterial({ color: 0x8b1e1e }));
        stripe.position.y = -0.7; ship.add(stripe);
        for (let x=-1.6;x<=1.6;x+=0.55){
          for (let z=-0.35;z<=0.35;z+=0.35){
            const box = corrugate(0.42, 0.42, 0.85);
            box.scale.set(0.22,0.22,0.22);
            box.position.set(x, 0.05, z);
            ship.add(box);
          }
        }
        root.add(ship);
        camera.position.set(3.2, 2.4, 8.5);
      }
      if (kind === "packages" || kind === "buyer") {
        for (let i=0;i<8;i++){
          const p = crate(0.5 + Math.random()*0.25, i%2?0x00adef:0xc8a165);
          p.position.set((i-3.5)*0.85, Math.sin(i)*0.4, (i%3-1)*0.8);
          p.userData.base = p.position.clone();
          root.add(p);
        }
      }
      if (kind === "air") {
        const plane = new THREE.Group();
        const fuse = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.22, 3.2, 12), new THREE.MeshStandardMaterial({ color: 0xe8eef6, metalness:0.6, roughness:0.3 }));
        fuse.rotation.z = Math.PI/2; plane.add(fuse);
        const wing = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.06, 0.5), new THREE.MeshStandardMaterial({ color: 0x2e3192, metalness:0.5, roughness:0.35 }));
        plane.add(wing);
        const tail = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.4, 0.06), new THREE.MeshStandardMaterial({ color: 0x00adef }));
        tail.position.set(-1.4, 0.22, 0); plane.add(tail);
        root.add(plane);
        for (let i=0;i<12;i++){
          const cloud = new THREE.Mesh(new THREE.SphereGeometry(0.35+Math.random()*0.4, 8, 8), new THREE.MeshStandardMaterial({ color: 0xffffff, transparent:true, opacity:0.18 }));
          cloud.position.set((Math.random()-0.5)*10, (Math.random()-0.5)*4, (Math.random()-0.5)*8);
          root.add(cloud);
        }
        camera.position.set(1.2, 0.6, 6.2);
      }
      if (kind === "scan" || kind === "docs") {
        const c = corrugate(1.6, 1.6, 3.2); c.position.x = -1.4; root.add(c);
        for (let i=0;i<6;i++){
          const paper = new THREE.Mesh(
            new THREE.BoxGeometry(1.4, 0.02, 1.9),
            new THREE.MeshStandardMaterial({ color: 0xf4f7fb, roughness: 0.8, metalness: 0.05 })
          );
          paper.position.set(1.4, 0.18*i - 0.4, 0);
          paper.rotation.y = 0.18 + i*0.04;
          paper.rotation.x = -0.4;
          root.add(paper);
        }
        const beam = new THREE.Mesh(new THREE.PlaneGeometry(3.6, 0.05), new THREE.MeshBasicMaterial({ color: 0x00adef, transparent:true, opacity:0.8 }));
        beam.rotation.x = -0.2; beam.userData.beam = true; root.add(beam);
      }
      if (kind === "quote") {
        const pack = crate(1.4, 0xc8a165);
        pack.name = "quotePack";
        root.add(pack);
        window.__quotePack = pack;
      }

      const clock = new THREE.Clock();
      let raf;
      const onResize = () => {
        const w = el.clientWidth, h = el.clientHeight;
        camera.aspect = w / Math.max(h,1);
        camera.updateProjectionMatrix();
        renderer.setSize(w, h, false);
      };
      window.addEventListener("resize", onResize);
      const loop = () => {
        raf = requestAnimationFrame(loop);
        const t = clock.getElapsedTime();
        root.rotation.y += (pointer.x * 0.35 - root.rotation.y) * 0.04;
        root.rotation.x += (-pointer.y * 0.18 - root.rotation.x) * 0.04;
        root.position.y = Math.sin(t * 0.8) * 0.12;
        scene.traverse((o) => {
          if (o.userData.wave && o.geometry.attributes.position) {
            const pos = o.geometry.attributes.position;
            for (let i=0;i<pos.count;i++){
              const x = pos.getX(i), y = pos.getY(i);
              pos.setZ(i, Math.sin(x*0.45 + t*1.4)*0.12 + Math.cos(y*0.4 + t)*0.08);
            }
            pos.needsUpdate = true; o.geometry.computeVertexNormals();
          }
          if (o.userData.beam) o.position.y = Math.sin(t*1.6)*1.1;
          if (o.userData.base) o.position.y = o.userData.base.y + Math.sin(t + o.position.x)*0.18;
        });
        if (kind === "globe") {
          const spin = root.userData.globeSpin;
          const boost = root.userData.scrollSpin || 0;
          if (spin) {
            const step = 0.0018 + boost;
            if (spin.userData.useLocalSpin) spin.rotateY(step);
            else spin.rotation.y += step;
          }
          root.traverse((o) => {
            if (o.userData.route) {
              const r = o.userData.route;
              r.t = (r.t + r.speed * 0.016) % 1;
              o.position.copy(r.curve.getPointAt(r.t));
            }
            if (o.userData.pulse) {
              const s = 1 + Math.sin(t * 2.2) * 0.18;
              o.scale.set(s, s, s);
              if (o.material) o.material.opacity = 0.45 + Math.sin(t * 2.2) * 0.35;
            }
          });
        }
        renderer.render(scene, camera);
      };
      if (!reduce) loop(); else renderer.render(scene, camera);
      const rec = { renderer, scene, camera, root, el, raf, onMove, onResize };
      scenes.push(rec);
      const io = new IntersectionObserver((ents) => {
        ents.forEach((en) => {
          if (!en.isIntersecting && rec.raf) { cancelAnimationFrame(rec.raf); rec.raf = 0; }
          else if (en.isIntersecting && !rec.raf && !reduce) loop();
        });
      }, { threshold: 0.05 });
      io.observe(el);
    } catch (err) {
      document.body.classList.add("no-webgl");
    }
  }

  const start3d = () => {
    if (canvas && canvas.dataset.scene) bootScene(canvas, canvas.dataset.scene || page);
    document.querySelectorAll("canvas[data-scene]").forEach((el) => {
      if (el.id === "scene" || el.id === "heroFrames") return;
      bootScene(el, el.dataset.scene);
    });
  };
  requestAnimationFrame(() => requestAnimationFrame(start3d));

  window.addEventListener("pagehide", () => {
    scenes.forEach((s) => {
      cancelAnimationFrame(s.raf);
      window.removeEventListener("pointermove", s.onMove);
      window.removeEventListener("resize", s.onResize);
      disposeScene(s.scene);
      s.renderer.dispose();
    });
    ScrollTrigger.getAll().forEach((t) => t.kill());
    if (lenis) lenis.destroy();
  });

  /* Quote package scale */
  const h = document.getElementById("height");
  const w = document.getElementById("width");
  const d = document.getElementById("depth");
  function updatePack(){
    const pack = window.__quotePack;
    if (!pack) return;
    const hv = Math.max(10, Number(h && h.value) || 40);
    const wv = Math.max(10, Number(w && w.value) || 40);
    const dv = Math.max(10, Number(d && d.value) || 40);
    gsap.to(pack.scale, { x: wv/40, y: hv/40, z: dv/40, duration: 0.45 });
  }
  [h,w,d].forEach((el) => el && el.addEventListener("input", updatePack));

  /* Quote form */
  const form = document.getElementById("quoteForm");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll("[required]").forEach((inp) => {
        const wrap = inp.closest(".field");
        const valid = inp.value.trim() && (inp.type !== "email" || /.+@.+\..+/.test(inp.value));
        wrap?.classList.toggle("error", !valid);
        if (!valid) ok = false;
      });
      if (!ok) {
        document.getElementById("formStatus").textContent = "Please complete the required fields.";
        return;
      }
      const data = new FormData(form);
      const lines = [];
      data.forEach((v,k) => lines.push(k + ": " + v));
      const mailto = "mailto:sayyam7@imexclearing.com?subject=" + encodeURIComponent("IMEX quote request") + "&body=" + encodeURIComponent(lines.join("\n"));
      document.getElementById("formStatus").textContent = "Opening your email client to send this enquiry to IMEX. No quote is generated on this page.";
      window.location.href = mailto;
    });
  }

  /* 1994 story band */
  (function storyBand(){
    const band = document.querySelector("[data-story-band]");
    if (!band) return;
    const copy = band.querySelector(".story-copy");
    const visual = band.querySelector(".story-visual");
    const year = band.querySelector(".story-year");
    const truck = band.querySelector(".story-truck");
    const yard = band.querySelector(".story-yard");
    const mmS = gsap.matchMedia();
    mmS.add("(prefers-reduced-motion: no-preference)", () => {
      const tl = gsap.timeline({
        defaults: { ease: "power3.out" },
        scrollTrigger: { trigger: band, start: "top 88%", once: true }
      });
      tl.from(year, { y: 28, opacity: 0, duration: 0.7 })
        .from(band.querySelector(".story-title"), { y: 32, opacity: 0, duration: 0.75 }, "-=0.4")
        .from(band.querySelector(".story-rule"), { scaleX: 0, transformOrigin: "left center", duration: 0.45 }, "-=0.35")
        .from(band.querySelectorAll(".story-copy .lede"), { y: 18, opacity: 0, stagger: 0.08, duration: 0.55 }, "-=0.25")
        .from(band.querySelectorAll(".story-actions > *"), { y: 16, opacity: 0, stagger: 0.07, duration: 0.45 }, "-=0.28")
        .from(yard, { scale: 1.08, opacity: 0, duration: 0.9 }, 0)
        .from(truck, { x: 56, opacity: 0, duration: 0.9 }, 0.18)
        .from(band.querySelectorAll(".story-pill"), { y: 20, opacity: 0, scale: 0.94, stagger: 0.08, duration: 0.5 }, 0.45)
        .from(band.querySelector(".story-corner"), { opacity: 0, duration: 0.5 }, 0.5);

      if (copy) {
        gsap.fromTo(copy, { y: 90 }, {
          y: -36,
          ease: "none",
          scrollTrigger: { trigger: band, start: "top bottom", end: "bottom top", scrub: 1.05 }
        });
      }
      if (visual) {
        gsap.fromTo(visual, { y: 48 }, {
          y: -72,
          ease: "none",
          scrollTrigger: { trigger: band, start: "top bottom", end: "bottom top", scrub: 1.2 }
        });
      }
    });
    mmS.add("(prefers-reduced-motion: reduce)", () => {
      gsap.from(band, { opacity: 0, duration: 0.2, ease: "none", scrollTrigger: { trigger: band, start: "top 85%", once: true } });
    });
  })();

  /* Enquiry band */
  (function quoteBand(){
    const band = document.querySelector("[data-quote-band]");
    if (!band) return;
    const courier = band.querySelector(".qb-courier");
    const path = band.querySelector(".qb-dash");
    const plane = band.querySelector(".qb-plane");
    if (courier) gsap.set(courier, { xPercent: -50 });

    const mmQ = gsap.matchMedia();
    mmQ.add("(prefers-reduced-motion: no-preference)", () => {
      const tl = gsap.timeline({
        defaults: { ease: "power3.out" },
        scrollTrigger: { trigger: band, start: "top 78%", once: true }
      });
      tl.from(band.querySelector(".qb-kicker"), { y: 20, opacity: 0, duration: 0.55 })
        .from(band.querySelector(".qb-title"), { y: 36, opacity: 0, duration: 0.8 }, "-=0.32")
        .from(band.querySelector(".qb-lede"), { y: 18, opacity: 0, duration: 0.55 }, "-=0.45")
        .from(band.querySelector(".qb-cta"), { y: 16, opacity: 0, scale: 0.94, duration: 0.45 }, "-=0.32")
        .from(band.querySelector(".qb-flight"), { opacity: 0, duration: 0.6, ease: "none" }, "-=0.2")
        .fromTo(band.querySelector(".qb-frame"), { x: 48, opacity: 0, rotation: -8 }, { x: 0, opacity: 1, rotation: -14, duration: 0.9 }, 0.12)
        .fromTo(courier, { y: 36, opacity: 0, scale: 0.96, xPercent: -50 }, { y: 0, opacity: 1, scale: 1, xPercent: -50, duration: 0.85 }, 0.22)
        .from(band.querySelectorAll(".qb-chip"), { scale: 0.92, opacity: 0, stagger: 0.07, duration: 0.45 }, 0.48)
        .from(band.querySelector(".qb-globe"), { opacity: 0, y: 24, duration: 0.9 }, 0.18)
        .from(band.querySelector(".qb-orbit"), { opacity: 0, duration: 0.6 }, 0.4);

      gsap.to(band.querySelector(".qb-orbit"), { rotation: 360, duration: 22, repeat: -1, ease: "none", transformOrigin: "50% 52%" });
      gsap.to(band.querySelector(".qb-chip-box"), { y: -10, duration: 2.6, yoyo: true, repeat: -1, ease: "sine.inOut" });
      gsap.to(band.querySelector(".qb-chip-pin"), { y: 10, duration: 3.1, yoyo: true, repeat: -1, ease: "sine.inOut" });
      gsap.to(band.querySelector(".qb-blob-a"), { x: 18, y: -12, duration: 8, yoyo: true, repeat: -1, ease: "sine.inOut" });
      gsap.to(band.querySelector(".qb-blob-b"), { x: -14, y: 16, duration: 10, yoyo: true, repeat: -1, ease: "sine.inOut" });
      gsap.to(band.querySelector(".qb-globe-spin"), { rotation: 360, duration: 80, repeat: -1, ease: "none", transformOrigin: "260px 300px" });
      gsap.to(courier, { y: -8, duration: 3.4, yoyo: true, repeat: -1, ease: "sine.inOut" });

      if (path && plane) {
        const len = path.getTotalLength();
        const fly = { p: 0 };
        const place = () => {
          const d = fly.p * len;
          const a = path.getPointAtLength(d);
          const b = path.getPointAtLength(Math.min(len, d + 2));
          gsap.set(plane, { x: a.x, y: a.y, rotation: Math.atan2(b.y - a.y, b.x - a.x) * 180 / Math.PI, transformOrigin: "4px 2px" });
        };
        place();
        gsap.to(fly, { p: 1, duration: 7.2, repeat: -1, ease: "none", onUpdate: place });
      }
    });
    mmQ.add("(prefers-reduced-motion: reduce)", () => {
      gsap.from([band.querySelector(".qb-copy"), band.querySelector(".qb-visual")], {
        opacity: 0, duration: 0.2, ease: "none",
        scrollTrigger: { trigger: band, start: "top 85%", once: true }
      });
    });
  })();

  /* Kanpur desk */
  (function touchBand(){
    const band = document.querySelector("[data-touch-band]");
    if (!band) return;
    const mmT = gsap.matchMedia();
    mmT.add("(prefers-reduced-motion: no-preference)", () => {
      const tl = gsap.timeline({
        defaults: { ease: "power3.out" },
        scrollTrigger: { trigger: band, start: "top 78%", once: true }
      });
      tl.from(band.querySelector(".touch-kicker"), { y: 16, opacity: 0, duration: 0.45 })
        .from(band.querySelector(".touch-title"), { y: 28, opacity: 0, duration: 0.7 }, "-=0.22")
        .from(band.querySelector(".touch-addr"), { y: 16, opacity: 0, duration: 0.5 }, "-=0.4")
        .from(band.querySelector(".touch-copy .btn"), { y: 12, opacity: 0, duration: 0.4 }, "-=0.28")
        .from(band.querySelector(".touch-plate"), { y: 36, opacity: 0, duration: 0.8 }, 0.1)
        .from(band.querySelector(".touch-map"), { scale: 1.08, duration: 1.1 }, 0.12)
        .from(band.querySelector(".touch-pin"), { scale: 0, duration: 0.45, ease: "back.out(1.6)" }, 0.45)
        .from(band.querySelectorAll(".touch-lines a"), { y: 12, opacity: 0, stagger: 0.07, duration: 0.45 }, 0.4)
        .from(band.querySelectorAll(".touch-desks a"), { y: 8, opacity: 0, stagger: 0.06, duration: 0.35 }, 0.55);
      gsap.to(band.querySelector(".touch-pin"), {
        scale: 1.12, duration: 1.8, yoyo: true, repeat: -1, ease: "sine.inOut"
      });
    });
  })();

  /* Footer horizon */
  (function footBand(){
    const foot = document.querySelector(".site-foot");
    const line = foot && foot.querySelector(".foot-horizon");
    if (!foot || !line || reduce) return;
    gsap.fromTo(line, { scaleX: 0 }, {
      scaleX: 1, ease: "none",
      scrollTrigger: { trigger: foot, start: "top 96%", end: "top 72%", scrub: true }
    });
  })();

  /* VAS reference desk */
  (function vasBand(){
    const band = document.querySelector("[data-vas-band]");
    if (!band) return;
    const links = [...band.querySelectorAll("[data-vas-i]")];
    const imgs = [...band.querySelectorAll("[data-vas-img]")];
    const setActive = (i) => {
      links.forEach((a) => a.classList.toggle("is-on", a.dataset.vasI === String(i)));
      imgs.forEach((img) => img.classList.toggle("is-on", img.dataset.vasImg === String(i)));
    };
    links.forEach((a) => {
      const activate = () => setActive(a.dataset.vasI);
      a.addEventListener("pointerenter", activate);
      a.addEventListener("focus", activate);
    });
    if (reduce) return;
    gsap.from(band.querySelector(".vas-kicker"), {
      y: 16, opacity: 0, duration: 0.4, ease: "power3.out",
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
    gsap.from(band.querySelector(".vas-title"), {
      y: 28, opacity: 0, duration: 0.7, ease: "power3.out",
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
    gsap.from(band.querySelector(".vas-lede"), {
      y: 16, opacity: 0, duration: 0.5, delay: 0.08, ease: "power3.out",
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
    gsap.from(band.querySelector(".vas-copy .btn"), {
      y: 14, opacity: 0, duration: 0.45, delay: 0.14, ease: "power3.out",
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
    gsap.from(band.querySelector(".vas-stage"), {
      y: 36, opacity: 0, duration: 0.8, ease: "power3.out",
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
    gsap.from(links, {
      y: 16, opacity: 0, stagger: 0.08, duration: 0.45, delay: 0.2, ease: "power3.out",
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
  })();

  /* Track band */
  (function trackBand(){
    const band = document.querySelector("[data-track-band]");
    if (!band || reduce) return;
    const live = band.querySelector(".track-route-live");
    const plane = band.querySelector(".track-plane");
    const pulses = band.querySelectorAll(".track-pulse");
    const pathLen = live ? (live.getTotalLength ? live.getTotalLength() : 420) : 420;
    if (live) gsap.set(live, { strokeDasharray: pathLen, strokeDashoffset: pathLen });
    const tl = gsap.timeline({
      defaults: { ease: "power3.out" },
      scrollTrigger: { trigger: band, start: "top 78%", once: true }
    });
    tl.from(band.querySelector(".track-kicker"), { y: 16, opacity: 0, duration: 0.4 })
      .from(band.querySelector(".track-title"), { y: 28, opacity: 0, duration: 0.7 }, "-=0.2")
      .from(band.querySelector(".track-lede"), { y: 16, opacity: 0, duration: 0.45 }, "-=0.4")
      .from(band.querySelector(".track-console"), { y: 22, opacity: 0, duration: 0.55 }, "-=0.3")
      .from(band.querySelector(".track-radar"), { y: 30, opacity: 0, duration: 0.7 }, 0.12)
      .from(band.querySelectorAll(".track-stops span"), { y: 12, opacity: 0, stagger: 0.08, duration: 0.4 }, 0.45);
    if (live) {
      tl.to(live, { strokeDashoffset: 0, duration: 1.6, ease: "power2.inOut" }, 0.35);
    }
    if (plane) {
      gsap.set(plane, { x: -202, y: 160, rotation: -28, transformOrigin: "12px 4px" });
      tl.to(plane, { x: 0, y: 0, rotation: -18, duration: 0.9, ease: "power2.inOut" }, 0.45)
        .to(plane, { x: 280, y: -100, rotation: -12, duration: 0.9, ease: "power2.inOut" }, 0.95);
    }
    if (pulses.length) {
      gsap.to(pulses, {
        scale: 1.08, opacity: 0.35, duration: 2.4, stagger: 0.25,
        yoyo: true, repeat: -1, ease: "sine.inOut"
      });
    }
  })();

  /* Tracking */
  const track = document.getElementById("trackForm");
  if (track) {
    track.addEventListener("submit", (e) => {
      e.preventDefault();
      const n = (document.getElementById("awb")?.value || "").trim();
      const url = "https://www.track-trace.com/";
      window.open(url, "_blank", "noopener");
      const note = document.getElementById("trackNote");
      if (note) note.textContent = n
        ? "Continue on Track & Trace with number " + n + ". IMEX uses the original Track & Trace destination."
        : "Continue on the original Track & Trace destination.";
    });
  }

  /* Hero intro — waits for boot loader */
  whenBooted.then(() => {
    if (reduce || !document.querySelector(".hero")) {
      ScrollTrigger.refresh();
      return;
    }
    const tl = gsap.timeline({ defaults:{ ease:"power3.out" }, onComplete: () => ScrollTrigger.refresh() });
    tl.fromTo(".intro-line", { width:0 }, { width:"100%", duration:1.1 })
      .to(".intro-line", { autoAlpha: 0, duration: 0.45 }, "+=0.15");
    if (document.querySelector(".hero-film")) {
      tl.from(".hero-film .hero-lead", { y:16, opacity:0, duration:0.5 }, "-=0.4")
        .from(".hero-film .hero-line > span", { yPercent:110, opacity:0, stagger:0.1, duration:0.85 }, "-=0.2")
        .from(".hero-film .hero-sub", { y:18, opacity:0, duration:0.55 }, "-=0.45")
        .from(".hero-film .hero-aside, .hero-film .hero-actions", { y:20, opacity:0, stagger:0.08, duration:0.6 }, "-=0.35");
    } else {
      tl.from(".hero-copy .kicker", { y:20, opacity:0, duration:0.5 }, "-=0.4")
        .from(".hero h1 span", { yPercent:110, opacity:0, stagger:0.03, duration:0.9 }, "-=0.2")
        .from(".hero .lede, .hero-actions", { y:24, opacity:0, stagger:0.08, duration:0.7 }, "-=0.45");
    }
  });
})();
