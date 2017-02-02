import os
import subprocess
import sys
import getopt
import glob

#print os.path.dirname(os.path.abspath(__file__));
#print  os.getcwd();

def main(argv):

   indir = os.path.dirname(os.path.abspath(__file__));
   outdir = os.path.dirname(os.path.abspath(__file__));
   extensions = ['docx', 'doc', 'rtf', 'txt', 'otf'];
   recursive = 0;

   try:
      opts, args = getopt.getopt(argv,"ioer",["in=","out=", "ext=", "recursive="])
      print args
   except getopt.GetoptError:
      print 'not good'
      sys.exit(2)
   for opt, arg in opts:
      print opt
      if opt in ("-i", "--in"):
         indir = arg
      elif opt in ("-o", "--out"):
         outdir = arg
      elif opt in ("-e", "--ext"):
        extensions = arg.split(' ')
      elif opt in ("-r", "--recursive"):
         recursive = 1

   convertThis(indir, outdir, extensions)

   print '--- Done'


def convertThis(indir, outdir, extensions):

     print '--- Starting unoconv listener (just wait 20 seconds)'
     os.system('unoconv --listener & sleep 20')
     print '--- OK, let\'s go'
     
     for root, subdirs, files in os.walk(indir):
        print root	
        for ext in extensions:
            if next(glob.iglob(root + "/*." + ext), None):
               os.chdir(root)  
               cmd = "unoconv -f pdf *." + ext
               print cmd
               os.system(cmd)
               #subprocess.call(["doc2pdf", "*." + ext, "-v" ])
            else:
               print "--- No files of type: "+ext
               
     
     os.system('kill -15 %-')


if __name__ == "__main__":
   main(sys.argv[1:])
