# Mike Stephenson Design System — v0.1

**Status:** kickoff draft; awaiting local reference PDF audit  
**Project:** `mikestephenson.net`  
**Outputs:** Hugo + Tailwind/CSS website; Typst-generated resume PDF  
**Reference:** https://v4.brittanychiang.com/resume.pdf

## 1. Purpose
Create a coherent visual language for a personal technical journal covering engineering/software, photography, data analysis, health and fitness, veterinary interests, and other essays. The site should feel editorial and authored, not like a generic developer portfolio. The resume is one expression of the system, not the entire system.

## 2. Reference audit — pending

| Property | Finding | Evidence |
|---|---|---|
| Page size / page count | TBD | Pending PDF inspection |
| Margins / content bounds | TBD | Pending measurement |
| Main/sidebar ratio / gutter | TBD | Pending measurement |
| Font families and sizes | TBD | Pending PDF inspection |
| Primary and muted text colors | TBD | Pending PDF inspection |
| Accent color | TBD | Pending PDF inspection |
| Section spacing | TBD | Pending measurement |

## 3. Initial hypotheses (not yet measured)
1. Typography before decoration.
2. Asymmetric composition: primary narrative plus secondary information rail.
3. Whitespace can establish structure without unnecessary boxes or rules.
4. Metadata should support, not compete with, primary content.
5. Tight spacing within related groups; larger spacing between unrelated groups.
6. Use accent color to communicate hierarchy, not as decoration everywhere.
7. Different subjects may need different layouts while sharing one design language.
8. Avoid meaningless skill ratings and decorative charts without meaningful data.

## 4. Content areas
- Engineering and software
- Photography
- Data analysis and experiments
- Health, diet, and exercise
- Veterinary interests and animal health
- Other ideas and personal essays
- Projects, biography, and resume

Support long-form reading, code, equations, tables, charts, diagrams, and image-led stories.

## 5. Provisional token categories

### Color
`ink`, `ink-muted`, `accent`, `surface`, `surface-raised`, `rule`, `paper-grid-minor`, `paper-grid-major`

### Typography
`font-display`, `font-body`, `font-mono`, `text-name`, `text-section`, `text-subheading`, `text-body`, `text-small`, `text-caption`, `line-height-body`, `measure-reading`

### Spacing and layout
`space-1` through `space-6`, `space-section`, `gutter`, `page-margin`, `content-max`, `resume-main-column`, `resume-sidebar`, `article-measure`, `grid-gap`, `breakpoint-mobile`

Values will be chosen after the reference audit.

## 6. Component candidates
Site header/navigation; page introduction; section heading; category label; date/reading-time metadata; article header; prose; links; inline/code blocks; figure/image/caption; table; chart/diagram; callout/quotation; resume experience entry; project entry; skill list; footer.

## 7. Implementation strategy
- **Hugo:** content model, routing, taxonomies, templates, RSS, metadata.
- **Tailwind/CSS:** responsive web layout and reusable visual tokens.
- **Typst:** high-fidelity PDF resume.
- **Shared data:** consider structured shared resume data only after a first visual prototype proves it useful.
- **Version control:** track notes and decisions; leave reference material unchanged.

## 8. Open decisions
- Serif display face or all-sans?
- How prominent should the engineering-paper texture be?
- What accent color belongs to Mike's system?
- Should the resume be a restrained print adaptation of the site's identity?
- How should the layout adapt to mobile?
- Which decisions should be shared across web and PDF?

## 9. Next action
Add the PDF at `reference/brittany-chiang-resume.pdf`, run `tools/inspect_pdf.py`, and replace TBD values with measured findings. Keep measured facts separate from estimates and design decisions.
