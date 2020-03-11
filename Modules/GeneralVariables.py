class GeneralVariables:

    ## Name of the Biomart rRNA list in add_mat directory.
    rRNA_list = 'Dro_rRNA.txt'

    ## Bowtie2 General Parameters
    bowtie2_para = '--np 0 --n-ceil L,0,0.02 --rdg 0,6 --mp 6,2 --score-min L,0,-0.18'

    ## Strandedness of the experiment: '0', '1' or '2'
    stranded = '0'

    ## Include a list of features to be quantified.
    diff_features = ['miRNA']