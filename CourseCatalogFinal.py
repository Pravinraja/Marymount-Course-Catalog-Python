#Course Link 1
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Cybersecurity-Accelerated-Second-Degree-BS')
text = responses.text
couheading='Cybersecurity Accelerated Second Degree (B.S.)'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Cybersecurity Accelerated Second Degree BS.csv', 'a+'))
with open('Cybersecurity Accelerated Second Degree BS.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Cybersecurity Accelerated Second Degree BS.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Cybersecurity Accelerated Second Degree (B.S.)'])
    w.writerows(data)

#Course Link 2
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-B-S')
text = responses.text
couheading='Information Technology (B.S.) '
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Information Technology BS.csv', 'a+'))
with open('Information Technology BS.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Information Technology BS.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Information Technology (B.S.)'])
    w.writerows(data)

#course link 3
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-Combined-B-S-M-S-Program')
text = responses.text
couheading='Information Technology, Combined B.S./M.S. Program '
print (couheading)
print(" ")
#matchesfirst=re.findall(r''sc-courselink'>.*>(.*)</a></td><td class="sc-coursetitle">',text)
#matches=re.findall(r'a class='sc-courselink'>(.*)</a>',text)
#matchedboth=re.findall(r"<td><a class='sc-courselink' href='/en/2019-2020/Catalogs/Graduate-Catalog/Courses/IT-Information-Technology/500/IT-[0-9]+'>IT [0-9]+</a><br />\n\s+</td>\n\s+<td>(.*)</td>)", text                      
matchesfirst= re.findall(r"<td><a class='sc-courselink' href='/en/2019-2020/Catalogs/Graduate-Catalog/Courses/IT-Information-Technology/500/IT-[0-9]+'>IT [0-9]+</a><br />\n\s+</td>\n\s+<td>(.*)</td>", text)
matches2=re.findall(r"<td><a class='sc-courselink' href='/en/2019-2020/Catalogs/Graduate-Catalog/Courses/IT-Information-Technology/500/IT-[0-9]+'>IT [0-9]+</a></td>\n\s+<td>(.*)</td>", text)
matches=re.findall(r"<td><a class='sc-courselink' href='/en/2019-2020/Catalogs/Graduate-Catalog/Courses/IT-Information-Technology/500/IT-[0-9]+'>(.*)</a>",text)
#for event in matches:
#    print(event) 
f = open('file.txt', 'w')
for event in matches:
    print(event)
#for i in range(3):
    #f.write('\n')
    intvalue =0
    s = event
    f.write(s+'\n')
f.close() 
f = open('file2.txt', 'w')
for event1 in matches2:
    print(event1)
#for i in range(3):
    #f.write('\n')
    intvalue =0
    s = event1
    f.write(s+'\n')
f.close()   
f = open('file1.txt', 'w')
for event2 in matchesfirst:
    print(event2)
    #for i in range(3):
    #f.write('\n')
    intvalue =0
    s = event2
    f.write(s+'\n')
f.close()        
data = data2 = ""  
# Reading data from file1
with open('file1.txt') as fp:
    data = fp.read()  
# Reading data from file2
with open('file2.txt') as fp:
    data2 = fp.read()  
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2  
with open ('file3.txt', 'w') as fp:
    fp.write(data) 
with open('file3.txt', 'r+') as fd:
    lines = fd.readlines()
    fd.seek(0)
    fd.writelines(line for line in lines if line.strip())
    fd.truncate()
with open('file.txt') as f1, open('file3.txt') as f2, open("Information Technology Combined BSMS program.csv", "w") as f3:
  for x, y in zip(f1, f2):
     print("{0} \n {1}".format(x.strip(), y.strip()))
     #f3.write(x.strip()+y.strip())
     f3.write("{0}  {1}".format(x.strip(","), y.strip(",")))
with open('Information Technology Combined BSMS program.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Information Technology Combined BSMS program.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Information Technology, Combined B.S./M.S. program'])
    w.writerows(data)


#Course Link 4 #Not working
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-and-Cybersecurity-Combined-B-S-M-S-Program')
text = responses.text
couheading='Information Technology and Cybersecurity, Combined B.S./M.S. Program  '
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    #with open("Output.txt", "w") as text_file:
        #print(f"{results3}", file=text_file)
    print(results3)
    #print(results3,  file=open('Information Technology and Cybersecurity Combined BSMS Program.csv', 'a+'))
