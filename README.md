# WikiToPdf

WikiToPdf is a small tool that can help you export the content of the Azure DevOps Wiki into a single file in PDF or DOCX or any other format.

The basic idea behind this tool is to break the exporting operation into two steps.

1. Process the folder and file structure of the WIKI GIT repository and export its content into a single large markdown file.
2. Use a 3rd party converter to convert the resulting markdown file into either PDF or DOCX or anything as necessary.


## 1. Exporting a single markdown file




## 2. Conversion

I recommend to use `pandoc` as it supports lot of formats.



