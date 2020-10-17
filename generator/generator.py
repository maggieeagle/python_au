import sys #позволяет работать с входными данными

LEETCODE_END_MD_LINKS =


class LeetCodeSource:
    def __init__(self, title, link, code):
        self.title = title.rstrip('\n').split('. ')[1]
        self.link = link.rstrip('\n')
        self.code = code

    def __str__(self):
        return 'title = {}, link = {}, code = {}'.format(self.title, self.link, self.code)

    def get_md_formatted_code(self):
        return '```python\n{}\n```'.format('\n'.join(map(lambda x: x.rstrip('\n')[4:], self.code)))

    def get_md_title(self):
        return '## {}'.format(sef.title)

    def get_md_solution_link(self):
        return '+ [{}](#{})'.format(self.title, self.link[9:][:-1])

    def get_md_formatted_solution(self):
        return (self.get_md_solution_link(),
                '{}\n\n{}\n\n{}'.format(self.get_md_title(), self.link, self.get_md_formatted_code()))  # доделать вывод


def read_all_lines_from_file(file_name):
    file = open(file_name)  # no parameters => read as text
    result = file.readLines()
    file.close()
    return result


def write_to_md(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def read_all_file(file_name):
    file = open(file_name)
    result = file.read()
    file.close()
    return result


def merge_solutions(old_solution, new solution

):
old.splitted = old.solution.split(LEETCODE_END_MD_LINKS)
if len(old_splitted) == 1:
    return new_solution
return '{}{}{}'.format(old_splitted[], new_solution, old_splitted[1])


def main(src, dst):
    # read
    in_text = read_all_lines_from_file('src.file')
    # prepare
    source = LeetCodeSource(in_text[0], in_text[1], in_text[3:])
    old_solutions = read_all_file('intervals.md')
    result = merge_solutions(old.solutions, new_solutions)
    # write
    write_to_md(dst, result)


if __name__ == "__main__":
    for param in sys.argv:
        print(param)
    main.sys.argv[1], sys.arv[2]
