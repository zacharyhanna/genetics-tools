# genetics-tools
This is a repository for various tools for processing genetic and genomic data.  

## Contents
* [DP_sample_calc.sh](#dp\_sample\_calcsh)  
* [vcf_filter_highDP.sh](#vcf\_filter\_highdpsh)  

### DP_sample_calc.sh
This is a modification of the DP_means_std_dev.sh script from SPOW-BDOW-introgression-scripts version 1.1.1 (Hanna et al. 2017).  

Usage example:  
```
$ ./DP_sample_calc.sh variants.vcf | head -1 >variants_dp_means_stdev.txt  
```
Example output:
```
$ cat variants_dp_means_stdev.txt
0.745503,0.913129 0.34499,0.599295 0.996806,1.05703
```
Each space-separated field in the output is "mean coverage,standard deviation".  

Script requirements:  
GNU Awk - we used GNU Awk version 4.2.0 (Free Software Foundation, 2017)  

### vcf_filter_highDP.sh
The purpose of this script is to exclude variant sites with coverage greater than a user-specified value. It is a modification of the vcf_dp_filter.sh script from SPOW-BDOW-introgression-scripts version 1.1.1 (Hanna et al. 2017).  
  
Usage example:  
```
$ ./vcf_filter_highDP.sh variants.vcf 1000 >variants_filtered.vcf 
```
The above example would only keep variants with less than 1,000 DP coverage. The DP referenced here is the unfiltered depth across all samples at a site (see [GATK documentation](https://software.broadinstitute.org/gatk/documentation/tooldocs/3.8-0/org_broadinstitute_gatk_tools_walkers_annotator_Coverage.php) for further details). VCF headers are OK and will remain in the output file.  
  
Script requirements:  
GNU Awk - we used GNU Awk version 4.2.0 (Free Software Foundation, 2017)  

#### Authorship
Code author: <a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em," alt="ORCID iD icon">Zachary R. Hanna</a>  
README.md author: Zachary R. Hanna  

#### All Versions

Please cite this repository as follows (you should also add which version you used):  

<a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Hanna ZR</a>. 2018. genetics-tools. *Zenodo*. [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1215826.svg)](https://doi.org/10.5281/zenodo.1215826)  

## References
Hanna ZR, Henderson JB, Wall JD. 2017. SPOW-BDOW-introgression-scripts. Version 1.1.1. *Zenodo*. [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1065056.svg)](https://doi.org/10.5281/zenodo.1065056)  
  
Free Software Foundation 2017. GNU Awk . Version 4.2.0. [Accessed 2018 Mar 15]. Available from: https://www.gnu.org/software/gawk.  
