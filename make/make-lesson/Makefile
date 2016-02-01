include config.mk

TXT_FILES=$(wildcard books/*.txt)
DAT_FILES=$(patsubst books/%.txt, %.dat, $(TXT_FILES))
PNG_FILES=$(patsubst %.dat, %.png, $(DAT_FILES)) 

.PHONY : variables
variables:
	@echo TXT_FILES: $(TXT_FILES)
	@echo DAT_FILES: $(DAT_FILES)
	@echo PNG_FILES: $(PNG_FILES)

# Generate archive files
analysis.tar.gz : $(DAT_FILES) $(PNG_FILES) $(COUNT_SRC) $(PLOT_SRC)
	tar -czf $@ $^ $(PNG_FILES)

# Count words
.PHONY : dats
dats : $(DAT_FILES)

%.dat: $(TXT_FILES) $(COUNT_SRC)
	$(COUNT_EXE) $< $*.dat

# Plot

.PHONY : plots
plots : $(PNG_FILES)

%.png: $(DAT_FILES) $(TXT_FILES) $(COUNT_SRC) $(PLOT_SRC)
	$(PLOT_EXE) $< $*.png


.PHONY : clean
clean:
	rm -f $(DAT_FILES) $(PNG_FILES) analysis.tar.gz
