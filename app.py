from flask import Flask, render_template, request, redirect
import yt_dlp as ytdl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('topPage.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        ytdl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
        }

        url = request.form['yt_url']
        # urlがyoutubeのものでない場合はエラーを返す
        # 正規表現でチェックする
        if not url.startswith('https://www.youtube.com/watch?v='):
            return 'YouTubeのURLを入力してください。'
        else:
            pass
        
        with ytdl.YoutubeDL(ytdl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            return redirect(info['requested_formats'][0]['url'])
    except Exception as e:
        return 'エラーが発生しました。もう一度やり直してください。<br/>何度試してもエラーが発生する場合は、入力いただいたurlが正しいか確認してください。'

if __name__ == '__main__':
    app.run(debug=True)
