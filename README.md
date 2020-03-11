# Small RNA (sRNA) Data Analyzer

This repository contain a series of python based modules to automate sequencing data generated from small RNA (*i.e.*, miRNA, siRNA, piRNA, *etc*.) libraries. I ***highly recommend*** reading through this step-by-step manual *carefully* before you start analyzing your data. If you are interested in a protocol for sRNA library preparation I recommend looking at the [Sokol lab](http://sokollab.mystrikingly.com/) sRNA library preparation protocol given [here](http://sokollab.mystrikingly.com/).

## Requirements
The sRNA-seq data analyzer requires following tools to be installed for data analysis.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
- [Cutadapt](https://cutadapt.readthedocs.io/en/stable/)
- [TagDust2](http://tagdust.sourceforge.net/)
- [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
- [QualiMap](http://qualimap.bioinfo.cipf.es/)
- [ShortStack](https://github.com/MikeAxtell/ShortStack)
- [SAMtools](https://github.com/samtools/samtools)
- [deepTools](https://github.com/deeptools/deepTools/)
- [Subread](http://subread.sourceforge.net/)
- [MultiQC](https://github.com/ewels/MultiQC)

We thank developers of these valueble tools!

## Getting started
Start data analysis with setting up a conda environment with all the above tools installed, as it gives you the opportunity to use most updated versions. To set up the conda environment (i.e., srna_analyzer):
```
conda create -n srna_analyzer -c conda-forge -c bioconda python=3.7
conda install -n srna_analyzer -c conda-forge -c bioconda fastqc cutadapt bowtie2 qualimap shortstack samtools deeptools subread multiqc
```
To update your conda environment:
```
conda update -n srna_analyzer -c conda-forge -c bioconda --all
```
To activate the enironment:
```
source activate srna_analyzer
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
rm -rf sRNA-Data-Analyzer.git
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
