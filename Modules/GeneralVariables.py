class GeneralVariables:

    ## Name of the Biomart rRNA list in add_mat directory
    rRNA_list = 'Dro_rRNA.txt'

    ## Link to the Biomart genome file of interest
    genome = 'ftp://ftp.ensembl.org/pub/release-99/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.28.dna_sm.toplevel.fa.gz'

    ## Link to the annotation file of interest (i.e., FlyBase annotation from FTP site)
    feature = 'ftp://ftp.flybase.net/genomes/Drosophila_melanogaster/dmel_r6.32_FB2020_01/gtf/dmel-all-r6.32.gtf.gz'

    ## Bowtie2 General Parameters
    bowtie2_para = '--np 0 --n-ceil L,0,0.02 --rdg 0,6 --mp 6,2 --score-min L,0,-0.18'

    ## Strandedness of the experiment: '0', '1' or '2'
    stranded = '0'

    ## Include a list of features to be quantified
    diff_features = ['miRNA']