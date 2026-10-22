(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const scene = $('scene');
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const state = { choice: null, beat: 0, playing: false, revision: 0 };
  let timer = null;
  let paymentMotion = null;
  let detailSubject = null;
  let returnFocus = null;
  const beatDuration = 1000;

  function scenario() { return state.choice ? window.FPModel.scenarios[state.choice] : null; }
  function expose() { window.salaryLessonState = { ...state }; }
  function cancel() { clearTimeout(timer); timer = null; state.revision++; }
  function render() {
    const data = scenario();
    scene.dataset.choice = state.choice || 'none';
    scene.dataset.beat = state.beat;
    scene.classList.toggle('paused', Boolean(state.choice) && !state.playing && state.beat < 3);
    scene.setAttribute('aria-busy', String(state.playing));
    for (const name of ['salary', 'dividend']) $(name).setAttribute('aria-pressed', String(state.choice === name));
    $('pause').disabled = !state.choice || state.beat === 3;
    $('pause').textContent = state.playing ? 'Pause' : 'Continue';
    $('replay').disabled = !state.choice;
    if (data) {
      $('company-label').textContent = data.labels.company;
      $('personal-label').textContent = data.labels.personal;
      $('cpp-label').textContent = data.labels.cpp;
      $('rrsp-label').textContent = data.labels.rrsp;
      $('payment-caption').textContent = data.paymentLabel;
      $('story').textContent = data.beats[Math.max(0, state.beat - 1)];
    } else {
      $('company-label').textContent = 'Company tax';
      $('personal-label').textContent = 'Personal tax';
      $('cpp-label').textContent = 'Pensionable earnings';
      $('rrsp-label').textContent = 'Contribution room';
      $('payment-caption').textContent = 'One symbolic payment';
      $('story').textContent = 'Choose how to pay yourself. Follow what changes now, and what follows you.';
    }
    if (detailSubject) updateDetail();
    expose();
  }
  function pulse() {
    scene.querySelectorAll('.pulse').forEach(el => el.classList.remove('pulse'));
    const ids = state.beat === 1 ? ['company-tax','owner-tax'] : state.beat === 2 ? ['cpp-record'] : ['rrsp-room'];
    for (const id of ids) { void $(id).offsetWidth; $(id).classList.add('pulse'); }
  }
  function schedule() {
    const revision = state.revision;
    timer = setTimeout(() => {
      if (revision !== state.revision || !state.playing) return;
      if (state.beat < 3) {
        state.beat++;
        pulse();
        if (state.beat === 3) state.playing = false;
        render();
        if (state.playing) schedule();
      }
    }, beatDuration);
  }
  function choose(choice) {
    cancel();
    paymentMotion?.cancel();
    paymentMotion = null;
    state.choice = choice;
    state.beat = 0;
    state.playing = !motion.matches;
    render();
    // Commit the starting pose before beginning a fresh payment journey.
    void scene.offsetWidth;
    state.beat = motion.matches ? 3 : 1;
    render();
    if (state.playing) {
      paymentMotion = $('payment').animate([
        { left:'30%', top:'66%', transform:'rotate(-10deg)' },
        { left:'59%', top:'35%', transform:'rotate(-1deg)', offset:.55 },
        { left:'82%', top:'40%', transform:'rotate(8deg)' }
      ], { duration:900, easing:'cubic-bezier(.35,0,.3,1)' });
      pulse(); schedule();
    }
  }
  function updateDetail() {
    const data = scenario();
    const detail = data?.details[detailSubject] || window.FPModel.introduction[detailSubject];
    $('detail-title').textContent = detail.title;
    $('detail-body').textContent = detail.body;
  }
  function closeDetail() {
    $('detail-note').hidden = true;
    detailSubject = null;
    if (returnFocus) returnFocus.focus({preventScroll:true});
  }
  for (const choice of ['salary','dividend']) $(choice).addEventListener('click', () => choose(choice));
  $('replay').addEventListener('click', () => { if (state.choice) choose(state.choice); });
  $('pause').addEventListener('click', () => {
    if (!state.choice || state.beat === 3) return;
    cancel(); state.playing = !state.playing; render();
    if (state.playing) { paymentMotion?.play(); schedule(); }
    else paymentMotion?.pause();
  });
  $('reset').addEventListener('click', () => {
    cancel(); state.choice = null; state.beat = 0; state.playing = false;
    paymentMotion?.cancel(); paymentMotion = null;
    scene.querySelectorAll('.pulse').forEach(el => el.classList.remove('pulse'));
    $('detail-note').hidden = true; detailSubject = null; render();
  });
  for (const el of document.querySelectorAll('[data-detail]')) el.addEventListener('click', () => {
    detailSubject = el.dataset.detail; returnFocus = el;
    updateDetail(); $('detail-note').hidden = false;
    $('detail-note').scrollIntoView({ behavior: motion.matches ? 'instant' : 'smooth', block:'nearest' });
    $('close-detail').focus({preventScroll:true});
  });
  $('close-detail').addEventListener('click', closeDetail);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && detailSubject) closeDetail(); });
  motion.addEventListener('change', () => {
    if (motion.matches && state.choice && state.beat < 3) { cancel(); paymentMotion?.cancel(); state.beat = 3; state.playing = false; render(); }
  });
  render();
})();
