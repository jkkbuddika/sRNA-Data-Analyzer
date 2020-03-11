import os
import GeneralVariables

class CommonVariables:
    gv = GeneralVariables.GeneralVariables()

    ## General
    home_dir = os.path.dirname(os.getcwd())
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
    genome_url = genome_path + genome_file
    genome_dir_name = 'genome'
    genome_dir = home_dir + 'genome/'
    dm6_path = home_dir + 'genome/Drosophila_melanogaster/UCSC/dm6/'
    genome_fa = dm6_path + 'Sequence/WholeGenomeFasta/genome.fa'
    genes_gtf = dm6_path + 'Annotation/Genes/genes.gtf'
    bowtie2_index = genome_dir + 'Drosophila_melanogaster/UCSC/dm6/Sequence/Bowtie2Index/genome'
    bowtie_index = genome_dir + 'Drosophila_melanogaster/UCSC/dm6/Sequence/BowtieIndex/genome.fa'
    feature_file = os.path.basename(gv.feature)
    feature_path = os.path.dirname(gv.feature) + '/'
    feature_url = feature_path + feature_file
    feature_dir_name = 'genome_feature'
    feature_dir = home_dir + 'genome_feature/'

    ## Alignment Variables
    bt2_aligned = home_dir + 'bt2_aligned/'
    shortstack_aligned = home_dir + 'shortstack_aligned/'

    ## Sam Tools Sorting
    sam_sorted = home_dir + 'sam_sorted/'

    ## DeepTools BigWig Files
    bigwig_files = home_dir + 'bigwig_files/'

    ## FeatureCounts
    fc_output = home_dir + 'feature_counts'