import sys

def readFile(file_in):

    src = open(file_in, 'r')
    code = src.read().split("\n")
    title = code[0][code[0].find(".") + 2:]

    link = code[1]
    sublink = link[link.rfind("problems/"):10]

    solution = ""
    for i in range(3, len(code)):
        code[i] = code[i][3:] + "\n"
        solution += code[i]
    return " " + title + "\n\n" + link + "\n\n```python\n" + solution + "```\n\n##"

    src.close()

def writeFile(file_out, text):
    md = open('intervals.md', 'r+')
    if (md.read(1) != "#"):
        md.write("# Intervals\n\n\n##")

    md.seek(0)
    page = md.read()

    page = page.replace("##", "+ [" + title + "](#" + sublink + ")\n\n##", 1)
    md.seek(0)
    md.write(page)

    md.write(text)

    md.close()

def main(file_in, file_out):

    writeFile(file_out, readFile(file_in))

if __name__ == "__main__":
    param = sys.argv
    main(param[1], param[2])