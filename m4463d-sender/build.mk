ARDUINO_PATH := /opt/arduino-1.8.7
BUILD_PATH   := .build
SRC_PATH     := src
ENTRY_POINT  := $(SRC_PATH)/sketch.ino
IMAGE_FILE   := $(BUILD_PATH)/sketch.ino.hex
TERMINAL     := picocom

serial-port ?= /dev/ttyACM0
board-model ?= uno

ARDUINO_CMD := $(ARDUINO_PATH)/arduino --port $(serial-port) --board arduino:avr:$(board-model) --pref build.path=$(BUILD_PATH) --pref sketchbook.path=.  
AVRDUDE_CMD := avrdude -v -patmega2560 -cstk500v1 -P$(serial-port) -b19200 -Uflash:w:$(IMAGE_FILE):i -Ulock:w:0x0F:m

.DEFAULT_GOAL := compile

.PHONY: compile upload serial clean

build: compile

compile:
	$(ARDUINO_CMD) --verify $(ENTRY_POINT)

upload:
	$(ARDUINO_CMD) --upload $(ENTRY_POINT)

upload2:
	$(AVRDUDE_CMD)

serial:
	$(TERMINAL) $(serial-port)

clean:
	$(RM) -r $(BUILD_PATH)
