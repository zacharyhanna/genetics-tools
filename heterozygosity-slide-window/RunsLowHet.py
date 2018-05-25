import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from textwrap import wrap

# python RunsLowHet.py het_value_file means_file decimal_percentage_mean_cutoff sample_name outfile_name
def grab_mean_het(mean_file, mean_percentage):
    mean_dict = {}
    with open(mean_file, 'r') as meanfile:
        for line in meanfile:
            line = line.strip()
            splitline = line.split()
            samp = str(splitline[0])
            samp_mean = float(splitline[1]) * mean_percentage
            mean_dict[samp] = samp_mean
    return mean_dict

def grab_data(het_file, het_cutoff):
    low_het_runs_ls = []
    with open(het_file, 'r') as infile:
        line_num = 0
        preceed_low_het = 0
        low_het_start = 0
        low_het_end = 0
        for line in infile:
            line_num += 1
            line = line.strip()
            splitline = line.split()
            new_scaf = str(splitline[0])
            window_start = int(splitline[1])
            window_end = int(splitline[2])
            het_val = float(splitline[3])
            if line_num == 1:
                if het_val < het_cutoff:
                    preceed_low_het = 1
                    low_het_start = window_start
                    low_het_end = window_end
            elif line_num > 1:
                if old_scaf == new_scaf:
                    if het_val < het_cutoff:
                        if preceed_low_het == 1:
                            low_het_end = window_end
                        elif preceed_low_het == 0:
                            low_het_start = window_start
                            low_het_end = window_end
                            preceed_low_het = 1
                    else:
                        if preceed_low_het == 1:
                            length_low_wind = low_het_end - low_het_start + 1
                            low_het_runs_ls.append(length_low_wind)
                            low_het_start = 0
                            low_het_end = 0
                        elif preceed_low_het == 0:
                            pass
                        preceed_low_het = 0
                elif old_scaf != new_scaf:
                    if preceed_low_het == 1: #take care of window from preceeding scaffold
                        length_low_wind = low_het_end - low_het_start + 1
                        low_het_runs_ls.append(length_low_wind)
                    elif preceed_low_het == 0:
                        pass
                    low_het_start = 0 # reset all values for this new scaffold
                    low_het_end = 0
                    preceed_low_het = 0
                    if het_val < het_cutoff:
                        if preceed_low_het == 1:
                            low_het_end = window_end
                        elif preceed_low_het == 0:
                            low_het_start = window_start
                            low_het_end = window_end
                            preceed_low_het = 1
                    else:
                        if preceed_low_het == 1:
                            length_low_wind = low_het_end - low_het_start + 1
                            low_het_runs_ls.append(length_low_wind)
                            low_het_start = 0
                            low_het_end = 0
                        elif preceed_low_het == 0:
                            pass
                        preceed_low_het = 0
            old_scaf = new_scaf
    return low_het_runs_ls

HetDataTable = sys.argv[1]
mean_file = sys.argv[2]
perc_mean_cutoff = float(sys.argv[3])
samp = sys.argv[4]
meanDict = grab_mean_het(mean_file, perc_mean_cutoff)
LowHetCutoff = meanDict[samp]
LowHetRuns = grab_data(HetDataTable, LowHetCutoff)
print LowHetRuns

pop_dict = {
"Sequoia":"Marin",
"ZRHG103":"Nevada",
"ZRHG104":"SanDiego",
"ZRHG125":"Humboldt"
}

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
percent_str = "{0:.2f}".format(perc_mean_cutoff)
title_string = "Histogram of window tracts with heterozygosity less than " + percent_str  + " of mean genome-wide heterozygosity for " + sample_pop + " population"
title_string2 = "\n".join(wrap(title_string, 60))
plt.title(title_string2)
plt.xlabel("Genome window tract length (Mb)")
plt.ylabel("Number of windows within each length bin")
ax.xaxis.set_major_formatter(myformatter)
plt.savefig(sys.argv[5], dpi=600, bbox_inches='tight')
#plt.show()
