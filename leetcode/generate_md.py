src = open('source_leetcode_data.txt', 'r')
md = open('intervals.md', 'r+')

if (md.read(1) != "#"):
    md.write("# Intervals\n\n\n##")

md.seek(0)
page = md.read()

tcode = src.read().split("\n")

title = tcode[0][tcode[0].find(".") + 2:-1]

link = tcode[1]
sublink = link[link.rfind("problems/"):-1]

solution = ""
for i in range(3, len(tcode)):
    tcode[i] = tcode[i][7:] + "\n"
    solution += tcode[i]

page = page.replace("##", "+ [" + title + "](#" + sublink + ")\n\n##", 1)
md.seek(0)
md.write(page)

md.write(" " + title + "\n\n" + link + "\n\n```Python\n" + solution + "```\n\n##")

src.close()
md.close()
