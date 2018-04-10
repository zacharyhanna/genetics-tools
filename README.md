# genetics-tools
This is a repository for various tools for processing genetic and genomic data.  

## Contents
* [DP_means_std_dev_mod.sh](#dp\_means\_std\_dev\_modsh)  

### DP_means_std_dev_mod.sh
This is a modification of the DP_means_std_dev.sh script from SPOW-BDOW-introgression-scripts (Hanna et al. 2017).  

Usage example:  
```
$ ./DP_means_std_dev_mod.sh variants.vcf | head -1 >variants_dp_means_stdev.txt  
```
Example output:
```
$ cat variants_dp_means_stdev.txt
0.745503,0.913129 0.34499,0.599295 0.996806,1.05703
```
Each space-separated field in the output is "mean coverage,standard deviation".  

Script requirements:  
GNU Awk - we used GNU Awk version 4.0.1 (Free Software Foundation, 2012)  

Modifications  
1) Modified to accept vcf files with headers.  

#### Authorship
Code author: <a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em," alt="ORCID iD icon">Zachary R. Hanna</a>  
README.md author: Zachary R. Hanna  

#### All Versions

Please cite this repository as follows (you should also add which version you used):  

<a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Hanna ZR</a>. 2018. genetics-tools. *Zenodo*.

## References
<a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Hanna ZR</a>, Henderson JB, Wall JD. 2017. SPOW-BDOW-introgression-scripts. *Zenodo*. [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1065056.svg)](https://doi.org/10.5281/zenodo.1065056)  
  
Free Software Foundation. 2012. GNU Awk. Version 4.0.1. Available from: https://www.gnu.org/software/gawk/  
