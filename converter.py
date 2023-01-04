import sys
import markdown
from exceptions import InvalidArgException, InvalidCommandException, InvalidExtensionException


def to_html(inpath: str, outpath: str) -> None:
    if inpath[-3:] != '.md' or outpath[-5:] != '.html':
        raise InvalidExtensionException

    content = ''
    html = ''
    with open(inpath) as f:
        content = f.read()
        html = markdown.markdown(content)

    with open(outpath, 'w') as f:
        f.write(html)


try:
    if len(sys.argv) < 2:
        raise InvalidArgException

    command = sys.argv[1]
    if command != 'markdown':
        raise InvalidCommandException

    if len(sys.argv) != 4:
        raise InvalidArgException

    to_html(sys.argv[2], sys.argv[3])

except InvalidCommandException:
    print('Invalid command. Command supported is `markdown`.')
except InvalidArgException:
    print('Invalid number of arguments.')
except InvalidExtensionException:
    print('Invalid file extensions. You can only convert `.md` to `.html`.')
