import os
import glob
import subprocess as sp
import ColorTextWriter

class Tagduster:

    def __init__(self, home_dir, tagdust_sing, input_dir, rrna, extensions):
        self.home_dir = home_dir
        self.tagdust_sing = tagdust_sing
        self.input_dir = input_dir
        self.rrna_list = rrna
        self.extensions = extensions

    def tagdust(self):

        outdir = os.path.join(self.home_dir, 'tagdust_out')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        r1_reads = sorted(glob.glob(self.input_dir + '*_trimmed.fastq'))

        ctw = ColorTextWriter.ColorTextWriter()

        print('\n' + ctw.CBEIGE + ctw.CBOLD + 'Running TagDust ...' + ctw.CEND)

        for i in r1_reads:
            print('\n' + ctw.CBEIGE + ctw.CBOLD + 'Tagdusting: ' + ctw.CBLUE + os.path.basename(i) + ctw.CBEIGE + ctw.CBOLD + ' ...' + ctw.CEND + '\n')

            output_file = outdir + '/' + os.path.basename(i).split('_trimmed')[0] + '_tagdustout'

            command = [
                'module load singularity;singularity exec -e -C -B', self.home_dir,
                '-H', self.home_dir, self.tagdust_sing,
                'tagdust -1 O:N -2 R:N',
                '-o', output_file,
                '-ref', self.rrna_list, '-fe 3', i
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

        print('\n' + ctw.CRED + ctw.CBOLD + 'Running TagDust Completed!!!' + ctw.CEND + '\n')