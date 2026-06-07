# Example Document
Your Name
2026-06-07

This page serves as a live demonstration of how to export individual
documents into multiple formats (PDF, Word, OpenDocument, EPUB, and
GitHub Flavored Markdown) directly from a single Quarto Markdown
(`.qmd`) source.

You can download any of the generated alternate formats using the
**Download** links shown at the top of the sidebar.

## Format Configuration

To generate these outputs, specify the desired formats in the document’s
YAML front matter:

``` yaml
format:
  html: {}
  typst:
    toc: true
    toc-depth: 2
    number-sections: true
    template: ../_extensions/typst-template.typ
    template-partials:
      - ../_extensions/typst-show.typ
  odt:
    toc: true
  epub:
    toc: true
  docx:
    toc: true
  gfm:
    toc: false
```

## Features Demonstrated

### 1. Callout Boxes

We include custom CSS/Typst styles for callouts. Here is an example:

> [!NOTE]
>
> This is a standard callout note. It renders with a clean left border
> and specific color matching the style theme.

### 2. Math & Code blocks

You can write code blocks and mathematical formulations:

$$E = mc^2$$

``` python
def hello_world():
    print("Hello from Quarto!")
```

### 3. Native Layouts

Table alignments and figure layout work flawlessly across HTML, Typst
(PDF), and EPUB formats.
