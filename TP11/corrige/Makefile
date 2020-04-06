FILE=$(wildcard *.py)
TARGET=$(FILE:.py=.pdf) $(FILE:.py=.html)

all: $(TARGET)

%.pdf: %.md
	pandoc $< -V geometry:margin=1.1cm --highlight-style=monochrome -o $@

%.html: %.md
	pandoc -s  -V geometry:margin=1.5cm --mathjax -t slidy $< -o $@

# Commentaires spéciaux : """! ... !"""
%.md: %.py
	echo "~~~python" > $@
	awk '/^"""!$$/{sub(/^"""!/,"~~~\n")}/^!"""$$/{sub(/^!"""/,"\n~~~python")}{print}' $< >> $@
	echo "~~~" >> $@

