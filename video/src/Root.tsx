import React from 'react';
import {Composition} from 'remotion';
import {WithinReach} from './WithinReach';
import {SalaryDividendPassage} from './salary-dividend/SalaryDividendPassage';

export const Root = () => (
  <>
    <Composition id="WithinReach" component={WithinReach}
      durationInFrames={270} fps={30} width={1280} height={720} />
    <Composition id="SalaryDividendPassage" component={SalaryDividendPassage}
      durationInFrames={420} fps={30} width={1280} height={720} />
  </>
);
