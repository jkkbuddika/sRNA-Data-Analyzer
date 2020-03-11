class GeneralVariables:

    ## Name of the Biomart rRNA list in add_mat directory.
    rRNA_list = 'Dro_rRNA.txt'

    ## Bowtie2 General Parameters
    bowtie2_para = '--np 0 --n-ceil L,0,0.02 --rdg 0,6 --mp 6,2 --score-min L,0,-0.18'

    ## Link to the Biomart genome file of interest.
    genome = 'http://igenomes.illumina.com.s3-website-us-east-1.amazonaws.com/Drosophila_melanogaster/UCSC/dm6/Drosophila_melanogaster_UCSC_dm6.tar.gz'

    ## Link to the Biomart annotation file of interest.
    feature = 'ftp://ftp.flybase.net/genomes/Drosophila_melanogaster/dmel_r6.32_FB2020_01/gtf/dmel-all-r6.32.gtf.gz'

    ## Strandedness of the experiment: '0', '1' or '2'
    stranded = '0'

    ## Include a list of features to be quantified.
    diff_features = ['miRNA', 'gene', 'three_prime_utr', 'CDS', 'five_prime_utr']