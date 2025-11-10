s1=sys.argv[0]
s2=sys.argv[1]
s3=sys.argv[2]
s4=sys.argv[3]
s5=sys.argv[4]
avg_mrks=(sys.argv[0]+sys.argv[1]+sys.argv[2]+sys.argv[3]+sys.argv[4])/
print("----------Grade Evaluation----------")
print(f"Average Marks:",avg_mrks)

if(avg_mrks >= 85):
    print("Grade A")

elif(avg_mrks >= 60):
    print("Grade B")

elif(avg_mrks >= 40):
    print("Grade C")

else:
    print("Grade D")
