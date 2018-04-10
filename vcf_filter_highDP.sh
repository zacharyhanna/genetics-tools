#!/bin/bash
in_vcf=$1
maxDP=$2
awk '/^#/ {print $0; next}
    {for(i=1; i<=(split($8,zfd,";"));i++) if(split(zfd[i],numDP,"DP=")==2 && numDP[2]<$maxDP) {print}}' $in_vcf
