import GeneralVariables
import CommonVariables
import FastQCRunner
import Tagduster
import TDSummaryProcessor
import CutAdapt
import WebDownloader
import Bt2Aligner
import ShortStack
import SamTools
import BigWigFileMaker
import FeatureCounter
import MultiQCRunner
import ColorTextWriter

#### Executing the Program

ctw = ColorTextWriter.ColorTextWriter()
print('\n' + ctw.CRED + ctw.CBOLD + 'Initiating sRNA data analyzer ...' + ctw.CEND + '\n')
print(ctw.CRED + 'This script can take minutes to hours to analyze your data based on the number of libraries to be analyzed ...' + '\n')

gv = GeneralVariables.GeneralVariables()
cv = CommonVariables.CommonVariables()

qc_raw = FastQCRunner.FastQCRunner(cv.home_dir, cv.fastqc_raw, cv.raw_sequences_dir, cv.file_type[0])
qc_raw.fastqc()

ca = CutAdapt.CutAdapt(cv.home_dir, cv.raw_sequences_dir, cv.extensions, cv.cutadapt_dir)
ca.cutadapt()

td = Tagduster.Tagduster(cv.home_dir, cv.tagdust_singu, cv.raw_sequences_dir, cv.rRNA_path, cv.extensions)
td.tagdust()

tdsp = TDSummaryProcessor.TDSummaryProcessor(cv.tagdust_out, cv.summary_dir)
tdsp.td_summary()

wd = WebDownloader.WebDownloader(cv.home_dir, cv.genome_dir_name, cv.genome_path, cv.genome_file)
wd.download()

wd = WebDownloader.WebDownloader(cv.home_dir, cv.feature_dir_name, cv.feature_path, cv.feature_file)
wd.download()

bt2 = Bt2Aligner.Bt2Aligner(cv.home_dir, cv.tagdust_out, cv.Threads, cv.bowtie2_index, gv.bowtie2_para, cv.extensions)
bt2.aligner()

qc_mapped = FastQCRunner.FastQCRunner(cv.home_dir, cv.fastqc_bam, cv.bt2_aligned, cv.file_type[1])
qc_mapped.fastqc()

ssa = ShortStack.ShortStack(cv.home_dir, cv.cutadapt_dir, cv.bowtie_index)
ssa.ss_aligner()

ss = SamTools.SamTools(cv.bt2_aligned, cv.Threads, cv.extensions, cv.sam_sorted)
ss.sam_sorting()

bw = BigWigFileMaker.BigWigFileMaker(cv.home_dir, cv.sam_sorted, cv.extensions)
bw.bigwig()

fc = FeatureCounter.FeatureCounter(cv.home_dir, cv.sam_sorted, gv.diff_features, gv.stranded, cv.feature_dir, cv.feature_file, cv.extensions)
fc.feature()

mqc = MultiQCRunner.MultiQCRunner(cv.home_dir)
mqc.multiqc()

ctw = ColorTextWriter.ColorTextWriter()
print('\n' + ctw.CGREEN + ctw.CBOLD +ctw.CURL + ctw.CBLINK + 'Data analysis is complete!!!' + ctw.CEND + '\n')
