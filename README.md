![Version](https://img.shields.io/static/v1?label=modular-annotated-bibliography-bibtex-org-mode&message=0.2&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# Template for making an enhanced annotated and illustrated bibliography with BibTeX in LaTeX

## An annotated bibliography for the 21st Century
An annotated bibliography summarizes notes about papers being read during a research project.
It is one of several methods for working with the knowledge gleaned from reading.
The classic annotated bibliography limits the annotation to one paragraph.

In contrast, our modern approach makes the annotation as long and detailed as needed for self-study.
It is also not limited to prose. 
It can include graphical objects of various types to accelerate recall of the paper's content.

![Screenshot 2024-10-24 at 1 40 36 PM](https://github.com/user-attachments/assets/edfd7bd6-85db-40e9-9ad0-53ceb1dc3173)



This modular approach enables the reuse of annotations in the modular annotated bibliographies of related projects.
It has the following enhanced features that the classic annotated bibliography lacks:

- No longer restrained by the `annote` field in the BibTeX entry.
- Modular annotation for easy reuse in related projects.
- Images
- Tables
- Equations
- Code blocks
- Hyperlinks: internal and external
- Bibliographic entries can be reordered for subgrouping by category. 
- Table of contents, hyperlinked to sections
- Index of terms
- Bibliography includes papers cited outside of those listed in the annotated bibliography.
- List of acronyms used
- List of glossary terms used
- List of mathematical notation

![Screenshot 2024-10-24 at 1 41 09 PM](https://github.com/user-attachments/assets/c1fa04fa-7e62-407a-85f3-628f22defc06)


## Why LaTeX

It is the gold standard for typesetting scientific documents.
This template can be used on Overleaf.
It can also be used collaboratively online in Overleaf.


## PDF of Annotated Bibliography
When exported to a PDF, the org file reads the BibTeX file with formatting set by the *apacannx.bst* file. 
The top of the output PDF looks like the following:


## One-time directory creation

The modular bibliographic notes are stored in folders at the top level in the home directory.
The global.bib file is stored in `~/Documents`.
Adjust the location and copy the examples to these folders.

```bash
mkdir ~/glossaries
mkdir ~/bibNotes
mkdir ~/imagesBlaine # Rename
````

## Bash Function to generate subfolder with required files

Edit the file paths as needed.
Replace `~/6112MooersLabGitHubLabRepos` with the path to wherever you downloaded the file.
Takes a project ID as the only argument.

Run from the top level of your writing project directory.

```bash
function maborg {
echo "Create a modular annotated bibliography (mab) subfolder and populate with required files with project number in the title."
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: not enough arguments"
  echo "Usage1: maborg projectIndexNumber"
  return 2
elif [ $# -gt 1 ]; then
  echo 1>&2 "$0: too many projectIndexNumber"
  echo "Usage1: maborg projectIndexNumber"
  return 2
fi
projectID="$1"
mkdir mab$1
cp ~/6112MooersLabGitHubLabRepos/modular-annotated-bibliography-bibtex-org-mode/mabib0573.org ./mab$1/.
cp ~/6112MooersLabGitHubLabRepos/modular-annotated-bibliography-bibtex-org-mode/apacannx.bst ./mab$1/.
cp ~/6112MooersLabGitHubLabRepos/modular-annotated-bibliography-bibtex-org-mode/compile.sh ./mab$1/.
}
```


## Installation

1. git clone this project to your software directory
2. Copy one of the bash function and paste into your .bashr or .zshrc file.
3. source .bashrc
4. cd project directory
3. maborg <projectID> to create subfolder 


## Usage

1. Create one tex file per reference in the `~/bibNotes folder`. Use the supplies examples as templates. Use the cite key from BibTeX as the name of the bibNote file. Use a blank line between paragraphs. Note that text-wrapping figures is more straightforward than text-wrapping tables. Skip text-wrapping if it is too tedious at this time. Add figures, tables, equations, URLs, citekeys, index macros, acronyms, glossary terms, and math notation as you work.
2. Use the citekey as the argument of the `\bibentry` macro inside a new subsection heading. This will inject the bibliography entry upon export to PDF.
3. You can cluster citations by topic and subtopic. You can lower the heading level to a subsubsection for the bibliographic entry.
4. Compile to HTML to enjoy in a web browser. Compile to PDF to edit while traveling or away from the computer.
5. Compiles with *texlive*; no extra packages required.


## Coming soon

- Variant for biblatex.

## Sources of funding

- NIH: R01 CA242845
- NIH: R01 AI088011
- NIH: P30 CA225520 (PI: R. Mannel)
- NIH: P20 GM103640 and P30 GM145423 (PI: A. West)

## Update history

| Version           |  Changes                                                                                                            | Date                      |
|:------------------|:--------------------------------------------------------------------------------------------------------------------|:--------------------------| 
| 0.1               | Initial commit.                                                                                                     | 2024  October 24          |
| 0.2               | Customized the bash script to work in the org files.                                                                | 2024  December 11         |


# modular-annotated-bibliography-bibtex-org-mode
