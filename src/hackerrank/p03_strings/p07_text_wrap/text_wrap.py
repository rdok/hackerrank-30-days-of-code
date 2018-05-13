import textwrap

if __name__ == '__main__':
    string_s = raw_input()
    width_w = int(raw_input())

    print textwrap.fill(string_s, width_w)
