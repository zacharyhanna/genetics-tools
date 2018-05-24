import sys
import matplotlib
import matplotlib.pyplot as plt
from itertools import cycle

def grab_data(file_in):
    vals_sets = []
    scaf_indx = []
    indices = []
    pi_vals = []
    myIterator = cycle([1,2])
    with open(file_in, 'r') as infile:
        line_num = 0
        scaf_indx_val = 0
        for line in infile:
            line_num += 1
            line = line.strip()
            splitline = line.split()
            new_scaf = splitline[0]
            if line_num == 1:
                scaf_indx_val = myIterator.next()
                indices.append(int(splitline[1]))
                scaf_indx.append(scaf_indx_val)
                pi_vals.append(float(splitline[2]))
                old_scaf = new_scaf
            elif line_num > 1:
                if old_scaf == new_scaf:
                    scaf_indx.append(scaf_indx_val)
                    indices.append(int(splitline[1]))
                    pi_vals.append(float(splitline[2]))
                elif old_scaf != new_scaf:
                    vals_sets.append([indices,pi_vals,scaf_indx_val])
                    indices = []
                    pi_vals = []
                    indices.append(int(splitline[1]))
                    pi_vals.append(float(splitline[2]))
                    scaf_indx_val = myIterator.next()
                    scaf_indx.append(scaf_indx_val)
                    old_scaf = new_scaf
    return vals_sets

MarinDataTable = sys.argv[1]
Marin_vals = grab_data(MarinDataTable)

colors ={
"1": "#000000",
"2": "#0072b2"
}
#for kind in data_dict:

#plt.plot(Marin_vals[1], Marin_vals[2], c=colors[Marin_vals[0]])
for scafset in Marin_vals:
    plt.bar(scafset[0], scafset[1], width=1, color=colors[str(scafset[2])])
    #plt.bar(scafset[0], scafset[1], width=.8, linewidth=.1, color=colors[str(scafset[2])], edgecolor=colors[str(scafset[2])])
#plt.plot(Marin_vals[1], Marin_vals[2], c=colors[kind])
#plt.xlim(0,1)
#plt.ylim(0,7)
#plt.grid(linestyle='-')
#plt.ylabel("Effective Population Size ($\mathit{N_e}$)")
#plt.xlabel("Time (Generations)")
#plt.xscale('log')
#plt.yscale('log')

#line1 = matplotlib.lines.Line2D(color="blue",label='blue data')
#point1 = Line2D([0],[0],color="#000000",lw=4,label='Northern Spotted Owl (Marin County)')
#point2 = Line2D([0],[0],color="#d55e00",lw=4,label='Northern Spotted Owl (Humboldt County)')
#point3 = Line2D([0],[0],color="#cc79a7",lw=4,label='California Spotted Owl (Nevada County)')
#point4 = Line2D([0],[0],color="#2b9f78",lw=4,label='California Spotted Owl (San Diego County)')
#plt.legend(handles, labels)
#fig, ax = plt.subplots()
#plt.legend(handles=[point1,point2,point3,point4],framealpha=1)
locs, labels = plt.xticks()
locs2 = [indloc for indloc in locs if indloc >= 0]
locs2 = locs2[:-1]
print locs2
scaledVals = [indlocs2 * 100000 for indlocs2 in locs2]
scaledMb = [int(indVal / 1000000) for indVal in scaledVals]
plt.xticks(locs2, scaledMb)
plt.ylabel("Heterozygosity (per variant site)")
plt.xlabel("Genome position (Mb)")
plt.savefig(sys.argv[2], dpi=600, bbox_inches='tight')
#plt.show()
