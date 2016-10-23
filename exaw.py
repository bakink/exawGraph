import os


def parse_mpstat(mpstatout_dir):
    print('Parsing mpstat files...')
    for filename in os.listdir(mpstatout_dir):
        if filename.endswith('.dat'):
            print(filename)
            with open(mpstatout_dir + '\\' + filename) as f:
                rows = f.readlines()

            print(rows[7])




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
