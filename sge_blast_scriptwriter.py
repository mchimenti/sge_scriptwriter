import os

def get_path():
    current = os.getcwd()
    user = os.getenv("USER")
    return current, user
    
def get_options():
    queue = raw_input("Which queue would you like to use? ('all', 'priority', 'parallel'): ")
    pe = raw_input("How many threads? (1-50): ")
    input_file = raw_input("What is the name of your input file?: ")
    
    blast_dict = {"p":"blastp","n":"blastn",'x':'blastx'}
    blast_type = raw_input("What kind of blast do you want to use? (enter one letter, e.g., 'blast(p)', 'blast(n)', 'blast(x)') ")
    
    e_value = raw_input("What e-value cutoff do you want?")
    return queue, int(pe), input_file, blast_dict[blast_type], float(e_value)

def write_qsub_header(queue_name, pe_number, input_name):
    print "*****COPY AND PASTE THE LINES BELOW INTO A TEXT EDITOR***"
    print "*****FILL IN THE PATH TO YOUR SEQUENCE FILES AND DATABASE FILE IN THE LAST LINE***"
    print 
    print "#!/bin/bash"
    print "#"
    print "#$ -q {}.q".format(queue_name)
    print "#$ -pe threads {}".format(pe_number)
    print "#$ -o {}.stdout".format(input_name)
    print "#$ -e {}.stderr".format(input_name)
    
def write_blast_command(blast_type, e_val, cwd):
    print 
    print "blastall -p {} -d {} -i {} -o {} -e {}".format(blast_type, cwd, cwd, cwd, e_val)
    
if __name__ == "__main__":
    q, pe, inp, blast, e_val = get_options()
    cwd, user = get_path()
    
    write_qsub_header(q, pe, inp)
    write_blast_command(blast, e_val, cwd)