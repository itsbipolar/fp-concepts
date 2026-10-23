import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Audio, Easing, Img, cancelRender, continueRender, delayRender, interpolate, staticFile, useCurrentFrame} from 'remotion';

const ease = (f: number, a: number, b: number) => interpolate(f, [a, b], [0, 1], {
  extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic),
});
const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const art = (name: string) => staticFile(`assets/${name}.png`);
const grid: React.CSSProperties = {position: 'absolute', width: 1536, height: 1024};
const label: React.CSSProperties = {position: 'absolute', fontSize: 40, lineHeight: 1.08};

// The same unmodified 1536×1024 alignment plane is used in every shot.
// Note dimensions never encode tax, credit or take-home amounts.
export const SalaryDividendPassage: React.FC = () => {
  const [fontHandle] = useState(() => delayRender('Load passage font'));
  useEffect(() => {
    const font = new FontFace('WithinReachSans', `url(${staticFile('fonts/LiberationSans-Bold.ttf')})`, {weight: '700'});
    font.load().then((loaded) => {document.fonts.add(loaded); continueRender(fontHandle);}).catch(cancelRender);
  }, [fontHandle]);
  const f = useCurrentFrame();
  const companyShot = f >= 81 && f < 249;
  const wide = ease(f, 321, 355);
  const scale = companyShot ? 0.68 : lerp(0.82, 0.53, wide);
  const x = companyShot ? 285 : lerp(-160, 180, wide);
  const y = companyShot ? -85 : lerp(80, 130, wide);
  // Exact arrival path is retraced for six frames; the edit then leaves this shot.
  const arrival = ease(f, 10, 57);
  const reverse = ease(f, 75, 80);
  const replay = ease(f, 259, 306);
  const contact = ease(f, 306, 320);
  const dividendX = f < 81 ? lerp(945, 1030, arrival * (1 - reverse))
    : lerp(945, 1030, replay) + 80 * contact;
  const tax = ease(f, 112, 190);
  const taxX = lerp(350, -720, tax);
  const taxY = lerp(650, 1110, tax);
  const caption = f >= 99 && f < 196
    ? <>Take it as a dividend, and the company<br />pays its tax first.</>
    : f >= 249 && f < 347
      ? <>You get a tax break for that,<br />but you still pay tax on the rest.</> : null;

  return <AbsoluteFill style={{backgroundColor: '#ffdf08', color: '#151819', fontFamily: 'WithinReachSans', fontWeight: 700}}>
    <Audio src={staticFile('assets/salary-dividend-passage.wav')} />
    <svg width="1280" height="720" style={{position: 'absolute', opacity: 0.045}} aria-hidden="true">
      <filter id="salary-paper"><feTurbulence type="fractalNoise" baseFrequency="0.72" numOctaves="3" seed="12" stitchTiles="stitch" /></filter>
      <rect width="1280" height="720" filter="url(#salary-paper)" />
    </svg>
    <div style={{...grid, left: x, top: y, transform: `scale(${scale})`, transformOrigin: '0 0'}}>
      {(companyShot || f >= 321) && <Img src={art('company')} style={grid} />}
      {!companyShot && <Img src={art('owner')} style={grid} />}
      {companyShot ? <>
        {f >= 112 && f <= 190 && <Img src={art('payment')} style={{position: 'absolute', left: taxX, top: taxY,
          width: 245, height: 122.5, transform: 'rotate(-8deg)'}} />}
        {/* Recessed aperture: the unchanged blue foreground covers the moving
            note at the left jamb and bottom sill. The baked notes stay static. */}
        <svg width="1536" height="1024" style={{position: 'absolute', left: 0, top: 0}}>
          <defs><clipPath id="company-foreground"><path clipRule="evenodd"
            d="M0 0H1536V1024H0Z M168 555L687 433L693 935L158 942Z" /></clipPath></defs>
          <image href={art('company')} width="1536" height="1024" clipPath="url(#company-foreground)" />
        </svg>
      </> : <Img src={art('payment')} style={{position: 'absolute', left: dividendX, top: 420,
        width: 245, height: 122.5, transform: 'rotate(-8deg)'}} />}
    </div>

    {f < 75 && <div style={{...label, left: 870, top: 296}}>Your dividend tax</div>}
    {f >= 75 && f < 112 && <div style={{position: 'absolute', left: 64, top: 52, fontSize: 52}}>Before the dividend</div>}
    {companyShot && f >= 112 && f < 204 && <div style={{...label, left: 64, top: 210}}>Company tax<br />on profit</div>}
    {f >= 204 && f < 249 && <div style={{position: 'absolute', left: 64, top: 52, fontSize: 52}}>Then, the dividend</div>}
    {f >= 249 && f < 306 && <div style={{position: 'absolute', left: 64, top: 24, fontSize: 46}}>Same dividend, fuller picture</div>}
    {f >= 321 && <>
      <div style={{position: 'absolute', left: 64, top: 45, fontSize: 50}}>Both belong in the comparison.</div>
      <div style={{...label, left: 175, top: 204}}>Company tax</div>
      <div style={{...label, left: 1010, top: 318}}>Your<br />dividend tax</div>
    </>}
    {caption && <div style={{position: 'absolute', left: 0, right: 0, bottom: 40, textAlign: 'center', fontSize: 32,
      lineHeight: 1.15}}><span style={{backgroundColor: '#fff9d8', padding: '4px 14px', boxDecorationBreak: 'clone'}}>{caption}</span></div>}
    <div style={{position: 'absolute', bottom: 10, left: 64, fontSize: 17, opacity: 0.75}}>Symbolic payments • no amounts compared</div>
  </AbsoluteFill>;
};
