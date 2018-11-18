#r is read
gene = open("BRCA1_BAP1.txt","r")

#set values to zero
g=0
a=0
c=0
t=0

#skip the first line of header in FASTA format
gene.readline()


for line in gene:
        line=line.lower()
        for char in line:
                if char == "g":
                        g+=1
                if char == "a":
                        a+=1
                if char == "c":
                        c+=1
                if char == "t":
                        t+=1

#0.convert to floating point --important but why?
gc = (g+c+0.) / (a+t+c+g+0.)

at = (a+t+0.) / (a+c+t+g+0.)

print"       "
print"       "
print"--------------------------------"
print" THE NUCLEOTIDE SEQUENCER 9000"
print"--------------------------------"
print"      count        percent composition  "
print "G COUNT: " + str(g) + "    " + str(g/(g+a+t+c+0.)) + "%"
print "C COUNT: " + str(c) + "    " + str(c/(g+a+t+c+0.)) + "%"
print "A COUNT: " + str(a) + "    " + str(a/(g+a+t+c+0.)) + "%"
print "T COUNT: " + str(t) + "    " + str(t/(g+a+t+c+0.)) + "%"
print"----------------------------"
print "GC PERCENTAGE: " + str(gc)
print "AT PERCENTAGE: " + str(at)
print"----------------------------"

total=(g+c+a+t)

print "TOTAL NUCLEOTIDE COUNT: " + str(total)
print"----------------------------"

#attempting to print over9000 if the GC is over.. wish me luck
if (g+c) > 9000:
        print "ITS OVER 9000!"
else:
        print "dont worry its not over 9000"

print"----------------------------"
    
x= (total) - (9000)

print "in fact this count is.. " + str(x) + " digits over 9000, to be exact.."

print"----------------------------"
print"       "
print"       "















