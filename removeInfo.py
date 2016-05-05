# remote any info before INFO for each line
import re, os, sys, getopt


def main(argv):
   inputfile = ''
   outputfile = ''

   info = re.compile(".* PID.* TID.* INFO.*:");

   try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
       print 'test.py -i <inputfile> -o <outputfile>'
       sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print 'test.py -i <inputfile> -o <outputfile>'
           sys.exit()
       elif opt in ("-i", "--ifile"):
           inputfile = arg
       elif opt in ("-o", "--ofile"):
           outputfile = arg

   fw = open(outputfile, 'w')

   with open(inputfile, 'r') as fr:
       for line in fr:
           result = info.search(line)
           if result:
               fw.write(line[result.end():])




if __name__ == "__main__":
   main(sys.argv[1:])

