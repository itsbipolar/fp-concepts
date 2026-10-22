# Within reach drawing system

The approved visual anchor is [the original Within reach frame](../explorations/style-frames/assets/within-reach.png). Inspect it before making artwork; words alone cannot recover its drawing. This contract preserves the drawing language across lessons, not one company's props. Read [interaction principles](INTERACTION-PRINCIPLES.md) for teaching behaviour and the [current brief](../explorations/within-reach/BRIEF.md) for this prototype's scope.

## Canonical kit

- Master: `explorations/style-frames/assets/within-reach.png`.
- Approved production components: `explorations/within-reach/assets/{company,owner,payment}.png`. The [owner](../explorations/within-reach/assets/owner.png) is the figure reference; match it alongside the master when adding people.
- Machine-readable handoff: [style tokens](../design/within-reach/style-tokens.json) and [asset manifest](../design/within-reach/asset-manifest.json). Consult the manifest before regenerating an existing subject.
- Generation instructions: [image prompt template](templates/IMAGE-PROMPT.md).

**The colossus** (`explorations/style-frames/assets/colossus.png`, woodcut) and **Separate bodies** (`…/separate-bodies.png`, sculpture) remain archived alternatives. They are not secondary references for Within reach. Switching direction requires an explicit choice; never blend their hatchwork, sculptural finish or palettes into this kit by accident.

## Drawing grammar

| Feature | Keep fixed | May vary with the lesson |
| --- | --- | --- |
| Colour | Lemon stage `#ffdf08`; ultramarine `#1244bb` structural masses; near-black `#151819` ink/clothing; orange `#f47b0d` accent; ivory `#fff9d8` light paper. These are role anchors, not exact values of every textured pixel. | Which subject uses a role; accent area and placement. Colours must remain legible together. |
| Material | Dense tactile paper grain, compressed creases, scuffs and small ivory scratches in black areas. Broad coloured paper shapes retain texture throughout. Uneven, clipped or slightly torn edges; restrained edge thickness. | Local fold direction, scratch placement and grain. Do not repeat one stamped texture visibly. |
| Silhouette | Bold, angular, asymmetrical shapes readable at thumbnail size. Large uninterrupted masses with lively corners; irregularity feels deliberately cut. | Subject, clothing, pose, body type and identity. |
| Figure | Expressive editorial caricature: master has a small pointed profile, wedge nose/chin, swept black hair, broad shoulders, narrow waist, very long trouser legs, angular shoes and oversized articulated hands. Facial marks are sparse black cuts/lines; posture and hands carry intent. | New people need their own features, proportions and emotions within that angular grammar. Do not clone the same man into every lesson. Preserve useful hand anatomy and readable gestures. |
| Abstraction | Recognisable subjects simplified into paper planes. The master company is one stepped blue mass with an inset aperture, not detailed architecture. Notes are fictional orange symbols. | Companies, people, rights, objects and metaphors chosen for what their behaviour teaches. No requirement for a building, money bag or cash in every scene. |
| Space/light | Frontal editorial composition, generous lemon negative space, shallow overlaps and restrained contact shadows. The aperture is dark and recessed; paper has slight relief, not volumetric rendering. | Overlap, separation, scale and placement when they clarify a relationship. Perspective stays simple and coherent. |

Do not substitute smooth vector/SVG illustration, uniform rounded outlines, flat icon packs, glossy 3D clay, photoreal people, detailed miniature streets or decorative financial dashboards. Texture must support the silhouette rather than obscure it. Do not add scenic detail to make an otherwise unclear concept feel finished.

## Artwork and interface

Illustration dominates. System sans interface text stays quiet: 16px body, 13px supporting text, 23–34px responsive narrative (25px on phone) as the initial prototype baseline; exact anchors live in the token file. Keep controls below the scene and labels near the subject they explain. Build all new labels, amounts, dates, numbers and controls as accessible HTML/SVG text outside generated pixels. SVG may position and animate artwork; the drawing itself must retain the approved paper finish. The retained master includes “INC.”; that historical detail is not permission to generate new interface lettering.

Keep moving cash independent of baked decorative notes. The existing company's internal notes are part of its fixed illustration; `payment.png` is the one transferable payment. Future quantified scenes must distinguish symbolic texture from value-bearing objects and must not infer amounts from decorative note counts.

## Reproduction workflow

1. Start with matching transparent components from the manifest; reuse them if the required action permits. Inspect the master and relevant component visually before any generation.
2. For a new subject or pose, use image generation editing with **both actual reference images**: master for the full drawing language, closest approved component for local anatomy/material continuity. If references are unavailable, retrieve them before generating. Use the fixed style block plus a lesson-specific subject/action block from the template.
3. Produce one representative new asset. Place it beside existing subjects in the actual scene, at desktop and phone sizes, before generating a set. Critique the settled scene as well as motion; fix drift in this sample first.
4. For components, request real alpha transparency, full uncropped extremities and only shallow local paper shadows. Inspect alpha and composite over lemon and a contrasting background: checkerboard pixels, opaque rectangles and distracting halos fail. The current owner's soft edges are acceptable on the approved lemon scene; dark-background inspection is matte QA, not a request to revise this asset.
5. Save the accepted original, production copy, exact prompt and revisions, reference paths/hashes, exposed tool/model/version/settings, date and QA screenshots in the manifest or linked provenance record. Record unavailable metadata as unknown. Historical exact prompts/model identifiers have not been recovered; the new template is a reconstruction, not the original prompt.

Generative output is stochastic: the contract cannot guarantee pixel-identical fresh renders. Reusing approved pixels provides exact continuity; actual image references plus visual review control new asset consistency.

## Screenshot acceptance rubric

Review a screenshot of the actual scene beside the master; record pass/fail and the correction for each failure. Accept only after all pass:

- **Material:** paper grain and creases remain visible; edges feel cut; no smooth plastic, uniform vector finish or woodcut substitution.
- **Figure:** angular silhouette, expressive gesture and hands read at phone size; no cropped limbs, fused fingers or accidental change to an existing character.
- **Colour/space:** lemon, blue, ink, ivory and orange roles feel continuous; shallow overlaps remain readable without heavy cast shadows or a miniature world.
- **Meaning:** subject behaviour explains the lesson; future timing and value types are legible; ornamental counts cannot imply unsupported quantities.
- **Integration:** no matte rectangle or distracting halo, generated lettering or duplicate payment; UI stays readable and subordinate. Capture both the representative settled state and the important changed state.
