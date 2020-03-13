import os
import GeneralVariables

class CommonVariables:
    gv = GeneralVariables.GeneralVariables()

    ## General
    home_dir = os.path.dirname(os.getcwd()) + '/'
    raw_sequences_dir = home_dir + 'raw_sequences/'
    add_mat = home_dir + 'add_mat/'
    Threads = '8'
    extensions = ['.fastq', '.sam', '.csv', '.txt', '.bam', '.bw']
    summary_dir = home_dir + 'summary_files/'

    ## TagDust Variables
    tagdust_singu = add_mat + 'gostripes.simg'
    tagdust_out = home_dir + 'tagdust_out/'
    rRNA_path = add_mat + gv.rRNA_list

    ## Cutadapt Variables
    cutadapt_dir = home_dir + 'cutadapt/'

    ## Variables for FastQC
    file_type = ['*.fastq', '*.bam']
    fastqc_raw = 'fastqc_raw'
    fastqc_bam = 'fastqc_mapped'

    ## Genome sequences, annotations and Bowtie Indices
    genome_file = os.path.basename(gv.genome)
    genome_path = os.path.dirname(gv.genome) + '/'
    genome_dir_name = 'genome'
    genome_dir = home_dir + 'genome/'
    genome_fa = genome_dir + os.path.splitext(genome_file)[0]
    feature_file = os.path.basename(gv.feature)
    feature_path = os.path.dirname(gv.feature) + '/'
    feature_dir_name = 'genome_feature'
    feature_dir = home_dir + 'genome_feature/'
    genes_gtf = feature_dir + os.path.splitext(feature_file)[0]

    ## Alignment Variables
    bt2_index = home_dir + 'bt2_index/'
    bt2_aligned = home_dir + 'bt2_aligned/'
    shortstack_aligned = home_dir + 'shortstack_aligned/'

    ## Sam Tools Sorting
    sam_sorted = home_dir + 'sam_sorted/'

    ## FeatureCounts
    fc_output = home_dir + 'feature_counts'