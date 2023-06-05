from flask import Flask, render_template, request, jsonify, redirect
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

        if textContent:
            lines = textContent.strip().split('\n')
            cleaned_lines = [line.rstrip() for line in lines]  # 将内容切割成每行的列表

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

            counts_matrix = logomaker.alignment_to_matrix(cleaned_lines)
            logo = logomaker.Logo(counts_matrix, color_scheme=colors)

            # 设置图片大小和格式
            logo.style_spines(visible=False)
            logo.style_xticks(rotation=90, fmt="%s")
            logo.ax.set_title("My Sequence Logo")
            logo.fig.set_size_inches(6, 4)
            logo_path = "assets/my_logo.png"
            logo.fig.savefig(logo_path, dpi=300)

        return redirect('/')

    return jsonify({"error": "Invalid request method"})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
