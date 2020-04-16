##
## Golang Project, 13/04/2020 by valentinmne
## Docker Container Written In Go
##      Makefile
##

CC =		python3
SRC =		pyipresolver.py
ARG2 =		/bin/bash
RM = 		rm -rf
FILE1 =		host_list
FILE2 = 	info


run:

	$(CC) $(SRC)

rm:

	$(RM) $(FILE1) $(FILE2)

re: rm run