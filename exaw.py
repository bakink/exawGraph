import os
import re


def get_stat_date(file_rows_list):
    string_num = 7
    p = re.compile('<.*>')
    m = p.search(file_rows_list[string_num])
    return m.group().split()[0][1:]


def parse_mpstat(mpstatout_dir):
    print('Parsing mpstat files...')
    data_struct = []
    for filename in os.listdir(mpstatout_dir):
        if filename.endswith('.dat'):
            print()
            print(filename)
            with open(mpstatout_dir + '\\' + filename) as f:
                rows = f.readlines()
            stat_date = get_stat_date(rows)
            for line in rows:
                all_cpu_rows = re.findall(r'all', line)
                if all_cpu_rows:
                    l = line.split()
                    data_struct.append([stat_date + ' ' + l[0] + ' ' + l[1], {'%user': l[3], '%sys': l[5], '%iowait': l[6]}])
            print(data_struct)


def parse(archive_dest=None, begin_time=None, end_time=None):
    # print(archive_dest)
    if archive_dest is None:
        archive_dest = os.getcwd() + '\\archive'
    # print(archive_dest)
    parse_mpstat(mpstatout_dir=archive_dest + '\\Mpstat.ExaWatcher')


def main():
    parse('R:\downloads\Exawatcher_archive_exadata_node1_28092016')
    # drawg()


if __name__ == '__main__':
        main()
