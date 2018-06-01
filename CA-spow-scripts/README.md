# CA-spow-scripts
Directory for scripts related to analysis of genomes from California populations of spotted owls.  

## Introduction
For scripts that take a variant call format (VCF) file as input, we created our VCF file using the Genome Analysis Toolkit (GATK) version 3.8.0 (DePristo et al. 2011; McKenna et al. 2010; van der Auwera et al. 2013) HaplotypeCaller tool. We designed some of these scripts for our specific sample set and analyses, so you made need to modify the code for them to be useful in analyzing your own data. Our main purpose in providing these scripts is for documentation of our analysis methodology.  

## vcf_dp_filter_1898.sh
The purpose of this script is to exclude variant sites with excessive coverage. We excluded sites with coverage greater than the mean + 5σ (in our data set this meant keeping sites with coverage less than 1,898X).  

Usage example:  
```
$ ./vcf_dp_filter_1898.sh variants.vcf >variants_filt.vcf
```
Script requirements:  
GNU Awk (GAWK) - we used GAWK version 4.2.0 (Free Software Foundation, 2017)  

## HistROHlengths.py
The purpose of this script was to produce a histogram of the lengths of runs of homozygosity (ROH) output from a PLINK version 1.9 (Chang et al. 2015; Purcell & Chang 2018) analyses of ROH.  

## Citing the repository
### Authorship
Code author: <a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Zachary R. Hanna</a>  
README.md author: Zachary R. Hanna  

Please refer to the genetics-tools repository README.md for citation details:  

## References
Chang CC., Chow CC., Tellier LC., Vattikuti S., Purcell SM., Lee JJ. 2015. Second-generation PLINK: rising to the challenge of larger and richer datasets. GigaScience 4:7. DOI: 10.1186/s13742-015-0047-8.  

DePristo MA., Banks E., Poplin R., Garimella KV., Maguire JR., Hartl C., Philippakis AA., del Angel G., Rivas MA., Hanna M., McKenna A., Fennell TJ., Kernytsky AM., Sivachenko AY., Cibulskis K., Gabriel SB., Altshuler D., Daly MJ. 2011. A framework for variation discovery and genotyping using next-generation DNA sequencing data. *Nature Genetics* 43:491–498. DOI: 10.1038/ng.806.  

Free Software Foundation 2017. GNU Awk . Version 4.2.0. [Accessed 2018 Mar 15]. Available from: https://www.gnu.org/software/gawk.  

McKenna A., Hanna M., Banks E., Sivachenko A., Cibulskis K., Kernytsky A., Garimella K., Altshuler D., Gabriel S., Daly M., DePristo MA. 2010. The Genome Analysis Toolkit: A MapReduce framework for analyzing next-generation DNA sequencing data. *Genome Research* 20:1297–1303. DOI: 10.1101/gr.107524.110.  

Purcell SM., Chang CC. 2018. PLINK. Version 1.90b5.4. [Accessed 2018 Apr 12]. Available from: https://www.cog-genomics.org/plink/1.9.  

van der Auwera GA., Carneiro MO., Hartl C., Poplin R., del Angel G., Levy-Moonshine A., Jordan T., Shakir K., Roazen D., Thibault J., Banks E., Garimella KV., Altshuler D., Gabriel S., DePristo MA. 2013. From FastQ data to high confidence variant calls: the Genome Analysis Toolkit best practices pipeline. *Current Protocols in Bioinformatics* 11:11.10.1-11.10.33. DOI: 10.1002/0471250953.bi1110s43.  
