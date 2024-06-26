import zipfile
import io
import json

ICON_SVG = '<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><g fill="#D8D8D8" fill-rule="nonzero"><path d="M34.613 7.325H15.79a3.775 3.775 0 00-3.776 3.776v37.575a3.775 3.775 0 003.776 3.776h28.274a3.775 3.775 0 003.776-3.776V20.714a.8.8 0 00-.231-.561L35.183 7.563a.8.8 0 00-.57-.238zm-.334 1.6l11.96 12.118v27.633a2.175 2.175 0 01-2.176 2.176H15.789a2.175 2.175 0 01-2.176-2.176V11.1c0-1.202.973-2.176 2.176-2.176h18.49z"/><path d="M35.413 8.214v11.7h11.7v1.6h-13.3v-13.3z"/></g><path fill="#0290F5" d="M23.291 27h13.5v2.744h-13.5z"/><path fill="#D8D8D8" d="M38.428 27h4.32v2.744h-4.32zM17 27h2.7v2.7H17zM17 31.86h2.7v2.744H17zM28.151 31.861h11.34v2.7h-11.34zM17 36.72h2.7v2.7H17zM34.665 36.723h8.1v2.7h-8.1z"/><path fill="#0290F5" d="M28.168 36.723h4.86v2.7h-4.86z"/></g></svg>'
manifest_json ='{"type":"python","appType":"llsp3","autoDelete":false,"created":"2024-06-10T10:50:29.054Z","id":"1gGx6h4FCJhC","lastsaved":"2024-06-10T10:50:29.054Z","size":0,"name":"srps","slotIndex":0,"workspaceX":120,"workspaceY":120,"zoomLevel":0.5,"hardware":{"python":{"type":"flipper"}},"state":{"canvasDrawerOpen":true},"extraFiles":[]}'


def create_pycode_to_llsp3(code):
    output_file = io.BytesIO()
    project_body = {"main": code}
    with zipfile.ZipFile(output_file, 'w', compresslevel=0) as zf:
        zf.writestr( 'icon.svg',ICON_SVG)
        zf.writestr('manifest.json', manifest_json)
        zf.writestr('projectbody.json', json.dumps(project_body))

    return output_file