import Foundation
import MarsDawnKit
// Reads Markdown on stdin, writes MarsDawnKit's preview HTML on stdout.
let data = FileHandle.standardInput.readDataToEndOfFile()
print(MarkdownRenderer.render(String(decoding: data, as: UTF8.self)), terminator: "")
