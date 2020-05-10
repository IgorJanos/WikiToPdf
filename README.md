# WikiToPdf

WikiToPdf is a small tool that can help you export the content of the Azure DevOps Wiki into a single file in PDF or DOCX or any other format.

The basic idea behind this tool is to break the exporting operation into two steps.

1. Process the folder and file structure of the WIKI GIT repository and export its content into a single large markdown file.
2. Use a 3rd party converter to convert the resulting markdown file into either PDF or DOCX or anything as necessary.


## 1. Exporting a single markdown file

The `WikiToSingle.py` script operates on a locally cloned GIT repository of your wiki. 

You can use it like this:
```
python WikiToSingle.py -s D:\Work\Example.wiki -o D:\Work\Example.wiki\result.md
```


## 2. Conversion

I recommend to use `pandoc` as it supports a lot of formats.

You can download pandoc here - [Pandoc - Installing pandoc](https://pandoc.org/installing.html)

There is however a small problem with pandoc and it is related to images. DevOps Wiki stores images in the `/.attachments` folder and when referencing them, the leading slash `/.` is preserved. Pandoc does not like this, so you need to remove the leading slashes. 

Luckily pandoc supports Lua for input processing so I've included a `fixImages.lua` script in the repository that will help you do this.

```
function Image(el)
	return pandoc.Image(el.title, string.gsub(el.src, "^/", ""), "asd")
end
```

And then you call pandoc like this:
```
REM -----------------------------------
REM  Sample exporting script
REM -----------------------------------

set SRCFILE=%1
set DSTFILE=%~n1.docx

pandoc -s %SRCFILE% --lua-filter fixImages.lua -o %DSTFILE%
```


Igor
