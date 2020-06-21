#Name: Charles Cheung
#Email: charles.cheung24@myhunter.cuny.edu
#Date: February 04, 2020
#This program tells you the length of a strand of DNA, tells you the number of C and G nucleotides, the percent of GC pairs in the strand, and the positions of the first G and C

DNA = input("PUT DNA HERE")

l = len(DNA)
print("Length is", l)
numc = DNA.count("C")
numg = DNA.count("G")

gc = (numc + numg) / l
gcPercent = gc
print("GC-content is", gcPercent)

findfirstg = DNA.find("G")
findfirstc = DNA.find("C")
print("First G found at position", findfirstg)
print("First C found at position", findfirstc)


