/* Qualitative teaching states. No unverified tax rates or take-home estimates. */
(() => {
  'use strict';
  const model = {
    status: 'qualitative-prototype',
    quantified: false,
    scope: 'Working controlling shareholder, age 40; pensionable salary below the annual CPP ceiling; no other earned income or employer pension plan. Canadian corporation, non-eligible taxable dividends.',
    verification: {
      suppliedNotes: 'sources/v0-cfp-crash-notes/notes.txt',
      livePrimarySources: false,
      reason: 'Official source hosts blocked by environment policy; network additions saved for review. No tax amounts, contribution amounts, pension estimate or equal-cost outcome are calculated.'
    },
    introduction: {
      company: {title: 'Start with the company', body: 'Salary and dividends leave the company under different rules. Choose a route to see the deduction or after-tax-profit relationship. The illustrated note is symbolic; it is not an equal-cost comparison.'},
      personal: {title: 'The payment reaches you', body: 'Both routes can create personal income tax. The route also changes CPP contributions and which tax rules apply. This scene explains the mechanism, without estimating your take-home pay.'},
      cpp: {title: 'Your earnings record follows you', body: 'Earlier pensionable earnings remain on your CPP record. Watch whether this payment adds pensionable earnings. The record is not a cash account, and its marks are not equal pension amounts.'},
      rrsp: {title: 'Room is permission to contribute', body: 'Existing unused RRSP room carries forward. New room depends on earned income from the preceding year and applicable limits and adjustments. Opening a paper flap means more contribution capacity, not money already saved.'}
    },
    scenarios: {
      salary: {
        labels: {company: 'A deductible expense', personal: 'Income tax + your CPP', cpp: 'Pensionable earnings added', rrsp: 'New room can open'},
        paymentLabel: 'Salary payment',
        beats: [
          'Salary is an expense for the company and employment income for you.',
          'You and the company pay CPP. Pensionable earnings join your record.',
          'This year’s salary can also create RRSP room for next year.'
        ],
        details: {
          company: {title: 'Salary is an expense for work', body: 'A reasonable salary paid for work is generally deductible when the company calculates its taxable income. Employer CPP is an additional company cost and is generally deductible too. A deduction reduces taxable income; it is not a dollar-for-dollar tax refund.'},
          personal: {title: 'Your salary is employment income', body: 'Personal income tax and employee CPP can reduce cash available to you. The company also pays its employer share of CPP. Actual income tax depends on your full-year income, province, deductions and credits; this prototype calculates none of those amounts.'},
          cpp: {title: 'Contributions and a pension record', body: 'For this working owner below the CPP earnings ceiling, the salary creates pensionable earnings and both employee and employer contributions. The new mark represents pensionable earnings recorded, not a fixed pension increment or money deposited in a personal account. Future pension entitlement depends on the complete contribution history, applicable limits and benefit rules.'},
          rrsp: {title: 'Salary can create next year’s room', body: 'Salary counts as earned income for calculating new RRSP room in the following year, subject to the annual limit and adjustments. This scene assumes no employer pension plan or other earned income. Existing unused room remains; the unfolding flap represents potential additional room. You still need to contribute money to use it.'}
        }
      },
      dividend: {
        labels: {company: 'Paid from after-tax profit', personal: 'Dividend income tax rules', cpp: 'No earnings added by this dividend', rrsp: 'No new room from this dividend'},
        paymentLabel: 'Taxable dividend',
        beats: [
          'A dividend comes from after-tax profit. Personal tax can still arise.',
          'This dividend adds no CPP earnings. Your earlier record stays.',
          'It creates no new RRSP room. Any room you already have remains.'
        ],
        details: {
          company: {title: 'A distribution of after-tax profit', body: 'This route assumes a lawfully declared non-eligible taxable dividend from a Canadian corporation’s after-tax profits. The dividend is not a salary expense or a corporate tax deduction. The tax label describes tax on the underlying profit, not a new corporate tax charged each time a dividend is paid.'},
          personal: {title: 'Dividend tax rules still apply', body: 'Taxable dividends are included in personal income using the applicable gross-up. Dividend tax credits help recognise company tax already paid. A dividend is not automatically tax-free or cheaper than salary. No employee or employer CPP arises from the dividend itself; this prototype does not rank the routes by take-home cash.'},
          cpp: {title: 'No new CPP earnings from a dividend', body: 'Dividends are investment income, not CPP pensionable earnings. This payment adds no employee or employer CPP contributions and no pensionable earnings to the record. Earlier contributions and any resulting entitlement remain; the unchanged record does not mean you have no CPP pension.'},
          rrsp: {title: 'Existing room stays available', body: 'Dividends do not count as earned income for creating new RRSP room. This dividend therefore adds no new room for next year. Unused room carried forward and room generated by other eligible income are not removed.'}
        }
      }
    }
  };
  function freeze(value) {
    Object.values(value).forEach(item => { if (item && typeof item === 'object') freeze(item); });
    return Object.freeze(value);
  }
  window.FPModel = freeze(model);
})();
