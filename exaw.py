import os
import re
import matplotlib.pyplot as plt


def plot_data(parsed_data_list, y_value):
    x_list = []
    y_list = []
    for dt in parsed_data_list:
        x_list.append(dt[0])
        y_list.append(dt[1][y_value])
    x_num_ordered = [n for n in range(1, len(x_list) + 1)]
    plt.xticks(x_num_ordered, x_list)
    plt.plot(x_num_ordered, y_list)
    plt.ylabel('user CPU utilization, %')
    plt.show()


def get_stat_date(file_rows_list):
    string_num = 7
    p = re.compile('<.*>')
    m = p.search(file_rows_list[string_num])
    return m.group().split()[0][1:]


def parse_mpstat(mpstatout_dir):
    print('Parsing mpstat files...')
    mpstat_data = []
    ctime = lambda fn: os.stat(os.path.join(mpstatout_dir, fn)).st_mtime
    for filename in list(sorted(os.listdir(mpstatout_dir), key=ctime)):
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
                    mpstat_data.append(
                        [stat_date + ' ' + l[0] + ' ' + l[1], {'%user': l[3], '%sys': l[5], '%iowait': l[6]}])
    return mpstat_data


def parse(archive_dest=None, begin_time=None, end_time=None):
    # print(archive_dest)
    if archive_dest is None:
        archive_dest = os.getcwd() + '\\archive'
    # print(archive_dest)
    return parse_mpstat(mpstatout_dir=archive_dest + '\\Mpstat.ExaWatcher')



def main():
    data_p = parse('R:\downloads\Exawatcher_archive_exadata_node1_28092016')
    plot_data(data_p, '%user')


if __name__ == '__main__':
    main()
