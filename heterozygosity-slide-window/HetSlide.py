import sys
import pysam
# calculates overlapping or non-overlapping windows depending on the provided slide size
# python HetSlide.py scaffolds_lengths_file min_length_scaffold window_size slide_size vcf_file output_file_base
def window_slicer(scaf_leng, wind_size, slide_size):
    window_coords = []
    scaf_pos = 1
    while scaf_pos < scaf_leng:
        start_pos = scaf_pos
        end_pos = scaf_pos + wind_size - 1
        if end_pos > scaf_leng:
            return window_coords
        else:
            window_coords.append([start_pos, end_pos])
            scaf_pos = start_pos + slide_size #for non-overlapping windows, slide_size = window_size

def window_creator(scafs_lengths_file, min_length, wind_size, slide_size):
    #scafs_lengths_file format
    #C7929205        1000
    #C7929245        1000
    with open(scafs_lengths_file, 'r') as scafs_lengs:
        kept_scafs = []
        wind_dict = {}
        for line in scafs_lengs:
            splitline = line.strip().split()
            scaf = str(splitline[0])
            length = int(splitline[1])
            if length >= min_length:
                kept_scafs.append(scaf)
                scaf_winds = window_slicer(length, wind_size, slide_size)
                wind_dict[scaf]=scaf_winds
    return kept_scafs, wind_dict

#def figure_num_sites(wind_dict, masked_bed):

kept_scafs_ls, dict_scaf_winds = window_creator(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

hets_dict = {}
vcf_in = pysam.VariantFile(sys.argv[5])  # auto-detect input format based on extension (vcf or bcf)
samp_ls = list((vcf_in.header.samples))
for scaffold in kept_scafs_ls:
    hets_dict[scaffold] = []
    ls_winds = dict_scaf_winds[scaffold]
    for window in ls_winds:
        calls = [0]*len(samp_ls)
        hets = [0]*len(samp_ls)
        for rec in vcf_in.fetch(scaffold, window[0], window[1]):
            splitrec = str(rec).strip().split()
            for i in range(0,len(samp_ls)):
                GT = splitrec[i+9]
                if GT[:1] != '.':
                    calls[i] += 1.0
                if GT[:3] == '0/1':
                    hets[i] += 1
        wind_het_ls = [0]*len(samp_ls)
        for indx, ind_call in enumerate(calls):
            if ind_call == 0:
                wind_het_ls[indx] = 0.0
            elif ind_call != 0:
                wind_het_ls[indx] = hets[indx]/ind_call
        hets_dict[scaffold].append(wind_het_ls)
#print hets_dict

def write_results(file_out, kept_scafs_ls, hets_dict, samp_ls):
    for sampIdx, samp in enumerate(samp_ls):
        full_out_file = file_out + "_" + samp
        with open(full_out_file, 'w') as outfile:
            for scaffold in kept_scafs_ls:
                ls_het_scores = hets_dict[scaffold]
                for HetIdx, het_score in enumerate(ls_het_scores):
                    samp_het_val = str(het_score[sampIdx])
                    line_out = scaffold + "\t" + samp_het_val + "\n"
                    outfile.write(line_out)

write_results(sys.argv[6], kept_scafs_ls, hets_dict, samp_ls)
