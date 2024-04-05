# pip install markdown-pdf

from markdown_pdf import MarkdownPdf

pdf = MarkdownPdf(toc_level=2)

from markdown_pdf import Section

pdf.add_section(Section("# Title\n", toc=False))
pdf.add_section(Section("""# Header 1\n\nbody\n## Header 2\n\n### Head 3\n\n
[![Hello](example.png)](https://github.com/agstephens/pystripes)

Python command line application to convert Markdown to PDF.
\n\n"""))
pdf.meta["title"] = "My Stripes"

pdf.save("example2.pdf")

