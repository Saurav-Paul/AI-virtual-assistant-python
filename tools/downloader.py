import wget, os , requests
def wget_downloader(url,path=''):
    try :
        wget.download(url,path)
    except :
        print('link error')

def downloader(url):
    chunk_size = 1024
    r = requests.get(url, stream = True)
    total_size = int(r.headers['content.length'])
    print(total_size)
    with open ("python.pdf","wb") as f:
        for data in tqdm(iterable = r.iter_content(chunk_size=chunk_size),total_size/chunk_size,unit = 'KB'):
            f.write(data)
            
if __name__ == "__main__":
    url = 'https://www.python.org/static/img/python-logo@2x.png'
    downloader(url)