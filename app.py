from flask import Flask, render_template, request

app = Flask(__name__)

def upper(name):
    return ''.join([chr(ord(ch) - 32) if 'a' <= ch <= 'z' else ch for ch in name])

def count_uncommon_letters(smaller, larger, length):
    Y = [-1] * (len(smaller) + len(larger))
    index = 0
    count = 0

    for i in range(len(smaller)):
        if smaller[i] == ' ':
            continue
        for j in range(len(larger)):
            if larger[j] == ' ':
                continue
            if smaller[i] == larger[j]:
                found = 0
                for k in range(len(Y)):
                    if Y[k] == -1:
                        break
                    if j == Y[k]:
                        found = 1
                        break
                if found == 0:
                    count += 1
                    Y[index] = j
                    index += 1
                    Y[index] = -1
                    break

    return (len(smaller.replace(' ', '')) + len(larger.replace(' ', '')) - count * 2)

def flames(diff):
    categories = ['F', 'L', 'A', 'M', 'E', 'S']
    eliminated = [0] * 6
    remaining = 6
    count = 0
    i = 0

    while remaining > 1:
        if eliminated[i] == 0:
            count += 1
            if count == diff:
                eliminated[i] = 1
                count = 0
                remaining -= 1
        i += 1
        if i >= 6:
            i = 0

    for idx in range(6):
        if eliminated[idx] == 0:
            final = idx
            break

    result = {
        0: "FRIENDS 🤝",
        1: "LOVERS 💘",
        2: "AFFECTIONATE 🐥",
        3: "MARRIAGE 💍",
        4: "ENEMIES ⚔️",
        5: "SIBLING 👯‍♀️"
    }
    return result[final]

@app.route('/', methods=['GET', 'POST'])
def index():
    relationship = ""
    error = ""
    name1 = ""
    name2 = ""
    
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']

        if name1.strip().lower() == name2.strip().lower():
            error = "The names are identical. Please enter two different names."
        else:
            name1_u = upper(name1)
            name2_u = upper(name2)

            length1 = sum(1 for ch in name1_u if ch != ' ')
            length2 = sum(1 for ch in name2_u if ch != ' ')

            if length1 == length2:
                uncommon = count_uncommon_letters(name1_u, name2_u, length2)
            elif length1 > length2:
                uncommon = count_uncommon_letters(name2_u, name1_u, length2)
            else:
                uncommon = count_uncommon_letters(name1_u, name2_u, length1)

            if uncommon == 0:
                error = "No uncommon letters found, both names are identical."
            else:
                relationship = flames(uncommon)

    return render_template('index.html', name1=name1, name2=name2, relationship=relationship, error=error)

if __name__ == '__main__':
    app.run(debug=True)
