import React from 'react';
import {Composition} from 'remotion';
import {WithinReach} from './WithinReach';

export const Root = () => (
  <Composition id="WithinReach" component={WithinReach}
    durationInFrames={270} fps={30} width={1280} height={720} />
);
