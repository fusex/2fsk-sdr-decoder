#!/bin/bash - 
#===============================================================================
#
#          FILE:  all.sh
# 
#         USAGE:  ./all.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Zakaria ElQotbi (zakaria), zakaria@ghs.com
#       COMPANY:  Green Hills Software
#       VERSION:  1.0
#       CREATED:  26/12/2018 00:24:29 CET
#      REVISION:  ---
#===============================================================================

#device="driver=rtlsdr"
Device="driver=hackrf"

SFreq=1.2M
Freq=433.99M
BASE=F${Freq}-S${SFreq}

workdir=/home/zakaria/manip/2fsk/
cd $workdir

id=$(ls -1v ${BASE}-record* 2>/dev/null| tail -1 | sed 's/.*record\([0-9]*\)/\1/')
[ -z "$id" ] && id=1 || id=$((id+1))

record=${BASE}-record${id}
demod=${BASE}-demod${id}
decod=${BASE}-decod${id}

echo "###################################################"
echo "1. Recording into $record :"
echo "###################################################"
rx_sdr -f ${Freq} -F CF32 -d ${Device} -s ${SFreq} $record 

echo
echo "###################################################"
echo "2. Demoding into $demod:"
echo "###################################################"

/home/zakaria/workspace/fusex/radio/spino/gnuradio/decode2FSK.py  --fileIN=$record --fileOUT=$demod

echo
echo "###################################################"
echo "3. Decoding into $decod:"
echo "###################################################"
/home/zakaria/manip/2fsk/scripts/convert.rb $demod $decod
