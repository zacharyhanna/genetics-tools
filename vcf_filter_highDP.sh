#!/bin/bash
## Usage:
## ./vcf_filter_highDP.sh variants.vcf maximum_depth
in_vcf=$1
maximumDP=$2
awk -v maxDP=$maximumDP '/^#/ {print $0; next}
    {for(i=1; i<=(split($8,zfd,";"));i++) if(split(zfd[i],numDP,"DP=")==2 && numDP[2]<maxDP) {print}}' $in_vcf
