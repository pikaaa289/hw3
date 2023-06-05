from flask import Flask, render_template, request, jsonify,redirect
import subprocess
import os
import logomaker


app = Flask(__name__, static_folder='assets')


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/download_file', methods=['POST'])
def download_file():
    if request.method == 'POST':
        # 获取 textarea_data 的内容
        textContent = request.form.get('textarea_data')
        # 指定要下載的資料夾路徑和檔案名稱
        directory = 'assets'
        filename = 'example.txt'

        # 将输入的内容写入文件
        with open(f'{directory}/{filename}', 'w', encoding='utf-8') as file:
            if textContent:
                lines = textContent.strip().split('\n')
                cleaned_lines = [line.rstrip() for line in lines]  # 将内容切割成每行的列表
                file.write('\n'.join(cleaned_lines))  # 写入时重新组合成换行符号分隔的字符串

        with open("assets/example.txt", "r") as f:
            sequences = [line.strip() for line in f]
            print(sequences)

        colors = {
            "A": "red",
            "B": "orange",
            "C": "yellow",
            "D": "green",
            "E": "blue",
            "F": "purple",
            "G": "black",
            "H": "grey",
            "I": "pink",
            "J": "brown",
            "K": "c",
            "L": "lime",
            "M": "salmon",
            "N": "navy",
            "O": "plum",
            "P": "violet",
            "Q": "teal",
            "R": "lavender",
            "S": "aqua",
            "T": "m",
            "U": "greenyellow",
            "V": "orchid",
            "W": "tan",
            "X": "beige",
            "Y": "peru",
            "Z": "aquamarine"
        }
        counts_matrix = logomaker.alignment_to_matrix(sequences)
        logo = logomaker.Logo(counts_matrix, color_scheme=colors)

        # 设置图片大小和格式
        logo.style_spines(visible=False)
        logo.style_xticks(rotation=90, fmt="%s")
        logo.ax.set_title("My Sequence Logo")
        logo.fig.set_size_inches(6, 4)
        logo_path = "assets/my_logo.png"
        logo.fig.savefig(logo_path, dpi=300)

        # 构建返回的 JSON 数据
        return redirect('/')
    # 如果请求不是 POST，则返回错误信息
    return jsonify({"error": "Invalid request method"})


if __name__ == "__main__":
    app.run(debug=True, threaded=True)