# Within reach: ownership before tax

Selected visual language: the cut-paper Within reach style frame. The colossus and Separate bodies remain saved for later use. Keep the original frames intact.

## The one discovery

You own shares in a company; the company owns its cash. Moving the owner illustration does not carry company money along. Moving the company does. A deliberately labelled dividend transfers one highlighted payment, which subsequently moves with the owner.

## Scope

An individual shareholder receiving a lawfully declared taxable dividend from after-tax company funds. No amounts, rates, tax slice or implied savings. State that personal tax may arise and dividend tax credits help recognise corporate tax already paid. Salary, shareholder loans, returns of capital and capital dividends follow other rules. Illustration movement is only a way to reveal grouping, not a legal action or transfer.

## Art and composition

The approved frame is separated into transparent company, owner and payment assets using image generation. The money baked into the company remains company property throughout. One extra, visually highlighted orange note is the payment; it must exist exactly once. It begins with the company and ends at the owner's open hand.

Color tokens: lemon #ffdf08, ultramarine artwork #1244bb, ink #151819, orange artwork #f47b0d, ivory #fff9d8. Quiet system sans UI: 16px body, 13px supporting text, 28–34px narrative. Artwork dominates, no new ornamental icons or content cards. Controls sit below the scene, with one short state-specific sentence above them. The strongest visual is still the character and company relationship.

Composition: familiar full illustration in a roomy stage; stage moves remain bounded. Mobile keeps the whole relationship in view and has equivalent buttons so precision dragging is unnecessary. Native buttons, visible focus, live narrative, reduced motion and reset are required.

## State invariants

- Before dividend: moving owner never moves the highlighted note. Company movement carries it.
- During transfer: moving subjects is locked; reset cancels and restores a consistent state.
- After dividend: note follows the owner; remaining notes stay with the company.
- One payment per run; repeated activation cannot mint notes.
- Reset restores positions, ownership, narrative and control states together.

## Assets

Original style frame: `../style-frames/assets/within-reach.png`.
Generated cutouts: `assets/company.png`, `assets/owner.png`, `assets/payment.png`. These production files and the original style frame are versioned in the repository and catalogued with hashes in `../../design/within-reach/asset-manifest.json`. Historical exact generation requests were not recovered. For future consistent assets, use `../../docs/STYLE-SYSTEM.md` and the reconstructed image prompt template; record exact new requests. This is a working teaching prototype, not compliance-approved financial marketing material.
