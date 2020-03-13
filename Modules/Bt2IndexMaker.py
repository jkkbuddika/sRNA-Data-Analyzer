import os
import subprocess as sp
import ColorTextWriter

class Bt2IndexMaker:

    def __init__(self, home_dir, threads, genes_fa, extensions):
        self.home_dir = home_dir
        self.threads = threads
        self.genes_fa = genes_fa
        self.extensions = extensions

    def bt2_index_maker(self):

        outdir = os.path.join(self.home_dir, 'bt2_index')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        ctw = ColorTextWriter.ColorTextWriter()

        print(ctw.CBEIGE + ctw.CBOLD + 'Generating Bowtie2 Genome Indices ...' + ctw.CEND + '\n')

        bt2_index_path = outdir + '/' + 'bt2_index'

        command = [
            'bowtie2-build',
            '--threads', self.threads, '-q',
            self.genes_fa, bt2_index_path
        ]

        command = ' '.join(command)
        sp.check_call(command, shell=True)

        print('\n' + ctw.CRED + ctw.CBOLD + 'Bowtie2 Genome Indices Generated!!!' + ctw.CEND + '\n')