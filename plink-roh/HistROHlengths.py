import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
#import matplotlib.ticker as ticker
#from textwrap import wrap

# python HistROHlengths.py plink_file.hom outfile_name
def grab_lengths(file_in):
    length_dict = {}
    line_num = 0
    with open(file_in, 'r') as infile:
        for line in infile:
            line_num += 1
            if line_num != 1:
                line = line.strip()
                splitline = line.split()
                samp = str(splitline[0])
                roh_length = float(splitline[8]) * 1000 #plink file reports lengths in kilobases
                if samp not in length_dict:
                    length_dict[samp] = [roh_length]
                elif samp in length_dict:
                    length_dict[samp].append(roh_length)
    return length_dict

def make_LenBins(length_dict):
    #min 1 Mb, max 8906.136 Mb
    bin_dict = {}
    bin1 = range(1,10)
    bin2 = [z+.5 for z in range(1,9)]
    bin3 = bin1 + bin2
    bin3.sort()
    for val_idx, val in enumerate(bin3):
        scale_val = 1000000*val
        bin_dict[val]={}
        for samp in length_dict:
            bin_dict[val][samp]=[]
            for len_val in length_dict[samp]:
                try:
                    next_val = bin3[val_idx+1]
                    scale_next_val = 1000000*next_val
                    if scale_val <= len_val < scale_next_val:
                        bin_dict[val][samp].append(len_val)
                except IndexError: #this should only happen with the last bin
                    if scale_val <= len_val:
                        bin_dict[val][samp].append(len_val)
    percent_dict = make_percentage(bin_dict)
    samp_transformed = transform_dict(percent_dict, bin3)
    return samp_transformed, bin3

def make_percentage(bin_dict):
    perc_dict = {}
    length_genome = 1255541132.0
    for bin in bin_dict:
        perc_dict[bin] = {}
        for samp in bin_dict[bin]:
            perc_dict[bin][samp]=(float(sum(bin_dict[bin][samp]))/length_genome)*100
    return perc_dict

def transform_dict(bin_dict, bin_ls):
    samp_data_dict = {}
    for bin in bin_ls:
        for samp in bin_dict[bin]:
            if samp not in samp_data_dict:
                samp_data_dict[samp]=[]
                samp_data_dict[samp].append(bin_dict[bin][samp])
            elif samp in samp_data_dict:
                samp_data_dict[samp].append(bin_dict[bin][samp])
    return samp_data_dict



pop_dict = {
"Sequoia":"Marin",
"ZRHG103":"Nevada",
"ZRHG104":"SanDiego",
"ZRHG125":"Humboldt"
}

samp_dict = {
"Marin":"Sequoia",
"Nevada":"ZRHG103",
"SanDiego":"ZRHG104",
"Humboldt":"ZRHG125"
}

colors ={
"Humboldt": "#d55e00",
"Nevada": "#cc79a7",
"Marin": "#000000",
"SanDiego": "#2b9f78"}

PLINK_hom_file = sys.argv[1]
#output_file = sys.argv[2]

lengthsDict = grab_lengths(PLINK_hom_file)

percentDict, bin_ls = make_LenBins(lengthsDict)

print percentDict
samp_order = ["Marin","Humboldt","Nevada","SanDiego"]
offset_ls = [0.125*rn_ele for rn_ele in range(4)]
print offset_ls
bin_ls_array = np.array(bin_ls)
print bin_ls_array

fig, ax = plt.subplots()
for mysamp_idx, mysamp in enumerate(samp_order):
    plt.bar(bin_ls_array + offset_ls[mysamp_idx], percentDict[samp_dict[mysamp]], color=colors[mysamp], width=0.125)
plt.xticks(bin_ls_array)
ax.set_xticks(bin_ls_array - (.5*0.125))
# len(bin_ls_array) is 17
myxtick_names = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9]
ax.set_xticklabels(myxtick_names)
#plt.setp(ax.get_xticklabels()[::2], visible=False)
# legend plotting
point1 = Line2D([0],[0],color="#000000",lw=4,label='Northern Spotted Owl (Marin County)')
point2 = Line2D([0],[0],color="#d55e00",lw=4,label='Northern Spotted Owl (Humboldt County)')
point3 = Line2D([0],[0],color="#cc79a7",lw=4,label='California Spotted Owl (Nevada County)')
point4 = Line2D([0],[0],color="#2b9f78",lw=4,label='California Spotted Owl (San Diego County)')
plt.legend(handles=[point1,point2,point3,point4],framealpha=1)
title_string = "Histogram of runs of homozygosity (ROH)"
#plt.title(title_string)
plt.xlabel("ROH tract length bins (Mb)")
plt.ylabel("Proportion of reference genome (%)")
plt.savefig(sys.argv[2], dpi=600, bbox_inches='tight')
plt.show()
'''
sample_pop = pop_dict[samp]

def update_xlabels(ax):
    myxlabels = [format(mylabel, ',.0f') for mylabel in ax.get_xticks()]
    ax.set_xticklabels(myxlabels)

#def divide_xlabels(ax):
#    scale_x = 1e6
#    ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
#    ax.xaxis.set_major_formatter(ticks_x)

def megabases(x, pos):
    #The two args are the value and tick position
    return '%1.1f' % (x*1e-6)

myformatter = ticker.FuncFormatter(megabases)

fig, ax = plt.subplots()
bin1 = range(1,8)
bin2 = [z+.5 for z in range(1,8)]
bin3 = bin1 + bin2
bin3.sort()
bins = [y*1e6 for y in bin3]
plt.hist(LowHetRuns,bins)
#percent_str = "{0:.2f}".format(perc_mean_cutoff)
ax.xaxis.set_major_formatter(myformatter)
plt.savefig(sys.argv[5], dpi=600, bbox_inches='tight')
#plt.show()
'''
