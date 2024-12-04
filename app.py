from flask import Flask, render_template, url_for
import markdown2
import chardet
import re

# Flaskアプリケーションを初期化
app = Flask(__name__,static_folder='static')

# ルート ('/') にアクセスした場合、index.md を表示するエンドポイント
@app.route('/')
def home():
    # show_markdown関数を呼び出して index.md を表示
    return show_markdown('index')

# 任意のMarkdownファイルを表示するエンドポイント
@app.route('/<filename>')
def show_markdown(filename='index'):
    try:
        # 指定されたMarkdownファイルを開く
        with open(f'markdown_files/{filename}.md', 'rb') as f:
            content = f.read()
            
            # ファイルのエンコーディングを自動検出
            result = chardet.detect(content)
            encoding = result['encoding']

            # BOM付きUTF-8の場合はエンコーディングを修正
            if encoding == 'utf-8-sig':
                encoding = 'utf-8'

            # ファイルを指定されたエンコーディングでデコード
            content = content.decode(encoding)

            # MarkdownリンクをHTMLリンクに変換するための関数
            def md_link_to_html(match):
                # リンクテキストとリンク先のMarkdownファイル名を取得
                link_text = match.group(1)  # [リンクテキスト]
                md_filename = match.group(2).replace('.md', '')  # ファイル名 (拡張子を除く)
                
                # FlaskのURLルートに変換
                html_url = url_for('show_markdown', filename=md_filename)
                
                # HTML形式のリンクを返す
                return f'<a href="{html_url}">{link_text}</a>'

            # Markdown内のリンクをFlaskエンドポイントのURL形式に変換
            content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', md_link_to_html, content)

            # MarkdownをHTMLに変換
            html = markdown2.markdown(content, extras=['code-friendly', 'fenced-code-blocks', 'highlightjs-lang'])
            
            # HTMLテンプレートに変換済みのMarkdown内容を渡して表示
            return render_template('index.html', content=html)
    except FileNotFoundError:
        # ファイルが見つからなかった場合のエラーメッセージ
        return 'ファイルが見つかりません'
    except Exception as e:
        # その他のエラーが発生した場合のメッセージ
        return f"予期せぬエラーが発生しました: {str(e)}"

# アプリケーションをデバッグモードで起動
if __name__ == '__main__':
    app.run()
