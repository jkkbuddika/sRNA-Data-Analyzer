import os
import glob
import subprocess as sp
import ColorTextWriter

class ShortStack:

    def __init__(self, home_dir, input_dir, bt_index):
        self.home_dir = home_dir
        self.input_dir = input_dir
        self.bt_index = bt_index

    def ss_aligner(self):

        outdir = os.path.join(self.home_dir, 'shortstack_aligned')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        fastq_list = sorted(glob.glob(self.input_dir + '*tagdustout.fq'))

        ctw = ColorTextWriter.ColorTextWriter()

        print(ctw.CBEIGE + ctw.CBOLD + 'Running ShortStack Aligner ...' + ctw.CEND + '\n')

        for i in fastq_list:

            print(ctw.CBEIGE + ctw.CBOLD + 'ShortStacking: ' + ctw.CBLUE + os.path.basename(i) + ctw.CBEIGE + ctw.CBOLD + ' ...' + ctw.CEND + '\n')

            sub_directory = outdir + '/' + os.path.basename(i).split('.fq')[0] + '/'

            command = [
                'ShortStack',
                '--genomefile', self.bt_index,
                '--readfile', i,
                '--outdir', sub_directory
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

        print('\n' + ctw.CRED + ctw.CBOLD + 'Mapping with ShortStack is Completed!!!' + ctw.CEND + '\n')