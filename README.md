# TextInputLineNumber

### Another Kivy Widget

This is an attempt (that actually is not that bad) of a TextInput that shows the line numbering

It handles:
- Word wrapping (there is no possibility of disabling the word-wrapping)
- Word breaking (when the word is so big that it needs to flow to the next line)

#### TODO

It doesn't handle well 4000+ lines. I think that this happens mainly because of the line numbering: the numbers are totally refreshed every new line, which is not very smart.