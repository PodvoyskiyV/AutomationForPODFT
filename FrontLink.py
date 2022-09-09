files = ["templates/catalog.html", "templates/login.html", "templates/registration.html"]

for file in files:
    html_file = open(file)
    string_list = html_file.readlines()
    html_file.close()

    for i in range(len(string_list)):
        if '{{' in string_list[i]:
            start_index = string_list[i].find('{{')
            end_index = string_list[i].find('}}') + 2
            row = string_list[i][:start_index]

            if 'filename=' in string_list[i]:
                begin_of_folder = string_list[i].find("'", start_index) + 1
                end_of_folder = string_list[i].find("'", begin_of_folder)
                folder = string_list[i][begin_of_folder:end_of_folder]
                row += '../' + folder + '/'

                begin_of_file = string_list[i].find("'", end_of_folder + 1) + 1
                end_of_file = string_list[i].find("'", begin_of_file)
                filename = string_list[i][begin_of_file:end_of_file]

            elif 'index' in string_list[i]:
                begin_of_file = string_list[i].find("'", start_index) + 1
                end_of_file = string_list[i].find("'", begin_of_file)
                filename = '../' + string_list[i][begin_of_file:end_of_file] + '.html'

            else:
                begin_of_file = string_list[i].find("'", start_index) + 1
                end_of_file = string_list[i].find("'", begin_of_file)
                filename = string_list[i][begin_of_file:end_of_file] + '.html'

            row += filename + string_list[i][end_index:]
            string_list[i] = row

    html_file = open(file, "w")
    new_content = "".join(string_list)
    html_file.write(new_content)
    html_file.close()

html_file = open("templates/index.html")
string_list = html_file.readlines()
html_file.close()

for i in range(len(string_list)):
    if '{{' in string_list[i]:
        start_index = string_list[i].find('{{')
        end_index = string_list[i].find('}}') + 2
        row = string_list[i][:start_index]

        if 'filename=' in string_list[i]:
            begin_of_folder = string_list[i].find("'", start_index) + 1
            end_of_folder = string_list[i].find("'", begin_of_folder)
            folder = string_list[i][begin_of_folder:end_of_folder]
            row += folder + '/'

            begin_of_file = string_list[i].find("'", end_of_folder + 1) + 1
            end_of_file = string_list[i].find("'", begin_of_file)
            filename = string_list[i][begin_of_file:end_of_file]

        elif 'index' in string_list[i]:
            begin_of_file = string_list[i].find("'", start_index) + 1
            end_of_file = string_list[i].find("'", begin_of_file)
            filename = string_list[i][begin_of_file:end_of_file] + '.html'

        else:
            begin_of_file = string_list[i].find("'", start_index) + 1
            end_of_file = string_list[i].find("'", begin_of_file)
            filename = 'templates/' + string_list[i][begin_of_file:end_of_file] + '.html'

        row += filename + string_list[i][end_index:]
        string_list[i] = row

html_file = open('index.html', "w")
new_content = "".join(string_list)
html_file.write(new_content)
html_file.close()
