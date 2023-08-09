.DEFAULT_GOAL := all
.PHONY: all release clean

all:
	tailwindcss -i ./input.css -o ./static/style.css