#with open('Information Technology and Cybersecurity Combined BSMS Program.csv',newline='') as f:
    #r = csv.reader(f)
    #data = [line for line in r]
#with open('Information Technology and Cybersecurity Combined BSMS Program.csv','w',newline='') as f:
    #w = csv.writer(f)
   # w.writerow(['Information Technology and Cybersecurity, Combined B.S./M.S. Program '])
    #w.writerows(data)

#Course Link 5
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-B-S-to-M-B-A-Program')
text = responses.text
couheading='Information Technology (B.S.) to M.B.A Program'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Information Technology BS to MBA Program.csv', 'a+'))
with open('Information Technology BS to MBA Program.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Information Technology BS to MBA Program.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Information Technology (B.S.) to M.B.A Program '])
    w.writerows(data)

#Course Link 6 # Nothing to scrape here
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-M-B-A-Guaranteed-Admission-Program')
text = responses.text
couheading='Information Technology (B.S.)/M.B.A. Guaranteed Admission Program'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Information Technology BS to MBA Program.csv', 'a+'))
with open('Information Technology BS to MBA Program.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Information Technology BS to MBA Program.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Information Technology (B.S.) to M.B.A Program '])
    w.writerows(data)

#Course Link 7
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Computer-Networking-and-Cybersecurity-Minor')
text = responses.text
couheading='Computer Networking and Cybersecurity (Minor)'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Computer Networking Cybersecurity Minor.csv', 'a+'))
with open('Computer Networking Cybersecurity Minor.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Computer Networking Cybersecurity Minor.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Computer Networking and Cybersecurity (Minor) '])
    w.writerows(data)

#Course Link 8
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Computer-Science-Minor')
text = responses.text
couheading='Computer Science (Minor)'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Computer Science Minor.csv', 'a+'))
with open('Computer Science Minor.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Computer Science Minor.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Computer Science (Minor)'])
    w.writerows(data)

#Course Link 9
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Data-Science-Minor')
text = responses.text
couheading='Data Science (Minor)'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Data Science Minor.csv', 'a+'))
with open('Data Science Minor.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Data Science Minor.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Data Science (Minor)'])
    w.writerows(data)

#Course Link 10
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Forensic-Computing-Minor')
text = responses.text
couheading='Forensic Computing (Minor) '
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Forensic Computing minor.csv', 'a+'))
with open('Forensic Computing minor.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Forensic Computing minor.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Forensic Computing Minor'])
    w.writerows(data)

#Course Link 11
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-Minor')
text = responses.text
couheading='Information Technology (Minor) '
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Information Technology minor.csv', 'a+'))
with open('Information Technology minor.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Information Technology minor.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Information Technology (Minor)'])
    w.writerows(data)

#Course Link 12
import requests
import re
import csv
responses = requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Data-Science-Post-Baccalaureate-Certificate')
text = responses.text
couheading='Data Science (Post-Baccalaureate Certificate)'
print (couheading)
print(" ")
matchesfirst=re.findall(r'"sc-coursenumber">.*>(.*)</a></td><td class="sc-coursetitle">',text)
matches=re.findall(r'td class="sc-coursetitle">(.*)</td>',text)
#for event in matches:
    #print(event)   
#for event1 in matchesfirst:
    #print(event1)
for event,event1 in zip(matches,matchesfirst):
    #print(event1,event)

    res=event1+ "," +event
    results1=re.sub('</td><td><p class="', ",", res)
    results2=re.sub('">',",",results1)
    results3=re.sub('</p>'," ",results2)
    results34=results3.strip()
    #print(results1,results2,results3,results34)
    print(results34)
    with open("Output.txt", "w") as text_file:
        print(f"{results3}", file=text_file)
    print(results3)
    print(results3,  file=open('Data Science Post-Baccalaureate certificate.csv', 'a+'))
with open('Data Science Post-Baccalaureate certificate.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Data Science Post-Baccalaureate certificate.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Data Science (Post-Baccalaureate Certificate)'])
    w.writerows(data)
