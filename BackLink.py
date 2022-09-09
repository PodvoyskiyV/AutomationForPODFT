files = ["templates/mrot.html", "templates/octo.html", "templates/p2p.html"]

for file in files:
    html_file = open(file)
    string_list = html_file.readlines()
    html_file.close()

    for i in range(len(string_list)):
        if '<link' in string_list[i]:
            if 'href=' in string_list[i]:
                if '"http' in string_list[i]:
                    continue
                else:
                    start_index = string_list[i].find('href=') + 9
                    tail = string_list[i].find('>', start_index)
                    end_index = string_list[i].find('/', start_index, tail)
                    folder = string_list[i][start_index:end_index]
                    end_of_filename = string_list[i].find('"', end_index)
                    filename = string_list[i][end_index + 1:end_of_filename]
                    after_file_name = string_list[i][end_of_filename:]
                    string_list[i] = string_list[i][:start_index - 3]
                    string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name
        elif '<a' in string_list[i]:
            if '#' in string_list[i]:
                continue
            elif 'href=' in string_list[i]:
                if '.html' in string_list[i]:
                    start_index = string_list[i].find('href=') + 6
                    tail = string_list[i].find('>', start_index)
                    end_index = string_list[i].find('/', start_index, tail)
                    if end_index == -1:
                        end_of_filename = string_list[i].find('"', start_index)
                        filename = string_list[i][start_index:end_of_filename - 5]
                        after_file_name = string_list[i][end_of_filename:]
                        string_list[i] = string_list[i][:start_index]
                        string_list[i] += "{{ url_for('%s') }}" % filename + after_file_name
                    else:
                        end_of_filename = string_list[i].find('"', start_index)
                        filename = string_list[i][end_index + 1:end_of_filename - 5]
                        after_file_name = string_list[i][end_of_filename:]
                        string_list[i] = string_list[i][:start_index]
                        string_list[i] += "{{ url_for('%s') }}" % filename + after_file_name
                else:
                    start_index = string_list[i].find('href=') + 6
                    tail = string_list[i].find('>', start_index)
                    end_index = string_list[i].find('/', start_index, tail)
                    if end_index != -1:
                        folder = string_list[i][start_index:end_index]
                        end_of_filename = string_list[i].find('"', end_index)
                        filename = string_list[i][end_index + 1:end_of_filename]
                    else:
                        continue
                    after_file_name = string_list[i][end_of_filename:]
                    string_list[i] = string_list[i][:start_index]
                    string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name
            elif 'src=' in string_list[i]:
                start_index = string_list[i].find('src=') + 5
                tail = string_list[i].find('>', start_index)
                end_index = string_list[i].find('/', start_index, tail)
                folder = string_list[i][start_index:end_index]
                end_of_filename = string_list[i].find('"', end_index)
                filename = string_list[i][end_index + 1:end_of_filename]
                after_file_name = string_list[i][end_of_filename:]
                string_list[i] = string_list[i][:start_index]
                string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name
        elif 'src=' in string_list[i]:
            if '..' in string_list[i]:
                start_index = string_list[i].find('src=') + 8
                tail = string_list[i].find('>', start_index)
                end_index = string_list[i].find('/', start_index, tail)
                folder = string_list[i][start_index:end_index]
                end_of_filename = string_list[i].find('"', end_index)
                filename = string_list[i][end_index + 1:end_of_filename]
                after_file_name = string_list[i][end_of_filename:]
                string_list[i] = string_list[i][:start_index-3]
                string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name

    html_file = open(file, "w")
    new_content = "".join(string_list)
    html_file.write(new_content)
    html_file.close()


html_file = open("index.html")
string_list = html_file.readlines()
html_file.close()

for i in range(len(string_list)):
    if '<link' in string_list[i]:
        if 'href=' in string_list[i]:
            if '"http' in string_list[i]:
                continue
            else:
                start_index = string_list[i].find('href=') + 6
                tail = string_list[i].find('>', start_index)
                end_index = string_list[i].find('/', start_index, tail)
                folder = string_list[i][start_index:end_index]
                end_of_filename = string_list[i].find('"', end_index)
                filename = string_list[i][end_index + 1:end_of_filename]
                after_file_name = string_list[i][end_of_filename:]
                string_list[i] = string_list[i][:start_index]
                string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name
    elif '<a' in string_list[i]:
        if '#' in string_list[i]:
            continue
        elif 'href=' in string_list[i]:
            if '.html' in string_list[i]:
                start_index = string_list[i].find('href=') + 6
                tail = string_list[i].find('>', start_index)
                end_index = string_list[i].find('/', start_index, tail)
                if end_index == -1:
                    end_of_filename = string_list[i].find('"', start_index)
                    filename = string_list[i][start_index:end_of_filename - 5]
                    after_file_name = string_list[i][end_of_filename:]
                    string_list[i] = string_list[i][:start_index]
                    string_list[i] += "{{ url_for('%s') }}" % filename + after_file_name

                else:
                    end_of_filename = string_list[i].find('"', start_index)
                    filename = string_list[i][end_index + 1:end_of_filename - 5]
                    after_file_name = string_list[i][end_of_filename:]
                    string_list[i] = string_list[i][:start_index]
                    string_list[i] += "{{ url_for('%s') }}" % filename + after_file_name
            else:
                start_index = string_list[i].find('href=') + 6
                tail = string_list[i].find('>', start_index)
                end_index = string_list[i].find('/', start_index, tail)
                if end_index != -1:
                    folder = string_list[i][start_index:end_index]
                    end_of_filename = string_list[i].find('"', end_index)
                    filename = string_list[i][end_index + 1:end_of_filename]
                else:
                    continue
                after_file_name = string_list[i][end_of_filename:]
                string_list[i] = string_list[i][:start_index]
                string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name
    elif 'src=' in string_list[i]:
        start_index = string_list[i].find('src=') + 5
        tail = string_list[i].find('>', start_index)
        end_index = string_list[i].find('/', start_index, tail)
        folder = string_list[i][start_index:end_index]
        end_of_filename = string_list[i].find('"', end_index)
        filename = string_list[i][end_index + 1:end_of_filename]
        after_file_name = string_list[i][end_of_filename:]
        string_list[i] = string_list[i][:start_index]
        string_list[i] += "{{ url_for('%s', filename='%s') }}" % (folder, filename) + after_file_name


html_file = open('templates/index.html', "w")
new_content = "".join(string_list)
html_file.write(new_content)
html_file.close()

