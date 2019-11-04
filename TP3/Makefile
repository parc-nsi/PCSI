NAME    := $(shell basename $(CURDIR))

TARGET  := $(NAME)-handout.pdf
MAIN    := $(NAME).pdf
SOURCES := sujet/$(NAME)-sujet.pdf corrige/$(NAME)-corrige.pdf
SUBDIRS := $(foreach file, $(SOURCES), $(dir $(file)))

all: $(TARGET)

.INTERMEDIATE: $(MAIN)

$(MAIN): $(SOURCES)
	pdftk $^ cat output $@

%-handout.pdf: %.pdf
	pdfnup $< --quiet --landscape --outfile $@

clean:
	rm -f $(TARGET) $(SOURCES)

.PHONY: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -s -C $@

$(SOURCES): $(SUBDIRS)
	$(MAKE) -s -C $(shell dirname $@) $(shell basename $@)

