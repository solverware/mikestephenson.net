# Mike Stephenson Design System

Goal: audit Brittany Chiang's resume PDF, then adapt its useful design principles into an original system for mikestephenson.net, Hugo/Tailwind, and Typst PDFs.

## First steps
1. Extract this folder to `C:\dev\mike-design-system` (or another stable working directory).
2. Put the PDF in `reference/brittany-chiang-resume.pdf`.
3. In the VS Code terminal, run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install pymupdf
py tools\inspect_pdf.py reference\brittany-chiang-resume.pdf
```

The script reports page geometry, fonts, text sizes, colors, and text bounding boxes. PDF measurements are evidence; visual interpretation still matters.

## Evidence labels
- **Measured:** extracted directly from the PDF/source.
- **Observed:** visually evident but not yet numerically measured.
- **Estimated:** approximate value.
- **Decision:** a choice for Mike's system, not a claim about the reference.

Keep the source PDF unchanged and record design decisions in `spec/design-spec-v0.1.md`.
