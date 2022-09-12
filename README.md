# Python-tools

## PDF converter
It’s notably challenging, as a result of the 2 file formats are immensely completely different in nature.

PDF uses a hard and fast document structure, wherever every character, line and image is positioned exploitation absolute coordinates on the page. every page is totally independent.Doc(x), on the opposite hand, could be a flowable document format, with no construct of pages or coordinates whatsoever. 

Content in paragraphs and tables flows mechanically to fill the obtainable space, or to flow around varied shapes. Positioning is not absolute, however relative to the margins or the previous paragraph.In other words, PDF solely is aware of concerning characters, curves and images. 

Docx deals with paragraphs, tables, lists, relative spacing and shapes.

Conversion from fixed page content to flowable text requires some sort of an intelligence. In its simplest form, characters are arranged into lines, then lines are arranged in paragraphs, and finally, spacing on top, bottom, left, right and first indentation are measured. In more complicated situations, columns of paragraphs and tables are discovered, and reading order is guessed. At least in theory, the layout in a PDF can be so complicated that it may be impossible to represent it in a Docx.

Some structures are ambiguous, or different than usual. For example, a children’s book has a totally different layout than a financial statement, which in turn is different than a resume or a scientific publication. A programming book uses vastly different formatting than a novel. The challenge is to teach the computer enough intelligence to discover the layout on its own. After all, we people have billions of neurons, and have spent over a decade in schools, learning this all day every day.

Other issues are related to how PDF has dual content internally. First, it has a display content, which involves curves and lines that only we humans can interpret. Short of an OCR software, computers cannot read, and generally have a really hard time interpreting the curves that look like text, especially in fancy fonts.

But PDF also has a secondary content, which is the computer’s own representation of the text, as you can copy it on the clipboard, and paste it in another document. Each character is supposed to be encoded as an integer number. There is supposed to be a mutual agreement between people and the computer, which is called an encoding. For example, 65 is the letter A, 66 is B, and so on. There are special symbols and ligatures to deal with. For example,
“fi” is often encoded as a single ligature character in the PDF, but it needs to come out as two individual characters, an “f” followed by an “i”.

Fonts are often protected by copyright. In a way PDF protects the font by mangling it so much that text is difficult or impossible to extract. It may display and print correctly, but the content may not be extractable without flaws.

Unfortunately, PDFs are often created badly, intentionally or accidentally. The encoding is sometimes damaged, and the extracted content may come out as meaningless garbage. It may look 100% perfect on the screen, but that’s just an illusion. If the content is a meaningless stream of random numbers, with no standard way of mapping each character code into a meaningful character, then content extraction is nearly impossible.

Sometimes only particular characters are damaged. For example, consider a bullet character, which obviously seems like a bullet to a human, but for the computer, it is just a weird unknown symbol. You may consider the first symbol character in a line to be a bullet, although that may as well be a guess. Analyzing the structure, the indentation, the spacing can make your decision stronger, but at the end of the day, the computer is still not as intelligent as a person.

Sometimes even we people have a hard time deciding where an advertisement begins, and where the text continues; what’s part of a chart, and what’s its caption, or where an individual table cell begins and ends. In Asian documents, where spaces are not used in between words, table cells can be significantly more compact than in Roman fonts, where small spaces are word delimiters, and big spaces are cell or column separators. Sometimes even people can’t tell, unless they can read the meaning behind it. For example, someone who has never studied any math would be unable to decode the meaning of a big equation.

This brings us to equations, which is even harder, because individual mathematical symbols are positioned absolutely in the PDF. If you want to convert it into an editable document that isn’t a JPEG image, then you have to understand the meaning behind the equations (for example, integral, summation, subscript, superscript).

There are two approaches to teach the computer, both require heaps of various different sample documents. The programmer can try to discover the rules, and tell the computer how paragraphs, tables and lists look in general. The other method involves artificial intelligence, where the computer itself learns from the humans. This usually involves manually marking up every paragraph, table cell, chart, illustration, and use machine learning. However, a totally new document layout that the computer has never seen will always cause problems. At some point the computer will get smart enough, but there’s always a situation where a human can beat it. For example, give the computer a 1000 year old document, and it will totally fail. Or teach the computer Latin text only, then give it a Chinese financial document, and it will struggle considerably.


## Paraphraser




## Image compressor



## 
