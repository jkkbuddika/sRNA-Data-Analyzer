# Small RNA (sRNA) Data Analyzer

This repository contain a series of python based modules to automate sequencing data generated from small RNA (*i.e.*, miRNA, siRNA, piRNA, *etc*.) libraries. I ***highly recommend*** reading through this step-by-step manual *carefully* before you start analyzing your data. If you are interested in a protocol for sRNA library preparation I recommend looking at the [Sokol lab](http://sokollab.mystrikingly.com/) sRNA library preparation protocol given [here](http://sokollab.mystrikingly.com/).

## Requirements
The sRNA-seq data analyzer requires following tools to be installed for data analysis.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) : Quality assessment
- [Cutadapt](https://cutadapt.readthedocs.io/en/stable/) : Adaptor trimming
- [TagDust2](http://tagdust.sourceforge.net/) : Remove rRNA reads
- [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml) : Mapping reads to a given genome
- [QualiMap](http://qualimap.bioinfo.cipf.es/) : Mapping quality assessment
- [SAMtools](https://github.com/samtools/samtools) : Sorting and indexing of mapped reads
- [deepTools](https://github.com/deeptools/deepTools/) : Generate bigwig files for IGV visualization
- [Subread](http://subread.sourceforge.net/) : Count features
- [MultiQC](https://github.com/ewels/MultiQC) : Summarize logs
- [ShortStack](https://github.com/MikeAxtell/ShortStack) : Predict/identify small RNAs

We thank developers of these valueble tools!

## Getting started
Start data analysis with setting up a conda environment with all the above tools installed, as it gives you the opportunity to use most updated versions. To set up the conda environment (i.e., dataanalyzer):
```
conda create -n dataanalyzer -c conda-forge -c bioconda python=3.7
conda install -n dataanalyzer -c conda-forge -c bioconda fastqc cutadapt bowtie2 qualimap shortstack samtools deeptools subread multiqc pandas
```
To update your conda environment:
```
conda update -n dataanalyzer -c conda-forge -c bioconda --all
```
To activate the enironment:
```
source activate dataanalyzer
```
To deactivate the environment:
```
source deactivate
```
For more details on managing conda enviroments [click here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

## User guide
### Step 1: Cloning the repository
To clone the current repository on to your local repository using terminal/commandline, first navigate to the home directory (i.e., where you want analyzed data to be deposited), paste and enter the following command:
```
git clone https://github.com/jkkbuddika/sRNA-Data-Analyzer.git
```
Once cloning is completed:
```
mkdir scripts
mv sRNA-Data-Analyzer/Modules/*.py scripts/
rm -rf sRNA-Data-Analyzer
ls
```
> scripts   

At this point, your home directory will have a directory named *scripts* with all individual modules of the python analysis pipeline.
### Step 2: Download additional materials
This data analysis pipeline integrates [TagDust2](http://tagdust.sourceforge.net/) to remove rRNAs, the major form of RNA contaminant during early steps of analysis. You can directly [download](https://sourceforge.net/projects/tagdust/) and [install](http://tagdust.sourceforge.net/#install) TagDust2 on to your local environment and include the path to executables into your PATH environment. Alternatively in this manual, we will download the singularity image from [GoSTRIPES](https://github.com/BrendelGroup/GoSTRIPES) workflow to use TagDust2. For this:
```
mkdir add_mat
cd add_mat
singularity pull --name gostripes.simg shub://BrendelGroup/GoSTRIPES
ls
cd ..
```
Now that we have downloaded the singularity image to call and run TagDust2, next step is to download the most updated rRNA sequence list from Ensembl [BioMart](http://useast.ensembl.org/biomart/martview/b56f6bc18af941cb4a61c1ef121b91d1). For example, [click here](https://www.ensembl.org/biomart/martview/67dcc0a3e364a6154fcdfd992dcdbdf2) to download Drosophila rRNA sequence list to your local computer, rename the file name (i.e., "Dro_rRNA.txt") and transfer the file to *add_mat* directory.
At the end of this step your home directory will have a second directory named *add_mat* with the "gostripes" singularity image and a .txt file with rRNA sequences to be removed (i.e., "Dro_rRNA.txt").
### Step 3: Analysis mode selection and defining additional experiment specific variables
To specify experiment specific variables, open and update "GeneralVariables.py" module using emacs text editor.
```
cd scripts
emacs GeneralVariables.py
```
- Specify the name of the rRNA sequence list in *add_mat* directory by updating the string value of variable **rRNA_list**.
- You can customize Bowtie2 alignment parameters by updating the string value of variable **bowtie2_para**.
- To specify the strandedness of the experiment change the value of variable "stranded". Options are 0 (unstranded), 1 (stranded) and 2 (reversely stranded).
- You can define which features to be counted using featureCounts by updating values of the list **diff_features**. To check supported features, download and open the annotation file using "less" command.
Once necessary changes are being made:
```
Ctrl+x+s then Ctrl+x+c ## To save and quit emacs
cd ..
ls
```
> add_mat  
> scripts

### Step 4: Input data preparation
The pipeline uses adapter trimmed input files in .fastq format for analysis. To make the "raw_sequences" on your home directory, navigate first to the home directory and create a directory *raw_sequences*.
```
mkdir raw_sequences
ls
```
> add_mat  
> raw_sequences   
> scripts   

Then upload adapter trimmed sequences to the raw_sequences directory. The naming of files is ***very important*** and follow the recommended naming scheme. Always the name of a file should end with ***'_R1.fastq'*** for single-end data inputs. If the input is paired-end, the name of two read mates should end with ***'_R1.fastq'*** and ***'_R2.fastq'***. During analysis the pipeline sorts and lists input files based on this architecture.
### Step 5: Executing the pipeline
All executables of the pipeline are written onto *run.py* module. To start analyzing data activate the conda environment above, navigate to the scripts directory and execute *run.py* using python.
```
source activate dataanalyzer
cd scripts
python run.py
```
## Analysis process
All analyzed data will be saved onto the home directory where you created the *scripts* directory. The pipeline first use [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess the quality of raw input files. Subsequently, the program [Cutadapt](https://cutadapt.readthedocs.io/en/stable/) is used to trim off standard illumina adaptors from the 3'-end of input reads. Next [TagDust2](http://tagdust.sourceforge.net/) is being used to remove rRNA contaminants from individual datasets. A datamining module in the pipeline will summarize TagDust2 rRNA removal logs and deposit mined data onto a file named **TagDust_summary.csv** which will be saved onto a directory named *summary_files*. Subsequently, user defined genome and annotation files will be downloaded and genome indices will be created. Subsequently, rRNA-depleted sequences are mapped to the given genome using [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml) genome aligner. Additionally, this pipeline use [ShortStack](https://github.com/MikeAxtell/ShortStack) to identify all types of small RNAs from mapped sequences. The analysis scheme then uses [SAMtools](https://github.com/samtools/samtools) to coordinate sort, remove unmapped sequences and index Bowtie2 alignment output files. The pipeline subsequently use [QualiMap](http://qualimap.bioinfo.cipf.es/) to assess the quality of sequence alignment. The sorted alignment file and the index will be used by [deepTools](https://github.com/deeptools/deepTools/) to generate bigwig files for [IGV](https://software.broadinstitute.org/software/igv/) visualization. Next subread package [featureCounts](http://subread.sourceforge.net/) will be called to quantify user defined set of features. Finally, the pipeline integrates [MultiQC](https://github.com/ewels/MultiQC) to generate summary files in an interactive manner.
## Retrieve additional information
It is important to track the number of sequences retained after each step. You can use following bash commands to acheive this.
1. If the directory of interest have a series of *.fastq* files, you can use the following bash command to get read counts saved into a *.txt* file in the same directory. As an example let's save read counts of the *raw_sequences* directory.
```
cd raw_sequences

for i in `ls *.fastq`; do
c=`cat $i | wc -l`
c=$((c/4))
echo $i $c
done > raw_readCounts.txt
```
> Executing the above bash command will save a file named *raw_readCounts.txt* in the *raw_sequences* directory with file name and number of reads in each file.

2. If the directory of interest have a series of *.bam* files, you can use the following bash command that uses [SAMtools](https://github.com/samtools/samtools). As an example let's save read counts of the *bt2_aligned* directory.
```
cd bt2_aligned

for i in `ls *.bam`; do
echo ${i} $(samtools view -F 4 -c $i)
done > bam_readCounts_aligned.txt
```
> Executing the above bash command will save a file named *bam_readCounts_aligned.txt* in the *star_aligned* directory with bam file names and number of reads that are mapped to the reference genome. Note that the [sam flag](https://broadinstitute.github.io/picard/explain-flags.html) ***4*** eliminates unmapped sequences from the count, thus giving the total number of sequences that are successfully aligned.
