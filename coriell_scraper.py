from lxml import html
import requests
import sys
# coriell_scraper.py takes a list of Coriell Cell Repository samples and retrieves
# age, gender, cell_subtype, transform_type, cell_type, and ethnicity for each
# and then outputs them into a tab-delimited table whose name one specifies as
# the second argument
# Example :
# python coriell_scraper.py sample_file output_file
# written for use with python 3

def get_gender(tree):
    gender = tree.xpath('//span[@id="lblGender"]/text()')
    return gender[0]

def get_age(tree):
    age_ls = tree.xpath('//div[@id="Age"]/div[2]/h4/text()')
    age = age_ls[0]
    age = age.strip()
    return age

def get_ethnicity(tree):
    ethnicity = tree.xpath('//span[@id="lblEthnicity"]/text()')
    return ethnicity[0]

def get_cell_type(tree):
    cell_type = tree.xpath('//span[@id="lblCell_Type"]/text()')
    return cell_type[0]

def get_cell_subtype(tree):
    cell_subtype = tree.xpath('//span[@id="lblCell_Subtype"]/text()')
    return cell_subtype[0]

def get_transform_type(tree):
    transform_type = tree.xpath('//span[@id="lblTransform_Type"]/text()')
    return transform_type[0]

def get_data_str(tree):
    age = get_age(tree)
    gender = get_gender(tree)
    ethnicity = get_ethnicity(tree)
    cell_type = get_cell_type(tree)
    cell_subtype = get_cell_subtype(tree)
    transform_type = get_transform_type(tree)
    data_ls = [age, gender, cell_subtype, transform_type, cell_type, ethnicity]
    return "\t".join(data_ls)

def get_sample_list(file_in):
    with open(file_in, 'r') as infile:
        sample_ls = []
        for line in infile:
            splitline = line.strip().split()
            sample = splitline[0] #the samples are in the first column of my input
            # file, but this might need to be altered for use with other files
            sample_ls.append(sample)
    return sample_ls

def write_out_data(file_out, data_ls):
    with open(file_out, 'w') as outfile:
        for item in data_ls:
            outfile.write(item)
            outfile.write("\n")

def get_sample_data(sample_ls):
    data_ls = []
    ls_header = ["sample", "age", "gender", "cell_subtype", "transform_type", "cell_type", "ethnicity"]
    data_ls.append("\t".join(ls_header)) # append header line
    for sample in sample_ls:
        page_addr = 'https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=' + sample + '&PgId=166'
        page = requests.get(page_addr)
        tree = html.fromstring(page.content)
        data_str = get_data_str(tree)
        new_data_str = sample + "\t" + data_str
        data_ls.append(new_data_str)
    return data_ls

def scrape_data(sample_file):
    sample_ls = get_sample_list(sample_file)
    data_ls = get_sample_data(sample_ls)
    write_out_data(sys.argv[2], data_ls)

scrape_data(sys.argv[1])
