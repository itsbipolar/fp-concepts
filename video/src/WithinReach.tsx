import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Easing, Img, cancelRender, continueRender, delayRender, interpolate, staticFile, useCurrentFrame} from 'remotion';
import tokens from '../../design/within-reach/style-tokens.json';

// Project-authored composition. The supplied kit informs beat mapping and
// paper staging; no stock art filters, font loaders or style modules are used.
const C = Object.fromEntries(Object.entries(tokens.colors).map(([k, v]) => [k, v.hex]));
const progress = (frame: number, start: number, end: number) =>
  interpolate(frame, [start, end], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic),
  });
const between = (a: number, b: number, p: number) => a + (b - a) * p;
const art = (name: string) => staticFile(`assets/${name}.png`);

export const WithinReach: React.FC = () => {
  const [fontHandle] = useState(() => delayRender('Load the bundled Within reach font'));
  useEffect(() => {
    const font = new FontFace('WithinReachSans', `url(${staticFile('fonts/LiberationSans-Bold.ttf')})`, {weight: '700'});
    font.load().then((loaded) => {document.fonts.add(loaded); continueRender(fontHandle);}).catch(cancelRender);
  }, [fontHandle]);
  const f = useCurrentFrame();
  const travel = progress(f, 36, 99);
  const widen = progress(f, 114, 174);
  const reveal = progress(f, 147, 195);
  const title = progress(f, 129, 150);
  const scale = between(810 / 1536, 760 / 1536, widen);
  const x = between(235, 24, widen);
  const y = between(155, 172, widen);
  const paymentX = between(350, 1290, travel);
  const paymentY = between(680, 410, travel) - Math.sin(Math.PI * travel) * 150;

  return (
    <AbsoluteFill style={{backgroundColor: C.ground, color: C.ink, fontFamily: 'WithinReachSans'}}>
      <svg width="1280" height="720" style={{position: 'absolute', opacity: 0.045}} aria-hidden="true">
        <filter id="paper-grain"><feTurbulence type="fractalNoise" baseFrequency="0.72" numOctaves="3" seed="12" stitchTiles="stitch" /></filter>
        <rect width="1280" height="720" filter="url(#paper-grain)" />
      </svg>
      <div style={{position: 'absolute', left: 64, top: 30, fontSize: 17, fontWeight: 700, letterSpacing: 0.2}}>
        Within reach
      </div>
      <div style={{position: 'absolute', right: 64, top: 31, fontSize: 15, fontWeight: 700, opacity: 0.65}}>
        Motion study · 01
      </div>
      <div style={{position: 'absolute', left: 64, top: 73, fontSize: 53, fontWeight: 700, letterSpacing: -1.5}}>
        <div style={{opacity: 1 - title}}>One decision.</div>
        <div style={{position: 'absolute', left: 0, top: 0, whiteSpace: 'nowrap', opacity: title}}>A longer view.</div>
      </div>

      {/* Preserve the common 1536×1024 image grid: elbow and company stay aligned. */}
      <div style={{position: 'absolute', left: x, top: y, width: 1536, height: 1024,
        transform: `scale(${scale})`, transformOrigin: '0 0'}}>
        <Img src={art('company')} style={{position: 'absolute', width: 1536, height: 1024}} />
        <Img src={art('owner')} style={{position: 'absolute', width: 1536, height: 1024}} />
        <Img src={art('payment')} style={{position: 'absolute', left: paymentX, top: paymentY,
          width: 245, height: 122.5, transform: `rotate(${between(-12, 8, travel)}deg)`}} />
      </div>

      {/* No cash enters this paper. It introduces time, not a savings balance. */}
      <div style={{position: 'absolute', left: 555 + (1 - reveal) * 110, top: 164,
        width: 1536, height: 1024, opacity: reveal,
        transform: `scale(${800 / 1536})`, transformOrigin: '0 0'}}>
        <Img src={art('future-owner')} style={{position: 'absolute', width: 1536, height: 1024}} />
        <div style={{position: 'absolute', left: 488, top: 245, fontSize: 60, fontWeight: 700,
          transform: 'rotate(-6deg)', opacity: progress(f, 174, 201)}}>Later.</div>
      </div>
      <div style={{position: 'absolute', left: 64, top: 153, fontSize: 27, fontWeight: 700,
        opacity: progress(f, 12, 28)}}>Today.</div>
    </AbsoluteFill>
  );
};
