CFLAGS = -Wall -O2 -fstack-protector-all -D_FORTIFY_SOURCE=2 -std=c99


prefix = /usr/local
bindir = $(prefix)/bin

binaries = door_manager open_door close_door


all: door_manager

install: all
	install $(binaries) $(bindir)/

.PHONY: clean
clean:
	 rm -f door_manager
