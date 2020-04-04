TARGET = sip.so
OFILES = siplib.o apiversions.o descriptors.o qtlib.o threads.o objmap.o voidptr.o array.o int_convertors.o bool.o
HFILES = sip.h sipint.h array.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -I. -I/usr/include/python3.7m
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS = -shared -Wl,--version-script=sip.exp
LIBS = 
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	@echo '{ global: PyInit_sip; local: *; };' > sip.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages || mkdir -p $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages
	cp -f $(TARGET) $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages/$(TARGET)
	strip $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages/$(TARGET)
	@test -d $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages || mkdir -p $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages
	cp -f /home/arnaud/tmp/sip-4.19.22/sip.pyi $(DESTDIR)/home/arnaud/.virtualenv/test3.7/lib/python3.7/site-packages/sip.pyi

clean:
	-rm -f $(TARGET)
	-rm -f siplib.o
	-rm -f apiversions.o
	-rm -f descriptors.o
	-rm -f qtlib.o
	-rm -f threads.o
	-rm -f objmap.o
	-rm -f voidptr.o
	-rm -f array.o
	-rm -f int_convertors.o
	-rm -f bool.o
	-rm -f sip.exp
